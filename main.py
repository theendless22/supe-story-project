# Create your superhero name
import random

superPowers = [
    "Flying",
    "Super Strength",
    "Telepathy",
    "Super Speed",
    "Unlimited Eating capability",
    "Invisibility",
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
