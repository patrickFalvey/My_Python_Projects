import cmath
import math

## Establishing 'side' variables for later use
lengthA = 0
lengthB = 0
lengthC = 0

ax = float(raw_input("Please enter the x coordinate of the first point in your triangle."))
ay = float(raw_input("Please enter the y coordinate of the first point in your triangle."))
bx = float(raw_input("Please enter the x coordinate of the second point in your triangle."))
by = float(raw_input("Please enter the y coordinate of the second point in your triangle."))
cx = float(raw_input("Please enter the x coordinate of the third point in your triangle."))
cy = float(raw_input("Please enter the y coordinate of the third point in your triangle."))
print ""
print ""

## Loop checks whether the values are solvable before continuing the script. 
while True:
    if (ax == bx and ax == cx) and (ay == by and ay == cy):
        print "Please check your coordinates again.  The three points you entered are the same."
        break
    elif (ax == bx and ax == cx) or (ay == by and ay == cy):
        print "Please check your coordinates again.  The three points you entered are inline with each other."
        break
## If the values do not produce an error, these 'side' functions
## will define the length of each side via pythagorean theorum.
    def sideA(ax,ay,bx,by):
        a = ax - bx
        b = ay - by
        csquare = a**2 + b**2
        global lengthA
        lengthA = float(math.sqrt(csquare))
        print "Side 'A' is " + str(lengthA) + " in length."

    sideA(ax,ay,bx,by)

    def sideB(bx,by,cx,cy):
        a = bx - cx
        b = by - cy
        csquare = a**2 + b**2
        global lengthB
        lengthB = float(math.sqrt(csquare))
        print "Side 'B' is " + str(lengthB) + " in length."

    sideB(bx,by,cx,cy)

    def sideC(cx,cy,ax,ay):
        a = cx - ax
        b = cy - ay
        csquare = a**2 + b**2
        global lengthC
        lengthC = float(math.sqrt(csquare))
        print "Side 'C' is " + str(lengthC) + " in length."
      
    sideC(cx,cy,ax,ay)
    lengthA = round(lengthA,1)
    lengthB = round(lengthB,1)
    lengthC = round(lengthC,1)
    sidea = lengthA
    sideb = lengthB
    sidec = lengthC
    
## Once the length of the sides have been established,  
## the law of cosines is used to find the first two angles.
    
    divisora = sideb * sidec
    divisorb = sidec * sidea
    divisorc = sideb * sidea

    cosa = (sidec**2 + sideb**2 - sidea**2)/(2 * divisora)
    cosb = (sidec**2 + sidea**2 - sideb**2)/(2 * divisorb)
    cosc = (sidea**2 + sideb**2 - sidec**2)/(2 * divisorc)
## Python function for finding the radian of an angle.
    
    testa = cmath.acos(cosa)
    testb = cmath.acos(cosb)
    testc = cmath.acos(cosc)
## Python function for converting the radians into degrees.
    
    sola = math.degrees(testa.real)
    solb = math.degrees(testb.real)
    solc = 180 - (sola + solb)
## Check to ensure sum of all angles is 180.0
    check = sola + solb + solc
    if check != 180.0:
        print """Something is wrong with this program. The values appear to be valid but
        the angles are not adding up to 180.0 degrees."""
    print ""
    print ""
    print str("Angle 'A' is aproximately ") + str(round(sola,1)) + str(" degrees")
    print str("Angle 'B' is aproximately ") + str(round(solb,1)) + str(" degrees")
    print str("Angle 'C' is aproximately ") + str(round(solc,1)) + str(" degrees")
    print ""
    print str("Sum of all the angles = " + str(check) + " degrees")
    break

