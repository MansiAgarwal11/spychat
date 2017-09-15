print "hello"
print "Let's get started"


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
    if spy_age > 12 and spy_age < 50:   #and is a keyword

        spy_rating = input("What is your spy rating?")

        if spy_rating > 4.5:
            print 'Great ace!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'

        spy_is_online = True
        print "Authentication complete!Welcome " +spy_name + " age: " + str(spy_age) + " and rating of " + str(spy_rating) + ".Proud to have you onboard!"

    else:
            print 'Sorry you are not of the correct age to be a spy'
else:
    print "invalid entry. please enter your name again."









