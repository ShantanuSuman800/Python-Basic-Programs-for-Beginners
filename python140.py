#Python function to convert height (in feet and inches) to centimeters.
def height_centi(feet,inches):
    f = feet*12
    i = (inches+f)*2.54
    print("Your height in centimeters is:",i)
height_centi(5,3)