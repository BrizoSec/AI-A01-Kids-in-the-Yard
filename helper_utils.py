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

    # Citation: https://docs.python.org/3/library/random.html#random.choices
    return random.choices(genders, weights=weights)[0]


def f_name_picker(first_name_data, gender_prob_data, decade):
    """Pick a first name weighted by frequency for specific gender  """

    # first get gender by probability - need to support gendered first names
    gender = gender_picker(gender_prob_data, decade)

    first_name_options: list = first_name_data.get((gender, decade), [])

    # TODO - there is a possibility where spouse name is NA because the spouse is +10 years
    # and there is no data for beyound 2120 - accepting that as an edge case

    if not first_name_options:
        return 'NA'

    # convert to names and weights to rows (name, weight) with values as columns (transpose)
    # Citation: https://www.w3schools.com/python/ref_func_zip.asp
    names, weights = zip(*first_name_options)

    # use rand to get a random value therein
    return random.choices(names, weights=weights)[0]


def l_name_picker(last_name_data, rank_prob_data, decade):
    """Pick a last name weighted by rank probability for a given decade."""
    potential_last_names_itms = last_name_data.get(decade, [])

    # return unknown if no lookup values
    if not potential_last_names_itms:
        return 'NA'

    # get name and rank probabilities
    _name_options = [name for name, rank, dec in potential_last_names_itms]
    # TODO - fix out of bounds error - list is zero indexd
    _corresponding_weights = [rank_prob_data[rank - 1] for name, rank, dec in potential_last_names_itms]

    # Citation: https://www.w3schools.com/python/ref_random_choice.asp
    return random.choices(_name_options, weights=_corresponding_weights)[0]


def deceased_year_picker(life_exp_data, yr_born):
    """Pick a year of death based on life expectancy +/- 10 years."""

    # extract life exp for given year or use default
    life_exp = life_exp_data.get(yr_born, 75.0)

    # Citation: https://docs.python.org/3/library/random.html#random.uniform
    rand_off = random.uniform(-10, 10)
    return int(yr_born + life_exp + rand_off)
