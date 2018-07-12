import math
def trigcalc():
    notdone = True
    print()
    print("Welcome to the trigonometry calculator.")
    print()
    print("Please select a mode from the following:")
    print("1. Pythagoras' Theorem (right angled triangle)")
    print("2. tan(), sin(), cos() for unknown side (right angled triangle)")
    print("3. tan(), sin(), cos() for unknown angle (right angled triangle)")
    print("4. Sine rule (two sides, non-included angle)")
    print("5. Cosine rule (two sides, included angle OR three sides)")
    print("6. Area of triangle (two sides, included angle)")
    print()
    while notdone:
        try:
            mode = int(input("Please enter a mode: "))
            if mode > 0 and mode <= 6:
                notdone = False
                if mode == 1:
                    pythagoras()
                if mode == 2:
                    rightangledtrig()
                if mode == 3:
                    rightangledtrigangle()
                if mode == 4:
                    sinrule()
                if mode == 5:
                    cosrule()
                if mode == 6:
                    areatriangle()
            else:
                print()
                print("Enter a number between 1 and 6 - there are only 6 modes")
                print()
        except ValueError:
            print()
            print("Please enter a valid number")
            print()

def pythagoras():
    notdone = True
    while notdone:
        try:
            mode = int(input("Please specify the mode: 1 for finding the hypotenuse or 2 for finding a side given the hypotenuse and a side: "))
            if mode in [1,2]:
                if mode == 1:
                    side1 = float(input("Side 1: "))
                    side2 = float(input("Side 2: "))
                    result = math.hypot(side1,side2)
                    print("Hypotenuse = sqrt(" + str(side1) + " + " + str(side2) + ")")
                    print()
                    print("The hypotenuse is",result,"units long. (please round off if needed.)")
                    print()
                    notdone = False
                    return
                if mode == 2:
                   side1 = float(input("Length of hypotenuse: "))
                   side2 = float(input("Length of other known side: "))
                   result = math.sqrt((side1**2 - side2**2))
                   print("Hypotenuse = sqrt(" + str(side1) + "- " + str(side2) + ")")
                   print()
                   print("The hypotenuse is",result,"units long. (please round off if needed.)")
                   print()
                   notdone = False
                   return
            else:
                print()
                print("Please enter 1 or 2.")
                print()
        except ValueError:
            print()
            print("One of your inputs is incorrect.")
            print()

def sinrule():
    notdone = True
    while notdone:
        try:
            mode = int(input("Please specify the mode: 1 for finding a side and 2 for finding an angle: "))
            if mode in [1,2]:
                if mode == 1:
                    side1 = float(input("Side 1 length: "))
                    angle1 = float(input("Angle 1 (corresponding to side 1, in degrees, without the unit): "))
                    angle2 = float(input("Angle 2 (corresponding to unknown side, in degrees, without the unit): "))
                    print("By sine rule,")
                    print("unknown side / sin({0}) = {1} / sin({2})".format(angle2,side1,angle1))
                    print("thus,")
                    print("unknown side = {0} * {1}) / sin({2})".format(side1,angle2,angle1))
                    result = (side1 * math.sin(math.radians(angle1))) / math.sin(math.radians(angle2))
                    print()
                    print("The side is",result,"units long. (please round off if needed.)")
                    print()
                    notdone = False
                    return
                if mode == 2:
                    side1 = float(input("Side 1 length (corresponding to known angle): "))
                    side2 = float(input("Side 2 length (corresponding to unknown angle): "))
                    angle1 = float(input("Angle (corresponding to side 1, in degrees, without the unit): "))
                    print("By sine rule,")
                    print("sin(unknown angle) / {0} = sin({1}) / {2} ".format(side2,angle1,side1))
                    print("thus,")
                    print("unknown angle = inv sine({0}  *  sin({1})) /  {2})".format(side2,angle1,side1))
                    result = math.degrees(math.asin((side2 * math.sin(math.radians(angle1))) / side1))
                    print()
                    print("The angle is",result,"or",(180 - result),"degrees wide. (please round off if needed.) Note that you may have to reject one of the answers.")
                    print()
                    notdone = False
                    return
            else:
                print()
                print("Please enter 1 or 2.")
                print()
        except ValueError:
            print()
            print("One of your inputs is incorrect.")
            print()
    return

def cosrule():
    notdone = True
    while notdone:
        try:
            mode = int(input("Please specify the mode: 1 for finding a side and 2 for finding an angle."))
            if mode in [1,2]:
                if mode == 1:
                    side1 = float(input("Side 1 length: "))
                    side2 = float(input("Side 2 length: "))
                    angle1 = float(input("Angle (non-included from specified sides): "))
                    print("By cosine rule,")
                    print('{0}^2 + {1}^2 - (2 * {0} * {1} * cos({2})'.format(side1,side2,angle1))
                    calc = side1 ** 2 + side2 ** 2 - (2*side1*side2*math.cos((math.radians(angle1))))
                    result = math.sqrt(calc)
                    print()
                    print("The side is",result,"units long (please round off if needed.)")
                    print()
                    notdone = False
                    return
                if mode == 2:
                    a = float(input("Side 1 length: "))
                    b = float(input("Side 2 length: "))
                    c = float(input("Side 3 length: "))
                    print("By cosine rule,")
                    print("Angle A = inv cos( ({0}^2 + {1}^2 - {2}^2) / (2*{0}*{1}) )".format(b,c,a))
                    print("Angle B = inv cos( ({0}^2 + {1}^2 - {2}^2) / (2*{0}*{1}) )".format(a,c,b))
                    print("Angle C = inv cos( ({0}^2 + {1}^2 - {2}^2) / (2*{0}*{1}) )".format(a,b,c))
                    print("Angles found:")
                    calc1 = (b**2 + c**2 - a**2) / (2*b*c)
                    calc2 = (a**2 + c**2 - b**2) / (2*a*c)
                    calc3 = (a**2 + b**2 - c**2) / (2*a*c)
                    calcs = [calc1,calc2,calc3]
                    for calc in calcs:
                        if calc >= -1 and calc <= 1:
                            result = math.degrees(math.acos(calc))
                            print(result)
                    print("If angles are irrational, please round off if needed.")
                    notdone = False
                    return
        except ValueError:
            print("One of your inputs is incorrect.")
          



def rightangledtrig():
    notdone = True
    while notdone:
        try:
            unknown = input("Specify the unknown side relative to your angle. h for hypotenuse, a for adjacent, o for opposite: ")
            known = input("Specify the known side relative to your angle. h for hypotenuse, a for adjacent, o for opposite: ")
            if unknown.lower() in ["h", "a", "o"] and known.lower() in ["h", "a", "o"] and unknown != known:
                angle = float(input("Enter your known angle (in degrees, without the sign): "))
                known1 = float(input("Enter the length of your known side: "))
                notdone = False
                if unknown == "h":
                    print("Hypotenuse is unknown")
                    if known == "a":
                        print("Adjacent side known, using cos()")
                        print("Since cos() = adj / hyp,")
                        print("unknown side = {0} / cos({1})".format(known1,angle))
                        result = known1/math.cos(math.radians(angle))
                        print()
                        print("The side is",result,"units long (please round off if needed.)")
                        print()
                        return
                    if known == "o":
                        print("Opposite side known, using sin()")
                        print("Since sin() = opp/hyp,")
                        print("unknown side = {0} / sin({1})".format(known1,angle))
                        result = known1/math.sin(math.radians(angle))
                        print()
                        print("The side is",result,"units long (please round off if needed.)")
                        print()
                        return
                if unknown == "a":
                    print("Adjacent side is unknown")
                    if known == "h":
                        print("Hypotenuse known, using cos()")
                        print("Since cos() = adj / hyp,")
                        print("unknown side = {0} * cos({1})".format(known1,angle))
                        result = math.cos(math.radians(angle) * known1)
                        print()
                        print("The side is",result,"units long (please round off if needed.)")
                        print()
                        return
                    if known == "o":
                        print("Opposite side known, using tan()")
                        print("Since tan() = opp/adj,")
                        print("unknown side = {0} / tan({1})".format(known1,angle))
                        result = known1/math.tan(math.radians(angle))
                        print()
                        print("The side is",result,"units long (please round off if needed.)")
                        print()
                        return
                if unknown == "o":
                    print("Opposite side is unknown")
                    if known == "h":
                        print("Since sin() = opp/hyp,")
                        print("unknown side = {0} * sin({1})".format(known1,angle))
                        result = math.sin(math.radians(angle) * known1)
                        print()
                        print("The side is",result,"units long (please round off if needed.)")
                        print()
                        return
                    if known == "a":
                        print("Opposite side known, using tan()")
                        print("Since tan() = opp/adj,")
                        print("unknown side = {0} * tan({1})".format(known1,angle))
                        result = known1 * math.tan(math.radians(angle))
                        print()
                        print("The side is",result,"units long (please round off if needed.)")
                        print()
                        return
            else:
                print("Please specify either \"h\", \"a\" or \"o\"")
        except ValueError:
            print()
            print("You did not specify a correct input. Try again.")
            print()

def rightangledtrigangle():
    notdone = True
    while notdone:
        try:
            known1 = input("Specify the first known side relative to your angle. h for hypotenuse, a for adjacent, o for opposite: ")
            known2 = input("Specify the second known side relative to your angle. h for hypotenuse, a for adjacent, o for opposite: ")
            if known2.lower() in ["h", "a", "o"] and known1.lower() in ["h", "a", "o"] and known1 != known2:
                length1 = float(input("Specify the length of the first known side: "))
                length2 = float(input("Specify the length of the second known side: "))
                if known1 == "h" and known2 == "a":
                    print("Hypotenuse and adjacent side known, using arc (inverse) cosine")
                    print("Since cos() = adj/hyp,")
                    print("unknown angle = inv cos({0} / {1})".format(length2,length1))
                    result = math.degrees(math.acos(length2/length1))
                    print()
                    print("Angle is",result,"degrees (please round off if needed.)")
                    print()
                if known1 == "h" and known2 == "o":
                    print("Hypotenuse and opposite side known, using arc (inverse) sine")
                    print("Since sin() = opp/hyp,")
                    print("unknown angle = inv sin({0} / {1})".format(length2,length1))
                    result = math.degrees(math.asin(length2/length1))
                    print()
                    print("Angle is",result,"degrees (please round off if needed.)")
                    print()
                if known1 == "a" and known2 == "h":
                    print("Hypotenuse and adjacent side known, using arc (inverse) cosine")
                    print("Since cos() = adj/hyp,")
                    print("unknown angle = inv cos({0} / {1})".format(length1,length2))
                    result = math.degrees(math.acos(length1/length2))
                    print()
                    print("Angle is",result,"degrees (please round off if needed.)")
                    print()
                if known1 == "o" and known2 == "h":
                    print("Hypotenuse and opposite side known, using arc (inverse) sine")
                    print("Since sin() = opp/hyp,")
                    print("unknown angle = inv sin({0} / {1})".format(length1,length2))
                    result = math.degrees(math.asin(length1/length2))
                    print()
                    print("Angle is",result,"degrees (please round off if needed.)")
                    print()
                if known1 == "o" and known2 == "a":
                    print("Opposite and adjacent side known, using arc (inverse) tangent")
                    print("Since tan() = opp/adj,")
                    print("unknown angle = inv tan({0} / {1})".format(length1,length2))
                    result = math.degrees(math.atan(length1/length2))
                    print()
                    print("Angle is",result,"degrees (please round off if needed.)")
                    print()
                if known1 == "a" and known2 == "o":
                    print("Adjacent and opposite side known, using arc (inverse) tangent")
                    print("Since tan() = opp/adj,")
                    print("unknown angle = inv tan({0} / {1})".format(length2,length1))
                    result = math.degrees(math.atan(length2/length1))
                    print()
                    print("Angle is",result,"degrees (please round off if needed.)")
                    print()
                notdone = False
                return
            else:
                print("Please specify either \"h\", \"a\" or \"o\"")
        except ValueError:
                print("One of your inputs is incorrect. Try again.")

def areatriangle():
    notdone = True
    while notdone:
        try:
            length1 = float(input("Side 1 length: "))
            length2 = float(input("Side 2 length: "))
            angle = float(input("Angle (the inclusive angle of the two sides): "))
            print("As area of triangle = 0.5(a*b*sin(C)),")
            print("area = 0.5({0} * {1} * sin({2}))".format(length1,length2,angle))
            result = 0.5 * length1 * length2 * math.sin(math.radians(angle))
            print()
            print("Area is",result,"units squared (please round off if needed.)")
            print()
            notdone = False
        except ValueError:
            print()
            print("You did not specify a correct input. Try again.")
            print()

while True:
    trigcalc()
       
        
        
