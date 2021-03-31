from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def simple_match(content,match):
    return fuzz.ratio(content,match)

def partial_match(content,match):
    return fuzz.partial_ratio(content,match)
    

def relevant_match(content,match):
    return fuzz.token_sort_ratio(content,match)
    
