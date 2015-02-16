print raw_input("Enter your total balance due:$ ")
ans = ob
print raw_input("Enter your mimimum monthly payment percentage as a decimal: ")
ans = v
print raw_input("How many months would you like to calculate for? ")
ans = m
print raw_input("What is the apr for the card in decimal form? ")
ans = a

def findrate():
    for ans in range(1, m + 1):
            i = ob * (a/12)
            p = ob * v
            nb = (ob - p + i)
            pp = ob - nb
            ob = nb
            numGueses += 1
            rpp = rpp + pp
            print "Month: ",numGueses 
            print "Minimum monthly payment:$",round(p,2)
            print "Principal paid:$",round(pp,2)
            print "Remaining balance: $",round(nb,2)
            print "Total principal paid over year:$",round(rpp,2)
            principal = rpp   
            findrate()

findrate()



