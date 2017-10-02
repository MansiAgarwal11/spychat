from spy_details import spy
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']
friends = []



def start_chat(spy) :

    current_status_message = None

    spy['name'] = spy['salutation'] + " " + spy['name']

    if spy['age'] > 12 and spy['age'] < 50:

        print "Authentication complete. Welcome %s age: %d and rating of %.1f.Proud to have you onboard " %(spy['name'],spy['age'],spy['rating'])
        spy['is_online']=True
        show_menu = True
        current_status_message=None


        while show_menu:
            menu_choice =int(raw_input("What do you want to do? \n1. Add a status update \n2. Add a friend \n3.Select a friend \n4.Close application \n"))
            if menu_choice == 1:
                current_status_message=add_status(current_status_message)
            elif menu_choice == 2:
                add_friend()
            elif menu_choice == 3:
                select_a_friend()
            else:
                show_menu=False

    else :
          print 'Sorry you are not of the correct age to be a spy'

def add_status(current_status_message):
    if current_status_message != None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)

    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print str(item_position) + ". " + message
            item_position = item_position + 1
        message_selection = int(raw_input("\nChoose from the above messages "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[(message_selection) - 1]


    return updated_status_message


def add_friend():
    new_friend= {'name': '', 'salutation': '', 'age': 0, 'rating': 0.0}
    new_friend['name'] = raw_input("Please add your friend's name:")
    new_friend['salutation'] = raw_input(" Mr. or Ms.?: ")
    new_friend['name'] =  new_friend['salutation'] + " " + new_friend['name'] 
    new_friend['age'] =int( raw_input("Age?"))
    new_friend['rating'] = float(raw_input("rating?"))

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends)

def select_a_friend():
    itemno=1
    for i in friends:
        print '%d ) %s ' %(itemno, i['name'])
        itemno=itemno+1
    choice=input("enter the recipient number")
    return (choice-1)
print "hello"
answer=raw_input("do you want to continue as the default user %s %s ?(y/n)" %(spy['salutation'], spy['name']) )


if answer=='y':
    print "Let's get started"
    start_chat(spy)


else:
    #introducing spy
    spy['name']=raw_input("What should we call you?");
    if len(spy['name'])>0:
        spy_salu= raw_input("what should we call you? Mr or Ms.")
        spy['name']= spy['salutation'] + " " + spy['name']   #string concatenation and re-assignment
        print "Alright " + spy['name'] + "I'd like to know more about you.."

        spy['age'] = 0
        spy['rating'] = 0.0
        spy['is_online'] = False
        spy['age']=input("what is your age?")
        spy['rating'] = input("What is your spy rating?")
        start_chat(spy)


    else:
         print "invalid entry. please enter your name again."









