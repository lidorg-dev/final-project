from termcolor import colored

def search(myDict, search1):
    search.a = []
    for key, value in myDict.items():
        if search1 in value:
            search.a.append(key)
            #print(key)
            return key


with open('log.txt', 'r') as document:
    answer_day = {}
    answer_place = {}

    for line in document:
        if " I can do" in line:
            key, value = line.split(":", 1)
            answer_day.setdefault(key, [])
            answer_day[key].append(value[10:])

            value = value[10:]
            list_of_keys = [key for key, list_of_values in answer_day.items()
                            if value in list_of_values]
            if len(list_of_keys) == 8:
                #print(value)
                day_answer_match = value
                print(colored("OK FOUND MATCH FOR MEETING", 'blue'))

                search(answer_place, day_answer_match)  # function search match day/home

                print(colored(f"\nWe will meet at {search.a} house ... on {day_answer_match}",
                              'blue'))  # from {day_answer_match} to ...", 'blue'))  # "to" , int(day_answer_match[21:23])+1,":00")
                input(colored("Press Enter to continue and search next meeting option...", 'blue'))
                continue
            else:
                print(colored(f"Searching... NO YET FOUND A NEW MATCH FOR MEETING for {len(answer_day)} participants",  'red'))
                continue

        if " My yard is" in line:
            key, value = line.split(":", 1)
            answer_place.setdefault(key, [])
            answer_place[key].append(value[22:])
