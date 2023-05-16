# Create your superhero name
import random

superPowers = [
    "Flying",
    "Super Strength",
    "Telepathy",
    "Super Speed",
    "Unlimited Eating capability",
    "Invisibility",
    "Super Sonic Voice",
    "Mad driving skills",
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
    "Fun",
    "Un-fun",
    "Scary",
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

print("your super-name is!")
print(superName)
print("your super power is:")
print(random.choice(superPowers))
