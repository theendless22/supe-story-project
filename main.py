# Create your superhero name
import random

superPowers = [
    "Flying",
    "Super Strength",
    "Telepathy",
    "Super Speed",
    "Unlimited Eating capability",
    "Invisibility",
    "Fire-breath",
    "Ice-breath",
]

superFirstName = [
    "Wonder",
    "Super",
    "Mad",
    "Incredible",
    "Astonishing",
    "Decent",
    "Stupendous",
    "Organised",
    "That Guy",
    "Notably",
]
superLastName = [
    "Woman",
    "Man",
    "Girl",
    "Boy",
    "Thing",
    "Treat",
    "Dude",
    "Chick",
    "Vikram",
    "Deepika",
    "Macho Lady",
    "Stag",
]

print("lets generate your random super hero name!")

superName = random.choice(superFirstName) + random.choice(superLastName)

# this is the super hero segment

print("your super-name is!")
print(superName)
print("your super power is:")
print(random.choice(superPowers))

# TO DO: Add super villains to this code

villainPowers = [
    "Flying",
    "Super Strength",
    "Telepathy",
    "Super Speed",
    "Unlimited Eating capability",
    "Invisibility",
    "Fire-breath",
    "Ice-breath",
]

villan_first_name = [
    "Dark",
    "Blue",
    "Unhappy",
    "Lifeless",
    "White",
    "Unplanned",
    "Rich",
    "Psycotic",
]

villan_last_name = [
    "Fly",
    "Engineer",
    "Pilot",
    "Bitch",
    "Freak",
    "Student",
    "Manager",
    "Builder",
    "Politician",
]

villainName = superName = random.choice(villan_first_name) + random.choice(
    villan_last_name
)

print("your arch nemesis is :O ")
print(villainName)
print("your arch nemisis power is:")
print(random.choice(villainPowers))
