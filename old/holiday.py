# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

again = True;

while(again):
    # get input
    name = input("What is your name? ")
    age = int(input("And what is your age, {}? ".format(name)))
    # display msg according to age
    if age < 18:
        print("I'm sorry, {}. You are too young to enter.".format(name))
    elif age > 30:
        print("I'm sorry, {}. You are too old to enter.".format(name))
    else:
        print("Welcome to the holiday, {}!!!!".format(name))
    # repeat?
    if input("Again? ").upper() != "Y":
        again = False;
        print("Bye!")
    print()