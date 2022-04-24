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

def capital_Idaho():
    print(STATES_CAPITALS['Idaho'])
capital_Idaho()
pass

def all_states():
    print(STATES_CAPITALS.keys())
all_states()
pass

def all_capitals():
    print(STATES_CAPITALS.values())
all_capitals()
pass

def states_capitals_string():
    lst = STATES_CAPITALS.keys()
    sort = sorted(lst)
    print(sort)
states_capitals_string()
pass

def get_state():
    stat = input('Provide Capital:')
    for st, cap in STATES_CAPITALS.items():
        if cap.lower() == stat:
            results = st+ " " +cap
            print(results)
get_state()
pass

