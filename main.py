# Create your superhero vs villain story
import random
import tkinter as tk


def generate_superhero():
    # this is the super hero segment of our game.
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
        "Uma",
        "Macho Lady",
        "Stag",
        "Guy",
    ]

    print("lets generate your random super hero name!")

    superName = random.choice(superFirstName) + random.choice(superLastName)
    superPower = random.choice(superPowers)

    return f"Your Super Hero Name is {superName} and your power is {superPower}"

    # print("your super-name is!")
    # print(superName)
    # print("your super power is:")
    # print(random.choice(superPowers))


# This is super villains segment


def gerenate_super_villain():
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

    villainName = random.choice(villan_first_name) + random.choice(villan_last_name)
    villainpower = random.choice(villainPowers)

    return f"Your arch nemesis is {villainName} and their power is {villainpower}"

    # print("your arch nemesis is :O ")
    # print(villainName)
    # print("your nemesis has the power of:")
    # print(random.choice(villainPowers))
