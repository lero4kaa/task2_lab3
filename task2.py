"""
If you want to stop running program, just enter "STOP"
"""
import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl
import sys


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def reaction(tw_object, path):
    """
    dict/list, list -> dict/list/str
    Function gives user information about his current location
    in the file and asks whether user wants to move further or
    print current object. Function returns dictionary, list or
    string, to which user decided to move. Function returns
    "Get out og the loop", if user decided to print current
    object.
    """
    if type(tw_object) == dict:
        print("Here you have dictionary and there are", 
              len(tw_object), "objects.")
        print("Do you want to have whole dictionary" 
              "printed, or continue looking for data" 
              "inside this dictionary? Please enter 'printing'"
              "for printing whole dictionary and 'continue' for"
              "continue searching.")
        decision = taking_decision()
        if decision == "printing":
            print("Result ", tw_object)
            return "Get out of the loop"

        elif decision == "continue":
            if len(tw_object) == 0:
                print("The dictionary is empty")
                return "Get out of the loop"

            else:
                print("Dictionary contains next keys:", "\n",
                      list(tw_object.keys()), "\n",
                      "Which of them do you want to choose?")
                choice = taking_choice_dict(list(tw_object.keys()))
                path.append(choice)
                next_branch = tw_object[choice]
                return next_branch

    elif type(tw_object) == list:
        print("Here you have list and there are", len(tw_object), "objects.")
        print("Do you want to have whole list printed, or continue "
              "looking for data inside this list?. Please enter "
              "'printing' for printing whole list and 'continue'"
              "for continue searching.")
        decision = taking_decision()
        if decision == "printing":
            print("Result ", tw_object)
            return "Get out of the loop"

        elif decision == "continue":
            if len(tw_object) > 1:
                print("Which of the list`s elements do you want to choose? "
                      "Please, enter number in in range from 1 to "
                      "{}".format(len(tw_object)))
                choice = taking_choice_lst(len(tw_object))
                next_branch = tw_object[choice-1]
                path.append(str(choice))
            elif len(tw_object) == 1:
                next_branch = tw_object[0]
                path.append(str(1))
            else:
                print("The list is empty.")
                return "Get out of the loop"

            return next_branch


def taking_decision():
    """
    () -> str
    Function controls user`s input about decision. It has to be "printing"
    or "continue", otherwise user enters it again. Function returns
    "printing" or "continue".
    Function stops running program, if user enters "STOP".
    """
    while True:
        decision = input()
        if decision == "printing" or decision == "continue":
            return decision
        elif decision == "STOP":
            print("You`ve stopped running program.")
            sys.exit()
        else:
            print("Please, enter 'printing' for printing whole object"
                  "or enter 'continue' for continue searching.")


def taking_choice_dict(keys):
    """
    list -> str
    Function controls user`s input about choosing a key in the
    dictionary. It has to be on of the given keys, otherwise
    user enters it again. Function returns key, that was input.
    Function stops running program, if user enters "STOP".
    """
    while True:
        choice = input()
        if choice in keys:
            return choice
        elif choice == "STOP":
            print("You`ve stopped running program.")
            sys.exit()
        else:
            print("Please, enter one of the following keys:", "\n", keys)


def taking_choice_lst(length):
    """
    int -> str
    Function controls user`s input about choosing the index of
    element in the list. It has to be in range of given number, otherwise
    user enters it again. Function returns number, that was input.
    Function stops running program, if user enters "STOP".
    """
    while True:
        choice = input()
        if choice == "STOP":
            print("You`ve stopped running program.")
            sys.exit()
        try:
            choice = int(choice)
            if choice in range(1, length+1):
                return choice
            else:
                print("Please, enter number in range from "
                      "1 to {}".format(length))
        except ValueError:
            print("Please, enter number in range from 1 to {}".format(length))


while True:
    print('')
    acct = input('Enter Twitter Account:')
    if acct == "STOP":
        print("You`ve stopped running program.")
        sys.exit()
    if len(acct) < 1:
        break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '10'})
    print('Retrieving', url)
    print('If you want to stop running program, just enter "STOP"')
    try:
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
        js = json.loads(data)
        with open("result_json.txt", mode="w", encoding="utf-8") as f:
            json.dump(js, f, indent=4, ensure_ascii=False)

        headers = dict(connection.getheaders())
        print('Remaining', headers['x-rate-limit-remaining'],
              'possible attempts to access data for these 15 minutes.')

        previous_object = js
        path = ["beginning"]

        while True:
            next_object = reaction(previous_object, path)
            print("Your path in the file ",  " --> ".join(path))
            previous_object = next_object
            if type(previous_object) != dict and type(previous_object) != list:
                if previous_object != "Get out of the loop":
                    print("Result ", previous_object)
                break

    except urllib.error.HTTPError:
        print("This account does not exist. Try again.")
        
