import sys
import json
import pytest

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


# CAPITALS_STATES = {capital:state for state, capital in STATES_CAPITALS.items()}
def capital_of_Idaho():
    return STATES_CAPITALS['Idaho']


def all_states():
    return STATES_CAPITALS.keys()


def all_capitals():
    return STATES_CAPITALS.values()


def states_capitals_string():
    return ' , '.join([f'{state} - > {capital}' for state, capital in STATES_CAPITALS.items()])


def get_state():
    sorted_states = sorted(STATES_CAPITALS.items())
    return ' , '.join([f'{state} - > {capital}' for (state, capital) in sorted_states])


def get_state_7():
    return {capital: state for state, capital in STATES_CAPITALS.items()}


# def get_state_8(capital):
#    return  CAPITALS_STATES.get(capital, "None")

# new_dict = {}
# for state, capital in STATES_CAPITALS.items():
#    new_dict[capital] = state
# def test_state_to_capital():
#     assert 'Cheyenne' == STATES_CAPITALS['Wyoming']


print("1)", capital_of_Idaho())
print("2)", all_states())
print("3)", all_capitals())
print("4)", states_capitals_string())
print("5)", get_state())
print("7)", get_state_7())
# a= get_state_8('Lansing')
# print (a)


##  with pytest.raises(KeyError):
#      STATES_CAPITALS['']


# def test_capital_to_state():
#  assert 'Wyoming' == get_state('Cheyenne')


# def test_capital_to_state_unknown():
#   with pytest.raises(KeyError):
#       get_state('')


# def main():
#  return pytest.main(__file__)


# if __name__ == '__main__':
#   sys.exit(main())
