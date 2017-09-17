from spy_details import spy_rating,spy_name,spy_age,spy_salutation,spy_is_online


def start_chat(spy_name, spy_age, spy_rating):

    current_status_message = None

    spy_name = spy_salutation + " " + spy_name

    if spy_age > 12 and spy_age < 50:

        print "Authentication complete. Welcome %s age: %d and rating of %.1f.Proud to have you onboard " %(spy_name,spy_age,spy_rating)
        spy_is_online=True
        show_menu = True

    else :
          print 'Sorry you are not of the correct age to be a spy'



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









