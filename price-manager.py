dict = {}

def create_dict(ppl) : 
    for p in ppl : 
        dict[p] = 0

def refresh_prices() : 
    dict.clear()

def det_split(price, splitters) : 
    per_person = price / len(splitters)
    for p in dict : 
        dict[p] += per_person

def print_results() : 
    for d in dict: 
        print(f'{d} owes {str(dict[d])}')

## sample usage - first create list of people splitting
l = ["kush", "om", "kaushal", "mit"]

## call 'create_dict' -> this will keep track of prices
create_dict(l)

## create a list of people splitting an item - let's say all four of us are splitting eggs
egg_splitters = l # set it to same list as all roommates

## call det_split to fix prices. enter egg price here as well.
det_split(5, egg_splitters)

print_results()