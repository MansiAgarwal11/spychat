from spy_details import spy_rating,spy_name,spy_age,spy_salutation,spy_is_online
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']
friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []

def start_chat(spy_name, spy_age, spy_rating):

    current_status_message = None

    spy_name = spy_salutation + " " + spy_name

    if spy_age > 12 and spy_age < 50:

        print "Authentication complete. Welcome %s age: %d and rating of %.1f.Proud to have you onboard " %(spy_name,spy_age,spy_rating)
        spy_is_online=True
        show_menu = True
        current_status_message=None


        while show_menu:
            menu_choice =int(raw_input("What do you want to do? \n1. Add a status update \n2. Close Application"))
            if menu_choice == 1:
                current_status_message=add_status(current_status_message)
            elif menu_choice == 2:
                show_menu = False

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
    new_name = raw_input("Please add your friend's name:")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")
    new_name = new_name + " " + new_salutation
    new_age =int( raw_input("Age?"))
    new_rating = int(raw_input("Spy rating?"))

    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_status.append(True)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends_name)

print "hello"
answer=raw_input("do you want to continue as the default user %s %s ?(y/n)" %(spy_salutation, spy_name) )


if answer=='y':
    print "Let's get started"
    start_chat(spy_name,spy_age,spy_rating)


else:
    #introducing spy
    spy_name=raw_input("What should we call you?"); #spy_name is a variable
    if len(spy_name)>0:
        spy_salu= raw_input("what should we call you? Mr or Ms.")   #spy_salu is a variable
        spy_name= spy_salu + " " + spy_name   #string concatenation and re-assignment
        print "Alright " + spy_name + "I'd like to know more about you.."

        spy_age = 0  # declaration of int datatype variable
        spy_rating = 0.0  # declaration of float datatype variable
        spy_online = False  # declaration of Boolean datatype variable
        spy_age=input("what is your age?")
        spy_rating = input("What is your spy rating?")
        start_chat(spy_name,spy_age,spy_rating)


    else:
         print "invalid entry. please enter your name again."









