db = int(raw_input("Please enter Dry Bulb:"))
wb = int(raw_input("Please enter Wet Bulb:"))
el = int(raw_input("What is your current elevation?"))
##ws = int(raw_input("Please enter the wind speed:"))
##wd = str(raw_input("What direction is the wind coming from?"))
rh = 0
def result(rh):
    print ""
    print "The current relative humidity is " + str(rh) + "%"
def summit(db, wb):

    if db == wb:
        print ""
        print "The current relative humidity is 100%"
    
    elif db == 31 and wb == 20:
        rh = 6
        result(rh)

    elif db == 31 and wb == 21:
        rh = 14
        result(rh)

    elif db == 31 and wb == 22:
        rh = 22
        result(rh)

    elif db == 31 and wb == 23:
        rh = 30
        result(rh)

    elif db == 31 and wb == 24:
        rh = 38
        result(rh)

    elif db == 31 and wb == 25:
        rh = 46
        result(rh)

    elif db == 31 and wb == 26:
        rh = 55
        result(rh)

    elif db == 31 and wb == 27:
        rh = 63
        result(rh)

    elif db == 31 and wb == 28:
        rh = 72
        result(rh)

    elif db == 31 and wb == 29:
        rh = 81
        result(rh)

    elif db == 31 and wb == 30:
        rh = 90
        result(rh)

    elif db == 32 and wb == 20:
        rh = 1
        result(rh)

    elif db == 32 and wb == 21:
        rh = 9
        result(rh)

    elif db == 32 and wb == 22:
        rh = 16
        result(rh)

    elif db == 32 and wb == 23:
        rh = 24
        result(rh)

    elif db == 32 and wb == 24:
        rh = 32
        result(rh)

    elif db == 32 and wb == 25:
        rh = 40
        result(rh)

    elif db == 32 and wb == 26:
        rh = 48
        result(rh)

    elif db == 32 and wb == 27:
        rh = 56
        result(rh)

    elif db == 32 and wb == 28:
        rh = 64
        result(rh)

    elif db == 32 and wb == 29:
        rh = 73
        result(rh)

    elif db == 32 and wb == 30:
        rh = 82
        result(rh)

    elif db == 32 and wb == 21:
        rh = 91
        result(rh)

    elif db == 33 and wb == 21:
        rh = 4
        result(rh)

    elif db == 33 and wb == 22:
        rh = 11
        result(rh)

    elif db == 33 and wb == 23:
        rh =18
        result(rh)

    elif db == 33 and wb == 24:
        rh = 26
        result(rh)

    elif db == 33 and wb == 25:
        rh = 34
        result(rh)

    elif db == 33 and wb == 26:
        rh = 41
        result(rh)

    elif db == 33 and wb == 27:
        rh = 49
        result(rh)

    elif db == 33 and wb == 28:
        rh = 57
        result(rh)

    elif db == 33 and wb == 29:
        rh = 66
        result(rh)

    elif db == 33 and wb == 30:
        rh = 74
        result(rh)

    elif db == 33 and wb == 31:
        rh = 83
        result(rh)

    elif db == 33 and wb == 32:
        rh = 92
        result(rh)

    elif db == 34 and wb == 22:
        rh = 6
        result(rh)

    elif db == 34 and wb == 23:
        rh = 13
        result(rh)

    elif db == 34 and wb == 24:
        rh = 21
        result(rh)

    elif db == 34 and wb == 25:
        rh = 28
        result(rh)

    elif db == 34 and wb == 26:
        rh = 35
        result(rh)

    elif db == 34 and wb == 27:
        rh = 43
        result(rh)

    elif db == 34 and wb == 28:
        rh = 51
        result(rh)

    elif db == 34 and wb == 29:
        rh = 59
        result(rh)

    elif db == 34 and wb == 30:
        rh = 67
        result(rh)

    elif db == 34 and wb == 31:
        rh = 75
        result(rh)

    elif db == 34 and wb == 32:
        rh = 84
        result(rh)

    elif db == 34 and wb == 33:
        rh = 92
        result(rh)

    elif db == 35 and wb == 22:
        rh = 2
        result(rh)

    elif db == 35 and wb == 23:
        rh = 9
        result(rh)

    elif db == 35 and wb == 24:
        rh = 16
        result(rh)

    elif db == 35 and wb == 25:
        rh = 23
        result(rh)

    elif db == 35 and wb == 26:
        rh = 30
        result(rh)

    elif db == 35 and wb == 27:
        rh = 37
        result(rh)

    elif db == 35 and wb == 28:
        rh = 45
        result(rh)

    elif db == 35 and wb == 29:
        rh = 52
        result(rh)

    elif db == 35 and wb == 30:
        rh = 60
        result(rh)

    elif db == 35 and wb == 31:
        rh = 68
        result(rh)

    elif db == 35 and wb == 32:
        rh = 76
        result(rh)

    elif db == 35 and wb == 33:
        rh = 84
        result(rh)

    elif db == 35 and wb == 34:
        rh = 92
        result(rh)

    elif db == 36 and wb == 23:
        rh = 4
        result(rh)

    elif db == 36 and wb == 24:
        rh = 11
        result(rh)

    elif db == 36 and wb == 25:
        rh = 18
        result(rh)

    elif db == 36 and wb == 26:
        rh = 25
        result(rh)

    elif db == 36 and wb == 27:
        rh = 32
        result(rh)

    elif db == 36 and wb == 28:
        rh = 39
        result(rh)    

    elif db == 36 and wb == 29:
        rh = 46
        result(rh)

    elif db == 36 and wb == 30:
        rh = 54
        result(rh)

    elif db == 36 and wb == 31:
        rh = 61
        result(rh)

    elif db == 36 and wb == 32:
        rh = 69
        result(rh)

    elif db == 36 and wb == 33:
        rh = 77
        result(rh)

    elif db == 36 and wb == 34:
        rh = 84
        result(rh)

    elif db == 36 and wb == 35:
        rh = 92
        result(rh)

    elif db == 37 and wb == 24:
        rh = 7
        result(rh)

    elif db == 37 and wb == 25:
        rh = 13
        result(rh)

    elif db == 37 and wb == 26:
        rh = 20
        result(rh)

    elif db == 37 and wb == 27:
        rh = 27
        result(rh)

    elif db == 37 and wb == 28:
        rh = 34
        result(rh)

    elif db == 37 and wb == 29:
        rh = 41
        result(rh)

    elif db == 37 and wb == 30:
        rh = 48
        result(rh)

    elif db == 37 and wb == 31:
        rh = 55
        result(rh)

    elif db == 37 and wb == 32:
        rh = 63
        result(rh)    

    elif db == 37 and wb == 33:
        rh = 70
        result(rh)

    elif db == 37 and wb == 34:
        rh = 77
        result(rh)

    elif db == 37 and wb == 35:
        rh = 85
        result(rh)

    elif db == 37 and wb == 36:
        rh = 92
        result(rh)

    elif db == 38 and wb == 24:
        rh = 3
        result(rh)

    elif db == 38 and wb == 25:
        rh = 9
        result(rh)

    elif db == 38 and wb == 26:
        rh = 16
        result(rh)

    elif db == 38 and wb == 27:
        rh = 22
        result(rh)

    elif db == 38 and wb == 28:
        rh = 29
        result(rh)

    elif db == 38 and wb == 29:
        rh = 35
        result(rh)

    elif db == 38 and wb == 30:
        rh = 42
        result(rh)

    elif db == 38 and wb == 31:
        rh = 49
        result(rh)

    elif db == 38 and wb == 32:
        rh = 57
        result(rh)

    elif db == 38 and wb == 33:
        rh = 64
        result(rh)

    elif db == 38 and wb == 34:
        rh = 71
        result(rh)

    elif db == 38 and wb == 35:
        rh = 78
        result(rh)

    elif db == 38 and wb == 36:
        rh = 85
        result(rh)

    elif db == 38 and wb == 37:
        rh = 92
        result(rh)

    elif db == 39 and wb == 25:
        rh = 5
        result(rh)

    elif db == 39 and wb == 26:
        rh = 11
        result(rh)

    elif db == 39 and wb == 27:
        rh = 18
        result(rh)

    elif db == 39 and wb == 28:
        rh = 24
        result(rh)

    elif db == 39 and wb == 29:
        rh = 31
        result(rh)

    elif db == 39 and wb ==30:
        rh = 37
        result(rh)

    elif db == 39 and wb == 31:
        rh = 44
        result(rh)

    elif db == 39 and wb == 32:
        rh = 51
        result(rh)

    elif db == 39 and wb == 33:
        rh = 58
        result(rh)

    elif db == 39 and wb == 34:
        rh = 64
        result(rh)

    elif db == 39 and wb == 35:
        rh = 71
        result(rh)

    elif db == 39 and wb == 36:
        rh = 78
        result(rh)

    elif db == 39 and wb == 37:
        rh = 85
        result(rh)

    elif db == 39 and wb == 38:
        rh = 93
        result(rh)

    elif db == 40 and wb == 25:
        rh = 2
        result(rh)

    elif db == 40 and wb == 26:
        rh = 8
        result(rh)

    elif db == 40 and wb == 27:
        rh = 14
        result(rh)

    elif db == 40 and wb == 28:
        rh = 20
        result(rh)

    elif db == 40 and wb == 29:
        rh = 26
        result(rh)

    elif db == 40 and wb == 30:
        rh = 32
        result(rh)

    elif db == 40 and wb == 31:
        rh = 39
        result(rh)

    elif db == 40 and wb == 32:
        rh = 46
        result(rh)

    elif db == 40 and wb == 33:
        rh = 52
        result(rh)

    elif db == 40 and wb == 34:
        rh = 58
        result(rh)

    elif db == 40 and wb == 35:
        rh = 65
        result(rh)

    elif db == 40 and wb == 36:
        rh = 72
        result(rh)

    elif db == 40 and wb == 37:
        rh = 79
        result(rh)

    elif db == 40 and wb == 38:
        rh = 86
        result(rh)

    elif db == 40 and wb == 39:
        rh = 93
        result(rh)

    elif db == 41 and wb == 26:
        rh = 4
        result(rh)

    elif db == 41 and wb == 27:
        rh = 10
        result(rh)

    elif db == 41 and wb == 28:
        rh = 16
        result(rh)

    elif db == 41 and wb == 29:
        rh = 22
        result(rh)

    elif db == 41 and wb == 30:
        rh = 28
        result(rh)

    elif db == 41 and wb == 31:
        rh = 34
        result(rh)

    elif db == 41 and wb == 32:
        rh = 41
        result(rh)

    elif db == 41 and wb == 33:
        rh = 47
        result(rh)

    elif db == 41 and wb == 34:
        rh = 53
        result(rh)

    elif db == 41 and wb == 35:
        rh = 59
        result(rh)
        
    elif db == 41 and wb == 36:
        rh = 66
        result(rh)

    elif db == 41 and wb == 37:
        rh = 72
        result(rh)

    elif db == 41 and wb == 38:
        rh = 79
        result(rh)

    elif db == 41 and wb == 39:
        rh = 86
        result(rh)

    elif db == 41 and wb == 40:
        rh = 93
        result(rh)

    elif db == 42 and wb == 26:
        rh = 1
        result(rh)

    elif db == 42 and wb == 27:
        rh = 6
        result(rh)

    elif db == 42 and wb == 28:
        rh = 12
        result(rh)

    elif db == 42 and wb == 29:
        rh = 18
        result(rh)

    elif db == 42 and wb == 30:
        rh = 24
        result(rh)

    elif db == 42 and wb == 31:
        rh = 30
        result(rh)

    elif db == 42 and wb == 32:
        rh = 36
        result(rh)

    elif db == 42 and wb == 33:
        rh = 42
        result(rh)

    elif db == 42 and wb == 34:
        rh = 48
        result(rh)

    elif db == 42 and wb == 35:
        rh = 54
        result(rh)

    elif db == 42 and wb == 36:
        rh = 60
        result(rh)

    elif db == 42 and wb == 37:
        rh = 66
        result(rh)

    elif db == 42 and wb == 38:
        rh = 73
        result(rh)

    elif db == 42 and wb == 39:
        rh = 80
        result(rh)

    elif db == 42 and wb == 40:
        rh = 86
        result(rh)

    elif db == 42 and wb == 41:
        rh = 93
        result(rh)
        
    
        
    else:
        print ""
        print """Sorry.  The code for this app is still under construnction and data for
those temperatures has not been entered yet."""

    
    














    
if el >= 6101 and el <= 8500:
    summit(db, wb)
    
##elif el >= 3900 and el <= 6100:
##    treeline(db, wb)
##    
##elif el >= 2000 and el <= 3899:
##    lowlands(db, wb)
##    
##elif el >= 0 and el <= 1999:
##    sealevel(db, wb)
    
else:
    print ""
    print """Sorry.  The code for this app is still under construnction
and data for your elevation has not been entered yet."""
    
