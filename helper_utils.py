import random


def gender_probability(lookup_data, decade):
    """get gender probabilities for a given decade"""
    if decade in lookup_data:
        return lookup_data[decade]

    # add a fall back in case the data is missing a decade
    return {'male': 0.5, 'female': 0.5}


def gender_picker(data, decade):
    """Pick a gender based on probabilities"""
    probs = gender_probability(data, decade)

    # get available genders and their weights
    genders = list(probs.keys())
    weights = list(probs.values())

    # use rand to get a random value therein
    return random.choices(genders, weights=weights)[0]


def fname_picker():
    pass


def lname_picker():
    pass


def deceased_year_picker():
    pass


def birth_rate_picker():
    pass


def marriage_rate_picker():
    pass