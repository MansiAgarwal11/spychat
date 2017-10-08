
#importing necessary python libraries
from steganography.steganography import Steganography
from datetime import datetime
from colorama import Fore
import re
import csv


#importing spy_details.py which is a module defined by us
from spy_details import Spy,ChatMessage


#spy is an object of class Spy
#has been initialised to a default user
spy = Spy('Bond', 'Mr.', 24, 4.7)


#list to hold the status messages of the spy
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']


#list to hold the details of the friends of the spy
friend1=Spy('Sherlock', 'Mr', 27, 4.9)
friend2=Spy('Kristen', 'Ms.', 21, 4.39)
friend3=Spy('Watson', 'Dr.', 37, 4.95)
friends = []


#function to load friends from friends.csv file
def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)

        for row in reader:
            spy = Spy(row[0], row[1],int( row[2]), float(row[3]))
            friends.append(spy)

#function to load previous chats from chats.csv file
def load_chats():
    with open('chats.csv', 'rb') as chats_data:
        reader = csv.reader(chats_data)

        for row in reader:
            chat1 = ChatMessage(row[1], row[2], bool(row[3]))
            for i in friends:
                if i.name == row[0]:
                    j= friends.index(i)
                    friends[j].chats.append(chat1)

#function to read old chats
def read_chats():
    choice = select_a_friend()
    print Fore.RED + friends[choice].name
    if len(friends[choice].chats) == 0:
        print Fore.BLACK + "NO CONVERATION YET!"
    else:
        for i in friends[choice].chats:
            print Fore.BLUE + str(i.time)
            print Fore.BLACK + i.message

#function to start the application
def start_chat(spy):

    load_friends()
    load_chats()

    #reassigning spy's name as a concatenated version of his salutation and name
    spy.name = spy.salutation + " " + spy.name

    #checking whether the spy is of correct age or not
    if spy.age > 12 and spy.age < 50:

        #printing statements on the basis of the rating of the spy
        if spy.rating > 4.5:
            print 'Great ace!'
        elif spy.rating > 3.5 and spy.rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy.rating >= 2.5 and spy.rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office'

        #printing authentication complete
        print "Authentication complete. Welcome %s age: %d and rating of %.1f.Proud to have you onboard " %(spy.name,spy.age,spy.rating)
        spy.is_online = True
        show_menu = True

        #using a while loop to perform actions of spy's choices till spy wishes to terminate the application
        while show_menu:
            menu_choice = int(raw_input("What do you want to do? \n1.Add a status update \n2.Add a friend \n3.Send a message \n4.Read a message \n5.Read old chats \n6.Close application \n"))
            if menu_choice == 1:
                spy.current_status_message=add_status(spy)
            elif menu_choice == 2:
                add_friend()
            elif menu_choice == 3:
                send_a_message()
            elif menu_choice == 4:
                read_a_message()
            elif menu_choice == 5:
                read_chats()
            else:
                show_menu=False

    else :
          print 'Sorry you are not of the correct age to be a spy'

#function for adding a status for the spy
def add_status(spy):
    if spy.current_status_message != None:
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

#function to add a friend
def add_friend():
    new_friend_name = raw_input("Please add your friend's name:")
    new_friend_salutation = raw_input("Mr. or Ms.?: ")
    new_friend_age =int( raw_input("Age?"))
    new_friend_rating = float(raw_input("rating?"))
    #new_friend is an object of the class Spy
    new_friend = Spy(new_friend_name,new_friend_salutation,new_friend_age,new_friend_rating)

    #checking whether the spy with entered details is fir to be the spy's friend
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)

        with open("friends.csv", 'ab') as friends_data:
            write = csv.writer(friends_data)
            write.writerow([new_friend.name, new_friend.salutation, new_friend.age, new_friend.rating])

    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    print "You have " + str(len(friends)) + " friends in your friend list."
    return len(friends)

#function to select a friend to send/read a message
def select_a_friend():
    itemno = 1
    for friend in friends:
        print '%d. %s' % (itemno , friend.name)
        itemno = itemno + 1
    choice = input("Choose from your friends")
    return (choice-1)

#function to send a message
def send_a_message():
    friend_choice = select_a_friend()
    input_path = raw_input("enter image path")
    secret_message = raw_input("enter text")
    output_path = "output.jpg"
    time = datetime.now()
    #l is an empty list
    l = []
    #using regular expressions to check whether the image is .jpg or not
    l = re.findall(r'\.jpg', input_path)
    if '.jpg' in l:
        Steganography.encode(input_path, output_path, secret_message)
        new_chat = ChatMessage(secret_message, time, True)
        friends[friend_choice].chats.append(new_chat)
        with open("chats.csv", 'ab') as chats_data:
            write = csv.writer(chats_data)
            time= time.strftime("%b %d %Y %H:%M:%S")
            write.writerow([friends[friend_choice].name,secret_message, time, True])

        print "message sent!"
    else:
        print "invalid input path entry!"


#function to read a message
def read_a_message():
    sender = select_a_friend()
    output_path = raw_input("enter path of image which needs to be decoded")
    text = Steganography.decode(output_path)
    time = datetime.now()
    new_chat = ChatMessage(text, time, False)
    friends[sender].chats.append(new_chat)
    with open("chats.csv", 'ab') as chats_data:
        write = csv.writer(chats_data)
        time = time.strftime("%b %d %Y %H:%M:%S")
        write.writerow([friends[sender].name, text, time, False])
    special1=[]
    special2=[]
    special1=re.findall(r'SOS', text)
    special2 = re.findall(r'SAVE ME', text)

    if 'SOS' in special1:
        print "Send help ASAP"
    elif 'SAVE ME' in special2:
        print "Friend needs help!"
    else:
        print "secret message has been saved!"


print "Hello"
answer = raw_input("Do you want to continue as the default user %s %s ?(y/n)" %(spy.salutation, spy.name) )


if answer.lower() == 'y':
    print "Let's get started"
    start_chat(spy)


else:
    #introducing spy
    spy.name = raw_input("What should we call you?");
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

