ob = float(raw_input("What is the balance on your credit card?"))
ans = float(ob)
mmp = float(raw_input("What is the minimum monthly payment in decimal form?"))
ans = float(mmp)
m = int(raw_input("How many months would you like to calculate for?"))
ans = float(m)
a = float(raw_input("What is your cards APR in form of a decimal?"))
ams = float(a)

                

def findrate(ob,mmp,m,a):
    numGueses = 0
    rpp = 0
    rp = 0
    for ans in range(1, m + 1):
        i = ob * (a/12)
        p = ob * mmp
        nb = (ob - p + i)
        pp = ob - nb
        ob = nb
        numGueses += 1
        rpp = rpp + pp
        rp = rp + p
        print "Month: ",numGueses
        print "Minimum monthly payment:$", + float(round(p,2))
        print "Principal paid:$", + float(round(pp,2))
        print "Remaining balance:$", + float(round(nb,2))
        if ans == m:
            print "RESULT"
            print "Total Paid:$", + float(round(rp,2))
            print "Total principal paid over term:$", + float(round(rpp,2))
            print "Remaining balance:$", + float(round(nb,2))
        
findrate(ob,mmp,m,a)


