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

import pytest

STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
}


def capital_of_Idaho():
    capital = 'Boise'
    for i in STATES_CAPITALS:
        if STATES_CAPITALS[i] == capital:
            print('Q1:', STATES_CAPITALS[i])
    pass

def all_states():
    state = list(STATES_CAPITALS.keys())
    print('Q2:', state)
    pass

def all_capitals():
    capitals = list(STATES_CAPITALS.values())
    print('Q3:', capitals)
    pass


def states_capitals_string():
    list = []
    for state, capital in STATES_CAPITALS.items():
        list.append(state)
        list.append('->')
        list.append(capital)
        list.append(',')
    string = ' '.join(list)
    print('Q4:', string)
    pass



def get_state(capital):
    capital_input = capital
    state_input = ''
    flag = 0
    for state, capital in STATES_CAPITALS.items():
        if capital == capital_input:
            state_input += state + ' '
            flag = 1
    if flag == 0:
        state_input = 'State not exist'
    return state_input




def main():
    capital = input("Write a capital and we will tell you the state:")
    print("the state is: ", get_state(capital))

    capital_of_Idaho()
    all_states()
    all_capitals()
    states_capitals_string()


if __name__ == '__main__':
    sys.exit(main())
