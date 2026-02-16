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


def f_name_picker(first_name_data, gender_prob_data, decade):
    """Pick a first name weighted by frequency for specific gender  """

    # determine name gender probabilistically based on decade
    gender_based_names = gender_picker(gender_prob_data, decade)

    first_name_options: list = first_name_data.get((gender_based_names, decade), [])

    # return unknown if no lookup values
    if not first_name_options:
        return 'NA'

    # convert to names and weights to rows (name, weight) with values as columns (transpose)
    # Citation: https://www.w3schools.com/python/ref_func_zip.asp
    names, weights = zip(*first_name_options)

    # use rand to get a random value therein
    return random.choices(names, weights=weights)[0]


def l_name_picker(last_name_data, rank_prob_data, decade):
    """Pick a last name weighted by rank probability for a given decade."""
    candidates = last_name_data.get(decade, [])

    # return unknown if no lookup values
    if not candidates:
        return 'NA'

    # get name and rank probabilities
    names = [name for name, rank, dec in candidates]
    weights = [rank_prob_data[rank - 1] for name, rank, dec in candidates]

    return random.choices(names, weights=weights)[0]


def deceased_year_picker(life_exp_data, yr_born):
    """Pick a year of death based on life expectancy +/- 10 years."""

    # extract life exp for given year or use default
    life_exp = life_exp_data.get(yr_born, 75.0)

    # add random offset
    offset = random.uniform(-10, 10)
    return int(yr_born + life_exp + offset)
