name = input("What is your name? ")
print("\n")


def cs_service_bot():
    print("Hello! Welcome", name, "to the DNS Cable Company's Service Portal. \
    \n\nAre you a new or existing customer?\
    \n[1] New Customer\
    \n[2] Existing Customer\n")
    response = int(input('Please enter the number corresponding to your choice: '))
    if response == 1:
        return new_customer()
    elif response == 2:
        return existing_customer()
    else:
        print("Sorry, we didn't understand your selection.")
        return cs_service_bot()


def existing_customer():
    print('What kind of support do you need ?\
    \n[1] Television Support\
    \n[2] Internet Support\
    \n[3] Speak to a support representative. ')
    choice = int(input('Please enter the number corresponding to your choice:'))
    if choice == 1:
        return television_support()
    elif choice == 2:
        return internet_support()
    elif choice == 3:
        return live_rep("support")
    else:
        print("Sorry we didn't understand your selection.")
        return existing_customer()


def new_customer():
    print("We're excited to have you join the DNS family, how can we help you?\
    \n[1] Sign up for service.\
    \n[2] Schedule a home visit.\
    \n[3] Speak to a sales representative.")
    choice = int(input('Please enter the number corresponding to your choice:'))
    if choice == 1:
        return sign_up()
    elif choice == 2:
        return home_visit("new install")
    elif choice == 3:
        return live_rep("sale")
    else:
        print("Sorry we didn't understand your selection.")
        return new_customer()


def television_support():
    print("What is the nature of your problem?\
    \n[1] I can't access certain channels.\
    \n[2] My picture is blurry.\
    \n[3] I keep losing service.\
    \n[4] Other issues.")
    choice = int(input("Enter your option:"))
    if choice == 1:
        print("Please check the channel lists at DefinitelyNotSinister.com.\
        If the channel you cannot access is there, please contact a live representative.")
        return did_that_help()
    elif choice == 2:
        print("Try adjusting the antenna above your television set.")
        return did_that_help()
    elif choice == 3:
        print(" Is it raining outside? If so, wait until it is not raining and then try again.")
        return did_that_help()
    elif choice == 4:
        return live_rep("support")
    else:
        print("Sorry we didn't understand your selection.")
        return television_support()


def internet_support():
    print("[1] I can't connect to the internet.\
    \n[2] My connection is very slow.\
    \n[3] I can't access certain sites.\
    \n[4] Other issues.")
    choice = int(input('Enter your option'))
    if choice == 1:
        print("Unplug your router, then plug it back in,then give it a good whack, like the Fonz.")
        return did_that_help()
    if choice == 2:
        print("Make sure that all cell phones and other peoples computers\
        are not connected to the internet, so that you can have all the bandwidth.")
        return did_that_help()
    if choice == 3:
        print("Move to a different region or install a VPN. Some areas block certain sites.")
        return did_that_help()
    if choice == 4:
        return live_rep("support")
    else:
        print("Sorry we didn't understand your selection.")
        return internet_support()


def did_that_help():
    response = (input("Did that help your to solve your problem ? [Yes]/[No]"))
    if response == 'Yes' or response == 'yes':
        print('Thank you for using our services')
    if response == 'No'or response == 'no':
        print("Would you rather [1] talk to a live reprentative or [2] schedual a home visit ?")
        response2 = int(input("[1]/[2]"))
        if response2 == 1:
            return live_rep("support")
        elif response2 == 2:
            return home_visit("support")
        else:
            print("Sorry we didn't understand your selection.")
            return did_that_help()


def sign_up():
    print("Great choice, friend! We're excited to have you join the DNS family!\
    \nPlease select the package you are interested in signing up for.\
            \n[1] Bundle Deal (Internet + Cable)\
            \n[2] Internet\
            \n[3] Cable")
    choice = int(input("Enter your option : "))
    if choice == 1:
        print("You've selected the Bundle Package!\
        \nPlease schedule a home visit and our technician will come and set up your new service.")
        return home_visit("new install")
    if choice == 2:
        print("You've selected the Internet Only Package!\
        \nPlease schedule a home visit and our technician will come and set up your new service.")
        return home_visit("new install")
    if choice == 3:
        print("You've selected the Cable Only Package!\
        Please schedule a home visit and our technician will come and set up your new service.")
        return home_visit("new install")
    else:
        print("Sorry we didn't understand your selection.")
        return sign_up()


def home_visit(purpose):
    if purpose == "none":
        purpose = int(input("Choose one of below option :\
         \n[1] New service installation.\
         \n[2] Existing service repair.\
         \n[3] Location scouting for unserviced region."))
    if purpose == 1:
        return home_visit('new install')
    if purpose == 2:
        return home_visit('support')
    if purpose == 3:
        return home_visit('scout')
    visit_date = input('Please enter a date below when you are available for a technician to come to your home and \
    \n[PURPOSE SPECIFIC TEXT HERE].')
    print('Wonderful! A technical will come visit you on', visit_date, '.\
    Please be available between the hours of 1:00 am and 11:00 pm.')
    return visit_date


def live_rep(purpose):
    if purpose == "sale":
        print('Please hold while we connect you with a live sales representative.\
        \nThe wait time will be between two minutes and six hours. We thank you for your patience.')
    if purpose == "support":
        print('Please hold while we connect you with a live support representative.\
        \nThe wait time will be between two minutes and six hours. We thank you for your patience.')


cs_service_bot()


