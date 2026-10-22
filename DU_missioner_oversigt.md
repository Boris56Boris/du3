# Denmark Universalis: missionstræer

Genereret af `tools/du_missions/build.py`. Teksterne i spillet er på engelsk som resten af DU.

## Sådan virker det

- **Age 1**: hvert af de 20 lande har sit eget træ (12 opgaver), synligt for landets tag (`has_or_had_tag`, så det overlever formables).
- **Age 2**: hver regional kulturgruppe har en mission (7 opgaver) for spillerlande med den kultur. De 20 lande ser i stedet deres egen unikke Age 2-mission. Situationslande, Holsten og Slesvig syd for Dannevirke er udelukket.
- **AI**: hver opgave har en AI-gren. AI'en kan opfylde det rigtige krav, eller få opgaven låst op 4 år efter sin sidste opgave. Når den tager opgaven, får den kravet opfyldt (bygning bygges gratis og øjeblikkeligt, by opgraderes, RGO udvides, samfundsværdi flyttes).
- **Erobring**: opgaven før en erobringsopgave giver kerner på målene og casus belli *Mission Claim* (`du_cb_mission_krav`), så AI'en invaderer. Lykkes det ikke, låses opgaven op for AI'en efter 15 år (uden land).
- **Kolding**: der findes to tags med navnet Kolding (QIC med 36 sogne inkl. Kolding by, og QCU med ét sogn). Begge ser Kolding-træet og Kolding-missionen.

## Age 1: landetræer

### The Crown's City (`du_m_qaa`)

*Synlig for:* `has_or_had_tag = QAA`

Copenhagen holds the crown of Denmark, a republic of merchants that rules a realm of lords. The war in our own streets must be won, the herring made to pay, and the city made worthy of the realm it governs.

| Opgave | Kræver | Krav |
|---|---|---|
| The War in Our Own Streets | – | `owns = location:frederiksberg_9181` |
| Punish Hvidovre | The War in Our Own Streets | `owns = location:hvidovre_7141` |
| The Citizen Watch | – | `capital = { has_building = building_type:city_walls }; regular_army_size >= 4` |
| The Crown Council | – | `any_estate = { estate_type = estate_type:crown_estate power >= 0.3 }; stability >= 30` |
| The Landsting Answers | The Crown Council | `prestige >= 30; num_subjects >= 60` |
| The Herring Monopoly | The Crown Council | `OR = { AND = { has_variable = du_sild_point var:du_sild_point >= 4000 } AND = { any_owned_location = { has_building = building_type:du_saltery count >= 3 } } }` |
| The Fleet at Holmen | The Herring Monopoly | `location:vor_frelsers_7082 = { owner ?= root has_building = building_type:dock }; regular_navy_size >= 12` |
| The Merchants' Harbour | – | `any_owned_location = { has_building = building_type:counting_house count >= 2 }; capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }` |
| Guilds of the Capital | The Merchants' Harbour | `capital = { has_building = building_type:guild_hall }; societal_value:capital_economy_vs_traditional_economy < -65` |
| The University | The Merchants' Harbour | `capital = { has_building = building_type:university }; any_owned_location = { has_building = building_type:library count >= 2 }` |
| Free Citizens | Guilds of the Capital | `societal_value:serfdom_vs_free_subjects > 90; any_estate = { estate_type = estate_type:burghers_estate power >= 0.3 }` |
| The Crown's City (slut) | Punish Hvidovre, The Landsting Answers, The Fleet at Holmen, The University, Free Citizens | `capital = { development >= 20 }; stability >= 50` |

### Gate of the Limfjord (`du_m_qdx`)

*Synlig for:* `has_or_had_tag = QDX`

Aalborg holds the narrows where the Limfjord meets the Kattegat. Herring, grain and fur all pass our quays, and the districts of the federation look to us. The lands across the fjord could look to us as well.

| Opgave | Kræver | Krav |
|---|---|---|
| Limfjord Herring | – | `any_owned_location = { has_building = building_type:fishing_village count >= 4 }` |
| Salt for the Barrels | Limfjord Herring | `any_owned_location = { has_building = building_type:du_saltery count >= 2 }` |
| The Sound at Nørresundby | Limfjord Herring | `location:noerresundby_8375 = { owner ?= root NOT = { location_rank = location_rank:rural_settlement } }` |
| Watch at Hals | The Sound at Nørresundby | `location:hals_8387 = { owner ?= root has_building = building_type:castle }` |
| The Aalborg Federation | – | `societal_value:centralization_vs_decentralization < -20; stability >= 25` |
| Claims on Vendsyssel | The Aalborg Federation | `regular_army_size >= 4` |
| Across the Fjord | Claims on Vendsyssel | `owns = location:dronninglund_8451 owns = location:broenderslev_8402` |
| The Rebild Hills | Across the Fjord | `owns = location:stoevring_8335` |
| City of the North | – | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }; num_of_non_rural >= 3` |
| The Holy Spirit House | City of the North | `capital = { has_building = building_type:library }; societal_value:spiritualist_vs_humanist > 40` |
| Merchants of Aalborg | City of the North, Salt for the Barrels | `any_owned_location = { has_building = building_type:counting_house count >= 1 }; regular_navy_size >= 6` |
| Capital of North Jutland (slut) | Watch at Hals, The Rebild Hills, The Holy Spirit House, Merchants of Aalborg | `num_locations >= 80; stability >= 40` |

### Heart of Funen (`du_m_qcd`)

*Synlig for:* `has_or_had_tag = QCD`

Odense is the oldest town on Funen and the shrine of Saint Knud, but our lands are small and our neighbours many. A humanist, open city must gather the island around it by trade, learning and, where needed, the sword.

| Opgave | Kræver | Krav |
|---|---|---|
| Shrine of Saint Knud | – | `capital = { has_building = building_type:temple }; any_estate = { estate_type = estate_type:clergy_estate power >= 0.25 }` |
| The Cathedral School | Shrine of Saint Knud | `capital = { has_building = building_type:library }` |
| The Lords Meet at Odense | The Cathedral School | `prestige >= 30; societal_value:belligerent_vs_conciliatory > 45` |
| Market of Funen | – | `any_owned_location = { has_building = building_type:market_village count >= 3 }; any_owned_location = { has_building = building_type:counting_house count >= 1 }` |
| The Brewers of Odense | Market of Funen | `any_owned_location = { has_building = building_type:du_mosteri count >= 1 }; any_owned_location = { has_building = building_type:du_bakery count >= 1 }` |
| A Way to the Sea | Market of Funen | `location:kerteminde_drigstrup_9293 = { owner ?= root has_building = building_type:wharf }` |
| Funen Levies | – | `regular_army_size >= 4; societal_value:quality_vs_quantity < -35` |
| North and East of Odense | Funen Levies | `owns = location:otterup_7891 owns = location:aarslev_7740` |
| The Harbour at Assens | North and East of Odense | `owns = location:assens_7801` |
| Town Hall and Charter | The Brewers of Odense | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }; societal_value:serfdom_vs_free_subjects > 70` |
| Trading Houses | A Way to the Sea, Town Hall and Charter | `any_owned_location = { has_building = building_type:counting_house count >= 2 }; stability >= 30` |
| Heart of Funen (slut) | The Lords Meet at Odense, The Harbour at Assens, Trading Houses | `area:odense_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 1.0 } }; capital = { development >= 18 }` |

### Gate of the Sound (`du_m_qfe`)

*Synlig for:* `has_or_had_tag = QFE`

Malmö faces Copenhagen across the Sound and trades with the whole Baltic. Our citizens are free, our council is generous, and our shore is the Scania Market, where half of Europe buys its herring.

| Opgave | Kræver | Krav |
|---|---|---|
| The Scania Market | – | `owns = location:skanor_sk owns = location:falsterbo_sk` |
| Fishing Camps on the Shore | The Scania Market | `any_owned_location = { has_building = building_type:fishing_village count >= 3 }; any_owned_location = { has_building = building_type:du_saltery count >= 1 }` |
| The Scanian League | Fishing Camps on the Shore | `OR = { AND = { has_variable = du_sild_point var:du_sild_point >= 5000 } AND = { prestige >= 40 } }` |
| Harbour of Malmö | – | `capital = { has_building = building_type:dock }; regular_navy_size >= 8` |
| Beyond the Sound | Harbour of Malmö | `regular_navy_size >= 15; societal_value:land_vs_naval > 40` |
| The Council of Malmö | – | `societal_value:serfdom_vs_free_subjects > 85; stability >= 30` |
| A Town of Strangers | The Council of Malmö | `societal_value:individualism_vs_communalism > 65; num_of_non_rural >= 3` |
| The Archbishop in Lund | The Council of Malmö | `regular_army_size >= 4` |
| Protectors of Lund | The Archbishop in Lund | `owns = location:lunds_domkyrkoforsamling_sk` |
| Answer to the Hanse | The Scania Market, A Town of Strangers | `any_owned_location = { has_building = building_type:counting_house count >= 2 }; any_owned_location = { has_building = building_type:merchants_guild count >= 1 }` |
| Silver of the Sound | Answer to the Hanse | `societal_value:capital_economy_vs_traditional_economy < -65; gold >= 150` |
| Gate of the Sound (slut) | The Scanian League, Beyond the Sound, Protectors of Lund, Silver of the Sound | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }; capital = { development >= 18 }` |

### The Fortress on the Helge (`du_m_qeu`)

*Synlig for:* `has_or_had_tag = QEU`

North-eastern Scania is forest, marsh and the broad Helge river. Our lords rule from the saddle, our peasants hunt and burn charcoal, and the border with the Göinge woods is never quiet. Kristianstad must become the bulwark of eastern Scania.

| Opgave | Kræver | Krav |
|---|---|---|
| The Helge River | – | `any_owned_location = { has_building = building_type:sawmill count >= 2 }; any_owned_location = { has_building = building_type:forest_village count >= 2 }` |
| The Port of Åhus | The Helge River | `location:aahus_sk = { owner ?= root NOT = { location_rank = location_rank:rural_settlement } }; location:aahus_sk = { owner ?= root has_building = building_type:wharf }` |
| Alum of Andrarum | The Helge River | `location:andrarum_sk = { owner ?= root rgo_level >= 2 }` |
| The Fortress | – | `capital = { has_building = building_type:castle }; regular_army_size >= 5` |
| Riders of the Plain | The Fortress | `any_owned_location = { has_building = building_type:training_fields count >= 2 }; societal_value:land_vs_naval < -45` |
| The Göinge Woods | The Fortress | `societal_value:aristocracy_vs_plutocracy < 20; any_estate = { estate_type = estate_type:peasants_estate power >= 0.25 }` |
| Lords of the Marches | – | `num_subjects >= 4; stability >= 25` |
| The Crossroads at Stoby | Lords of the Marches, Riders of the Plain | `owns = location:stoby_sk` |
| Into Central Scania | The Crossroads at Stoby | `owns = location:horby_sk owns = location:hoor_sk` |
| Manors of the Plain | Alum of Andrarum | `any_owned_location = { has_building = building_type:noble_villa count >= 3 }; any_estate = { estate_type = estate_type:nobles_estate power >= 0.3 }` |
| Market Town | The Port of Åhus, Manors of the Plain | `capital = { NOT = { location_rank = location_rank:rural_settlement } }; any_owned_location = { has_building = building_type:market_village count >= 2 }` |
| Bulwark of Eastern Scania (slut) | Into Central Scania, The Göinge Woods, Market Town | `regular_army_size >= 8; army_tradition >= 20` |

### City of the Bay (`du_m_qdi`)

*Synlig for:* `has_or_had_tag = QDI`

Aarhus is a bishop's town, a harbour and a republic of learned, free citizens. Our districts of Viby, Brabrand, Tilst and Mårslet are governed as one city. The lands beyond are rich, but we would rather buy them than burn them.

| Opgave | Kræver | Krav |
|---|---|---|
| The Cathedral of Saint Clement | – | `capital = { has_building = building_type:temple }; gold >= 80` |
| The Cathedral School | The Cathedral of Saint Clement | `capital = { has_building = building_type:library }; societal_value:spiritualist_vs_humanist > 72` |
| A City of Learning | The Cathedral School | `capital = { has_building = building_type:university }; societal_value:traditionalist_vs_innovative > 65` |
| Harbour on the Bay | – | `capital = { has_building = building_type:dock }; any_owned_location = { has_building = building_type:wharf count >= 1 }` |
| Grain for the Bay | Harbour on the Bay | `any_owned_location = { has_building = building_type:farming_village count >= 3 }; any_owned_location = { has_building = building_type:granary count >= 1 }` |
| Merchants of the Bay | Grain for the Bay | `any_owned_location = { has_building = building_type:counting_house count >= 2 }; societal_value:aristocracy_vs_plutocracy > 40` |
| One City, Many Districts | – | `societal_value:centralization_vs_decentralization < -40; stability >= 25` |
| Rights of Citizens | One City, Many Districts | `societal_value:serfdom_vs_free_subjects > 85; any_estate = { estate_type = estate_type:burghers_estate power >= 0.3 }` |
| Contracts, Not Conquest | One City, Many Districts | `societal_value:belligerent_vs_conciliatory > 55; prestige >= 25` |
| Rosenholm | Contracts, Not Conquest | `OR = { AND = { owns = location:halling_8230 } AND = { any_subject = { has_or_had_tag = QJJ } } }` |
| Guard of the Republic | Rights of Citizens | `regular_army_size >= 4; societal_value:quality_vs_quantity < -50` |
| City of the Bay (slut) | A City of Learning, Merchants of the Bay, Rosenholm, Guard of the Republic | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }; capital = { development >= 18 }` |

### Lord of the Heath (`du_m_qcw`)

*Synlig for:* `has_or_had_tag = QCW`

The heath of Hardsyssel is poor land and hard men. Our hall at Herning commands ten lords, and the riders of the heath respect only strength, faith and the old ways. The mink farmers grumble, Copenhagen sells our rights to Swedes, and the heath is waiting for a master.

| Opgave | Kræver | Krav |
|---|---|---|
| Sheep on the Heath | – | `any_owned_location = { has_building = building_type:sheep_farms count >= 4 }` |
| The Stocking Pedlars | Sheep on the Heath | `societal_value:capital_economy_vs_traditional_economy > 60; any_owned_location = { has_building = building_type:market_village count >= 2 }` |
| The Fur Houses | Sheep on the Heath | `any_owned_location = { raw_material ?= goods:fur rgo_level >= 2 count >= 3 }` |
| The Hall at Herning | – | `num_subjects >= 8; societal_value:centralization_vs_decentralization > 60` |
| Riders of the Heath | The Hall at Herning | `regular_army_size >= 6; societal_value:quality_vs_quantity > 25` |
| Faith of the Heath | – | `any_owned_location = { has_building = building_type:parish_church count >= 4 }; societal_value:spiritualist_vs_humanist < -45` |
| The Heath Thing | Faith of the Heath | `stability >= 30; societal_value:individualism_vs_communalism < -50` |
| Claims on Karup | Riders of the Heath | `societal_value:offensive_vs_defensive < -55` |
| Ride on Karup | Claims on Karup | `owns = location:karup_8603 owns = location:daugbjerg_8503` |
| The Hall on the Skive River | Ride on Karup | `owns = location:skive_8572` |
| East to the Lakes | The Hall on the Skive River | `owns = location:them_7998` |
| Lord of the Heath (slut) | The Stocking Pedlars, The Fur Houses, The Heath Thing, East to the Lakes | `num_locations >= 120; army_tradition >= 25` |

### The Lake Highlands (`du_m_qdf`)

*Synlig for:* `has_or_had_tag = QDF`

Silkeborg lies among lakes and beech forests where the Gudenå begins its journey to the sea. Our land is small, our men are few, and our neighbours are bigger. But the forest, the river and the water-mills can make the highlands strong.

| Opgave | Kræver | Krav |
|---|---|---|
| The Beech Forests | – | `any_owned_location = { has_building = building_type:sawmill count >= 2 }; any_owned_location = { has_building = building_type:forest_village count >= 2 }` |
| Barges on the Gudenå | The Beech Forests | `any_owned_location = { has_building = building_type:market_village count >= 2 }; capital = { NOT = { location_rank = location_rank:rural_settlement } }` |
| Water-Mills | The Beech Forests | `any_owned_location = { has_building = building_type:windmill count >= 2 }; capital = { has_building = building_type:du_bakery }` |
| Wool of the Highlands | – | `any_owned_location = { has_building = building_type:sheep_farms count >= 3 }` |
| Weavers of the Lakes | Wool of the Highlands, Water-Mills | `any_owned_location = { has_building = building_type:du_dairy count >= 1 }; societal_value:capital_economy_vs_traditional_economy > 30` |
| The Lake Lords | – | `num_subjects >= 4; stability >= 25` |
| Defence of the Lakes | The Lake Lords | `any_owned_location = { has_building = building_type:castle count >= 1 }; regular_army_size >= 3; societal_value:land_vs_naval < -55` |
| The Road to Ry | Defence of the Lakes | `societal_value:offensive_vs_defensive < -25` |
| Ry and the Southern Lakes | The Road to Ry | `owns = location:ry_9104` |
| The Monks of the Lakes | Barges on the Gudenå | `any_owned_location = { has_building = building_type:library count >= 1 }; any_estate = { estate_type = estate_type:clergy_estate power >= 0.2 }` |
| Market of the Highlands | The Monks of the Lakes, Weavers of the Lakes | `any_owned_location = { has_building = building_type:counting_house count >= 1 }; gold >= 100` |
| The Lake Highlands (slut) | Ry and the Southern Lakes, Market of the Highlands | `area:silkeborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; capital = { development >= 16 }` |

### Mouth of the Gudenå (`du_m_qde`)

*Synlig for:* `has_or_had_tag = QDE`

Randers sits where Denmark's longest river meets its fjord. Everything the Gudenå carries ends on our quays: grain, timber, hides and horses. Our council is balanced between old and new, and Djursland lies open to the east.

| Opgave | Kræver | Krav |
|---|---|---|
| The Quays of Randers | – | `capital = { has_building = building_type:dock }; any_owned_location = { has_building = building_type:wharf count >= 2 }` |
| The Glove-Makers | The Quays of Randers | `any_owned_location = { raw_material ?= goods:livestock rgo_level >= 2 count >= 2 }; any_owned_location = { has_building = building_type:du_dairy count >= 1 }` |
| Horses of the Gudenå | – | `any_owned_location = { raw_material ?= goods:horses rgo_level >= 2 count >= 1 }; any_owned_location = { has_building = building_type:training_fields count >= 1 }` |
| Fish of the Fjord | The Quays of Randers | `any_owned_location = { has_building = building_type:fishing_village count >= 4 }` |
| The Holy Spirit Monastery | – | `capital = { has_building = building_type:library }; any_estate = { estate_type = estate_type:clergy_estate power >= 0.2 }` |
| The Balanced Council | The Holy Spirit Monastery | `stability >= 40; societal_value:traditionalist_vs_innovative > -20 societal_value:traditionalist_vs_innovative < 20` |
| Lords of the Fjord | – | `num_subjects >= 3; regular_army_size >= 4` |
| Into Djursland | Lords of the Fjord, Horses of the Gudenå | `owns = location:alboege_8171` |
| The Harbour at Grenaa | Into Djursland | `owns = location:grenaa_8231` |
| Charter of Randers | The Glove-Makers, The Balanced Council | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }` |
| The River Market | Charter of Randers, Fish of the Fjord | `any_owned_location = { has_building = building_type:counting_house count >= 1 }; any_owned_location = { has_building = building_type:market_village count >= 3 }` |
| Mouth of the Gudenå (slut) | The Harbour at Grenaa, The River Market | `num_locations >= 90; capital = { development >= 18 }` |

### Heirs of Jelling (`du_m_qcv`)

*Synlig for:* `has_or_had_tag = QCV`

The mounds and runestones of Jelling stand on our land: here Gorm and Harald made Denmark. Vejle is a fjord town of farmers and furriers, proud of the old ways and eager for the fight. Kolding and Hedensted stand between us and the greatness our ancestors knew.

| Opgave | Kræver | Krav |
|---|---|---|
| The Stones of Jelling | – | `location:jelling_7905 = { owner ?= root has_building = building_type:parish_church }; societal_value:traditionalist_vs_innovative < 0` |
| The King's Hall | The Stones of Jelling | `prestige >= 30; any_owned_location = { has_building = building_type:noble_villa count >= 2 }` |
| The Vejle Fjord | – | `capital = { has_building = building_type:dock }; any_owned_location = { has_building = building_type:fishing_village count >= 3 }` |
| Furs of the Valleys | – | `any_owned_location = { raw_material ?= goods:fur rgo_level >= 2 count >= 3 }` |
| The Old Ways | Furs of the Valleys | `societal_value:capital_economy_vs_traditional_economy > 40; any_owned_location = { has_building = building_type:farming_village count >= 3 }` |
| Lords of the Valleys | – | `num_subjects >= 3; regular_army_size >= 4` |
| The Host of Vejle | Lords of the Valleys | `regular_army_size >= 6; societal_value:offensive_vs_defensive < -40` |
| North to Hedensted | The Host of Vejle | `owns = location:hedensted_7971` |
| The Triangle | North to Hedensted | `owns = location:trinitatis_7909 owns = location:sankt_nicolai_7927` |
| Market of Vejle | The Vejle Fjord, The Old Ways | `any_owned_location = { has_building = building_type:market_village count >= 2 }; capital = { NOT = { location_rank = location_rank:rural_settlement } }` |
| Saint Nicholas Church | The King's Hall | `capital = { has_building = building_type:temple }; societal_value:spiritualist_vs_humanist < 5` |
| Heirs of Jelling (slut) | The Triangle, Market of Vejle, Saint Nicholas Church | `num_locations >= 90; army_tradition >= 20` |

### Watch on the Sound (`du_m_qft`)

*Synlig for:* `has_or_had_tag = QFT`

Helsingborg looks across the narrowest part of the Sound to Zealand. Our tower of Kärnan watches every ship that passes, our hills hide coal, and our districts are governed by a free and open council. The Sound has two shores, and both could be watched from here.

| Opgave | Kræver | Krav |
|---|---|---|
| The Tower of Kärnan | – | `capital = { has_building = building_type:castle }; regular_army_size >= 3` |
| Ships on the Sound | The Tower of Kärnan | `capital = { has_building = building_type:dock }; regular_navy_size >= 8` |
| Coal of the Hills | – | `any_owned_location = { raw_material ?= goods:coal rgo_level >= 2 count >= 3 }` |
| Kilns and Brickworks | Coal of the Hills | `any_owned_location = { has_building = building_type:local_smelters count >= 1 }; any_owned_location = { has_building = building_type:counting_house count >= 1 }` |
| The Districts of Helsingborg | – | `societal_value:centralization_vs_decentralization < -45; stability >= 25` |
| The Harbour at Landskrona | The Districts of Helsingborg | `location:landskrona_sk = { owner ?= root NOT = { location_rank = location_rank:rural_settlement } }; location:landskrona_sk = { owner ?= root has_building = building_type:wharf }` |
| Free Trade on the Sound | The Districts of Helsingborg | `societal_value:serfdom_vs_free_subjects > 65; any_owned_location = { has_building = building_type:market_village count >= 2 }` |
| Claims on Ängelholm | Ships on the Sound | `regular_army_size >= 4` |
| The Bay of Skälderviken | Claims on Ängelholm | `owns = location:angelholm_sk` |
| Both Shores of the Sound | The Bay of Skälderviken, Kilns and Brickworks | `societal_value:belligerent_vs_conciliatory < 30` |
| The Far Shore | Both Shores of the Sound | `owns = location:sankt_olai_7437` |
| Watch on the Sound (slut) | The Harbour at Landskrona, Free Trade on the Sound, The Far Shore | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }; capital = { development >= 18 }` |

### Where Kings Are Hailed (`du_m_qdp`)

*Synlig for:* `has_or_had_tag = QDP`

At the Landsting of Viborg the kings of Denmark are hailed by the free men of Jutland. Our town is old, pious and proud, ruled by lords who ride to war down the Army Road. The old ways made Viborg great, and the old ways will make it great again.

| Opgave | Kræver | Krav |
|---|---|---|
| The Landsting | – | `prestige >= 30; societal_value:traditionalist_vs_innovative < -25` |
| The Law of Jutland | The Landsting | `stability >= 35; any_estate = { estate_type = estate_type:nobles_estate power >= 0.3 }` |
| The Kingmakers | The Law of Jutland | `prestige >= 50; num_subjects >= 2` |
| The Cathedral of Viborg | – | `capital = { has_building = building_type:temple }; any_owned_location = { has_building = building_type:parish_church count >= 3 }` |
| Town of Monasteries | The Cathedral of Viborg | `societal_value:spiritualist_vs_humanist < -20; any_owned_location = { has_building = building_type:library count >= 1 }` |
| The Army Road | – | `any_owned_location = { has_building = building_type:market_village count >= 2 }; societal_value:land_vs_naval < -50` |
| Lords on Horseback | The Army Road | `any_owned_location = { has_building = building_type:training_fields count >= 2 }; any_owned_location = { raw_material ?= goods:horses rgo_level >= 2 count >= 1 }; societal_value:aristocracy_vs_plutocracy < -25` |
| The Host of the Landsting | Lords on Horseback | `regular_army_size >= 6; societal_value:offensive_vs_defensive < -40` |
| Tjele and Bjerringbro | The Host of the Landsting | `owns = location:tjele_8634 owns = location:bjerringbro_8622` |
| West to Skive | Tjele and Bjerringbro | `owns = location:skive_8572` |
| The Old Ways | Town of Monasteries | `societal_value:capital_economy_vs_traditional_economy > 35; any_owned_location = { has_building = building_type:farming_village count >= 3 }` |
| Where Kings Are Hailed (slut) | The Kingmakers, West to Skive, The Old Ways | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }; army_tradition >= 20` |

### City of the Bishops (`du_m_qbg`)

*Synlig for:* `has_or_had_tag = QBG`

Roskilde was the royal seat before Copenhagen was more than a fishing village. The kings lie buried in our cathedral and the bishop still lives here. A learned, free and humanist town, it means to be Zealand's mind if Copenhagen is its purse.

| Opgave | Kræver | Krav |
|---|---|---|
| Burial Church of the Kings | – | `capital = { has_building = building_type:temple }; prestige >= 25` |
| The Bishop's Court | Burial Church of the Kings | `any_estate = { estate_type = estate_type:clergy_estate power >= 0.3 }` |
| The Cathedral School | The Bishop's Court | `capital = { has_building = building_type:library }; societal_value:spiritualist_vs_humanist > 58` |
| A Learned Town | The Cathedral School | `any_owned_location = { has_building = building_type:library count >= 2 }; societal_value:traditionalist_vs_innovative > 52` |
| Roskilde Fjord | – | `any_owned_location = { has_building = building_type:fishing_village count >= 3 }; capital = { has_building = building_type:wharf }` |
| Market of Zealand | Roskilde Fjord | `any_owned_location = { has_building = building_type:market_village count >= 2 }; any_owned_location = { has_building = building_type:counting_house count >= 1 }` |
| Free Citizens of Roskilde | Market of Zealand | `societal_value:serfdom_vs_free_subjects > 60; any_estate = { estate_type = estate_type:burghers_estate power >= 0.25 }` |
| Lords of the Fjord | – | `num_subjects >= 4; societal_value:quality_vs_quantity < -42` |
| Egedal | Lords of the Fjord | `owns = location:oelstykke_7409 owns = location:stenloese_7410` |
| South to Skovbo | Egedal | `owns = location:bjaeverskov_7537` |
| Counsel to the Crown | A Learned Town | `societal_value:belligerent_vs_conciliatory > 30; prestige >= 40` |
| City of the Bishops (slut) | Counsel to the Crown, Free Citizens of Roskilde, South to Skovbo | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }; capital = { development >= 18 }` |

### Iron of the King's River (`du_m_qcq`)

*Synlig for:* `has_or_had_tag = QCQ`

Vejen is a land of bog iron, heath and hard men by the King's River. We have no coast, no vassals and no patience. Our lords are pious, our farmers obey, and every one of them can hold a spear. The rich towns around us will learn what iron is for.

| Opgave | Kræver | Krav |
|---|---|---|
| Bog Iron | – | `any_owned_location = { raw_material ?= goods:iron rgo_level >= 2 count >= 3 }` |
| The Smelters | Bog Iron | `any_owned_location = { has_building = building_type:local_smelters count >= 2 }` |
| Smiths of the Heath | The Smelters | `any_owned_location = { has_building = building_type:armory count >= 1 }; regular_army_size >= 5` |
| The Levy of Every Farm | – | `societal_value:quality_vs_quantity > 40; any_owned_location = { has_building = building_type:training_fields count >= 2 }` |
| Churches of the King's River | – | `any_owned_location = { has_building = building_type:parish_church count >= 4 }; societal_value:spiritualist_vs_humanist < -55` |
| Lords of the Heath | Churches of the King's River | `societal_value:aristocracy_vs_plutocracy < -25; any_owned_location = { has_building = building_type:noble_villa count >= 2 }` |
| South Across the River | Smiths of the Heath, The Levy of Every Farm | `societal_value:offensive_vs_defensive < -55` |
| Vojens and Gram | South Across the River | `owns = location:vojens_8975 owns = location:gram_8946` |
| The Fall of Ribe | Vojens and Gram | `owns = location:ribe_domsogn_8886 owns = location:bramming_8900` |
| North to Varde | The Fall of Ribe | `owns = location:varde_8873` |
| The Thing at Askov | Lords of the Heath | `stability >= 30; societal_value:individualism_vs_communalism < -50` |
| Iron of the King's River (slut) | North to Varde, The Thing at Askov | `num_locations >= 90; army_tradition >= 30` |

### The Southern Archipelago (`du_m_qce`)

*Synlig for:* `has_or_had_tag = QCE`

Svendborg rules a scattered sea of islands south of Funen: Tåsinge, Thurø, Langeland and a dozen more, with vassals as far as Nakskov and Als. Our people are sailors, our council is free and open, and our wealth comes from the water. The archipelago must become one maritime power.

| Opgave | Kræver | Krav |
|---|---|---|
| Skippers of the Islands | – | `capital = { has_building = building_type:dock }; any_owned_location = { has_building = building_type:wharf count >= 3 }` |
| The Archipelago Fleet | Skippers of the Islands | `regular_navy_size >= 12; societal_value:land_vs_naval > 35` |
| Letters of Marque | The Archipelago Fleet | `regular_navy_size >= 18` |
| Fish of the Belts | – | `any_owned_location = { has_building = building_type:fishing_village count >= 5 }` |
| Orchards of South Funen | Fish of the Belts | `any_owned_location = { has_building = building_type:du_mosteri count >= 1 }; any_owned_location = { has_building = building_type:farming_village count >= 3 }` |
| Trade of the Islands | Orchards of South Funen, Skippers of the Islands | `any_owned_location = { has_building = building_type:counting_house count >= 2 }; societal_value:capital_economy_vs_traditional_economy < -50` |
| Council of Skippers | – | `societal_value:individualism_vs_communalism > 55; stability >= 30` |
| Lords of the Islands | Council of Skippers | `num_subjects >= 10` |
| Ærø | Lords of the Islands, The Archipelago Fleet | `OR = { AND = { owns = location:aeroeskoebing_7713 } AND = { location:aeroeskoebing_7713 = { is_owned_or_owned_by_subjects_or_below_of = root } } }` |
| Across to Lolland | Ærø | `owns = location:birket_7641` |
| The Great Shipyard | Letters of Marque, Trade of the Islands | `capital = { location_building_level = { building_type = building_type:dock value >= 2 } }; gold >= 150` |
| The Southern Archipelago (slut) | The Great Shipyard, Across to Lolland | `regular_navy_size >= 25; capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }` |

### Heart of Zealand (`du_m_qbn`)

*Synlig for:* `has_or_had_tag = QBN`

Ringsted lies in the middle of Zealand, far from any coast, among the best grain fields of the realm. The Valdemar kings lie in Saint Bendt's church and Zealand's Landsting meets here. We are neither old nor new, neither proud nor humble: we are the centre.

| Opgave | Kræver | Krav |
|---|---|---|
| Grain of Central Zealand | – | `any_owned_location = { has_building = building_type:farming_village count >= 4 }; any_owned_location = { has_building = building_type:windmill count >= 2 }` |
| The Granaries | Grain of Central Zealand | `any_owned_location = { has_building = building_type:granary count >= 1 }; gold >= 100` |
| Roads of Zealand | Grain of Central Zealand | `any_owned_location = { has_building = building_type:market_village count >= 3 }` |
| Saint Bendt's Church | – | `capital = { has_building = building_type:temple }; prestige >= 25` |
| The Zealand Landsting | Saint Bendt's Church | `stability >= 35; prestige >= 40` |
| Balance of the Estates | The Zealand Landsting | `any_estate = { estate_type = estate_type:nobles_estate power >= 0.2 }; any_estate = { estate_type = estate_type:peasants_estate power >= 0.2 }; societal_value:aristocracy_vs_plutocracy > -20 societal_value:aristocracy_vs_plutocracy < 25` |
| Lords of the Centre | – | `num_subjects >= 3; societal_value:land_vs_naval < -52` |
| Defence of the Centre | Lords of the Centre | `any_owned_location = { has_building = building_type:castle count >= 1 }; regular_army_size >= 4; societal_value:offensive_vs_defensive > 20` |
| A Harbour at Køge | Defence of the Centre | `owns = location:koege_7206` |
| Vallø and Stevns | A Harbour at Køge | `owns = location:endeslev_7546` |
| Charter of Ringsted | The Granaries, Roads of Zealand | `capital = { NOT = { location_rank = location_rank:rural_settlement } }; any_owned_location = { has_building = building_type:counting_house count >= 1 }` |
| Heart of Zealand (slut) | Balance of the Estates, Vallø and Stevns, Charter of Ringsted | `num_locations >= 70; stability >= 45` |

### The Sound Toll (`du_m_qax`)

*Synlig for:* `has_or_had_tag = QAX`

Helsingør is a small town at the narrowest point of the Sound, held as a vassal by the lord of Græsted-Gilleleje. Every ship between the Baltic and the North Sea must pass under our walls. A castle on the point and a toll on the water could make this little town the richest in the North.

| Opgave | Kræver | Krav |
|---|---|---|
| The Castle on the Point | – | `capital = { has_building = building_type:castle }` |
| Garrison of the Point | The Castle on the Point | `regular_army_size >= 2; societal_value:quality_vs_quantity < -28` |
| Free of Gilleleje | Garrison of the Point | `is_subject = no` |
| The Sound Toll | The Castle on the Point | `regular_navy_size >= 5; any_owned_location = { has_building = building_type:counting_house count >= 1 }` |
| The Toll Chamber | The Sound Toll | `gold >= 150; stability >= 30` |
| Ships of the Sound | The Sound Toll | `capital = { has_building = building_type:dock }; regular_navy_size >= 10` |
| Coal of Hellebæk | – | `any_owned_location = { raw_material ?= goods:coal rgo_level >= 2 count >= 2 }` |
| The Smiths of Hellebæk | Coal of Hellebæk | `any_owned_location = { has_building = building_type:local_smelters count >= 1 }; location:hellebaek_7442 = { owner ?= root }` |
| Settle with Gilleleje | Free of Gilleleje | `regular_army_size >= 3` |
| The North Coast | Settle with Gilleleje | `owns = location:blistrup_7392 owns = location:gilleleje_7431` |
| Fredensborg | The North Coast | `owns = location:asminderoed_7444` |
| Keepers of the Sound (slut) | The Toll Chamber, Ships of the Sound, The Smiths of Hellebæk, Fredensborg | `capital = { NOT = { location_rank = location_rank:rural_settlement } }; stability >= 40` |

### Town on the Suså (`du_m_qbt`)

*Synlig for:* `has_or_had_tag = QBT`

Næstved is a river town with friends in Lübeck and a vassal, Kalundborg, larger than itself. Our farmers are many and our burghers trade with the Hanse. Between the river, the monastery and the glass furnaces of the woods, South Zealand can be ours.

| Opgave | Kræver | Krav |
|---|---|---|
| Barges on the Suså | – | `any_owned_location = { has_building = building_type:market_village count >= 2 }; any_owned_location = { has_building = building_type:wharf count >= 1 }` |
| Friends in Lübeck | Barges on the Suså | `any_owned_location = { has_building = building_type:counting_house count >= 1 }; gold >= 100` |
| The Guilds of Næstved | Friends in Lübeck | `capital = { NOT = { location_rank = location_rank:rural_settlement } }; any_owned_location = { has_building = building_type:du_bakery count >= 1 }` |
| The Southern Woods | – | `any_owned_location = { has_building = building_type:sawmill count >= 2 }; any_owned_location = { has_building = building_type:forest_village count >= 1 }` |
| Glass of the Woods | The Southern Woods | `any_owned_location = { has_building = building_type:forest_village count >= 3 }; gold >= 80` |
| The Monastery School | – | `location:herlufsholm_7306 = { owner ?= root has_building = building_type:parish_church }; any_owned_location = { has_building = building_type:library count >= 1 }` |
| The Abbey at Sorø | The Monastery School | `location:soroe_7383 = { owner ?= root }; any_estate = { estate_type = estate_type:clergy_estate power >= 0.25 }` |
| The Lord of Kalundborg | – | `num_subjects >= 2; prestige >= 30` |
| The Peasant Levy | The Lord of Kalundborg | `regular_army_size >= 5; societal_value:quality_vs_quantity > 28` |
| The Goose Tower | The Peasant Levy | `owns = location:vordingborg_7469` |
| Burghers and Farmers | The Guilds of Næstved | `societal_value:serfdom_vs_free_subjects > 40; stability >= 30` |
| Town on the Suså (slut) | Glass of the Woods, The Abbey at Sorø, The Goose Tower, Burghers and Farmers | `num_locations >= 90; capital = { development >= 18 }` |

### Castle on the Border (`du_m_qic`)

*Synlig for:* `OR = { has_or_had_tag = QIC has_or_had_tag = QCU }`

Kolding stands where Jutland meets Schleswig and the Little Belt meets the fjord. Our lords hold vassals on both sides of the water, our farmers keep the old ways and our council looks south with a soldier's eye. Koldinghus must become the gate of the realm.

| Opgave | Kræver | Krav |
|---|---|---|
| The Town of Kolding | – | `location:sankt_nicolai_7927 = { owner ?= root }; location:sankt_nicolai_7927 = { owner ?= root NOT = { location_rank = location_rank:rural_settlement } }` |
| Koldinghus | The Town of Kolding | `location:sankt_nicolai_7927 = { owner ?= root has_building = building_type:castle }; regular_army_size >= 4` |
| The King's River | Koldinghus | `any_owned_location = { has_building = building_type:castle count >= 2 }; societal_value:offensive_vs_defensive < -28` |
| The Little Belt Crossing | – | `num_subjects >= 6; any_owned_location = { has_building = building_type:wharf count >= 1 }` |
| Lords of Both Shores | The Little Belt Crossing | `stability >= 30; prestige >= 25` |
| The Ox Road | – | `any_owned_location = { raw_material ?= goods:livestock rgo_level >= 2 count >= 2 }; societal_value:capital_economy_vs_traditional_economy > 45` |
| The Ox Market | The Ox Road | `any_owned_location = { has_building = building_type:market_village count >= 2 }; any_owned_location = { has_building = building_type:du_dairy count >= 1 }` |
| Old Families | The Ox Market | `societal_value:individualism_vs_communalism < -30; any_owned_location = { has_building = building_type:noble_villa count >= 2 }` |
| Claims South of the River | The King's River | `regular_army_size >= 6` |
| Into Schleswig | Claims South of the River | `owns = location:vojens_8975 owns = location:vor_frue_8961` |
| Assens Across the Belt | Into Schleswig, Lords of Both Shores | `owns = location:assens_7801` |
| Castle on the Border (slut) | Assens Across the Belt, Old Families | `num_locations >= 80; army_tradition >= 20` |

### The Queen's Island (`du_m_qbu`)

*Synlig for:* `has_or_had_tag = QBU`

Nykøbing guards the Guldborg Sound between Falster and Lolland, and its castle has housed widowed queens. We are a seafaring people of many farmers and few lords, old in our ways yet open to the sea. Falster should be one island under one town.

| Opgave | Kræver | Krav |
|---|---|---|
| Nykøbing Castle | – | `capital = { has_building = building_type:castle }; prestige >= 20` |
| The Queen's Dower | Nykøbing Castle | `gold >= 120; stability >= 30` |
| The Guldborg Sound | – | `capital = { has_building = building_type:dock }; any_owned_location = { has_building = building_type:wharf count >= 2 }` |
| Ships of Falster | The Guldborg Sound | `regular_navy_size >= 10; societal_value:land_vs_naval > 45` |
| Fishers of Gedser | The Guldborg Sound | `any_owned_location = { has_building = building_type:fishing_village count >= 3 }; any_owned_location = { has_building = building_type:du_saltery count >= 1 }` |
| Fields of Falster | – | `any_owned_location = { has_building = building_type:farming_village count >= 4 }; any_owned_location = { has_building = building_type:windmill count >= 1 }` |
| Roots and Sugar | Fields of Falster | `any_owned_location = { raw_material ?= goods:sugar rgo_level >= 2 count >= 1 }` |
| Farmers of Falster | Fields of Falster | `societal_value:quality_vs_quantity > 45; regular_army_size >= 4` |
| One Falster | Farmers of Falster | `owns = location:stubbekoebing_7607 owns = location:noerre_alslev_7613` |
| East Lolland | One Falster, Ships of Falster | `owns = location:sakskoebing_7642 owns = location:nysted_vantore_9319` |
| The Old Customs | The Queen's Dower | `societal_value:traditionalist_vs_innovative < -33; any_owned_location = { has_building = building_type:parish_church count >= 3 }` |
| The Queen's Island (slut) | The Old Customs, East Lolland, Fishers of Gedser, Roots and Sugar | `area:guldborgsund_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 1.0 } }; capital = { NOT = { location_rank = location_rank:rural_settlement } }` |

## Age 2: kulturgrupper og unikke missioner

### The King's Residence (`du_m2_koebenhavnsk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:koebenhavnsk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

The crown has come to stay in Copenhagen, and every parish around the city feels it. The king's court needs beer, bread, clerks and loyal suburbs, and pays well for all of them.

| Opgave | Kræver | Krav |
|---|---|---|
| The Brewers' Guild | – | `OR = { AND = { has_advance = dku_koebenhavnsk_2_bryggerlavet } AND = { any_owned_location = { has_building = building_type:du_mosteri count >= 2 } } }` |
| The King's Residence | – | `OR = { AND = { has_advance = dku_koebenhavnsk_2_kongens_residens } AND = { prestige >= 40 } }` |
| Bread for the Capital | The Brewers' Guild | `any_owned_location = { has_building = building_type:du_bakery count >= 2 }; any_owned_location = { has_building = building_type:granary count >= 1 }` |
| Clerks of the Chancery | The King's Residence | `any_owned_location = { has_building = building_type:library count >= 1 }; any_owned_location = { has_building = building_type:local_schools count >= 1 }` |
| Suburb of the Capital | Bread for the Capital | `capital = { NOT = { location_rank = location_rank:rural_settlement } }; stability >= 30` |
| Guard of the Approaches | Clerks of the Chancery | `regular_army_size >= 3; any_owned_location = { has_building = building_type:castle count >= 1 }` |
| Heart of the Capital Region (slut) | Suburb of the Capital, Guard of the Approaches | `capital = { development >= 16 }` |

### Cathedral and Landsting (`du_m2_storstad`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:storstad_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

The great towns of the North have cathedral schools and host the Landsting of their provinces. In the new age, learning and law make a city as much as walls and harbours.

| Opgave | Kræver | Krav |
|---|---|---|
| The Cathedral School | – | `OR = { AND = { has_advance = dku_storstad_2_domskolen } AND = { any_owned_location = { has_building = building_type:library count >= 2 } } }` |
| Town of the Landsting | – | `OR = { AND = { has_advance = dku_storstad_2_landstingsbyen } AND = { stability >= 40 } }` |
| The New Learning | The Cathedral School | `OR = { AND = { has_embraced_institution = institution:renaissance } AND = { capital = { has_building = building_type:university } } }` |
| Town Hall and Court | Town of the Landsting | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }; any_estate = { estate_type = estate_type:burghers_estate power >= 0.3 }` |
| Merchants of the Great Town | Town Hall and Court | `any_owned_location = { has_building = building_type:counting_house count >= 2 }; regular_navy_size >= 6` |
| A University | The New Learning | `capital = { has_building = building_type:university }; gold >= 150` |
| City of Learning and Law (slut) | Merchants of the Great Town, A University | `capital = { development >= 20 }` |

### Church and Skipper (`du_m2_koebstad`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:koebstad_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

The market towns of the realm have their own churches and their own skippers' guilds. In the new age the small town that trades by sea can grow as rich as any lord.

| Opgave | Kræver | Krav |
|---|---|---|
| The Town Church | – | `OR = { AND = { has_advance = dku_koebstad_2_koebstadskirken } AND = { capital = { has_building = building_type:temple } } }` |
| The Skippers' Guild | – | `OR = { AND = { has_advance = dku_koebstad_2_skipperlavet } AND = { any_owned_location = { has_building = building_type:wharf count >= 2 } } }` |
| The Market Square | The Town Church | `capital = { NOT = { location_rank = location_rank:rural_settlement } }; any_owned_location = { has_building = building_type:market_village count >= 2 }` |
| Voyages of Trade | The Skippers' Guild | `regular_navy_size >= 6; any_owned_location = { has_building = building_type:counting_house count >= 1 }` |
| Town Privileges | The Market Square | `stability >= 35; any_estate = { estate_type = estate_type:burghers_estate power >= 0.25 }` |
| The Latin School | Town Privileges | `any_owned_location = { has_building = building_type:library count >= 1 }; any_owned_location = { has_building = building_type:local_schools count >= 1 }` |
| A Proud Market Town (slut) | Voyages of Trade, The Latin School | `capital = { development >= 16 }` |

### Lime and Forest (`du_m2_nordjysk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:nordjysk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

North Jutland has the chalk hills of Himmerland and the great Rold forest. In the new age, the lime that builds churches and the timber that builds ships can make the north rich.

| Opgave | Kræver | Krav |
|---|---|---|
| Lime of Himmerland | – | `OR = { AND = { has_advance = dku_nordjysk_2_himmerlands_kalk } AND = { any_owned_location = { raw_material ?= goods:stone rgo_level >= 2 count >= 1 } } }` |
| The Rold Forest | – | `OR = { AND = { has_advance = dku_nordjysk_2_rold_skov } AND = { any_owned_location = { has_building = building_type:sawmill count >= 2 } } }` |
| Lime Kilns | Lime of Himmerland | `any_owned_location = { has_building = building_type:local_smelters count >= 1 }; any_owned_location = { has_building = building_type:market_village count >= 2 }` |
| Herring of the North | – | `any_owned_location = { has_building = building_type:fishing_village count >= 3 }` |
| Oak for Ships | The Rold Forest | `regular_navy_size >= 5; any_owned_location = { has_building = building_type:wharf count >= 1 }` |
| Churches of Chalk | Lime Kilns | `any_owned_location = { has_building = building_type:parish_church count >= 4 }` |
| Wealth of the North (slut) | Churches of Chalk, Oak for Ships, Herring of the North | `stability >= 35` |

### Stockings and Peat (`du_m2_vestjysk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:vestjysk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

The heath of West Jutland gives nothing for free. But a land of knitters, peat-cutters and drovers can trade its stockings in Hamburg and warm its houses with its own bogs.

| Opgave | Kræver | Krav |
|---|---|---|
| The Stocking Pedlars | – | `OR = { AND = { has_advance = dku_vestjysk_2_hosekraemmerne } AND = { any_owned_location = { has_building = building_type:sheep_farms count >= 3 } } }` |
| Peat and Heather | – | `OR = { AND = { has_advance = dku_vestjysk_2_toerv_og_lyng } AND = { any_owned_location = { has_building = building_type:forest_village count >= 2 } } }` |
| Flocks of the Heath | The Stocking Pedlars | `any_owned_location = { has_building = building_type:sheep_farms count >= 4 }` |
| Heath Churches | Peat and Heather | `any_owned_location = { has_building = building_type:parish_church count >= 3 }; societal_value:spiritualist_vs_humanist < 0` |
| Riders of the Heath | Flocks of the Heath | `regular_army_size >= 4` |
| Heath Market | Heath Churches | `any_owned_location = { has_building = building_type:market_village count >= 2 }` |
| Thrift of the West (slut) | Riders of the Heath, Heath Market | `stability >= 30` |

### Forests and Manors (`du_m2_oestjysk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:oestjysk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

East Jutland has the beech forests of the lake highlands and the great manors of Djursland. In the new age, timber and grain flow down the Gudenå to the sea, and the manor lords grow rich on both.

| Opgave | Kræver | Krav |
|---|---|---|
| Forests of the Highlands | – | `OR = { AND = { has_advance = dku_oestjysk_2_soehoejlandets_skove } AND = { any_owned_location = { has_building = building_type:sawmill count >= 2 } } }` |
| Manors of Djursland | – | `OR = { AND = { has_advance = dku_oestjysk_2_djurslands_herregaarde } AND = { any_owned_location = { has_building = building_type:noble_villa count >= 2 } } }` |
| Down the Gudenå | Forests of the Highlands | `any_owned_location = { has_building = building_type:market_village count >= 2 }` |
| Grain of the Manors | Manors of Djursland | `any_owned_location = { has_building = building_type:farming_village count >= 3 }` |
| East Jutland Horse | Grain of the Manors | `regular_army_size >= 4; any_owned_location = { has_building = building_type:training_fields count >= 1 }` |
| Mills on the River | Down the Gudenå | `any_owned_location = { has_building = building_type:windmill count >= 2 }` |
| Rich East Jutland (slut) | East Jutland Horse, Mills on the River | `stability >= 35` |

### Oxen and Chapter (`du_m2_sydjysk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:sydjysk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

South Jutland sends its oxen south by the thousand and its sons to the cathedral school at Ribe. In the new age, the drover's road and the chapter's lands are both worth more than ever.

| Opgave | Kræver | Krav |
|---|---|---|
| Oxen to the South | – | `OR = { AND = { has_advance = dku_sydjysk_2_oeksneudskibningen } AND = { any_owned_location = { raw_material ?= goods:livestock rgo_level >= 2 count >= 2 } } }` |
| The Cathedral Chapter | – | `OR = { AND = { has_advance = dku_sydjysk_2_domkapitlet } AND = { any_estate = { estate_type = estate_type:clergy_estate power >= 0.25 } } }` |
| Marsh Meadows | Oxen to the South | `any_owned_location = { has_building = building_type:farming_village count >= 2 }; any_owned_location = { has_building = building_type:du_dairy count >= 1 }` |
| Sons for the School | The Cathedral Chapter | `any_owned_location = { has_building = building_type:library count >= 1 }` |
| The Drovers' Road | Marsh Meadows | `any_owned_location = { has_building = building_type:market_village count >= 2 }; regular_army_size >= 3` |
| Watch on the Border | Sons for the School | `any_owned_location = { has_building = building_type:castle count >= 1 }` |
| Wealth of the South (slut) | The Drovers' Road, Watch on the Border | `stability >= 35` |

### Dike and Castle (`du_m2_soenderjysk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:soenderjysk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

South of the King's River the land must be defended twice: against the North Sea with dikes and against the lords of the south with castles. In the new age, the dike-builders and the castle-builders of Schleswig both prosper.

| Opgave | Kræver | Krav |
|---|---|---|
| The Dike Against the North Sea | – | `OR = { AND = { has_advance = dku_soenderjysk_2_diget_mod_vesterhavet } AND = { any_owned_location = { has_building = building_type:farming_village count >= 3 } } }` |
| The Castle by the Sound | – | `OR = { AND = { has_advance = dku_soenderjysk_2_slottet_ved_sundet } AND = { any_owned_location = { has_building = building_type:castle count >= 1 } } }` |
| Marsh Grain | The Dike Against the North Sea | `any_owned_location = { has_building = building_type:windmill count >= 1 }; any_owned_location = { has_building = building_type:granary count >= 1 }` |
| Garrisons of the March | The Castle by the Sound | `regular_army_size >= 4` |
| Marsh Cattle | Marsh Grain | `any_owned_location = { raw_material ?= goods:livestock rgo_level >= 2 count >= 1 }` |
| Court of the Duke | Garrisons of the March | `prestige >= 30` |
| Strong March (slut) | Marsh Cattle, Court of the Duke | `stability >= 35` |

### Shipwrights and Grain (`du_m2_fynsk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:fynsk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

Funen is the garden of the realm, and its sounds are full of shipwrights. In the new age the island sells its surplus grain to the whole Baltic, in ships it builds itself.

| Opgave | Kræver | Krav |
|---|---|---|
| Shipwrights of the Sound | – | `OR = { AND = { has_advance = dku_fynsk_2_sundets_skibsbyggere } AND = { any_owned_location = { has_building = building_type:wharf count >= 2 } } }` |
| The Funen Surplus | – | `OR = { AND = { has_advance = dku_fynsk_2_det_fynske_kornoverskud } AND = { any_owned_location = { has_building = building_type:farming_village count >= 3 } } }` |
| Grain by Sea | The Funen Surplus | `any_owned_location = { has_building = building_type:granary count >= 1 }; regular_navy_size >= 5` |
| Funen Ships | Shipwrights of the Sound | `regular_navy_size >= 8` |
| Garden of the Realm | Grain by Sea | `any_owned_location = { has_building = building_type:du_mosteri count >= 1 }` |
| Funen Manors | Funen Ships | `any_owned_location = { has_building = building_type:noble_villa count >= 2 }` |
| Prosperous Funen (slut) | Garden of the Realm, Funen Manors | `stability >= 35` |

### Monastery and Crown Lands (`du_m2_sjaellandsk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:sjaellandsk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

Zealand is the island of monasteries and crown estates. The monks of Esrum farm better than anyone, and the king's lands in the north grow every year. In the new age, Zealand's lords learn from both.

| Opgave | Kræver | Krav |
|---|---|---|
| Farming of Esrum | – | `OR = { AND = { has_advance = dku_sjaellandsk_2_esrum_klosters_landbrug } AND = { any_owned_location = { has_building = building_type:farming_village count >= 3 } } }` |
| Crown Lands of Zealand | – | `OR = { AND = { has_advance = dku_sjaellandsk_2_krongodset_i_nordsjaelland } AND = { any_estate = { estate_type = estate_type:crown_estate power >= 0.25 } } }` |
| Mills of Zealand | Farming of Esrum | `any_owned_location = { has_building = building_type:windmill count >= 2 }; any_owned_location = { has_building = building_type:du_bakery count >= 1 }` |
| Monastery Schools | Farming of Esrum | `any_owned_location = { has_building = building_type:library count >= 1 }; any_owned_location = { has_building = building_type:parish_church count >= 3 }` |
| Royal Roads | Crown Lands of Zealand | `any_owned_location = { has_building = building_type:market_village count >= 2 }` |
| Zealand Levy | Royal Roads | `regular_army_size >= 4` |
| Fruitful Zealand (slut) | Mills of Zealand, Monastery Schools, Zealand Levy | `stability >= 35` |

### Estates and Nuns (`du_m2_lollandsk_falstersk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:lollandsk_falstersk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

Lolland and Falster are islands of great estates and black soil. The Bridgettine nuns of Maribo teach and pray, and the estate lords grow grain for half the Baltic.

| Opgave | Kræver | Krav |
|---|---|---|
| The Great Estates | – | `OR = { AND = { has_advance = dku_lollandsk_falstersk_2_godsernes_lolland } AND = { any_owned_location = { has_building = building_type:noble_villa count >= 2 } } }` |
| The Bridgettines of Maribo | – | `OR = { AND = { has_advance = dku_lollandsk_falstersk_2_birgittinerklosteret } AND = { any_estate = { estate_type = estate_type:clergy_estate power >= 0.25 } } }` |
| Black Soil | The Great Estates | `any_owned_location = { has_building = building_type:farming_village count >= 3 }; any_owned_location = { has_building = building_type:windmill count >= 1 }` |
| Grain Harbours | Black Soil | `any_owned_location = { has_building = building_type:wharf count >= 2 }` |
| School of the Nuns | The Bridgettines of Maribo | `any_owned_location = { has_building = building_type:library count >= 1 }` |
| Island Ships | Grain Harbours | `regular_navy_size >= 5` |
| Rich Islands (slut) | School of the Nuns, Island Ships | `stability >= 35` |

### Stone and Hanse (`du_m2_bornholmsk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:bornholmsk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

Bornholm is a rock in the Baltic, quarried by its stonecutters and visited by every Hanseatic captain. In the new age, granite and herring both find buyers across the sea.

| Opgave | Kræver | Krav |
|---|---|---|
| The Stonecutters | – | `OR = { AND = { has_advance = dku_bornholmsk_2_stenhuggerne } AND = { any_owned_location = { raw_material ?= goods:stone rgo_level >= 2 count >= 1 } } }` |
| The Hanseatic Voyage | – | `OR = { AND = { has_advance = dku_bornholmsk_2_hansafarten } AND = { any_owned_location = { has_building = building_type:counting_house count >= 1 } } }` |
| Baltic Herring | The Hanseatic Voyage | `any_owned_location = { has_building = building_type:fishing_village count >= 3 }; any_owned_location = { has_building = building_type:du_saltery count >= 1 }` |
| Castle on the Rock | The Stonecutters | `any_owned_location = { has_building = building_type:castle count >= 1 }` |
| Ships of the Rock | Baltic Herring | `regular_navy_size >= 5` |
| Round Churches | Castle on the Rock | `any_owned_location = { has_building = building_type:parish_church count >= 3 }` |
| Pearl of the Baltic (slut) | Ships of the Rock, Round Churches | `stability >= 35` |

### Fishing Villages and Privileges (`du_m2_skaansk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:skaansk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

Scania is the richest land of the realm: herring on its shores, grain on its plain and privileged towns on its coast. In the new age, Scanian towns and villages both claim their share.

| Opgave | Kræver | Krav |
|---|---|---|
| Fishing Villages of Österlen | – | `OR = { AND = { has_advance = dku_skaansk_2_oesterlens_fiskerlejer } AND = { any_owned_location = { has_building = building_type:fishing_village count >= 3 } } }` |
| Privileges of the Trading Towns | – | `OR = { AND = { has_advance = dku_skaansk_2_handelsbyens_privilegier } AND = { any_estate = { estate_type = estate_type:burghers_estate power >= 0.25 } } }` |
| Grain of the Plain | Fishing Villages of Österlen | `any_owned_location = { has_building = building_type:farming_village count >= 3 }` |
| Scanian Markets | Privileges of the Trading Towns | `any_owned_location = { has_building = building_type:market_village count >= 2 }; any_owned_location = { has_building = building_type:counting_house count >= 1 }` |
| Scanian Ships | Scanian Markets | `regular_navy_size >= 6` |
| Scanian Manors | Grain of the Plain | `any_owned_location = { has_building = building_type:noble_villa count >= 2 }` |
| Rich Scania (slut) | Scanian Ships, Scanian Manors | `stability >= 35` |

### Oak and Salmon (`du_m2_hallandsk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:hallandsk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

Halland is a coast of oak forests and salmon rivers. In the new age the fleets of the North need its timber, and the tables of the North want its salmon.

| Opgave | Kræver | Krav |
|---|---|---|
| Ship Timber for the Fleet | – | `OR = { AND = { has_advance = dku_hallandsk_2_skibstoemmer_til_flaaden } AND = { any_owned_location = { has_building = building_type:sawmill count >= 2 } } }` |
| The Salmon Weirs | – | `OR = { AND = { has_advance = dku_hallandsk_2_laksegaardene } AND = { any_owned_location = { has_building = building_type:fishing_village count >= 2 } } }` |
| Halland Yards | Ship Timber for the Fleet | `any_owned_location = { has_building = building_type:wharf count >= 2 }` |
| Salted Salmon | The Salmon Weirs | `any_owned_location = { has_building = building_type:du_saltery count >= 1 }` |
| The Border Forests | Halland Yards | `any_owned_location = { has_building = building_type:castle count >= 1 }; regular_army_size >= 3` |
| Halland Squadron | Salted Salmon | `regular_navy_size >= 5` |
| Proud Halland (slut) | The Border Forests, Halland Squadron | `stability >= 35` |

### Fishers and Parishes (`du_m2_blekingsk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:blekingsk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

Blekinge is a coast of skerries, fishers and small parishes on the edge of the realm. In the new age its people take to the sea and its parishes grow strong.

| Opgave | Kræver | Krav |
|---|---|---|
| Fishers of Listerland | – | `OR = { AND = { has_advance = dku_blekingsk_2_listerlandets_fiskere } AND = { any_owned_location = { has_building = building_type:fishing_village count >= 2 } } }` |
| Parishes of Blekinge | – | `OR = { AND = { has_advance = dku_blekingsk_2_blekinges_sogne } AND = { any_owned_location = { has_building = building_type:parish_church count >= 3 } } }` |
| The Skerries | Fishers of Listerland | `any_owned_location = { has_building = building_type:wharf count >= 1 }; regular_navy_size >= 4` |
| Forests of Blekinge | Parishes of Blekinge | `any_owned_location = { has_building = building_type:sawmill count >= 1 }` |
| Free Shooters | Forests of Blekinge | `regular_army_size >= 3` |
| Coastal Trade | The Skerries | `any_owned_location = { has_building = building_type:market_village count >= 1 }` |
| Strong Blekinge (slut) | Free Shooters, Coastal Trade | `stability >= 35` |

### Estates and Gottorp (`du_m2_sydslesvigsk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:sydslesvigsk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

South Schleswig is a land of great noble estates on the Schwansen peninsula and the ducal castle of Gottorp. In the new age its lords build in brick and its dukes hold a court to rival kings'.

| Opgave | Kræver | Krav |
|---|---|---|
| Estates of Schwansen | – | `OR = { AND = { has_advance = dku_sydslesvigsk_2_svansoes_godser } AND = { any_owned_location = { has_building = building_type:noble_villa count >= 2 } } }` |
| Gottorp Castle | – | `OR = { AND = { has_advance = dku_sydslesvigsk_2_gottorp_slot } AND = { any_owned_location = { has_building = building_type:castle count >= 1 } } }` |
| Angeln Cattle | Estates of Schwansen | `any_owned_location = { has_building = building_type:du_dairy count >= 1 }; any_owned_location = { raw_material ?= goods:livestock rgo_level >= 2 count >= 1 }` |
| The Ducal Court | Gottorp Castle | `prestige >= 30` |
| The Knighthood | The Ducal Court | `regular_army_size >= 4; any_owned_location = { has_building = building_type:training_fields count >= 1 }` |
| Markets of the Schlei | Angeln Cattle | `any_owned_location = { has_building = building_type:market_village count >= 2 }` |
| Lords of South Schleswig (slut) | The Knighthood, Markets of the Schlei | `stability >= 35` |

### After the Great Drowning (`du_m2_nordfrisisk`)

*Synlig for:* `culture ?= { has_culture_group = culture_group:nordfrisisk_group } du_mission_unik_age2_trigger = no du_mission_spillerland_trigger = yes`

The Great Drowning of 1362 swallowed whole parishes of North Frisia. The survivors elect dike-reeves, build higher and refuse to leave. In the new age the Frisians win back the land from the sea.

| Opgave | Kræver | Krav |
|---|---|---|
| After the Great Drowning | – | `OR = { AND = { has_advance = dku_nordfrisisk_2_efter_manddrukningen } AND = { stability >= 25 } }` |
| The Dike-Reeves | – | `OR = { AND = { has_advance = dku_nordfrisisk_2_digegreverne } AND = { any_owned_location = { has_building = building_type:farming_village count >= 2 } } }` |
| New Polders | After the Great Drowning | `any_owned_location = { has_building = building_type:farming_village count >= 3 }` |
| Frisian Seafarers | The Dike-Reeves | `any_owned_location = { has_building = building_type:wharf count >= 1 }; regular_navy_size >= 3` |
| Marsh Cattle | New Polders | `any_owned_location = { raw_material ?= goods:livestock rgo_level >= 2 count >= 1 }` |
| Churches on the Mounds | Frisian Seafarers | `any_owned_location = { has_building = building_type:parish_church count >= 2 }` |
| Frisia Endures (slut) | Marsh Cattle, Churches on the Mounds | `stability >= 35` |

### Greater Copenhagen (`du_m2_qaa`)

*Synlig for:* `has_or_had_tag = QAA`

The king has made Copenhagen his residence, and the city has outgrown its walls. Our districts and suburbs must become one great city, a capital worthy of a northern kingdom.

| Opgave | Kræver | Krav |
|---|---|---|
| The King's Residence | – | `OR = { AND = { has_advance = dku_koebenhavnsk_2_kongens_residens } AND = { prestige >= 50 } }` |
| The Brewers' Guild | – | `OR = { AND = { has_advance = dku_koebenhavnsk_2_bryggerlavet } AND = { any_owned_location = { has_building = building_type:du_mosteri count >= 2 } } }` |
| University of the Realm | The King's Residence | `OR = { AND = { has_embraced_institution = institution:renaissance } AND = { any_owned_location = { has_building = building_type:university count >= 2 } } }` |
| The Royal Fleet | The Brewers' Guild | `regular_navy_size >= 25; location:vor_frelsers_7082 = { owner ?= root location_building_level = { building_type = building_type:dock value >= 2 } }` |
| The Suburbs | University of the Realm | `area:gentofte_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:taarnby_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:gladsaxe_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }` |
| Capital of Trade | The Royal Fleet | `any_owned_location = { has_building = building_type:counting_house count >= 4 }; societal_value:capital_economy_vs_traditional_economy < -70` |
| Greater Copenhagen (slut) | The Suburbs, Capital of Trade | `OR = { AND = { has_or_had_tag = QZD } AND = { area:koebenhavn_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:frederiksberg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:gentofte_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:hvidovre_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } }` |

### Kingdom of the North (`du_m2_qdx`)

*Synlig for:* `has_or_had_tag = QDX`

Aalborg is the great town of the north, with a cathedral school, a Landsting and a harbour full of ships. In the new age the whole of North Jutland could answer to one city.

| Opgave | Kræver | Krav |
|---|---|---|
| Cathedral School of Aalborg | – | `OR = { AND = { has_advance = dku_storstad_2_domskolen } AND = { any_owned_location = { has_building = building_type:library count >= 2 } } }` |
| Landsting of the North | – | `OR = { AND = { has_advance = dku_storstad_2_landstingsbyen } AND = { stability >= 40 } }` |
| Fleet of the Limfjord | – | `regular_navy_size >= 12; any_owned_location = { has_building = building_type:wharf count >= 3 }` |
| Vendsyssel | Landsting of the North | `OR = { AND = { has_or_had_tag = QZE } AND = { area:broenderslev_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:hjoerring_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:frederikshavn_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } }` |
| Himmerland | Vendsyssel | `area:rebild_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:vesthimmerlands_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }` |
| Merchants of the North | Fleet of the Limfjord, Cathedral School of Aalborg | `any_owned_location = { has_building = building_type:counting_house count >= 3 }; any_owned_location = { has_building = building_type:du_saltery count >= 3 }` |
| Kingdom of the North (slut) | Himmerland, Merchants of the North | `OR = { AND = { has_or_had_tag = QZI } AND = { area:aalborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:broenderslev_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:hjoerring_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:rebild_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:mariagerfjord_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:jammerbugt_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } }` |

### Albani and the Island (`du_m2_qcd`)

*Synlig for:* `has_or_had_tag = QCD`

Odense brews the best beer on Funen and hosts the island's Landsting. In the new age the town that is Funen's heart could become the master of the whole island.

| Opgave | Kræver | Krav |
|---|---|---|
| The Albani Brewery | – | `location:fredens_7782 = { owner ?= root has_building = building_type:du_albani }` |
| School of Saint Knud | – | `OR = { AND = { has_advance = dku_storstad_2_domskolen } AND = { any_owned_location = { has_building = building_type:library count >= 2 } } }` |
| Landsting of Funen | – | `OR = { AND = { has_advance = dku_storstad_2_landstingsbyen } AND = { prestige >= 40 } }` |
| Canal to the Sea | The Albani Brewery | `capital = { has_building = building_type:dock }; any_owned_location = { has_building = building_type:wharf count >= 2 }` |
| The Castle at Nyborg | Landsting of Funen | `OR = { AND = { owns = location:nyborg_7724 } AND = { location:nyborg_7724 = { is_owned_or_owned_by_subjects_or_below_of = root } } }` |
| Houses of Funen | School of Saint Knud, Canal to the Sea | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }; any_owned_location = { has_building = building_type:counting_house count >= 2 }` |
| Funen United (slut) | The Castle at Nyborg, Houses of Funen | `OR = { AND = { has_or_had_tag = QZL } AND = { area:odense_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:kerteminde_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:nordfyns_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:faaborg_midtfyn_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:assens_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } }` |

### Crown of Scania (`du_m2_qfe`)

*Synlig for:* `has_or_had_tag = QFE`

Malmö has become the greatest town of Scania. Lund's archbishops, the Scania Market and the trade of the Sound all depend on us. In the new age Scania could have a capital of its own.

| Opgave | Kræver | Krav |
|---|---|---|
| School of Malmö | – | `OR = { AND = { has_advance = dku_storstad_2_domskolen } AND = { any_owned_location = { has_building = building_type:library count >= 2 } } }` |
| Landsting of Scania | – | `OR = { AND = { has_advance = dku_storstad_2_landstingsbyen } AND = { prestige >= 40 } }` |
| University of Lund | School of Malmö | `OR = { AND = { location:lunds_domkyrkoforsamling_sk = { owner ?= root has_building = building_type:du_lund_universitet } } AND = { any_owned_location = { has_building = building_type:university count >= 1 } } }` |
| Fleet of the Sound | – | `regular_navy_size >= 20` |
| South Scania | Landsting of Scania | `area:lund_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:staffanstorp_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:svedala_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }` |
| Trade of the Sound | Fleet of the Sound | `any_owned_location = { has_building = building_type:counting_house count >= 3 }; any_owned_location = { has_building = building_type:merchants_guild count >= 1 }` |
| Crown of Scania (slut) | University of Lund, South Scania, Trade of the Sound | `OR = { AND = { has_or_had_tag = QZQ } AND = { area:malmo_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:lund_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:helsingborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:kristianstad_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:trelleborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:ystad_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } }` |

### Shield of Scania (`du_m2_qeu`)

*Synlig for:* `has_or_had_tag = QEU`

Kristianstad's fortress has held the east of Scania for a generation. In the new age, our brandy, our alum and our riders could make the fortress town the shield of all Scanian lands.

| Opgave | Kræver | Krav |
|---|---|---|
| Åhus Brandy | – | `location:aahus_sk = { owner ?= root has_building = building_type:du_ahus_braendevin }` |
| The Scanian Plain | – | `OR = { AND = { has_advance = dku_skaansk_2_handelsbyens_privilegier } AND = { any_owned_location = { has_building = building_type:farming_village count >= 3 } } }` |
| Fishers of Hanö Bay | – | `OR = { AND = { has_advance = dku_skaansk_2_oesterlens_fiskerlejer } AND = { any_owned_location = { has_building = building_type:fishing_village count >= 2 } } }` |
| The Ramparts | Åhus Brandy | `any_owned_location = { has_building = building_type:castle count >= 2 }; capital = { has_building = building_type:city_walls }` |
| Gate to Blekinge | The Scanian Plain | `area:solvesborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:bromolla_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }` |
| The Scanian Regiments | The Ramparts, Fishers of Hanö Bay | `regular_army_size >= 10; army_tradition >= 30` |
| Shield of Scania (slut) | Gate to Blekinge, The Scanian Regiments | `area:kristianstad_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 1.0 } }; area:hassleholm_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:ostra_goinge_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }` |

### Capital of East Jutland (`du_m2_qdi`)

*Synlig for:* `has_or_had_tag = QDI`

Aarhus has school, cathedral and harbour. In the new age the city of the bay could gather all East Jutland, from Randers to Horsens, around itself.

| Opgave | Kræver | Krav |
|---|---|---|
| School of the Bay | – | `OR = { AND = { has_advance = dku_storstad_2_domskolen } AND = { any_owned_location = { has_building = building_type:library count >= 2 } } }` |
| Court of East Jutland | – | `OR = { AND = { has_advance = dku_storstad_2_landstingsbyen } AND = { stability >= 40 } }` |
| The New Learning | School of the Bay | `OR = { AND = { has_embraced_institution = institution:renaissance } AND = { any_owned_location = { has_building = building_type:university count >= 1 } } }` |
| The Great Harbour | – | `capital = { location_building_level = { building_type = building_type:dock value >= 2 } }; regular_navy_size >= 10` |
| The Hinterland | Court of East Jutland | `area:favrskov_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:odder_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }` |
| Republic of Citizens | The New Learning, The Great Harbour | `societal_value:serfdom_vs_free_subjects > 90; any_estate = { estate_type = estate_type:burghers_estate power >= 0.35 }` |
| Capital of East Jutland (slut) | The Hinterland, Republic of Citizens | `OR = { AND = { has_or_had_tag = QZH } AND = { area:aarhus_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:favrskov_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:odder_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:skanderborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:syddjurs_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } }` |

### Master of the Hardland (`du_m2_qcw`)

*Synlig for:* `has_or_had_tag = QCW`

The heath has always followed the strongest hall. In the new age the riders of Hardland, the mink lords and the wool pedlars can be bound into one horde, and Herning can be its master.

| Opgave | Kræver | Krav |
|---|---|---|
| Ride with the Horde | – | `OR = { AND = { is_member_of_international_organization_of_type = { type = du_hede_horden } } AND = { num_subjects >= 12 } }` |
| The Stocking Pedlars | – | `OR = { AND = { has_advance = dku_vestjysk_2_hosekraemmerne } AND = { any_owned_location = { has_building = building_type:sheep_farms count >= 5 } } }` |
| Peat and Heather | – | `OR = { AND = { has_advance = dku_vestjysk_2_toerv_og_lyng } AND = { any_owned_location = { has_building = building_type:forest_village count >= 2 } } }` |
| The Mink Lords | Ride with the Horde | `any_owned_location = { raw_material ?= goods:fur rgo_level >= 3 count >= 3 }; any_estate = { estate_type = estate_type:nobles_estate power >= 0.35 }` |
| To the West Sea | Ride with the Horde | `area:holstebro_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:ringkoebing_skjern_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:lemvig_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }` |
| The Great Host | The Mink Lords, Peat and Heather | `regular_army_size >= 12; army_tradition >= 35` |
| Master of the Hardland (slut) | To the West Sea, The Great Host, The Stocking Pedlars | `OR = { AND = { has_or_had_tag = QZJ } AND = { area:herning_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:holstebro_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:ikast_brande_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:ringkoebing_skjern_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:lemvig_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:struer_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } }` |

### Paper and Lakes (`du_m2_qdf`)

*Synlig for:* `has_or_had_tag = QDF`

The water of the lakes turns our mills, and the new age wants paper: for bibles, for laws and for ledgers. Silkeborg's paper mill could make the lake highlands famous.

| Opgave | Kræver | Krav |
|---|---|---|
| The Paper Mill | – | `location:silkeborg_8017 = { owner ?= root has_building = building_type:du_silkeborg_papir }` |
| Forests of the Highlands | – | `OR = { AND = { has_advance = dku_oestjysk_2_soehoejlandets_skove } AND = { any_owned_location = { has_building = building_type:sawmill count >= 3 } } }` |
| Lords of the Lakes | – | `OR = { AND = { has_advance = dku_oestjysk_2_djurslands_herregaarde } AND = { any_owned_location = { has_building = building_type:noble_villa count >= 2 } } }` |
| Printers and Scribes | The Paper Mill | `any_owned_location = { has_building = building_type:library count >= 2 }; OR = { AND = { has_embraced_institution = institution:renaissance } AND = { stability >= 40 } }` |
| Skanderborg | Lords of the Lakes | `area:skanderborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }` |
| Barges to Randers | Forests of the Highlands, Printers and Scribes | `any_owned_location = { has_building = building_type:market_village count >= 3 }; any_owned_location = { has_building = building_type:counting_house count >= 1 }` |
| Duchy of the Lake Highlands (slut) | Skanderborg, Barges to Randers | `OR = { AND = { has_or_had_tag = QZA } AND = { area:silkeborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:skanderborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } }` |

### Lords of Djursland (`du_m2_qde`)

*Synlig for:* `has_or_had_tag = QDE`

Randers already holds the mouth of the river. In the new age the manors of Djursland, the river trade and the horse fairs could make Randers master of the whole peninsula.

| Opgave | Kræver | Krav |
|---|---|---|
| Manors of Djursland | – | `OR = { AND = { has_advance = dku_oestjysk_2_djurslands_herregaarde } AND = { any_owned_location = { has_building = building_type:noble_villa count >= 3 } } }` |
| Timber of the River | – | `OR = { AND = { has_advance = dku_oestjysk_2_soehoejlandets_skove } AND = { any_owned_location = { has_building = building_type:sawmill count >= 2 } } }` |
| The Horse Fair | – | `any_owned_location = { raw_material ?= goods:horses rgo_level >= 3 count >= 1 }; any_owned_location = { has_building = building_type:market_village count >= 3 }` |
| Leather and Gloves | Manors of Djursland | `any_owned_location = { has_building = building_type:du_dairy count >= 2 }; any_owned_location = { raw_material ?= goods:livestock rgo_level >= 3 count >= 2 }` |
| Mols and Ebeltoft | Timber of the River | `area:syddjurs_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }` |
| Ships of the Fjord | The Horse Fair, Leather and Gloves | `regular_navy_size >= 8; any_owned_location = { has_building = building_type:counting_house count >= 2 }` |
| Lords of Djursland (slut) | Mols and Ebeltoft, Ships of the Fjord | `OR = { AND = { has_or_had_tag = QZF } AND = { area:syddjurs_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:norddjurs_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } }` |

### Kingdom of the Triangle (`du_m2_qcv`)

*Synlig for:* `has_or_had_tag = QCV`

From the stones of Jelling, Gorm ruled a kingdom. In the new age the oxen roads, the fjords and the crossings of the Little Belt could be bound together again under the heirs of Jelling.

| Opgave | Kræver | Krav |
|---|---|---|
| Oxen to the South | – | `OR = { AND = { has_advance = dku_sydjysk_2_oeksneudskibningen } AND = { any_owned_location = { raw_material ?= goods:livestock rgo_level >= 2 count >= 3 } } }` |
| The Chapter and the Stones | – | `OR = { AND = { has_advance = dku_sydjysk_2_domkapitlet } AND = { any_estate = { estate_type = estate_type:clergy_estate power >= 0.3 } } }` |
| Royal Jelling | The Chapter and the Stones | `location:jelling_7905 = { owner ?= root has_building = building_type:castle }; prestige >= 60` |
| Host of Gorm's Heirs | Oxen to the South | `regular_army_size >= 10; army_tradition >= 30` |
| The Valleys | Host of Gorm's Heirs | `area:billund_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }; area:vejle_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 1.0 } }` |
| The Belt Crossing | The Valleys | `area:fredericia_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:kolding_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }` |
| Kingdom of the Triangle (slut) | Royal Jelling, The Belt Crossing | `OR = { AND = { has_or_had_tag = QZK } AND = { area:vejle_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:kolding_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:fredericia_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:billund_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:vejen_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } }` |

### Coal and the Sound (`du_m2_qft`)

*Synlig for:* `has_or_had_tag = QFT`

Helsingborg's coal and its watch on the Sound make it the second gate of the Baltic. In the new age our mines, kilns and ships could make the town as rich as any on the Sound.

| Opgave | Kræver | Krav |
|---|---|---|
| School of Helsingborg | – | `OR = { AND = { has_advance = dku_storstad_2_domskolen } AND = { any_owned_location = { has_building = building_type:library count >= 2 } } }` |
| Council of the Districts | – | `OR = { AND = { has_advance = dku_storstad_2_landstingsbyen } AND = { stability >= 40 } }` |
| Deep Mines | – | `any_owned_location = { raw_material ?= goods:coal rgo_level >= 3 count >= 3 }` |
| Höganäs Stoneware | Deep Mines | `any_owned_location = { has_building = building_type:local_smelters count >= 2 }; any_owned_location = { has_building = building_type:counting_house count >= 2 }` |
| Navy of the Sound | Council of the Districts | `regular_navy_size >= 15` |
| The Kullen Coast | School of Helsingborg | `area:hoganas_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:angelholm_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; area:aastorp_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }` |
| Second Gate of the Baltic (slut) | Höganäs Stoneware, Navy of the Sound, The Kullen Coast | `area:helsingborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 1.0 } }; area:landskrona_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }` |

### The Preacher of Viborg (`du_m2_qdp`)

*Synlig for:* `has_or_had_tag = QDP`

New preachers have come to Viborg, preaching in Danish from the town's churches. The Landsting listens and the bishops fear them. In the new age Viborg could lead Jutland in faith as it does in law.

| Opgave | Kræver | Krav |
|---|---|---|
| The Danish Preacher | – | `any_estate = { estate_type = estate_type:clergy_estate power >= 0.3 }; societal_value:spiritualist_vs_humanist < -15` |
| The Printing Press | The Danish Preacher | `any_owned_location = { has_building = building_type:library count >= 2 }; OR = { AND = { has_embraced_institution = institution:renaissance } AND = { prestige >= 50 } }` |
| Manors of the Landsting | – | `OR = { AND = { has_advance = dku_oestjysk_2_djurslands_herregaarde } AND = { any_owned_location = { has_building = building_type:noble_villa count >= 3 } } }` |
| Law of the Realm | Manors of the Landsting | `prestige >= 60; stability >= 45` |
| The Army Road North | – | `any_owned_location = { has_building = building_type:market_village count >= 3 }; regular_army_size >= 8` |
| Fjends and the Lakes | The Army Road North | `area:viborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 1.0 } }; area:skive_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.5 } }` |
| Faith of Jutland (slut) | The Printing Press, Law of the Realm, Fjends and the Lakes | `societal_value:traditionalist_vs_innovative < -30; capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }` |

### The Bishops' Zealand (`du_m2_qbg`)

*Synlig for:* `has_or_had_tag = QBG`

The bishop of Roskilde owns more of Zealand than the king. In the new age the cathedral town can use the Church's lands, schools and courts to make itself the master of central Zealand.

| Opgave | Kræver | Krav |
|---|---|---|
| The Cathedral Town | – | `OR = { AND = { has_advance = dku_koebstad_2_koebstadskirken } AND = { any_owned_location = { has_building = building_type:parish_church count >= 4 } } }` |
| Skippers of the Fjord | – | `OR = { AND = { has_advance = dku_koebstad_2_skipperlavet } AND = { any_owned_location = { has_building = building_type:wharf count >= 2 } } }` |
| Lands of the Bishop | The Cathedral Town | `any_estate = { estate_type = estate_type:clergy_estate power >= 0.4 }; any_owned_location = { has_building = building_type:noble_villa count >= 2 }` |
| Academy of Roskilde | Lands of the Bishop | `any_owned_location = { has_building = building_type:university count >= 1 }; OR = { AND = { has_embraced_institution = institution:renaissance } AND = { any_owned_location = { has_building = building_type:library count >= 3 } } }` |
| Lejre and the Fjord | Skippers of the Fjord | `area:lejre_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 1.0 } }; area:frederikssund_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }` |
| Road to Køge | Lejre and the Fjord | `area:greve_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }; area:solroed_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }` |
| The Bishops' Zealand (slut) | Academy of Roskilde, Road to Køge | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }; prestige >= 60` |

### Iron Host (`du_m2_qcq`)

*Synlig for:* `has_or_had_tag = QCQ`

Vejen's bog iron has made spears for a generation. In the new age our smiths can forge armour and guns, and our host can march where it pleases.

| Opgave | Kræver | Krav |
|---|---|---|
| The Ox Road | – | `OR = { AND = { has_advance = dku_sydjysk_2_oeksneudskibningen } AND = { any_owned_location = { raw_material ?= goods:livestock rgo_level >= 2 count >= 2 } } }` |
| Priests of the Host | – | `OR = { AND = { has_advance = dku_sydjysk_2_domkapitlet } AND = { any_owned_location = { has_building = building_type:parish_church count >= 5 } } }` |
| Iron for Armour | – | `any_owned_location = { raw_material ?= goods:iron rgo_level >= 3 count >= 4 }; any_owned_location = { has_building = building_type:local_smelters count >= 3 }` |
| The Armouries | Iron for Armour | `any_owned_location = { has_building = building_type:armory count >= 2 }` |
| Our Own Landsknechts | Priests of the Host | `regular_army_size >= 12; societal_value:quality_vs_quantity > 45` |
| March of the Iron Host | The Armouries, Our Own Landsknechts | `area:esbjerg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }; area:haderslev_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.5 } }` |
| Iron Host (slut) | The Ox Road, March of the Iron Host | `army_tradition >= 45; num_locations >= 120` |

### Masters of the Belts (`du_m2_qce`)

*Synlig for:* `has_or_had_tag = QCE`

Svendborg's skippers and Marstal's sailors know every sound between Funen and Lolland. In the new age the archipelago fleet could command the Belts themselves.

| Opgave | Kræver | Krav |
|---|---|---|
| Shipwrights of the Sound | – | `OR = { AND = { has_advance = dku_fynsk_2_sundets_skibsbyggere } AND = { any_owned_location = { has_building = building_type:wharf count >= 4 } } }` |
| The Funen Surplus | – | `OR = { AND = { has_advance = dku_fynsk_2_det_fynske_kornoverskud } AND = { any_owned_location = { has_building = building_type:farming_village count >= 4 } } }` |
| Sailors of Marstal | – | `OR = { AND = { location:marstal_7714 = { owner ?= root has_building = building_type:du_marstal_soefart } } AND = { regular_navy_size >= 20 } }` |
| Fleet of the Belts | Shipwrights of the Sound | `regular_navy_size >= 25; capital = { location_building_level = { building_type = building_type:dock value >= 2 } }` |
| Nyborg and the Belt | The Funen Surplus | `OR = { AND = { owns = location:nyborg_7724 } AND = { location:nyborg_7724 = { is_owned_or_owned_by_subjects_or_below_of = root } } }; area:langeland_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }` |
| Trade of the Belts | Sailors of Marstal, Fleet of the Belts | `any_owned_location = { has_building = building_type:counting_house count >= 3 }; any_owned_location = { has_building = building_type:merchants_guild count >= 1 }` |
| Masters of the Belts (slut) | Nyborg and the Belt, Trade of the Belts | `area:svendborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 1.0 } }; area:aeroe_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } }; regular_navy_size >= 30` |

### Where Zealand Hails Its King (`du_m2_qbn`)

*Synlig for:* `has_or_had_tag = QBN`

The kings of Denmark are hailed at the Landsting of Ringsted and buried in its church. In the new age, as the crown grows strong, Ringsted could make itself the indispensable seat of Zealand's law.

| Opgave | Kræver | Krav |
|---|---|---|
| Farming of the Monks | – | `OR = { AND = { has_advance = dku_sjaellandsk_2_esrum_klosters_landbrug } AND = { any_owned_location = { has_building = building_type:farming_village count >= 5 } } }` |
| Friends of the Crown | – | `OR = { AND = { has_advance = dku_sjaellandsk_2_krongodset_i_nordsjaelland } AND = { any_estate = { estate_type = estate_type:crown_estate power >= 0.3 } } }` |
| The Hailing of Kings | Friends of the Crown | `prestige >= 60; stability >= 45` |
| Grain Trade | Farming of the Monks | `any_owned_location = { has_building = building_type:granary count >= 2 }; OR = { AND = { area:koege_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } } } AND = { any_owned_location = { has_building = building_type:counting_house count >= 2 } } }` |
| Sorø and the Lakes | – | `area:soroe_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }; area:ringsted_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 1.0 } }` |
| The Law of Zealand | The Hailing of Kings, Sorø and the Lakes | `any_owned_location = { has_building = building_type:library count >= 1 }; societal_value:centralization_vs_decentralization < -15` |
| Where Zealand Hails Its King (slut) | Grain Trade, The Law of Zealand | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }; num_locations >= 100` |

### Toll of the Realm (`du_m2_qax`)

*Synlig for:* `has_or_had_tag = QAX`

The Sound Toll is the richest toll in the North, and Helsingør collects it. In the new age the toll town needs a great castle, a fleet and gunsmiths to keep what it takes.

| Opgave | Kræver | Krav |
|---|---|---|
| Saint Olai's Church | – | `OR = { AND = { has_advance = dku_koebstad_2_koebstadskirken } AND = { capital = { has_building = building_type:temple } } }` |
| Pilots of the Sound | – | `OR = { AND = { has_advance = dku_koebstad_2_skipperlavet } AND = { any_owned_location = { has_building = building_type:wharf count >= 1 } } }` |
| The Crown's Castle | Saint Olai's Church | `capital = { has_building = building_type:castle }; capital = { has_building = building_type:city_walls }; gold >= 250` |
| The Customs House | Pilots of the Sound | `any_owned_location = { has_building = building_type:counting_house count >= 2 }; stability >= 40` |
| Guardships of the Sound | The Customs House | `regular_navy_size >= 15` |
| North Zealand | The Crown's Castle | `area:gribskov_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }; area:fredensborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }` |
| Toll of the Realm (slut) | Guardships of the Sound, North Zealand | `capital = { OR = { location_rank = location_rank:city location_rank = location_rank:du_metropolis location_rank = location_rank:megalopolis } }; gold >= 300` |

### Duchy of the South (`du_m2_qbt`)

*Synlig for:* `has_or_had_tag = QBT`

Næstved's merchants, monks and farmers have made the town the centre of South Zealand. In the new age, with Vordingborg's castle and Falster across the water, it could rule a duchy of the south.

| Opgave | Kræver | Krav |
|---|---|---|
| Monastic Farming | – | `OR = { AND = { has_advance = dku_sjaellandsk_2_esrum_klosters_landbrug } AND = { any_owned_location = { has_building = building_type:farming_village count >= 4 } } }` |
| Crown and Town | – | `OR = { AND = { has_advance = dku_sjaellandsk_2_krongodset_i_nordsjaelland } AND = { prestige >= 40 } }` |
| Hanseatic Kontor | – | `any_owned_location = { has_building = building_type:counting_house count >= 3 }; regular_navy_size >= 6` |
| The Noble School | Monastic Farming | `any_owned_location = { has_building = building_type:library count >= 2 }; any_estate = { estate_type = estate_type:nobles_estate power >= 0.3 }` |
| The Western Lordship | Crown and Town | `OR = { AND = { area:kalundborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } } } AND = { num_subjects >= 3 } }` |
| Vordingborg and Faxe | Hanseatic Kontor, The Western Lordship | `area:vordingborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }; area:faxe_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }` |
| Duchy of the South (slut) | The Noble School, Vordingborg and Faxe | `OR = { AND = { has_or_had_tag = QZR } AND = { area:naestved_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:vordingborg_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:faxe_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:stevns_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } }` |

### Lords of the Little Belt (`du_m2_qic`)

*Synlig for:* `OR = { has_or_had_tag = QIC has_or_had_tag = QCU }`

Koldinghus watches the road south and our vassals hold both shores of the Little Belt. In the new age, the ox trade and the Belt crossing could make Kolding master of the Little Belt lands.

| Opgave | Kræver | Krav |
|---|---|---|
| Oxen to Hamburg | – | `OR = { AND = { has_advance = dku_sydjysk_2_oeksneudskibningen } AND = { any_owned_location = { raw_material ?= goods:livestock rgo_level >= 2 count >= 3 } } }` |
| Friends in Ribe | – | `OR = { AND = { has_advance = dku_sydjysk_2_domkapitlet } AND = { any_estate = { estate_type = estate_type:clergy_estate power >= 0.25 } } }` |
| Royal Koldinghus | Friends in Ribe | `location:sankt_nicolai_7927 = { owner ?= root has_building = building_type:castle }; prestige >= 50` |
| The Ferry Toll | Oxen to Hamburg | `area:middelfart_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }; area:fredericia_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }` |
| Riders of the Border | Royal Koldinghus | `regular_army_size >= 8; any_owned_location = { has_building = building_type:training_fields count >= 2 }` |
| The Funen Shore | The Ferry Toll | `area:assens_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }` |
| Lords of the Little Belt (slut) | Riders of the Border, The Funen Shore | `OR = { AND = { has_or_had_tag = QZG } AND = { area:kolding_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:middelfart_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:fredericia_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } AND = { area:assens_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.8 } } } }` |

### Islands of the Queen (`du_m2_qbu`)

*Synlig for:* `has_or_had_tag = QBU`

The queens of Denmark keep their dower at Nykøbing, and the great estates of Lolland send their grain through the Guldborg Sound. In the new age Falster and Lolland could be one realm of islands.

| Opgave | Kræver | Krav |
|---|---|---|
| The Great Estates | – | `OR = { AND = { has_advance = dku_lollandsk_falstersk_2_godsernes_lolland } AND = { any_owned_location = { has_building = building_type:noble_villa count >= 2 } } }` |
| The Nuns of Maribo | – | `OR = { AND = { has_advance = dku_lollandsk_falstersk_2_birgittinerklosteret } AND = { any_estate = { estate_type = estate_type:clergy_estate power >= 0.25 } } }` |
| Court of the Dowager | – | `capital = { has_building = building_type:castle }; prestige >= 50` |
| Fleet of the Islands | The Great Estates | `regular_navy_size >= 15` |
| Maribo and the Lakes | The Nuns of Maribo, Fleet of the Islands | `OR = { AND = { owns = location:maribo_domsogn_7648 } AND = { location:maribo_domsogn_7648 = { is_owned_or_owned_by_subjects_or_below_of = root } } }` |
| Sugar Fields | The Great Estates | `any_owned_location = { raw_material ?= goods:sugar rgo_level >= 3 count >= 2 }` |
| Islands of the Queen (slut) | Court of the Dowager, Maribo and the Lakes, Sugar Fields | `area:guldborgsund_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 1.0 } }; area:lolland_area = { any_location_in_area = { is_owned_or_owned_by_subjects_or_below_of = root percent >= 0.6 } }` |

