"""We have an existing dictionary that maps US states to their capitals.
1. Print the state capital of Idaho
2. Print all states.
3. Print all capitals.
4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
5. Ensure the string you created in 4. is alphabetically sorted by state
7. Now we want to add the reverse look up, given the name of a capital what state
is it in?
Implement the function def get_state(capital): below so it returns the state.
GOTCHAS: What happens if two states have the same capital name, how do you
handle that?
"""
import sys

STATES_CAPITALS = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne',
}


def capital_of_Idaho():
    global STATES_CAPITALS
    print(STATES_CAPITALS['Idaho'])


def all_states():
    global STATES_CAPITALS
    for state in list(STATES_CAPITALS.keys()):
        print(state)


def all_capitals():
    global STATES_CAPITALS
    for capital in list(STATES_CAPITALS.keys()):
        print(STATES_CAPITALS[capital])


def states_capitals_string():
    global STATES_CAPITALS
    string = ""
    for temp in list(STATES_CAPITALS.keys()):
        string += temp + " -> " + STATES_CAPITALS[temp] + ","
    string = string[:-1]
    print(string)
    return string


def alphabetically_sorted(string):
    sorted = string.split(",")
    sorted.sort()
    string_new = ""
    for x in sorted:
        string_new += x + ","
    string_new = string_new[:-1]
    print(string_new)


def get_state(capital):
    global STATES_CAPITALS
    index = list(STATES_CAPITALS.values()).index(capital)
    key = list(STATES_CAPITALS.keys())[index]
    print(key)


if __name__ == "__main__":
    print("1. - ", end="")
    capital_of_Idaho()
    print("2. - ", end="")
    all_states()
    print("3. - ", end="")
    all_capitals()
    print("4. - ", end="")
    string1 = states_capitals_string()
    print("5. - ", end="")
    alphabetically_sorted(string1)
    print(f"7. - ", end="")
    get_state("Des Moines")
