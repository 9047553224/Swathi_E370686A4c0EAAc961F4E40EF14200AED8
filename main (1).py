def isLeapyear (year):
    if(year%4==0 and
year%100!=0) or year%400==0:
       return True
    else:
       return False  
year=int(input("Enter the          year:"))
if isLeapyear(year):
       print("{} is a leap year".format(year))
else:
        print("{} is not a Leap year".format (year))


  
       