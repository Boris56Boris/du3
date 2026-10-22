# -*- coding: utf-8 -*-
"""Denmark Universalis: generator for missionstræer.

Hver opgave (task) har:
  - et rigtigt krav (det spilleren ser), bygget af betingelses-hjælpere herunder
  - en AI-gren: AI'en kan altid opfylde det rigtige krav, men får også opgaven
    låst op efter en ventetid (du_mission_ai_ventetid). Når AI'en tager opgaven,
    bliver kravet opfyldt for den (bygning bygges, by opgraderes, RGO udvides osv.).
  - erobringsopgaver: den forrige opgave giver kerner (claims) på målene og
    et casus belli (du_cb_mission_krav), så AI'en invaderer. Hvis det ikke er
    lykkedes efter en lang ventetid, låses opgaven op for AI'en uden land.

Alle effekter og triggere er nogle, der allerede bruges i Denmark Universalis
eller i mission tree-modden (senvm).
"""

import re

AI_VENTETID_AAR = 4          # år mellem AI-opgaver
AI_EROBRING_AAR = 15         # år AI'en har til at erobre efter at have fået krav

RANKS = {
    'town': 'NOT = { location_rank = location_rank:rural_settlement }',
    'city': 'OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis }',
}

# placering til AI-byggeri (fra bygningernes location_potential i DU)
RURAL = 'location_rank = location_rank:rural_settlement'
TOWN = 'NOT = { location_rank = location_rank:rural_settlement }'
CITY = RANKS['city']
BUILD_LIMIT = {
    'fishing_village': RURAL + ' is_coastal = yes',
    'farming_village': RURAL + ' OR = { raw_material = goods:wheat raw_material = goods:millet raw_material = goods:legumes }',
    'forest_village': RURAL + ' OR = { raw_material = goods:wild_game vegetation = forest vegetation = woods }',
    'sheep_farms': RURAL + ' OR = { vegetation = sparse vegetation = farmland vegetation = grasslands }',
    'market_village': RURAL,
    'windmill': RURAL + ' OR = { raw_material = goods:wheat raw_material = goods:millet }',
    'sawmill': RURAL + ' OR = { vegetation = woods vegetation = forest vegetation = farmland raw_material = goods:lumber }',
    'local_smelters': RURAL + ' raw_material = goods:iron',
    'training_fields': RURAL,
    'regimental_camp': RURAL,
    'noble_villa': RURAL,
    'free_village': RURAL,
    'local_markets': RURAL,
    'parish_church': '',
    'castle': '',
    'toll_castle': '',
    'conscription_center': '',
    'counting_house': TOWN, 'granary': TOWN, 'wharf': TOWN + ' is_coastal = yes',
    'dock': 'is_port = yes',
    'university': TOWN, 'library': TOWN, 'armory': TOWN, 'barracks': TOWN,
    'local_schools': TOWN, 'temple': TOWN, 'theater': TOWN,
    'merchants_guild': TOWN + ' is_port = yes',
    'du_saltery': TOWN, 'du_dairy': TOWN, 'du_bakery': TOWN, 'du_mosteri': TOWN,
    'guild_hall': CITY, 'cathedral': CITY, 'city_walls': CITY,
    'du_sild_skattekontor': 'raw_material ?= goods:fish',
}


def ind(text, n):
    pad = '\t' * n
    return '\n'.join((pad + l if l.strip() else l) for l in text.split('\n'))


def construct(b, n=1):
    one = ('construct_building = { building_type = building_type:%s owner = root payer = root '
           'instant = yes cost_multiplier = 0 cost_multiplier_reason = "DU_GRATIS_BYGNING" }' % b)
    return '\n'.join([one] * n)


def loc_scope(loc):
    """'capital' eller et lokationsnavn -> scope-udtryk"""
    return 'capital' if loc == 'capital' else 'location:%s' % loc


class C:
    """En betingelse: trigger (spilleren) + hvad AI'en får, når den tager opgaven."""
    def __init__(self, trig, ai=None, erobring=False):
        self.trig = trig
        self.ai = ai
        self.erobring = erobring


# ---------------------------------------------------------------- betingelser

def bygning(b, n=1):
    trig = 'any_owned_location = {\n\thas_building = building_type:%s\n\tcount >= %d\n}' % (b, n)
    lim = BUILD_LIMIT.get(b, '')
    ai = ('ordered_owned_location = {\n\tlimit = { %s NOT = { has_building = building_type:%s } }\n'
          '\torder_by = population\n\tcheck_range_bounds = no\n\tmax = %d\n%s\n}') % (lim, b, n, ind(construct(b), 1))
    return C(trig, ai)


def bygning_i(loc, b, level=1):
    sc = loc_scope(loc)
    own = '' if loc == 'capital' else 'owner ?= root\n\t'
    if level <= 1:
        trig = '%s = {\n\t%shas_building = building_type:%s\n}' % (sc, own, b)
    else:
        trig = ('%s = {\n\t%slocation_building_level = {\n\t\tbuilding_type = building_type:%s\n\t\tvalue >= %d\n\t}\n}'
                % (sc, own, b, level))
    ai = '%s = {\n\tif = {\n\t\tlimit = { owner ?= root }\n%s\n\t}\n}' % (sc, ind(construct(b, level), 2))
    return C(trig, ai)


def rang(loc, r):
    sc = loc_scope(loc)
    own = '' if loc == 'capital' else 'owner ?= root\n\t'
    trig = '%s = {\n\t%s%s\n}' % (sc, own, RANKS[r])
    ai = ('%s = {\n\tif = {\n\t\tlimit = { owner ?= root NOT = { %s } }\n'
          '\t\tchange_location_rank_effect = { location_rank = location_rank:%s }\n\t}\n}') % (sc, RANKS[r], r)
    return C(trig, ai)


def rgo(loc, n):
    sc = loc_scope(loc)
    own = '' if loc == 'capital' else 'owner ?= root\n\t'
    trig = '%s = {\n\t%srgo_level >= %d\n}' % (sc, own, n)
    ai = ('%s = {\n\tif = {\n\t\tlimit = { owner ?= root }\n\t\tconstruct_rgo_upgrade = { cost_multiplier = 0 '
          'cost_multiplier_reason = "DU_GRATIS_BYGNING" }\n\t}\n}') % sc
    return C(trig, ai)


def rgo_vare(goods, level, count):
    trig = ('any_owned_location = {\n\traw_material ?= goods:%s\n\trgo_level >= %d\n\tcount >= %d\n}'
            % (goods, level, count))
    ai = ('ordered_owned_location = {\n\tlimit = { raw_material ?= goods:%s }\n\torder_by = rgo_level\n'
          '\tcheck_range_bounds = no\n\tmax = %d\n\tconstruct_rgo_upgrade = { cost_multiplier = 0 '
          'cost_multiplier_reason = "DU_GRATIS_BYGNING" }\n}') % (goods, count)
    return C(trig, ai)


def udvikling(loc, n):
    sc = loc_scope(loc)
    own = '' if loc == 'capital' else 'owner ?= root\n\t'
    trig = '%s = {\n\t%sdevelopment >= %d\n}' % (sc, own, n)
    ai = '%s = {\n\tif = {\n\t\tlimit = { owner ?= root }\n\t\tchange_development = 5\n\t}\n}' % sc
    return C(trig, ai)


def ejer(*locs):
    return C('\n'.join('owns = location:%s' % l for l in locs), None, erobring=True)


def omraade(area, frac=0.8):
    trig = ('area:%s = {\n\tany_location_in_area = {\n\t\tis_owned_or_owned_by_subjects_or_below_of = root\n'
            '\t\tpercent >= %s\n\t}\n}') % (area, frac)
    return C(trig, None, erobring=True)


def vaerdi(axis, op, n):
    side = 'left' if op == '<' else 'right'
    trig = 'societal_value:%s %s %d' % (axis, op, n)
    ai = 'change_societal_value = { type = %s value = societal_value_move_to_%s }' % (axis, side)
    return C(trig, ai)


def haer(n):
    return C('regular_army_size >= %s' % n)


def flaade(n):
    return C('regular_navy_size >= %s' % n)


def stabilitet(n):
    return C('stability >= %d' % n)


def prestige(n):
    return C('prestige >= %d' % n)


def haertradition(n):
    return C('army_tradition >= %d' % n)


def guld(n):
    return C('gold >= %d' % n)


def stand(estate, p):
    return C('any_estate = {\n\testate_type = estate_type:%s_estate\n\tpower >= %s\n}' % (estate, p))


def undersaatter(n):
    return C('num_subjects >= %d' % n)


def uafhaengig():
    return C('is_subject = no')


def lokationer(n):
    return C('num_locations >= %d' % n)


def byer(n):
    return C('num_of_non_rural >= %d' % n)


def fremskridt(adv):
    return C('has_advance = %s' % adv)


def institution(inst):
    return C('has_embraced_institution = institution:%s' % inst)


def sild(n):
    return C('has_variable = du_sild_point\nvar:du_sild_point >= %d' % n)


def eller(*conds):
    """Mindst én af betingelserne. AI-effekten tages fra den første, der har en."""
    trig = 'OR = {\n%s\n}' % '\n'.join(ind('AND = {\n%s\n}' % ind(c.trig, 1), 1) for c in conds)
    ai = next((c.ai for c in conds if c.ai), None)
    return C(trig, ai, erobring=any(c.erobring for c in conds))


def raa(trig, ai=None, erobring=False):
    return C(trig, ai, erobring)


# ---------------------------------------------------------------- belønninger

class Registry:
    def __init__(self):
        self.modifiers = []      # (key, category, dict, name, desc)
        self.loc = []            # (key, text)
        self.mod_keys = set()

    def add_mod(self, key, cat, mods, name, desc):
        if key in self.mod_keys:
            raise ValueError('dobbelt modifier ' + key)
        self.mod_keys.add(key)
        self.modifiers.append((key, cat, mods, name, desc))

    def add_loc(self, key, text):
        self.loc.append((key, text))


REG = Registry()


class R:
    """En belønning: effekt-tekst. Modifiers registreres når opgaven bygges."""
    def __init__(self, eff, mod=None):
        self.eff = eff
        self.mod = mod   # (cat, dict, name, desc, suffix)


def mod(name, mods, desc='', years=-1, suffix=''):
    """Landsmodifier. years=-1 er permanent."""
    return R(('add_country_modifier = {\n\tmodifier = {KEY}\n\tmode = replace\n\tyears = %s\n}' % years),
             ('country', mods, name, desc, suffix))


def hovedstad_mod(name, mods, desc='', years=-1, suffix=''):
    return R(('capital = {\n\tadd_location_modifier = {\n\t\tmodifier = {KEY}\n\t\tmode = replace\n\t\tyears = %s\n\t}\n}' % years),
             ('location', mods, name, desc, suffix))


def sted_mod(loc, name, mods, desc='', years=-1, suffix=''):
    return R(('location:%s = {\n\tif = {\n\t\tlimit = { owner ?= root }\n\t\tadd_location_modifier = {\n\t\t\tmodifier = {KEY}\n'
              '\t\t\tmode = replace\n\t\t\tyears = %s\n\t\t}\n\t}\n}') % (loc, years),
             ('location', mods, name, desc, suffix))


def guld_r(n):
    return R('add_gold = %d' % n)


def prestige_r(kind='mild'):
    return R('add_prestige = prestige_%s_bonus' % kind)


def stabilitet_r():
    return R('add_stability = stability_severe_bonus')


def vaerdi_r(axis, side, minor=False):
    return R('change_societal_value = { type = %s value = societal_value_%smove_to_%s }'
             % (axis, 'minor_' if minor else '', side))


def udvikling_r(loc='capital', n=5):
    sc = loc_scope(loc)
    if loc == 'capital':
        return R('capital = { change_development = %d }' % n)
    return R('%s = {\n\tif = {\n\t\tlimit = { owner ?= root }\n\t\tchange_development = %d\n\t}\n}' % (sc, n))


def velstand_r(loc='capital'):
    sc = loc_scope(loc)
    return R('%s = {\n\tif = {\n\t\tlimit = { owner ?= root }\n\t\tchange_prosperity = prosperity_mild_bonus\n\t}\n}' % sc)


def byg_r(loc, b, n=1):
    sc = loc_scope(loc)
    return R('%s = {\n\tif = {\n\t\tlimit = { owner ?= root }\n%s\n\t}\n}' % (sc, ind(construct(b, n), 2)))


def rang_r(loc, r):
    sc = loc_scope(loc)
    return R(('%s = {\n\tif = {\n\t\tlimit = { owner ?= root NOT = { %s } }\n'
              '\t\tchange_location_rank_effect = { location_rank = location_rank:%s }\n\t}\n}') % (sc, RANKS[r], r))


def landsrang_r(level):
    rk = {2: 'rank_duchy', 3: 'rank_kingdom', 4: 'rank_empire'}[level]
    return R('if = {\n\tlimit = { country_rank_level < %d }\n\tset_country_rank_effect = { rank = country_rank:%s }\n}'
             % (level, rk))


def krav_r(*locs, ai_var=None):
    """Kerner (claims) på lokationer, som andre ejer, og adgang til du_cb_mission_krav."""
    lines = ['set_variable = du_mission_krav']
    for l in locs:
        lines.append('location:%s = {\n\tif = {\n\t\tlimit = { NOT = { owner ?= root } }\n\t\tadd_core = root\n\t}\n}' % l)
    lines.append('custom_tooltip = du_mission_krav_tt')
    if ai_var:
        lines.append('hidden_effect = {\n\tif = {\n\t\tlimit = { is_ai = yes }\n\t\tset_variable = { name = %s years = %d }\n\t}\n}'
                     % (ai_var, AI_EROBRING_AAR))
    return R('\n'.join(lines))


def krav_omraade_r(area, ai_var=None):
    lines = ['set_variable = du_mission_krav',
             'area:%s = {\n\tevery_location_in_area = {\n\t\tlimit = { is_ownable = yes NOT = { owner ?= root } }\n\t\tadd_core = root\n\t}\n}' % area,
             'custom_tooltip = du_mission_krav_tt']
    if ai_var:
        lines.append('hidden_effect = {\n\tif = {\n\t\tlimit = { is_ai = yes }\n\t\tset_variable = { name = %s years = %d }\n\t}\n}'
                     % (ai_var, AI_EROBRING_AAR))
    return R('\n'.join(lines))


def tt_r(key, text):
    REG.add_loc(key, text)
    return R('custom_tooltip = %s' % key)


def raa_r(eff):
    return R(eff)


# ---------------------------------------------------------------- opgaver og missioner

class Task:
    def __init__(self, tid, icon, name, desc, req=(), cond=(), reward=(), final=False,
                 ai_krav=None, duration=None):
        self.tid = tid
        self.icon = icon
        self.name = name
        self.desc = desc
        self.req = list(req)
        self.cond = list(cond)
        self.reward = list(reward)
        self.final = final
        self.ai_krav = ai_krav     # variabelnavn sat af den opgave, der gav kravene
        self.duration = duration


class Mission:
    def __init__(self, key, icon, name, desc, playstyle, visible, enabled, tasks, chance=5000):
        self.key = key
        self.icon = icon
        self.name = name
        self.desc = desc
        self.playstyle = playstyle
        self.visible = visible
        self.enabled = enabled
        self.tasks = tasks
        self.chance = chance


def render_task(m, t):
    key = '%s_%s' % (m.key, t.tid)
    REG.add_loc(key, t.name)
    REG.add_loc(key + '_desc', t.desc)
    real = '\n'.join(c.trig for c in t.cond)
    out = ['%s = {' % key, '\ticon = %s' % t.icon]
    if t.final:
        out.append('\tfinal = yes')
    out.append('\trequires = {\n%s\n\t}' % '\n'.join('\t\t%s_%s' % (m.key, r) for r in t.req) if t.req else '\trequires = { }')
    erob = any(c.erobring for c in t.cond)
    if erob and t.ai_krav:
        ai_ok = 'du_mission_ai_klar_trigger = yes\n\t\t\t\tNOT = { has_variable = %s }' % t.ai_krav
    else:
        ai_ok = 'du_mission_ai_klar_trigger = yes'
    enabled = ('\tenabled = {\n\t\ttrigger_if = {\n\t\t\tlimit = { is_ai = yes }\n\t\t\tOR = {\n\t\t\t\tAND = {\n%s\n\t\t\t\t}\n'
               '\t\t\t\tAND = {\n\t\t\t\t\t%s\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t\ttrigger_else = {\n%s\n\t\t}\n\t}') % (
        ind(real, 5), ai_ok.replace('\t\t\t\t', '\t\t\t\t\t'), ind(real, 3))
    out.append(enabled)
    # on_completion
    ai_effs = [c.ai for c in t.cond if c.ai]
    ai_block = ''
    if ai_effs:
        ai_block = 'if = {\n\tlimit = {\n\t\tNOT = {\n\t\t\tAND = {\n%s\n\t\t\t}\n\t\t}\n\t}\n%s\n}\n' % (
            ind(real, 4), ind('\n'.join(ai_effs), 1))
    hidden = ('hidden_effect = {\n\tif = {\n\t\tlimit = { is_ai = yes }\n%s\t\tdu_mission_ai_ventetid_effect = yes\n\t}\n}'
              % (ind(ai_block, 2) + '\n' if ai_block else ''))
    effs = []
    for i, r in enumerate(t.reward):
        e = r.eff
        if r.mod:
            cat, mods, name, desc, suffix = r.mod
            mkey = 'du_mm_%s_%s%s' % (m.key.replace('du_m2_', 'a2_').replace('du_m_', ''), t.tid, ('_' + suffix) if suffix else '')
            if mkey in REG.mod_keys:
                mkey = mkey + '_%d' % i
            REG.add_mod(mkey, cat, mods, name, desc)
            e = e.replace('{KEY}', mkey)
        effs.append(e)
    effs.append(hidden)
    out.append('\ton_completion = {\n%s\n\t}' % ind('\n'.join(effs), 2))
    out.append('}')
    return '\n'.join(out)


def render_mission(m):
    REG.add_loc(m.key, m.name)
    REG.add_loc(m.key + '_desc', m.desc)
    body = ['%s = {' % m.key,
            '\ticon = %s' % m.icon,
            '\trepeatable = no',
            '\tplayer_playstyle = %s' % m.playstyle,
            '\tvisible = {\n%s\n\t}' % ind(m.visible, 2),
            '\tenabled = {\n%s\n\t}' % ind(m.enabled, 2),
            '\ton_start = {\n\t\thidden_effect = {\n\t\t\tif = {\n\t\t\t\tlimit = { is_ai = yes }\n'
            '\t\t\t\tdu_mission_ai_ventetid_effect = yes\n\t\t\t}\n\t\t}\n\t}',
            '\tchance = %d' % m.chance, '']
    ids = {t.tid for t in m.tasks}
    for t in m.tasks:
        for r in t.req:
            if r not in ids:
                raise ValueError('%s: %s kræver ukendt %s' % (m.key, t.tid, r))
        body.append(ind(render_task(m, t), 1))
        body.append('')
    body.append('}')
    return '\n'.join(body)


def yml_escape(s):
    return s.replace('"', '\\"')
