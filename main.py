# Create your superhero vs villain story
import random

# this is the super hero segment

superPowers = [
    "Flying",
    "Super Strength",
    "Telepathy",
    "Super Speed",
    "Unlimited Eating capability",
    "Invisibility",
    "Ice breath",
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
    "That",
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
    "Guy",
]

print("lets generate your random super hero name!")

superName = random.choice(superFirstName) + random.choice(superLastName)

print("your super-name is!")
print(superName)
print("your super power is:")
print(random.choice(superPowers))

# This is super villains segment

villainPowers = [
    "Flying",
    "Super Strength",
    "Telepathy",
    "Super Speed",
    "Unlimited Eating capability",
    "Invisibility",
    "Ice breath",
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
    "Trvial",
    "Nutty",
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
    "Cricketer",
]

villainName = superName = random.choice(villan_first_name) + random.choice(
    villan_last_name
)

print("your arch nemesis is :O ")
print(villainName)
print("your nemesis has the power of:")
print(random.choice(villainPowers))
