# -*- coding: utf-8 -*-
"""Bygger missionsfilerne til Denmark Universalis.

Brug:  python3 build.py <ud-mappe> [<udpakket DU-mod til validering>]
"""
import os
import re
import sys
import glob

import framework as F
from framework import REG, render_mission, yml_escape, AI_VENTETID_AAR

import age1_a
import age1_b
import age2

HEADER = '# Denmark Universalis: missionstræer (genereret af tools/du_missions/build.py, ret i generatoren)\n\n'

# Lande der ikke er spillerlande: situationslande, Holsten og Slesvig syd for Dannevirke
IKKE_SPILLER = ('QMB QMF QLA QLB QLC QLD QLE QLF QLG QLH QLI QLJ QLK QLL QUA QUB QUC QUD QUE QUH '
                'QSA QSB QSC QSD QSE QSF QSG QSH QSI QSJ QSK QSL QSM QSN QSO QTA QTB QTC QTD QTE QTF QTG QTH QTI').split()
UNIKKE = 'QAA QDX QCD QFE QEU QDI QCW QDF QDE QCV QFT QDP QBG QCQ QCE QBN QAX QBT QIC QCU QBU'.split()


def triggers():
    return HEADER + '''# AI: opgaven er låst op efter ventetiden
du_mission_ai_klar_trigger = {
	is_ai = yes
	NOT = { has_variable = du_mission_ai_ventetid }
}

# Spillerland: ikke et land, der opstår i en situation, et holstensk land eller en slesvigsk herre syd for Dannevirke
du_mission_spillerland_trigger = {
	NOT = {
		OR = {
%s
		}
	}
}

# De lande, der har deres egen unikke Age 2-mission i stedet for kulturgruppens
du_mission_unik_age2_trigger = {
	OR = {
%s
	}
}

# Age 2-missionerne kan tages fra Age 2 og frem
du_mission_age2_trigger = {
	NOT = { current_age = age_1_traditions }
}
''' % ('\n'.join('\t\t\ttag = %s' % t for t in IKKE_SPILLER),
       '\n'.join('\t\thas_or_had_tag = %s' % t for t in UNIKKE))


def effects():
    return HEADER + '''# AI: ny ventetid til næste opgave
du_mission_ai_ventetid_effect = {
	if = {
		limit = { has_variable = du_mission_ai_ventetid }
		remove_variable = du_mission_ai_ventetid
	}
	set_variable = { name = du_mission_ai_ventetid years = %d }
}
''' % AI_VENTETID_AAR


def casus_belli():
    return HEADER + '''# Missionskrav: mod et land, der ejer en lokation, som vi har fået kerne på gennem en mission
du_cb_mission_krav = {
	speed = 10
	create_visible = {
		has_variable = du_mission_krav
		scope:target ?= {
			any_owned_location = { is_core_of = root }
		}
	}
	create_enabled = {
		NOT = { has_truce_with = scope:target }
	}
	war_goal_type = du_wg_mission_krav
	ai_will_do = {
		add = {
			desc = "CB_REASON_IMPORTANT_CB"
			value = 50
		}
	}
}
'''


def wargoals():
    return HEADER + '''du_wg_mission_krav = {
	type = superiority

	attacker = {
		antagonism = 0.5
		conquer_cost = 0.75
		subjugate_cost = 0.9
	}
	defender = {
		antagonism = 0.8
	}
	ticking_war_score = 0.5
}
'''


def fmt_val(v):
    if isinstance(v, float):
        s = ('%.4f' % v).rstrip('0').rstrip('.')
        return s
    return str(v)


def modifiers():
    out = [HEADER]
    for key, cat, mods, name, desc in REG.modifiers:
        lines = ['%s = {' % key, '\tgame_data = {', '\t\tcategory = %s' % cat, '\t}']
        for k, v in mods.items():
            lines.append('\t%s = %s' % (k, fmt_val(v)))
        lines.append('}')
        out.append('\n'.join(lines) + '\n')
        REG.add_loc(key, name)
        if desc:
            REG.add_loc(key + '_desc', desc)
    return '\n'.join(out)


def localisation():
    REG.add_loc('du_mission_krav_tt', 'We gain cores on these locations and the Mission Claim casus belli against whoever holds them.')
    REG.add_loc('du_cb_mission_krav', 'Mission Claim')
    REG.add_loc('du_cb_mission_krav_desc', 'Our council has laid claim to lands held by this country.')
    REG.add_loc('du_wg_mission_krav', 'Mission Claim')
    seen = {}
    lines = ['l_english:', ' # Denmark Universalis: missionstræer (genereret)']
    for k, v in REG.loc:
        if k in seen:
            if seen[k] != v:
                raise ValueError('loc-nøgle med to tekster: ' + k)
            continue
        seen[k] = v
        lines.append(' %s: "%s"' % (k, yml_escape(v)))
    return '\n'.join(lines) + '\n'


def write(path, text, bom=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8-sig' if bom else 'utf-8', newline='\n') as f:
        f.write(text)


def balance_check(name, text):
    depth = 0
    for i, ch in enumerate(re.sub(r'"[^"\n]*"', '', re.sub(r'#[^\n]*', '', text))):
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth < 0:
                raise ValueError('%s: for mange } ved tegn %d' % (name, i))
    if depth != 0:
        raise ValueError('%s: %d { mangler at blive lukket' % (name, depth))


def validate(du_root, texts):
    """Tjekker at alle location:/area:/building_type:/goods: m.fl. findes i DU."""
    defs = open(os.path.join(du_root, 'in_game/map_data/definitions.txt'), encoding='utf-8-sig').read()
    words = set(re.findall(r'[A-Za-z_0-9]+', re.sub(r'#.*', '', defs)))
    buildings, goods, advances, cultgroups = set(), set(), set(), set()
    for f in glob.glob(os.path.join(du_root, 'in_game/common/building_types/*.txt')):
        buildings |= set(re.findall(r'^(\w+) = \{', open(f, encoding='utf-8-sig').read(), re.M))
    for f in glob.glob(os.path.join(du_root, 'in_game/common/goods/*.txt')):
        goods |= set(re.findall(r'^(\w+) = \{', open(f, encoding='utf-8-sig').read(), re.M))
    for f in glob.glob(os.path.join(du_root, 'in_game/common/advances/*.txt')):
        advances |= set(re.findall(r'^(\w+) = \{', open(f, encoding='utf-8-sig').read(), re.M))
    cultgroups = set(re.findall(r'^(\w+) = \{', open(os.path.join(du_root, 'in_game/common/culture_groups/00_culture_groups.txt'), encoding='utf-8-sig').read(), re.M))
    # vanilla-bygninger, som DU ikke overskriver, men selv bygger (du_spilstart_effects)
    buildings |= {'dock'}
    # vanilla-varer, DU ikke overskriver (bruges i DU's egne filer)
    goods |= {'fish', 'wheat', 'millet', 'legumes', 'livestock', 'wool', 'lumber', 'fur', 'iron', 'horses',
              'wild_game', 'sand', 'clay', 'coal', 'fiber_crops', 'alum', 'sugar', 'fruit', 'stone', 'marble'}
    errors = []
    for name, text in texts.items():
        for kind, rx, known in (('location', r'location:(\w+)', words), ('area', r'area:(\w+)', words),
                                ('building', r'building_type:(\w+)', buildings), ('goods', r'goods:(\w+)', goods),
                                ('advance', r'has_advance = (\w+)', advances),
                                ('culture group', r'culture_group:(\w+)', cultgroups)):
            for m in set(re.findall(rx, text)):
                if m not in known:
                    errors.append('%s: ukendt %s %s' % (name, kind, m))
    tags = set()
    for f in glob.glob(os.path.join(du_root, 'in_game/setup/countries/*.txt')):
        tags |= set(re.findall(r'^([A-Z][A-Z0-9]{2}) = \{', open(f, encoding='utf-8-sig').read(), re.M))
    for name, text in texts.items():
        for m in set(re.findall(r'(?:has_or_had_tag|tag) = ([A-Z][A-Z0-9]{2})\b', text)):
            if m not in tags:
                errors.append('%s: ukendt tag %s' % (name, m))
    return errors


def flat(trig):
    return re.sub(r'\s+', ' ', trig).strip()


def overview(m1, m2):
    names = dict(REG.loc)
    out = ['# Denmark Universalis: missionstræer', '',
           'Genereret af `tools/du_missions/build.py`. Teksterne i spillet er på engelsk som resten af DU.', '',
           '## Sådan virker det', '',
           '- **Age 1**: hvert af de 20 lande har sit eget træ (12 opgaver), synligt for landets tag (`has_or_had_tag`, så det overlever formables).',
           '- **Age 2**: hver regional kulturgruppe har en mission (7 opgaver) for spillerlande med den kultur. De 20 lande ser i stedet deres egen unikke Age 2-mission. Situationslande, Holsten og Slesvig syd for Dannevirke er udelukket.',
           '- **AI**: hver opgave har en AI-gren. AI\'en kan opfylde det rigtige krav, eller få opgaven låst op %d år efter sin sidste opgave. Når den tager opgaven, får den kravet opfyldt (bygning bygges gratis og øjeblikkeligt, by opgraderes, RGO udvides, samfundsværdi flyttes).' % AI_VENTETID_AAR,
           '- **Erobring**: opgaven før en erobringsopgave giver kerner på målene og casus belli *Mission Claim* (`du_cb_mission_krav`), så AI\'en invaderer. Lykkes det ikke, låses opgaven op for AI\'en efter %d år (uden land).' % F.AI_EROBRING_AAR,
           '- **Kolding**: der findes to tags med navnet Kolding (QIC med 36 sogne inkl. Kolding by, og QCU med ét sogn). Begge ser Kolding-træet og Kolding-missionen.', '']
    for title, ms in (('Age 1: landetræer', m1), ('Age 2: kulturgrupper og unikke missioner', m2)):
        out += ['## ' + title, '']
        for m in ms:
            out += ['### %s (`%s`)' % (m.name, m.key), '', '*Synlig for:* `%s`' % flat(m.visible), '', m.desc, '']
            out += ['| Opgave | Kræver | Krav |', '|---|---|---|']
            for t in m.tasks:
                req = ', '.join(names.get('%s_%s' % (m.key, r), r) for r in t.req) or '–'
                krav = '; '.join(flat(c.trig) for c in t.cond).replace('|', '/')
                out.append('| %s%s | %s | `%s` |' % (t.name, ' (slut)' if t.final else '', req, krav))
            out.append('')
    return '\n'.join(out) + '\n'


def main():
    out = sys.argv[1]
    du_root = sys.argv[2] if len(sys.argv) > 2 else None
    missions1 = [f() for f in age1_a.TREES_A + age1_b.TREES_B]
    missions2 = age2.missions()
    txt1 = HEADER + '\n\n'.join(render_mission(m) for m in missions1) + '\n'
    txt2 = HEADER + '\n\n'.join(render_mission(m) for m in missions2) + '\n'
    files = {
        'in_game/common/missions/du_missions_lande.txt': txt1,
        'in_game/common/missions/du_missions_age2.txt': txt2,
        'in_game/common/scripted_triggers/du_mission_triggers.txt': triggers(),
        'in_game/common/scripted_effects/du_mission_effects.txt': effects(),
        'in_game/common/casus_belli/du_mission_cb.txt': casus_belli(),
        'in_game/common/wargoals/du_mission_wargoals.txt': wargoals(),
        'main_menu/common/static_modifiers/du_mission_modifiers.txt': modifiers(),
    }
    files['main_menu/localization/english/du_missions_l_english.yml'] = localisation()
    for name, text in files.items():
        if name.endswith('.txt'):
            balance_check(name, text)
    if du_root:
        errs = validate(du_root, files)
        if errs:
            print('\n'.join(sorted(set(errs))))
            sys.exit(1)
    for name, text in files.items():
        write(os.path.join(out, name), text, bom=True)
    write(os.path.join(out, 'DU_missioner_oversigt.md'), overview(missions1, missions2))
    n1 = sum(len(m.tasks) for m in missions1)
    n2 = sum(len(m.tasks) for m in missions2)
    print('Age 1: %d træer, %d opgaver | Age 2: %d missioner, %d opgaver | %d modifiers | %d loc-nøgler'
          % (len(missions1), n1, len(missions2), n2, len(REG.modifiers), len(REG.loc)))
    return missions1, missions2


if __name__ == '__main__':
    main()
