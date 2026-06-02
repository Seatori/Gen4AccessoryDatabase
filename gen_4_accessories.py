from typing import NamedTuple


class AccessoryData(NamedTuple):
    name: str
    page: int
    bright: int
    colorful: int
    created: int
    festive: int
    flexible: int
    gaudy: int
    intangible: int
    natural: int
    relaxed: int
    shapely: int
    sharp: int
    solid: int
    obtained: bool = True


class LocationData(NamedTuple):
    name: str
    dp: str
    plat: str = ""
    hgss: str = ""


# 1
white_fluff = AccessoryData("White Fluff", 1,          2, 1, 0, 1, 2, 1, 1, 2, 0, 1, 0, 1, False)
yellow_fluff = AccessoryData("Yellow Fluff", 1,        2, 2, 0, 1, 2, 1, 1, 2, 1, 1, 0, 1)
pink_fluff = AccessoryData("Pink Fluff", 1,            1, 2, 0, 1, 2, 1, 1, 2, 1, 1, 0, 1, False)
brown_fluff = AccessoryData("Brown Fluff", 1,          1, 2, 0, 1, 2, 1, 1, 2, 2, 1, 0, 1)
black_fluff = AccessoryData("Black Fluff", 1,          0, 2, 0, 1, 2, 1, 1, 2, 2, 1, 0, 1, False)
orange_fluff = AccessoryData("Orange Fluff", 1,        1, 2, 0, 1, 2, 1, 1, 2, 1, 1, 0, 1)
# 2
round_pebble = AccessoryData("Round Pebble", 2,        1, 1, 1, 1, 0, 2, 0, 1, 1, 2, 0, 2, False)
glitter_boulder = AccessoryData("Glitter Boulder", 2,  2, 1, 1, 2, 0, 2, 0, 1, 0, 2, 0, 2)
snaggy_pebble = AccessoryData("Snaggy Pebble", 2,      1, 0, 0, 0, 0, 1, 0, 2, 1, 2, 0, 2)
jagged_boulder = AccessoryData("Jagged Boulder", 2,    1, 0, 0, 0, 0, 1, 0, 2, 2, 2, 0, 2, False)
black_pebble = AccessoryData("Black Pebble", 2,        0, 2, 1, 1, 0, 2, 0, 1, 2, 2, 0, 2, False)
mini_pebble = AccessoryData("Mini Pebble", 2,          1, 1, 1, 1, 0, 2, 0, 1, 1, 2, 0, 2)
# 3
pink_scale = AccessoryData("Pink Scale", 3,            1, 2, 0, 1, 1, 2, 1, 2, 1, 1, 1, 2)
blue_scale = AccessoryData("Blue Scale", 3,            1, 2, 0, 1, 1, 2, 1, 2, 2, 1, 2, 2)
green_scale = AccessoryData("Green Scale", 3,          1, 2, 0, 1, 1, 2, 1, 2, 1, 1, 0, 2, False)
purple_scale = AccessoryData("Purple Scale", 3,        1, 2, 0, 1, 1, 2, 1, 2, 1, 1, 2, 2)
big_scale = AccessoryData("Big Scale", 3,              2, 1, 0, 1, 1, 2, 1, 2, 0, 1, 2, 2)
narrow_scale = AccessoryData("Narrow Scale", 3,        0, 1, 0, 1, 1, 2, 1, 2, 2, 1, 2, 2, False)
# 4
blue_feather = AccessoryData("Blue Feather", 4,        1, 2, 0, 1, 1, 2, 1, 2, 1, 1, 2, 1)
red_feather = AccessoryData("Red Feather", 4,          1, 2, 0, 1, 1, 2, 1, 2, 1, 1, 2, 1)
yellow_feather = AccessoryData("Yellow Feather", 4,    2, 2, 0, 1, 1, 2, 1, 2, 1, 1, 2, 1)
white_feather = AccessoryData("White Feather", 4,      2, 2, 0, 1, 1, 2, 1, 2, 0, 1, 2, 1)
# 5
black_moustache = AccessoryData("Black Moustache", 5,  0, 2, 2, 0, 2, 2, 1, 0, 2, 1, 1, 1)
white_moustache = AccessoryData("White Moustache", 5,  2, 1, 2, 0, 2, 2, 1, 0, 0, 1, 1, 1, False)
black_beard = AccessoryData("Black Beard", 5,          0, 2, 2, 0, 2, 2, 1, 0, 2, 1, 2, 1)
white_beard = AccessoryData("White Beard", 5,          2, 1, 2, 0, 2, 2, 1, 0, 0, 1, 2, 1)
small_leaf = AccessoryData("Small Leaf", 5,            1, 1, 0, 0, 2, 1, 1, 2, 1, 1, 1, 1)
big_leaf = AccessoryData("Big Leaf", 5,                1, 1, 0, 0, 2, 1, 1, 2, 1, 2, 1, 1)
narrow_leaf = AccessoryData("Narrow Leaf", 5,          1, 1, 0, 0, 2, 1, 1, 2, 1, 1, 2, 1, False)
# 6
shed_claw = AccessoryData("Shed Claw", 6,              2, 0, 1, 1, 0, 1, 1, 2, 0, 2, 2, 2, False)
shed_horn = AccessoryData("Shed Horn", 6,              2, 0, 1, 1, 0, 1, 1, 2, 0, 2, 2, 2, False)
thin_mushroom = AccessoryData("Thin Mushroom", 6,      2, 1, 1, 1, 1, 1, 1, 2, 0, 1, 2, 1)
thick_mushroom = AccessoryData("Thick Mushroom", 6,    1, 1, 1, 1, 1, 1, 1, 2, 0, 2, 1, 1, False)
stump = AccessoryData("Stump", 6,                      1, 0, 1, 0, 0, 1, 1, 2, 1, 2, 1, 2, False)
# 7
pretty_dewdrop = AccessoryData("Pretty Dewdrop", 7,    1, 1, 0, 2, 2, 1, 2, 2, 0, 1, 0, 0, False)
snow_crystal = AccessoryData("Snow Crystal", 7,        2, 1, 0, 2, 2, 1, 2, 2, 0, 1, 1, 0, False)
sparks = AccessoryData("Sparks", 7,                    2, 1, 1, 2, 2, 1, 2, 2, 1, 0, 0, 0, False)
shimmering_fire = AccessoryData("Shimmering Fire", 7,  2, 1, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, False)
mystic_fire = AccessoryData("Mystic Fire", 7,          2, 1, 1, 2, 2, 1, 2, 2, 1, 0, 0, 0, False)
# 8
determination = AccessoryData("Determination", 8,      2, 1, 1, 1, 2, 2, 2, 1, 1, 0, 1, 0, False)
peculiar_spoon = AccessoryData("Peculiar Spoon", 8,    1, 0, 2, 1, 1, 1, 0, 0, 1, 2, 1, 2, False)
puffy_smoke = AccessoryData("Puffy Smoke", 8,          1, 1, 0, 0, 2, 1, 2, 2, 1, 0, 0, 0, False)
poison_extract = AccessoryData("Poison Extract", 8,    0, 2, 1, 0, 2, 0, 2, 2, 2, 0, 0, 0, False)
# 9
wealthy_coin = AccessoryData("Wealthy Coin", 9,        1, 1, 2, 2, 0, 2, 0, 0, 0, 2, 0, 2, False)
eerie_thing = AccessoryData("Eerie Thing", 9,          0, 2, 1, 0, 2, 0, 2, 2, 2, 1, 0, 0, False)
spring = AccessoryData("Spring", 9,                    1, 1, 2, 1, 2, 2, 1, 0, 1, 2, 2, 2, False)
seashell = AccessoryData("Seashell", 9,                2, 0, 0, 1, 0, 1, 1, 2, 1, 2, 1, 2, False)
humming_note = AccessoryData("Humming Note", 9,        1, 1, 2, 2, 2, 2, 2, 1, 1, 0, 1, 1, False)
shiny_powder = AccessoryData("Shiny Powder", 9,        2, 1, 2, 2, 2, 2, 2, 1, 0, 1, 0, 1, False)
glitter_powder = AccessoryData("Glitter Powder", 9,    2, 1, 2, 2, 2, 2, 2, 1, 0, 1, 0, 1, False)
# 10
red_flower = AccessoryData("Red Flower", 10,           1, 2, 0, 1, 1, 1, 1, 2, 1, 2, 1, 1)
pink_flower = AccessoryData("Pink Flower", 10,         1, 2, 0, 1, 1, 1, 1, 2, 1, 2, 1, 1)
white_flower = AccessoryData("White Flower", 10,       2, 1, 0, 1, 1, 1, 1, 2, 0, 2, 1, 1)
blue_flower = AccessoryData("Blue Flower", 10,         1, 2, 0, 1, 1, 1, 1, 2, 1, 2, 1, 1)
orange_flower = AccessoryData("Orange Flower", 10,     1, 2, 0, 1, 1, 1, 1, 2, 1, 2, 1, 1)
yellow_flower = AccessoryData("Yellow Flower", 10,     2, 2, 0, 1, 1, 1, 1, 2, 1, 2, 1, 1)
# 11
googly_specs = AccessoryData("Googly Specs", 11,       1, 1, 2, 0, 0, 1, 1, 0, 2, 2, 1, 2)
black_specs = AccessoryData("Black Specs", 11,         0, 2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 2)
gorgeous_specs = AccessoryData("Gorgeous Specs", 11,   0, 2, 2, 2, 0, 2, 1, 0, 1, 2, 1, 2, False)
sweet_candy = AccessoryData("Sweet Candy", 11,         1, 1, 2, 1, 1, 2, 1, 0, 1, 2, 1, 2, False)
confetti = AccessoryData("Confetti", 11,               1, 2, 2, 1, 2, 2, 2, 0, 1, 1, 1, 1, False)
# 12
colored_parasol = AccessoryData("Colored Parasol", 12, 2, 2, 2, 2, 1, 2, 1, 0, 1, 2, 2, 2, False)
old_umbrella = AccessoryData("Old Umbrella", 12,       1, 1, 2, 0, 1, 1, 1, 0, 2, 2, 2, 2, False)
spotlight = AccessoryData("Spotlight", 12,             2, 0, 2, 2, 1, 2, 2, 0, 0, 2, 1, 2, False)
cape = AccessoryData("Cape", 12,                       0, 2, 2, 1, 2, 2, 1, 0, 2, 2, 2, 1, False)
standing_mike = AccessoryData("Standing Mike", 12,     1, 1, 2, 1, 1, 2, 1, 0, 1, 2, 2, 2, False)
surfboard = AccessoryData("Surfboard", 12,             1, 1, 2, 1, 0, 2, 1, 0, 1, 2, 2, 2, False)
carpet = AccessoryData("Carpet", 12,                   1, 2, 2, 2, 2, 2, 2, 0, 1, 2, 0, 2, False)
retro_pipe = AccessoryData("Retro Pipe", 12,           1, 1, 2, 0, 0, 1, 0, 0, 1, 2, 1, 2, False)
fluffy_bed = AccessoryData("Fluffy Bed", 12,           1, 1, 2, 1, 2, 2, 1, 0, 1, 2, 0, 1, False)
mirror_ball = AccessoryData("Mirror Ball", 12,         2, 1, 2, 2, 0, 2, 1, 0, 0, 2, 0, 2, False)
photo_board = AccessoryData("Photo Board", 12,         1, 1, 2, 1, 1, 2, 2, 0, 1, 2, 1, 2, False)
# 13
pink_barrette = AccessoryData("Pink Barrette", 13,     1, 2, 2, 1, 1, 2, 1, 0, 1, 1, 1, 1, False)
red_barrette = AccessoryData("Red Barrette", 13,       1, 2, 2, 1, 1, 2, 1, 0, 1, 1, 1, 1, False)
blue_barrette = AccessoryData("Blue Barrette", 13,     1, 2, 2, 1, 1, 2, 1, 0, 1, 1, 1, 1, False)
yellow_barrette = AccessoryData("Yellow Barrette", 13, 2, 2, 2, 1, 1, 2, 1, 0, 1, 1, 1, 1, False)
green_barrette = AccessoryData("Green Barrette", 13,   1, 2, 2, 1, 1, 2, 1, 0, 1, 1, 1, 1, False)
pink_balloon = AccessoryData("Pink Balloon", 13,       1, 2, 2, 1, 2, 2, 2, 0, 1, 1, 0, 0, False)
red_balloons = AccessoryData("Red Balloons", 13,       1, 2, 2, 1, 2, 2, 2, 0, 1, 1, 0, 0, False)
blue_balloons = AccessoryData("Blue Balloons", 13,     1, 2, 2, 1, 2, 2, 2, 0, 1, 1, 0, 0, False)
yellow_balloon = AccessoryData("Yellow Balloon", 13,   2, 2, 2, 1, 2, 2, 2, 0, 1, 1, 0, 0, False)
green_balloons = AccessoryData("Green Balloons", 13,   1, 2, 2, 1, 2, 2, 2, 0, 1, 1, 0, 0, False)
lace_headdress = AccessoryData("Lace Headdress", 13,   2, 0, 2, 2, 1, 2, 1, 0, 1, 2, 2, 1, False)
top_hat = AccessoryData("Top Hat", 13,                 0, 2, 2, 2, 1, 2, 1, 0, 2, 2, 1, 1, False)
silk_veil = AccessoryData("Silk Veil", 13,             2, 1, 2, 2, 2, 2, 2, 0, 0, 2, 1, 1, False)
heroic_headband = AccessoryData("Heroic Headband", 13, 1, 1, 2, 1, 2, 2, 2, 0, 1, 2, 1, 1, False)
professor_hat = AccessoryData("Professor Hat", 13,     1, 2, 2, 1, 1, 2, 1, 0, 1, 2, 2, 2, False)
flower_stage = AccessoryData("Flower Stage", 13,       1, 1, 2, 2, 0, 2, 0, 0, 1, 2, 1, 2, False)
gold_pedestal = AccessoryData("Gold Pedestal", 13,     2, 2, 2, 2, 0, 2, 0, 0, 0, 2, 1, 2, False)
glass_stage = AccessoryData("Glass Stage", 13,         2, 1, 2, 2, 0, 2, 0, 0, 1, 2, 1, 2, False)
award_podium = AccessoryData("Award Podium", 13,       2, 1, 2, 1, 0, 2, 0, 0, 1, 2, 1, 2, False)
cube_stage = AccessoryData("Cube Stage", 13,           1, 1, 2, 1, 0, 2, 0, 0, 1, 2, 1, 2, False)
# 14
turtwig_mask = AccessoryData("Turtwig Mask", 14,       1, 1, 2, 1, 1, 2, 1, 0, 1, 2, 0, 1)
chimchar_mask = AccessoryData("Chimchar Mask", 14,     1, 1, 2, 1, 1, 2, 1, 0, 1, 2, 0, 1)
piplup_mask = AccessoryData("Piplup Mask", 14,         1, 1, 2, 1, 1, 2, 1, 0, 1, 2, 0, 1)
big_tree = AccessoryData("Big Tree", 14,               1, 1, 0, 1, 1, 1, 0, 2, 1, 2, 1, 2)
flag = AccessoryData("Flag", 14,                       1, 2, 2, 1, 2, 2, 2, 0, 1, 2, 2, 2)
crown = AccessoryData("Crown", 14,                     2, 1, 2, 2, 1, 2, 1, 0, 0, 2, 2, 2, False)
tiara = AccessoryData("Tiara", 14,                     2, 1, 2, 2, 1, 2, 1, 0, 0, 2, 2, 2, False)
comet = AccessoryData("Comet", 14,                     2, 2, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, False)

dp = "Diamond & Pearl: "
pt = "Platinum: "
dppt = "Diamond, Pearl & Platinum: "
hgss = "HeartGold & SoulSilver: "

amity = "Amity Square"
massage = "Veilstone City Massage Girl"
floaroma = "Floaroma Town Flower Shop"

dp_skitty = "Clefairy, Skitty"
dp_shroomish = "Jigglypuff, Shroomish"
dp_psyduck = "Psyduck, Pachirisu"
dp_torchic = "Torchic, Drifloon"
dp_buneary = "Buneary, Happiny"

pt_pikachu = "Pikachu, Clefairy, Pachirisu, Happiny"
pt_skitty = "Jigglypuff, Torchic, Shroomish, Skitty"
pt_psyduck = "Psyduck, Drifloon, Buneary"
turtwig = "Turtwig, Grotle, Torterra"
chimchar = "Chimchar, Monferno, Infernape"
piplup = "Piplup, Prinplup, Empoleon"
amity_man = "Berries & Accessories Man"

follower = "Following Pokemon"
raffle = "Goldenrod Tunnel Raffle"

template = LocationData("", "Reward for winning a  Rank  Contest for the first time", f"{raffle}")
white_fluff_loc = LocationData("white fluff",
                               f"{amity} ({dp_skitty}, {dp_torchic})",
                               f"{amity} ({chimchar}], {piplup})",
                               f"{follower} (Route 31)")
yellow_fluff_loc = LocationData("yellow fluff",
                                f"{amity} (Pikachu)",
                                f"{amity} ({pt_pikachu})",
                                f"{follower} (Route 2)")
pink_fluff_loc = LocationData("pink fluff",
                              f"{amity} ({dp_torchic})",
                              f"{amity} ({pt_skitty}, {piplup})",
                              f"{follower} (Route 16, Route 33)")
brown_fluff_loc = LocationData("brown fluff",
                               f"{amity} (Pikachu, {dp_psyduck})",
                               f"{amity} ({pt_pikachu}, {turtwig})",
                               f"{follower} (Route 39)")
black_fluff_loc = LocationData("black fluff",
                               f"{amity} ({dp_buneary})",
                               f"{amity} ({pt_skitty})",
                               f"{follower} (Route 42, Route 46, Dark Cave)")
orange_fluff_loc = LocationData("orange fluff",
                                f"{amity} (Pikachu, {dp_skitty})",
                                f"{amity} ({pt_pikachu}, {chimchar})",
                                f"{follower} (Route 15, Route 36)")
round_pebble_loc = LocationData("round pebble",
                                f"{amity} ({dp_shroomish}, {dp_psyduck})",
                                f"{amity} ({turtwig}, {chimchar})",
                                f"{follower} (Route 22, Route 28, Route 44, Route 45, Mt. Moon)")
glitter_boulder_loc = LocationData("glitter boulder",
                                   f"{amity} (Pikachu)",
                                   f"{amity} ({pt_psyduck}, {turtwig}, {amity_man})",
                                   f"{follower} (Route 24)")
snaggy_pebble_loc = LocationData("snaggy pebble",
                                 f"{amity} ({dp_psyduck}, {dp_buneary})",
                                 f"{amity} ({pt_psyduck}, {turtwig})",
                                 f"{follower} (Mt. Silver, Diglett's Cave)")
jagged_boulder_loc = LocationData("jagged boulder",
                                  f"{amity} ({dp_shroomish}, {dp_psyduck})",
                                  f"{amity} ({pt_skitty}, {turtwig})",
                                  f"{follower} (Mt. Silver, Diglett's Cave)")
black_pebble_loc = LocationData("black pebble",
                                f"{amity} ({dp_buneary})",
                                f"{amity} ({pt_skitty}, {amity_man})",
                                f"{follower} (Dark Cave, Union Cave, Cerulean Cave, Rock Tunnel)")
mini_pebble_loc = LocationData("mini pebble",
                               f"{amity} ({dp_skitty}, {dp_psyduck})",
                               f"{amity} ({pt_pikachu}, {amity_man})",
                               f"{follower} (Route 10, Route 26)")
pink_scale_loc = LocationData("pink scale",
                              f"{amity} ({dp_shroomish}, {dp_buneary})",
                              f"{amity} ({pt_skitty}, {pt_psyduck})",
                              f"{follower} (Route 13, Route 19, Route 40, Azalea Town)")
blue_scale_loc = LocationData("blue scale",
                              f"{amity} ({dp_skitty}, {dp_shroomish})",
                              f"{amity} ({pt_psyduck}, {chimchar})",
                              f"{follower} (Route 14, Route 20, Route 41, Mahogany Town, Lake of Rage, S.S. Aqua)")
green_scale_loc = LocationData("green scale",
                               f"{amity} ({dp_psyduck}, {dp_buneary})",
                               f"{amity} ({pt_skitty}, {turtwig})",
                               f"{follower} (Route 21, Route 34)")
purple_scale_loc = LocationData("purple scale",
                                f"{amity} (Pikachu, {dp_torchic})",
                                f"{amity} ({pt_pikachu}, {piplup})",
                                f"{follower} (Route 47, Lake of Rage)")
big_scale_loc = LocationData("big scale",
                             f"{amity} (Pikachu, {dp_skitty})",
                             f"{amity} ({pt_pikachu}, {chimchar}, {amity_man})",
                             f"{follower} (Route 27, Route 48, Olivine City)")
narrow_scale_loc = LocationData("narrow scale",
                                f"{amity} ({dp_psyduck}, {dp_torchic})",
                                f"{amity} ({turtwig}, {piplup})",
                                f"{follower} (Route 12, Lake of Rage)")
blue_feather_loc = LocationData("blue feather",
                                f"{amity} ({dp_shroomish})",
                                f"{amity} ({pt_psyduck})",
                                f"{follower} (Route 37)")
red_feather_loc = LocationData("red feather",
                               f"{amity} (Pikachu, {dp_torchic})",
                               f"{amity} ({pt_pikachu}, {piplup})",
                               f"{follower} (Route 38)")
yellow_feather_loc = LocationData("yellow feather",
                                  f"{amity} (Pikachu, {dp_torchic}, {dp_buneary})",
                                  f"{amity} ({pt_pikachu}, {pt_skitty}, {piplup})",
                                  f"{follower} (Route 3)")
white_feather_loc = LocationData("white feather",
                                 f"{amity} ({dp_skitty}, {dp_shroomish})",
                                 f"{amity} ({pt_psyduck}, {chimchar})",
                                 f"{follower} (Route 4)")
black_moustache_loc = LocationData("black moustache",
                                   f"{amity} (Pikachu, {dp_psyduck})",
                                   f"{amity} ({pt_pikachu}, {turtwig})",
                                   f"{follower} (Sprout Tower, Tohjo Falls)")
white_moustache_loc = LocationData("white moustache",
                                   f"{amity} ({dp_torchic})",
                                   f"{amity} ({piplup})",
                                   f"{follower} (Sprout Tower, Tohjo Falls)")
black_beard_loc = LocationData("black beard",
                               f"{amity} ({dp_shroomish}, {dp_torchic})",
                               f"{amity} ({pt_psyduck}, {piplup})",
                               f"{follower} (Sprout Tower, Bell Tower, Dragon's Den)")
white_beard_loc = LocationData("white beard",
                               f"{amity} ({dp_skitty}, {dp_shroomish})",
                               f"{amity} ({pt_psyduck}, {chimchar})",
                               f"{follower} (Sprout Tower, Bell Tower, Dragon's Den)")
small_leaf_loc = LocationData("small leaf",
                              f"{amity} (Pikachu, {dp_skitty})",
                              f"{amity} ({pt_pikachu}, {chimchar})",
                              f"{follower} (Route 5, Route 8, Cherrygrove City)")
big_leaf_loc = LocationData("big leaf",
                            f"{amity} ({dp_shroomish}, {dp_buneary})",
                            f"{amity} ({pt_skitty}, {pt_psyduck}, {amity_man})",
                            f"{follower} (Route 6, Ilex Forest)")
narrow_leaf_loc = LocationData("narrow leaf",
                               f"{amity} ({dp_torchic})",
                               f"{amity} ({piplup})",
                               f"{follower} (Route 7)")
shed_claw_loc = LocationData("shed claw",
                             f"{amity} ({dp_torchic}, {dp_buneary})",
                             f"{amity} ({pt_skitty}, {piplup})",
                             f"{follower} (Mt. Mortar, Whirl Islands)")
shed_horn_loc = LocationData("shed horn",
                             f"{amity} ({dp_psyduck}, {dp_buneary})",
                             f"{amity} ({pt_skitty}, {turtwig})",
                             f"{follower} (Mt. Mortar, Whirl Islands)")
thin_mushroom_loc = LocationData("thin mushroom",
                                 f"{amity} ({dp_skitty}, {dp_shroomish})",
                                 f"{amity} ({pt_psyduck}, {chimchar})",
                                 f"{follower} (Ilex Forest, Viridian Forest)")
thick_mushroom_loc = LocationData("thick mushroom",
                                  f"{amity} ({dp_psyduck})",
                                  f"{amity} ({turtwig}, {amity_man})",
                                  f"{follower} (Ilex Forest, Viridian Forest)")
stump_loc = LocationData("stump",
                         f"{amity} ({dp_skitty})",
                         f"{amity} ({chimchar}, {amity_man})",
                         f"{follower} (Ilex Forest, Viridian Forest)")
pretty_dewdrop_loc = LocationData("pretty dewdrop",
                                  f"{massage}",
                                  f"{follower} (Ilex Forest, Blackthorn City, Mt. Silver Cave, Viridian Forest, "
                                  f"S.S. Aqua)")
snow_crystal_loc = LocationData("snow crystal",
                                f"{massage}",
                                f"{follower} (Ice Path, Mt. Silver Cave)")
sparks_loc = LocationData("sparks",
                          f"{massage}",
                          f"{follower} (Olivine Lighthouse, Power Plant)")
shimmering_fire_loc = LocationData("shimmering fire",
                                   f"{massage}",
                                   f"{follower} (Burned Tower, Olivine Lighthouse)")
mystic_fire_loc = LocationData("mystic fire",
                               f"{massage}",
                               f"{follower} (Burned Tower, Olivine Lighthouse)")
determination_loc = LocationData("determination",
                                 f"{massage}",
                                 f"{follower} (Ruins of Alph, Team Rocket HQ, Battle Frontier)")
peculiar_spoon_loc = LocationData("peculiar spoon",
                                  f"{massage}",
                                  f"{follower} (Goldenrod Radio Tower, Route 25)")
puffy_smoke_loc = LocationData("puffy smoke",
                               f"{massage}",
                               f"{follower} (Burned Tower, Bell Tower)")
poison_extract_loc = LocationData("poison extract",
                                  f"{massage}",
                                  f"{follower} (Ruins of Alph, Team Rocket HQ, Victory Road, Cerulean Cave)")
wealthy_coin_loc = LocationData("wealthy coin",
                                f"{massage}",
                                f"{follower} (S.S. Aqua, Power Plant)")
eerie_thing_loc = LocationData("eerie thing",
                               f"{massage}",
                               f"{follower} (Ruins of Alph, Victory Road, Union Cave)")
spring_loc = LocationData("spring",
                          f"{massage}",
                          f"{follower} (Goldenrod Radio Tower, Route 25, Power Plant)")
seashell_loc = LocationData("seashell",
                            f"{massage}",
                            f"{follower} (Whirl Islands)")
humming_note_loc = LocationData("humming note",
                                f"{massage}",
                                f"{raffle}")
shiny_powder_loc = LocationData("shiny powder",
                                f"{massage}",
                                f"{follower} (Goldenrod Radio Tower, Battle Frontier, Mt. Moon)")
glitter_powder_loc = LocationData("glitter powder",
                                  f"{massage}",
                                  f"{follower} (Battle Frontier, Power Plant)")
red_flower_loc = LocationData("red flower",
                              f"{floaroma} (Trade 10 Razz Berries)",
                              f"{floaroma} (Trade 1 Cheri Berry)",
                              f"{follower} (Route 35, Ecruteak City)")
pink_flower_loc = LocationData("pink flower",
                               f"{floaroma} (Trade 10 Bluk Berries)",
                               f"{floaroma} (Trade 1 Chesto Berry)",
                               f"{follower} (Route 30, Cherrygrove City)")
white_flower_loc = LocationData("white flower",
                                f"{floaroma} (Trade 10 Nanab Berries)",
                                f"{floaroma} (Trade 1 Pecha Berry)",
                                f"{follower} (Route 9, Route 32, National Park)")
blue_flower_loc = LocationData("blue flower",
                               f"{floaroma} (Trade 30 Cornn Berries)",
                               f"{floaroma} (Trade 1 Oran Berry)",
                               f"{follower} (Route 11, National Park)")
orange_flower_loc = LocationData("orange flower",
                                 f"{floaroma} (Trade 15 Magost Berries)",
                                 f"{floaroma} (Trade 1 Rawst Berry)",
                                 f"{follower} (Route 18, Route 43, National Park, Ecruteak City)")
yellow_flower_loc = LocationData("yellow flower",
                                 f"{floaroma} (Trade 15 Rabuta Berries)",
                                 f"{floaroma} (Trade 1 Aspear Berry)",
                                 f"{follower} (Route 1, Route 17, Pallet Town, Viridian City, Pewter City, "
                                 f"Cerulean City, Lavender Town, Vermilion City, Celadon City, Fuchsia City, "
                                 f"Cinnabar Island, Saffron City, Violet City, Ecruteak City)")
googly_specs_loc = LocationData("googly specs",
                                f"{floaroma} (Trade 20 Nomel Berries)",
                                f"{floaroma} (Trade 1 Leppa Berry)",
                                f"{raffle}")
black_specs_loc = LocationData("black specs",
                               f"{floaroma} (Trade 20 Wepear Berries)",
                               f"{floaroma} (Trade 1 Persim Berry)",
                               f"{raffle}")
gorgeous_specs_loc = LocationData("gorgeous specs",
                                  f"{floaroma} (Trade 40 Pinap Berries)",
                                  f"{floaroma} (Trade 10 Razz Berries)",
                                  f"{raffle}")
sweet_candy_loc = LocationData("sweet candy",
                               f"{floaroma} (Trade 30 Nanab Berries)",
                               f"{floaroma} (Trade 10 Bluk Berries)",
                               f"{raffle}")
confetti_loc = LocationData("confetti",
                            f"{floaroma} (Trade 30 Razz Berries)",
                            f"{floaroma} (Trade 10 Nanab Berries)",
                            f"{raffle}")
colored_parasol_loc = LocationData("colored parasol",
                                   f"{floaroma} (Trade 50 Magost Berries)",
                                   f"{floaroma} (Trade 10 Wepear Berries)",
                                   f"{raffle}")
old_umbrella_loc = LocationData("old umbrella",
                                f"{floaroma} (Trade 50 Pamtre Berries)",
                                f"{floaroma} (Trade 10 Pinap Berries)",
                                f"{raffle}")
spotlight_loc = LocationData("spotlight",
                             f"{floaroma} (Trade 80 Nomel Berries)",
                             f"{floaroma} (Trade 50 Cornn Berries)",
                             f"{raffle}")
cape_loc = LocationData("cape",
                        f"{floaroma} (Trade 250 Cornn Berries)",
                        f"{floaroma} (Trade 100 Pamtre Berries)",
                        f"{raffle}")
standing_mike_loc = LocationData("standing mike",
                                 f"{floaroma} (Trade 80 Bluk Berries)",
                                 f"{floaroma} (Trade 50 Magost Berries)",
                                 f"{raffle}")
surfboard_loc = LocationData("surfboard",
                             f"{floaroma} (Trade 180 Wepear Berries)",
                             f"{floaroma} (Trade 100 Watmel Berries)",
                             f"{raffle}")
carpet_loc = LocationData("carpet",
                          f"{floaroma} (Trade 100 Spelon Berries)",
                          f"{floaroma} (Trade 50 Rabuta Berries)",
                          f"{raffle}")
retro_pipe_loc = LocationData("retro pipe",
                              f"{floaroma} (Trade 120 Pamtre Berries)",
                              f"{floaroma} (Trade 50 Nomel Berries)",
                              f"{raffle}")
fluffy_bed_loc = LocationData("fluffy bed",
                              f"{floaroma} (Trade 150 Watmel Berries)",
                              f"{floaroma} (Trade 100 Durin Berries)",
                              f"{raffle}")
mirror_ball_loc = LocationData("mirror ball",
                               f"{floaroma} (Trade 250 Durin Berries)",
                               f"{floaroma} (Trade 100 Spelon Berries)",
                               f"{raffle}")
photo_board_loc = LocationData("photo board",
                               f"{floaroma} (Trade 200 Belue Berries)",
                               f"{floaroma} (Trade 100 Belue Berries)",
                               f"{raffle}")
pink_barrette_loc = LocationData("pink barrette",
                                 "Reward for winning a Normal Rank Cute Contest for the first time",
                                 f"{raffle}")
red_barrette_loc = LocationData("red barrette",
                                "Reward for winning a Normal Rank Cool Contest for the first time",
                                f"{raffle}")
blue_barrette_loc = LocationData("blue barrette",
                                 "Reward for winning a Normal Rank Beauty Contest for the first time",
                                 f"{raffle}")
yellow_barrette_loc = LocationData("yellow barrette",
                                   "Reward for winning a Normal Rank Tough Contest for the first time",
                                   f"{raffle}")
green_barrette_loc = LocationData("green barrette",
                                  "Reward for winning a Normal Rank Smart Contest for the first time",
                                  f"{raffle}")
pink_balloon_loc = LocationData("pink balloon",
                                "Reward for winning a Great Rank Cute Contest for the first time",
                                f"{raffle}")
red_balloons_loc = LocationData("red balloons",
                                "Reward for winning a Great Rank Cool Contest for the first time",
                                f"{raffle}")
blue_balloons_loc = LocationData("blue balloons",
                                 "Reward for winning a Great Rank Beauty Contest for the first time",
                                 f"{raffle}")
yellow_balloon_loc = LocationData("yellow balloon",
                                  "Reward for winning a Great Rank Tough Contest for the first time",
                                  f"{raffle}")
green_balloons_loc = LocationData("green balloons",
                                  "Reward for winning a Great Rank Smart Contest for the first time",
                                  f"{raffle}")
lace_headdress_loc = LocationData("lace headdress",
                                  "Reward for winning an Ultra Rank Cute Contest for the first time",
                                  f"{raffle}")
top_hat_loc = LocationData("top hat",
                           "Reward for winning an Ultra Rank Cool Contest for the first time",
                           f"{raffle}")
silk_veil_loc = LocationData("silk veil",
                             "Reward for winning an Ultra Rank Beauty Contest for the first time",
                             f"{raffle}")
heroic_headband_loc = LocationData("heroic headband",
                                   "Reward for winning an Ultra Rank Tough Contest for the first time",
                                   f"{raffle}")
professor_hat_loc = LocationData("professor hat",
                                 "Reward for winning an Ultra Rank Smart Contest for the first time",
                                 f"{raffle}")
flower_stage_loc = LocationData("flower stage",
                                "Reward for winning a Master Rank Cute Contest for the first time",
                                f"{raffle}")
gold_pedestal_loc = LocationData("gold pedestal",
                                 "Reward for winning a Master Rank Cool Contest for the first time",
                                 f"{raffle}")
glass_stage_loc = LocationData("glass stage",
                               "Reward for winning a Master Rank Beauty Contest for the first time",
                               f"{raffle}")
award_podium_loc = LocationData("award podium",
                                "Reward for winning a Master Rank Tough Contest for the first time",
                                f"{raffle}")
cube_stage_loc = LocationData("cube stage",
                              "Reward for winning a Master Rank Smart Contest for the first time",
                              f"{raffle}")
turtwig_mask_loc = LocationData("turtwig mask",
                                "Jubilife TV 2F (If the player started with Turtwig), "
                                "Veilstone Department Store 1F (If the player started with Chimchar), "
                                "Pastoria City (If the player started with Piplup)",
                                "Celadon Department Store 2F")
chimchar_mask_loc = LocationData("chimchar mask",
                                 "Jubilife TV 2F (If the player started with Chimchar), "
                                 "Veilstone Department Store 1F (If the player started with Piplup), "
                                 "Pastoria City (If the player started with Turtwig)",
                                 "Celadon Department Store 2F")
piplup_mask_loc = LocationData("piplup mask",
                               "Jubilife TV 2F (If the player started with Piplup), "
                               "Veilstone Department Store 1F (If the player started with Turtwig), "
                               "Pastoria City (If the player started with Chimchar)",
                               "Celadon Department Store 2F")
big_tree_loc = LocationData("big tree",
                            "Eterna Forest Outskirts",
                            f"{raffle}")
flag_loc = LocationData("flag",
                        "Cycling Road South Gate",
                        f"{raffle}")
crown_loc = LocationData("crown",
                         "Pal Park (FireRed in GBA slot)")
tiara_loc = LocationData("tiara",
                         "Pal Park (LeafGreen in GBA slot)")
comet_loc = LocationData("comet",
                         "Unobtainable")
accessories = [
    white_fluff, yellow_fluff, pink_fluff, brown_fluff, black_fluff, orange_fluff,
    round_pebble, glitter_boulder, snaggy_pebble, jagged_boulder, black_pebble, mini_pebble,
    pink_scale, blue_scale, green_scale, purple_scale, big_scale, narrow_scale,
    blue_feather, red_feather, yellow_feather, white_feather,
    black_moustache, white_moustache, black_beard, white_beard, small_leaf, big_leaf, narrow_leaf,
    shed_claw, shed_horn, thin_mushroom, thick_mushroom, stump,
    pretty_dewdrop, snow_crystal, sparks, shimmering_fire, mystic_fire,
    determination, peculiar_spoon, puffy_smoke, poison_extract,
    wealthy_coin, eerie_thing, spring, seashell, humming_note, shiny_powder, glitter_powder,
    red_flower, pink_flower, white_flower, blue_flower, orange_flower, yellow_flower,
    googly_specs, black_specs, gorgeous_specs, sweet_candy, confetti,
    colored_parasol, old_umbrella, spotlight, cape, standing_mike, surfboard, 
    carpet, retro_pipe, fluffy_bed, mirror_ball, photo_board,
    pink_barrette, red_barrette, blue_barrette, yellow_barrette, green_barrette,
    pink_balloon, red_balloons, blue_balloons, yellow_balloon, green_balloons,
    lace_headdress, top_hat, silk_veil, heroic_headband, professor_hat,
    flower_stage, gold_pedestal, glass_stage, award_podium, cube_stage,
    turtwig_mask, chimchar_mask, piplup_mask, big_tree, flag, crown, tiara, comet
]

accessory_locs = [
    white_fluff_loc, yellow_fluff_loc, pink_fluff_loc, brown_fluff_loc, black_fluff_loc, orange_fluff_loc,
    round_pebble_loc, glitter_boulder_loc, snaggy_pebble_loc, jagged_boulder_loc, black_pebble_loc, mini_pebble_loc,
    pink_scale_loc, blue_scale_loc, green_scale_loc, purple_scale_loc, big_scale_loc, narrow_scale_loc,
    blue_feather_loc, red_feather_loc, yellow_feather_loc, white_feather_loc,
    black_moustache_loc, white_moustache_loc, black_beard_loc, white_beard_loc,
    small_leaf_loc, big_leaf_loc, narrow_leaf_loc,
    shed_claw_loc, shed_horn_loc, thin_mushroom_loc, thick_mushroom_loc, stump_loc,
    pretty_dewdrop_loc, snow_crystal_loc, sparks_loc, shimmering_fire_loc, mystic_fire_loc,
    determination_loc, peculiar_spoon_loc, puffy_smoke_loc, poison_extract_loc,
    wealthy_coin_loc, eerie_thing_loc, spring_loc, seashell_loc, humming_note_loc, shiny_powder_loc, glitter_powder_loc,
    red_flower_loc, pink_flower_loc, white_flower_loc, blue_flower_loc, orange_flower_loc, yellow_flower_loc,
    googly_specs_loc, black_specs_loc, gorgeous_specs_loc, sweet_candy_loc, confetti_loc,
    colored_parasol_loc, old_umbrella_loc, spotlight_loc, cape_loc, standing_mike_loc, surfboard_loc,
    carpet_loc, retro_pipe_loc, fluffy_bed_loc, mirror_ball_loc, photo_board_loc,
    pink_barrette_loc, red_barrette_loc, blue_barrette_loc, yellow_barrette_loc, green_barrette_loc,
    pink_balloon_loc, red_balloons_loc, blue_balloons_loc, yellow_balloon_loc, green_balloons_loc,
    lace_headdress_loc, top_hat_loc, silk_veil_loc, heroic_headband_loc, professor_hat_loc,
    flower_stage_loc, gold_pedestal_loc, glass_stage_loc, award_podium_loc, cube_stage_loc,
    turtwig_mask_loc, chimchar_mask_loc, piplup_mask_loc, big_tree_loc, flag_loc, crown_loc, tiara_loc, comet_loc
]

error = "Something has gone terribly wrong here. Please report this to the developer."
min_heart_value = 2
theme_choice = 2

accessory_page_num = 1

while True:
    quit_loop = False
    choice = str(input("Choose a mode: ")).lower()
    if choice in ("s", "se", "sea", "sear", "searc", "search"):
        while True:
            searching = True
            search = str(input("Choose an accessory: ")).lower()
            if search in ("e", "ex", "exi", "exit", "q", "qu", "qui", "quit", "b", "ba", "bac", "back"):
                break
            elif search in ("h", "he", "hel", "help"):
                print('"accessories": Get a list of valid accessory names.')
                print('"exit", "quit", "back": Return to mode selection.')
                continue
            elif search in ("a", "ac") or "acc" in search:
                while True:
                    if quit_loop:
                        quit_loop = False
                        break
                    new_page = True

                    for accessory in accessories:
                        if new_page:
                            print(f"===== Page {accessory_page_num} =====")
                            new_page = False
                        if accessory and accessory[1] == accessory_page_num:
                            print("-", accessory[0])
                    while True:
                        get_next_page = input().lower()
                        if get_next_page in ("h", "he", "hel", "help"):
                            print('"next", enter: Display the next page.')
                            print('"back": Display the previous page.')
                            print('"1", "2", "3", etc.: Display the selected page.')
                            print('"exit", "quit": Return to search.')
                            continue
                        elif get_next_page in ("e", "ex", "exi", "exit", "q", "qu", "qui", "quit"):
                            quit_loop = True
                            break
                        elif get_next_page in ("", "n", "ne", "nex", "next"):
                            if accessory_page_num < 14:
                                accessory_page_num += 1
                            else:
                                quit_loop = True
                            break
                        elif get_next_page in ("b", "ba", "bac", "back"):
                            if accessory_page_num > 1:
                                accessory_page_num -= 1
                            else:
                                quit_loop = True
                            break
                        else:
                            try:
                                get_next_page_val = int(get_next_page)
                                if get_next_page_val < 15 and get_next_page_val > 0:
                                    accessory_page_num = get_next_page_val
                                    break
                                elif get_next_page_val < 1:
                                    print('Please input a number from 1 to 14.')
                                    continue
                                else:
                                    print('There are only 14 pages.')
                                    continue
                            except:
                                print('Use "help" to get a list of valid options.')
                                continue
                continue
            for accessory in accessory_locs:
                if accessory[0] == search:
                    searching = False
                    if accessory[2] == "":
                        print("All Games: " + accessory[1])
                    elif accessory[3] == "":
                        print(dppt + accessory[1])
                    else:
                        print(dp + accessory[1])
                    if accessory[3] == "" and not accessory[2] == "":
                        print(hgss + accessory[2])
                    elif accessory[3] != "":
                        print(pt + accessory[2])
                    else:
                        pass
                    if accessory[3] != "":
                        print(hgss + accessory[3])
                    else:
                        pass
                    break
            if searching:
                print('Please input a valid accessory name (or type "help" for information on valid commands).')
                continue
    elif choice in ("c", "co", "con", "cont", "conte", "contes", "contest", "contests"):
        while True:
            contest_page_num = 1
            theme = str(input("Choose a theme: ")).lower()
            if theme in ("e", "ex", "exi", "exit", "q", "qu", "qui", "quit", "b", "ba", "bac", "back"):
                break
            elif theme in ("h", "he", "hel", "help"):
                print('"themes": Get a list of valid theme names.')
                print('"minimum": Choose a minimum heart value to display. Default: 2')
                print('"exit", "quit", "back": Return to mode selection.')
                continue
            elif theme in ("t", "th", "the", "them", "theme", "themes"):
                print("'bright'")
                print("'colorful'")
                print("'created'")
                print("'festive'")
                print("'flexible'")
                print("'gaudy'")
                print("'intangible'")
                print("'natural'")
                print("'relaxed'")
                print("'shapely'")
                print("'sharp'")
                print("'solid'")
                continue
            elif theme in ("m", "mi", "min", "mini", "minim", "minimu", "minimum"):
                while True:
                    min_value = input("Choose a minimum heart value: ")
                    if min_value in ("1", "2"):
                        min_heart_value = int(min_value)
                        break
                    elif min_value in ("e", "ex", "exi", "exit", "q", "qu", "qui", "quit", "b", "ba", "bac", "back"):
                        break
                    else:
                        print("Minimum heart value must be either 1 or 2.")
                        continue
            elif theme in ("bright", "colorful", "created", "festive", "flexible", "gaudy",
                           "intangible", "natural", "relaxed", "shapely", "sharp", "solid"):
                match theme:
                    case "bright":
                        theme_choice = 2
                    case "colorful":
                        theme_choice = 3
                    case "created":
                        theme_choice = 4
                    case "festive":
                        theme_choice = 5
                    case "flexible":
                        theme_choice = 6
                    case "gaudy":
                        theme_choice = 7
                    case "intangible":
                        theme_choice = 8
                    case "natural":
                        theme_choice = 9
                    case "relaxed":
                        theme_choice = 10
                    case "shapely":
                        theme_choice = 11
                    case "sharp":
                        theme_choice = 12
                    case "solid":
                        theme_choice = 13
                    case _:
                        print("Invalid theme.")
                        print(error)
                        quit_loop = True
                while True:
                    if quit_loop:
                        quit_loop = False
                        break
                    new_page = True

                    for accessory in accessories:
                        if new_page:
                            print(f"===== Page {contest_page_num} =====")
                            new_page = False
                        if accessory[theme_choice] >= min_heart_value and accessory[1] == contest_page_num:
                            if accessory[14] is True:
                                print("-", accessory[0])
                    while True:
                        get_next_page = input().lower()
                        if get_next_page in ("h", "he", "hel", "help"):
                            print('"next", enter: Display the next page.')
                            print('"back": Display the previous page.')
                            print('"1", "2", "3", etc.: Display the selected page.')
                            print('"exit", "quit": Return to theme selection.')
                            continue
                        elif get_next_page in ("e", "ex", "exi", "exit", "q", "qu", "qui", "quit"):
                            quit_loop = True
                            break
                        elif get_next_page in ("", "n", "ne", "nex", "next"):
                            if contest_page_num < 14:
                                contest_page_num += 1
                            else:
                                quit_loop = True
                            break
                        elif get_next_page in ("b", "ba", "bac", "back"):
                            if contest_page_num > 1:
                                contest_page_num -= 1
                            else:
                                quit_loop = True
                            break
                        else:
                            try:
                                get_next_page_val = int(get_next_page)
                                if get_next_page_val < 15 and get_next_page_val > 0:
                                    contest_page_num = get_next_page_val
                                    break
                                elif get_next_page_val < 1:
                                    print('Please input a number from 1 to 14.')
                                    continue
                                else:
                                    print('There are only 14 pages.')
                                    continue
                            except:
                                print('Use "help" to get a list of valid options.')
                                continue
            else:
                print('Please input a valid theme (or type "help" for information on valid commands).')
    elif choice in ("bd", "bg") or "backd" in choice or "backg" in choice:
        print("Backdrops are another feature of dressing up Pokemon.")
        print("The ways of obtaining them are usually quite simple, and they apply to almost all backdrops, "
              "so those methods have instead been listed here:")
        print("In Diamond and Pearl, a random Backdrop is rewarded for getting a single-digit match at the "
              "Pokemon Lottery Corner located inside of the Jubilife TV building.")
        print("In Platinum, a random Backdrop is instead given to the player each day by a woman on the first floor of "
              "the Global Terminal, also located in Jubilife City.")
        print("In HeartGold and SoulSilver, Backdrops are included amongst the rewards of the Goldenrod Tunnel "
              "accessory raffle.")
        print("Additionally, the player receives a random selection of Backdrops along with the Fashion Case:")
        print("The 'Ranch', 'City at Night', 'Snowy Town', 'Fiery', 'Outer Space', 'Cumulus Cloud', 'Desert', "
              "and 'Flower Patch' Backdrops are all possible options.")
        print("There are also three Backdrops which require you to interact with a woman in the Pal Park with certain "
              "games in the GBA slot:")
        print("These are the 'Seafloor' Backdrop for Pokemon Sapphire, the 'Underground' Backdrop for Pokemon Ruby, "
              "and the 'Sky' Backdrop for Pokemon Emerald.")
        print("Lastly, the 'Theater' Backdrop exists within the game's files but was never made obtainable.")
        print('You can type "bd_list" for a full list of Backdrops.')
    elif choice in ("bd_list", "bg_list"):
        print("'Dress Up'")
        print("'Ranch'")
        print("'City at Night'")
        print("'Snowy Town'")
        print("'Fiery'")
        print("'Outer Space'")
        print("'Cumulus Cloud'")
        print("'Desert'")
        print("'Flower Patch'")
        print("'Future Room'")
        print("'Open Sea'")
        print("'Total Darkness'")
        print("'Tatami Room'")
        print("'Gingerbread Room'")
        print("'Seafloor'")
        print("'Underground'")
        print("'Sky'")
        print("'Theater'")
    elif choice in ("h", "he", "hel", "help"):
        print('"contests": Search for a contest theme to get a list of optimal accessories to use for it.')
        print('"search": Search for an accessory to find where it can be obtained in-game.')
        print('"backdrops", "backgrounds": Display information on obtaining Backdrops.')
        print('"exit", "quit": End the program.')
        continue
    elif choice in ("e", "ex", "exi", "exit", "q", "qu", "qui", "quit"):
        break
    else:
        print('Please input a valid mode (or type "help" for information on valid commands).')
        continue
