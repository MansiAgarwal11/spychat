from steganography.steganography import Steganography
from datetime import datetime
import re

from spy_details import Spy,ChatMessage

spy = Spy('Bond', 'Mr.', 24, 4.7)

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']

friend_one = Spy('Sherlock', 'Mr.', 27, 4.9)
friend_two = Spy('Kristen', 'Ms.', 21, 4.39)
friend_three = Spy('Watson', 'Dr.', 37, 4.95)

friends = [friend_one, friend_two, friend_three]



def start_chat(spy) :


    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:

        if spy.rating > 4.5:
            print 'Great ace!'
        elif spy.rating > 3.5 and spy.rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy.rating >= 2.5 and spy.rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office'

        print "Authentication complete. Welcome %s age: %d and rating of %.1f.Proud to have you onboard " %(spy.name,spy.age,spy.rating)
        spy.is_online=True
        show_menu = True


        while show_menu:
            menu_choice =int(raw_input("What do you want to do? \n1.Add a status update \n2.Add a friend \n3.Send a message \n4.Read a message \n5.Read old chats \n6.Close application \n"))
            if menu_choice == 1:
                spy.current_status_message=add_status(spy)
            elif menu_choice == 2:
                add_friend()
            elif menu_choice == 3:
                send_a_message()
            elif menu_choice == 4:
                read_a_message()
            elif menu_choice == 5:
                print "hey"
            else:
                show_menu=False

    else :
          print 'Sorry you are not of the correct age to be a spy'

def add_status(spy):
    if spy.current_status_message!= None:
        print "Your current status message is " + spy.current_status_message + "\n"
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

    print "Your status has been updated to " + updated_status_message
    return updated_status_message


def add_friend():
    new_friend_name = raw_input("Please add your friend's name:")
    new_friend_salutation = raw_input("Mr. or Ms.?: ")
    new_friend_age =int( raw_input("Age?"))
    new_friend_rating = float(raw_input("rating?"))
    new_friend = Spy(new_friend_name,new_friend_salutation,new_friend_age,new_friend_rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    print "You have " + str(len(friends)) + " friends in your friend list."
    return len(friends)

def select_a_friend():
    itemno=1
    for i in friends:
        print '%d ) %s ' %(itemno, i.name)
        itemno=itemno+1
    choice=input("enter the recipient number")
    return (choice-1)

def send_a_message():
    friend_choice=select_a_friend()
    input_path=raw_input("enter image path")
    secret_message=raw_input("enter text")
    output_path="output.jpg"
    time=datetime.now()
    l = []
    l = re.findall(r'\.jpg', input_path)
    if '.jpg' in l:
        Steganography.encode(input_path, output_path, secret_message)
        new_chat = ChatMessage(secret_message, time, True)
        friends[friend_choice].chats.append(new_chat)
        print "message sent!"
    else:
        print "invalid input path entry!"


def read_a_message():
    sender=select_a_friend()
    output_path = raw_input("enter path of image which needs to be decoded")
    text=Steganography.decode(output_path)
    time = datetime.now()
    new_chat = ChatMessage(text, time, False)
    friends[sender].chats.append(new_chat)
    print "secret message has been saved!"







print "Hello"
answer=raw_input("Do you want to continue as the default user %s %s ?(y/n)" %(spy.salutation, spy.name) )


if answer=='y':
    print "Let's get started"
    start_chat(spy)


else:
    #introducing spy
    spy.name=raw_input("What should we call you?");
    if len(spy.name)>0:
        spy_salu= raw_input("what should we call you? Mr or Ms.")
        spy.name= spy.salutation + " " + spy.name   #string concatenation and re-assignment
        print "Alright " + spy.name + " I'd like to know more about you.."

        spy.age = 0
        spy.rating = 0.0
        spy.is_online = False
        spy.age=input("what is your age?")
        spy.rating = input("What is your spy rating?")
        start_chat(spy)


    else:
         print "invalid entry. please enter your name again."









