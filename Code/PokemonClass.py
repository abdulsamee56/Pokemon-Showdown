import random

# Define a class for Pokémon characters
class Pokemon:
    # Initialize a new Pokémon with its basic attributes and an optional moveset
    def __init__(self, name, type1, type2, hp, attack, defense, specialAttack, specialDefense, speed, level, moveset=None):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.specialAttack = specialAttack
        self.specialDefense = specialDefense
        self.speed = speed
        self.level = level
        # If no moveset is provided, initialize with an empty list
        if moveset is None:
            self.moveset = []
        else:
            self.moveset = moveset
        # Calculate battle HP, currently unused in this implementation
        battleHP = hp + level + 10

    # Display basic information about the Pokémon
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Type 1: {self.type1}")
        print(f"Type 2: {self.type2}")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Special Attack: {self.specialAttack}")
        print(f"Special Defense: {self.specialDefense}")
        print(f"Speed: {self.speed}")
        print(f"Level: {self.level}")

# Define a class for moves that Pokémon can perform
class Move:
    # Initialize a new move with its attributes
    def __init__(self, name, move_type, attacktype, power, accuracy, pp):
        self.name = name
        self.move_type = move_type
        self.attacktype = attacktype  # Specifies if the move is Physical or Special
        self.power = power
        self.accuracy = accuracy
        self.pp = pp  # Power Points determine how many times a move can be used

# Current moves
body_slam = Move("Body Slam", "Normal", "Physical", 85, 100, 15)
earthquake = Move("Earthquake", "Ground", "Physical",100, 100, 10)
scald = Move("Scald", "Water", "Special", 80, 100, 15)
psychic_move = Move("Psychic", "Psychic", "Special", 90, 100, 10)
ice_beam = Move("Ice Beam", "Ice", "Special", 90, 100, 10)
waterfall = Move("Waterfall", "Water", "Physical", 80, 100, 15)
ice_punch = Move("Ice Punch", "Ice", "Physical", 75, 100, 15)
knock_off = Move("Knock Off", "Dark", "Physical", 65, 100, 20)
power_whip = Move("Power Whip", "Grass", "Physical", 120, 85, 10)
dazzling_gleam = Move("Dazzling Gleam", "Fairy", "Special", 80, 100, 10)
flare_blitz = Move("Flare Blitz", "Fire", "Physical", 120, 100, 15)
high_jump_kick = Move("High Jump Kick", "Fighting", "Physical", 130, 90, 10)
leaf_storm = Move("Leaf Storm", "Grass", "Special", 130, 90, 5)
dragon_pulse = Move("Dragon Pulse", "Dragon", "Special", 85, 100, 10)
focus_blast = Move("Focus Blast", "Fighting", "Special", 120, 70, 5)
energy_ball = Move("Energy Ball", "Grass", "Special", 90, 100, 10)
thunder_punch = Move("Thunder Punch", "Electric", "Physical", 75, 100, 15)
cross_chop = Move("Cross Chop", "Fighting", "Physical", 100, 80, 5)
close_combat = Move("Close Combat", "Fighting", "Physical", 120, 100, 5)
megahorn = Move("Megahorn", "Bug", "Physical", 120, 85, 10)
stone_edge = Move("Stone Edge", "Rock", "Physical", 100, 80, 5)
fire_fang = Move("Fire Fang", "Fire", "Physical", 65, 95, 15)
ice_shard = Move("Ice Shard", "Ice", "Physical", 40, 100, 30)
icicle_crash = Move("Icicle Crash", "Ice", "Physical", 85, 90, 10)
thunderbolt = Move("Thunderbolt", "Electric", "Special", 90, 100, 15)
flash_cannon = Move("Flash Cannon", "Steel", "Special", 80, 100, 10)
meteor_mash = Move("Meteor Mash", "Steel", "Physical", 90, 90, 10)
zen_headbutt = Move("Zen Headbutt", "Psychic", "Physical", 80, 90, 15)
bullet_punch = Move("Bullet Punch", "Steel", "Physical", 40, 100, 30)
fire_punch = Move("Fire Punch", "Fire", "Physical", 75, 100, 15)
aura_sphere = Move("Aura Sphere", "Fighting", "Special", 80, 100, 20)
extreme_speed = Move("Extreme Speed", "Normal", "Physical", 80, 100, 5)
hydro_pump = Move("Hydro Pump", "Water", "Special", 110, 80, 5)
air_slash = Move("Air Slash", "Flying", "Special", 75, 95, 15)
poison_jab = Move("Poison Jab", "Poison", "Physical", 80, 100, 20)
crunch = Move("Crunch", "Dark", "Physical", 80, 100, 15)
shadow_ball = Move("Shadow Ball", "Ghost", "Special", 80, 100, 15)
sludge_bomb = Move("Sludge Bomb", "Poison", "Special", 90, 100, 10)
superpower = Move("Superpower", "Fighting", "Physical", 120, 100, 5)
dragon_claw = Move("Dragon Claw", "Dragon", "Physical", 80, 100, 15)
blizzard =  Move("Blizzard", "Ice", "Special", 110, 70, 5)
X_Scissor = Move("X Scissor", "Bug", "Physical", 80, 100, 15)
tri_attack = Move("Tri Attack", "Normal", "Special", 80, 100, 15)
zap_cannon = Move("Zap Cannon", "Electric", "Special", 120, 50, 5)
shock_wave = Move("Shock Wave", "Electric", "Special", 60, 100, 20)

#Charizard's moveset
charizard_moves = [flare_blitz, dragon_claw, air_slash, earthquake]
charizard = Pokemon("Charizard", "Fire", "Flying", 78, 84, 78, 109, 85, 100, 50, charizard_moves)

# Snorlax's moveset
snorlax_moves = [body_slam, earthquake, blizzard, earthquake]
snorlax = Pokemon("Snorlax", "Normal", "Null", 160, 110, 65, 65, 110, 30, 50, snorlax_moves)

# Slowbro's moveset
slowbro_moves = [scald, psychic_move, blizzard, ice_beam]
slowbro = Pokemon("Slowbro", "Water", "Psychic", 95, 75, 110, 100, 80, 30, 50, slowbro_moves)

# Swampert's moveset
swampert_moves = [earthquake, waterfall, ice_punch, stone_edge]
swampert = Pokemon("Swampert", "Water", "Ground", 100, 110, 90, 85, 90, 60, 50, swampert_moves)

# Lickilicky's moveset
lickilicky_moves = [body_slam, knock_off, power_whip, blizzard]
lickilicky = Pokemon("Lickilicky", "Normal", "Null", 110, 85, 95, 80, 95, 50, 50, lickilicky_moves)

# Mr. Mime's moveset
mr_mime_moves = [psychic_move, dazzling_gleam, shock_wave, shadow_ball]
mr_mime = Pokemon("Mr. Mime", "Psychic", "Fairy", 40, 45, 65, 100, 120, 90, 50, mr_mime_moves)

# Blaziken's moveset
blaziken_moves = [flare_blitz, high_jump_kick, knock_off, close_combat]
blaziken = Pokemon("Blaziken", "Fire", "Fighting", 80, 120, 70, 110, 70, 80, 50, blaziken_moves)

#Sceptile's moveset
sceptile_moves = [leaf_storm, dragon_pulse, focus_blast, energy_ball]
sceptile = Pokemon("Sceptile", "Grass", "Null", 70, 85, 65, 105, 85, 120, 50, sceptile_moves)

# Electivire's moveset
electivire_moves = [thunder_punch, ice_punch, earthquake, cross_chop]
electivire = Pokemon("Electivire", "Electric", "Null", 75, 123, 67, 95, 85, 95, 50, electivire_moves)

#Heracross's moveset
heracross_moves = [close_combat, megahorn, stone_edge, knock_off]
heracross = Pokemon("Heracross", "Bug", "Fighting", 80, 125, 75, 40, 95, 85, 50, heracross_moves)

# Garchomp's moveset
garchomp_moves = [earthquake, dragon_claw, stone_edge, fire_fang]
garchomp = Pokemon("Garchomp", "Dragon", "Ground", 108, 130, 95, 80, 85, 102, 50, garchomp_moves)

#Mamoswine's moveset
mamoswine_moves = [ice_shard, earthquake, icicle_crash, stone_edge]
mamoswine = Pokemon("Mamoswine", "Ice", "Ground", 110, 130, 80, 70, 60, 80, 50, mamoswine_moves)

#Magmezone's moveset
magnezone_moves = [thunderbolt, flash_cannon, tri_attack, zap_cannon]
magnezone = Pokemon("Magnezone", "Electric", "Steel", 70, 70, 115, 130, 90, 60, 50, magnezone_moves)

#Metagross's moveset
metagross_moves = [meteor_mash, zen_headbutt, earthquake, bullet_punch]
metagross = Pokemon("Metagross", "Steel", "Psychic", 80, 135, 130, 95, 90, 70, 50, metagross_moves)

#Flygon's moveset
flygon_moves = [earthquake, dragon_claw, fire_punch, stone_edge]
flygon = Pokemon("Flygon", "Ground", "Dragon", 80, 100, 80, 80, 80, 100, 50, flygon_moves)

#Lucario's moveset
lucario_moves = [aura_sphere, flash_cannon, close_combat, extreme_speed]
lucario = Pokemon("Lucario", "Fighting", "Steel", 70, 110, 70, 115, 70, 90, 50, lucario_moves)

#Empoleon's moveset
empoleon_moves = [hydro_pump, flash_cannon, ice_beam, earthquake]
empoleon = Pokemon("Empoleon", "Water", "Steel", 84, 86, 88, 111, 101, 60, 50, empoleon_moves)

#Tyranitar's moveset
tyranitar_moves = [stone_edge, crunch, earthquake, fire_punch]
tyranitar = Pokemon("Tyranitar", "Rock", "Dark", 100, 134, 110, 95, 100, 61, 50, tyranitar_moves)

#Drapion's Moveset
drapion_moves = [knock_off, poison_jab, earthquake, crunch]
drapion = Pokemon("Drapion", "Poison", "Dark", 70, 90, 110, 60, 75, 95, 50, drapion_moves)

#Gengar's moveset
gengar_moves = [shadow_ball, sludge_bomb, focus_blast, thunderbolt]
gengar = Pokemon("Gengar", "Ghost", "Poison", 60, 65, 60, 130, 75, 110, 50, gengar_moves)

#Scizor's moveset
scizor_moves = [bullet_punch, body_slam, superpower, X_Scissor]
scizor = Pokemon("Scizor", "Bug", "Steel", 70, 130, 100, 55, 80, 65, 50, scizor_moves)

# Function to calculate damage dealt from one Pokémon to another using a specific move
def damagecalc(attackingPokemon,aiPokemon,Move):

    # Calculate various factors influencing damage
    # Includes Pokémon's level, move's power, attacker's attack vs. defender's defense, etc.
    # Type effectiveness and STAB (Same Type Attack Bonus) are also considered

    pkmLevel = attackingPokemon.level
    movePower = Move.power
    pkmAttack = attackingPokemon.attack
    pkmDefense = aiPokemon.defense
    pkmspeAttack = attackingPokemon.specialAttack
    pkmspeDefense = aiPokemon.specialDefense
    attackType = Move.attacktype
    attackingType1 = attackingPokemon.type1
    attackingType2 = attackingPokemon.type2
    moveType = Move.move_type
    defendingType1 = aiPokemon.type1
    defendingType2 = aiPokemon.type2
    moveAccuracy = Move.accuracy

    hits = (random.randint(0, 100))
    if hits <= moveAccuracy:
        type_effectiveness = {
            'Normal': {'Fighting': 2, 'Ghost': 0},
            'Fire': {'Water': 2, 'Grass': 0.5, 'Ice': 0.5, 'Bug': 0.5, 'Steel': 0.5, 'Fire': 0.5, 'Rock': 2, 'Dragon': 0.5},
            'Water': {'Electric': 2, 'Grass': 2, 'Fire': 0.5, 'Water': 0.5, 'Ice': 0.5, 'Steel': 0.5},
            'Electric': {'Ground': 2, 'Electric': 0.5, 'Flying': 0.5, 'Steel': 0.5},
            'Grass': {'Fire': 2, 'Ice': 2, 'Poison': 2, 'Flying': 2, 'Bug': 2, 'Water': 0.5, 'Grass': 0.5, 'Electric': 0.5, 'Ground': 0.5},
            'Ice': {'Fire': 2, 'Fighting': 2, 'Rock': 2, 'Steel': 2, 'Ice': 0.5},
            'Fighting': {'Flying': 2, 'Psychic': 2, 'Fairy': 2, 'Bug': 0.5, 'Rock': 0.5, 'Dark': 0.5},
            'Poison': {'Ground': 2, 'Psychic': 2, 'Grass': 0.5, 'Fighting': 0.5, 'Poison': 0.5, 'Bug': 0.5, 'Fairy': 0.5},
            'Ground': {'Water': 2, 'Grass': 2, 'Ice': 2, 'Poison': 0.5, 'Rock': 0.5, 'Electric': 0},
            'Flying': {'Electric': 2, 'Ice': 2, 'Rock': 2, 'Grass': 0.5, 'Fighting': 0.5, 'Bug': 0.5, 'Ground': 0},
            'Psychic': {'Bug': 2, 'Ghost': 2, 'Dark': 2, 'Fighting': 0.5, 'Psychic': 0.5},
            'Bug': {'Fire': 2, 'Flying': 2, 'Rock': 2, 'Grass': 0.5, 'Fighting': 0.5, 'Ground': 0.5},
            'Rock': {'Water': 2, 'Grass': 2, 'Fighting': 2, 'Ground': 2, 'Steel': 2, 'Fire': 0.5, 'Ice': 0.5, 'Flying': 0.5, 'Bug': 0.5},
            'Ghost': {'Ghost': 2, 'Dark': 2, 'Bug': 0.5, 'Poison': 0.5, 'Normal': 0, 'Fighting': 0},
            'Dragon': {'Ice': 2, 'Dragon': 2, 'Fairy': 2, 'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Grass': 0.5},
            'Dark': {'Fighting': 2, 'Bug': 2, 'Fairy': 2, 'Ghost': 0.5, 'Psychic': 0},
            'Steel': {'Fire': 2, 'Fighting': 2, 'Ground': 2, 'Poison': 0, 'Flying': 0.5, 'Rock': 0.5, 'Bug': 0.5, 'Steel': 0.5, 'Grass': 0.5, 'Psychic': 0.5, 'Ice': 0.5, 'Dragon': 0.5, 'Fairy': 0.5},
            'Fairy': {'Poison': 2, 'Steel': 2, 'Fighting': 0.5, 'Bug': 0.5, 'Dark': 0.5, 'Dragon': 0},
            'Null': {}
        }

        #Checks First Type
        if defendingType1 in type_effectiveness and moveType in type_effectiveness[defendingType1]:
            TYPE1 = type_effectiveness[defendingType1][moveType]
        else:
            TYPE1 = 1
        #Checks Second Type
        if defendingType2 in type_effectiveness and moveType in type_effectiveness[defendingType2]:
            TYPE2 = type_effectiveness[defendingType2][moveType]
        else:
            TYPE2 = 1
        #checks stab
        if attackingType1 == moveType or (attackingType2 == moveType and attackingType2 != "Null"):
            STAB = 1.5
        else:
            STAB = 1
        #random num from (.85 to 1)
        randdam = 1-((random.randint(0, 15))/100)
        
        #checks crits
        critint = (random.randint(0, 15))
        if critint == 0:
            critical = 2
        else:
            critical = 1

        #Checks whether attack is physical or special
        if attackType == "Physical":
            damageDone = ((((((pkmLevel*2)/5)+2)*movePower*(pkmAttack/pkmDefense))/50)+2)*STAB*TYPE1*TYPE2*randdam*critical
        elif attackType == "Special":
            damageDone = ((((((pkmLevel*2)/5)+2)*movePower*(pkmspeAttack/pkmspeDefense))/50)+2)*STAB*TYPE1*TYPE2*randdam*critical
        return int(damageDone)
    else:
        return 0
    
# Example damage calculations
#print(damagecalc(scizor,gengar,bullet_punch))
#print(damagecalc(drapion,snorlax,poison_jab))
#print(damagecalc(swampert, gengar, hydro_pump))
#print(damagecalc(magnezone, snorlax, thunderbolt))
#print(damagecalc(scizor, drapion, bullet_punch))
#print(damagecalc(gengar, magnezone, thunderbolt))
#print(damagecalc(drapion, swampert, poison_jab))
#print(damagecalc(snorlax, scizor, body_slam))

def aiLogic(aiPokemon, attackingPokemon):
    # Calculate estimated damage for each move
    Move1 = aiPokemon.moveset[0]
    Move2 = aiPokemon.moveset[1]
    Move3 = aiPokemon.moveset[2]
    Move4 = aiPokemon.moveset[3]
    estMove1 = damagecalc(aiPokemon, attackingPokemon, Move1)
    estMove2 = damagecalc(aiPokemon, attackingPokemon, Move2)
    estMove3 = damagecalc(aiPokemon, attackingPokemon, Move3)
    estMove4 = damagecalc(aiPokemon, attackingPokemon, Move4)

    # Store the results in a dictionary to easily identify which move has the largest estimate
    moves = {
        'Move1': estMove1,
        'Move2': estMove2,
        'Move3': estMove3,
        'Move4': estMove4
    }

    # Find the move with the largest estimated damage
    maxMove = max(moves, key=moves.get)
    maxDamage = moves[maxMove]

    # Return the move with the largest estimate and its value
    return maxMove, maxDamage

#print(aiLogic(gengar, magnezone))