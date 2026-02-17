# CS 562 - Family Tree Generator - Summary

## Citations

- https://docs.python.org/3/library/random.html#random.choices
- https://docs.python.org/3/library/random.html#random.choice
- https://docs.python.org/3/library/random.html#random.uniform
- https://docs.python.org/3/library/math.html#math.ceil
- https://docs.python.org/3/reference/expressions.html#generator-expressions
- https://www.w3schools.com/python/ref_func_zip.asp
- https://www.w3schools.com/python/ref_random_randint.asp
- https://www.w3schools.com/python/ref_random_choice.asp

## Design Decisions

Data Layer (input_extractor.py) loads CSV files 
    - First names (by gender and decade)
    - Last names (by decade and rank)
    - Gender probabilities
    - Birth rates
    - Marriage rates
    - Life expectancy

Data is stored in dictionaries keyed by decade or year for later refernce


Data Model (person.py) is a Python dataclass w/ each person by:
    - Unique ID
    - Name
    - Gender
    - Birth year
    - Death year
    - Spouse
    - Children

**Person Creation (person_factory.py, helper_utils.py)** uses an enum (ROOT, CHILD, SPOUSE) 

Rules / Logic:
- Names are determined probabilistically and gender is picked first by weighted probability
- Once gender is determined, a first name is chosen by frequency for that gender and decade in the data input - Descendants can get names from either parent
- Spouses get a name from the CSV weighted by rank and death year is life expectancy ± 10 years w/ some random variation

# Key Design Patterns
Tree Building (tree_factory.py) is recursive
- The root couple is created at generation 1 manually, after which build_children runs for each couple
- Child count is randomized around the decade's birth rate (give or take 1.5)
- Birth years are evenly distributed across a 20-year window starting at parent age 25. 
- Each child is then probabilistically assigned a spouse based on the marriage rate, and 
- build_children then recurses. 

## Custom Rules 
- Single parents produce one fewer child
- Recursion stops when a child's birth year exceeds 2120.

**UI (ui.py)** is an interactive CLI that supports three questions: total person count (T), count by birth decade (D), and duplicate full names (N)
