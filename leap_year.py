print "This program will calculate whether or not the year you enter is a leap year or not."

query = int(raw_input("What year would you like me to calculate?"))

if query % 4 != 0:
    print "The year " + str(query) + " is not a leap year."
elif query % 4 == 0 and query % 400 == 0:
    print "The year " + str(query) + " is a leap year."
elif query % 4 == 0 and query % 100 == 0:
    print "The year " + str(query) + " is not a leap year."
elif query % 4 == 0 and query % 100 != 0:
    print "The year " + str(query) + " is a leap year."
else:
    print "The year " + str(query) + " is not a leap year."
    
