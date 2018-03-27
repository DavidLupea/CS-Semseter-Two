#Team David + Kevin
#David Lupea and Kevin Mesta
#IntroCS2 pd 5
#Labwork 07
#2018-02-12


#Checks if the given year is a leap year
def isLeapYr(year):
    if (year % 400 == 0): #Checks if the century is one of a multiple of 400
        return True
    if (year % 4 == 0) and (year % 100 != 0): #checks to see that the year is one of every 4 but not a multiple of 100 like 700 or 900
        return True
    else:
        return False #if th year does not fit any of the cases above then its not a leap year

      
#gives you the number of days in a given month given the month and year. cross references the isLeapYr function.
def daysInMonth(month, year):
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12): #all of these months have 31 days no matter what so if any of these months are chosen there is no need to check the year
        return 31
    if (month == 4) or (month == 6) or (month == 9) or (month == 11): #all of these months have 30 days no matter what so if any of these are chosen then there is no need to check the year
        return 30
    if (month == 2 and isLeapYr(year)): #month 2 is the only one with varying days so by using the function above if the month is 2 and if it is a leap year then there will be 29 days
        return 29
    else:
        return 28 #if month 2 is chosen but its not a leap year then 28 will be what is returned

      
#Tells you whether or not to sleep in given true or false statements as to whether it is a weekday or vacation day      
def sleep_in(weekday, vacation):
    if vacation:
        return True # if there is vacation then we will always sleep in no matter what regardless of whether or not its a weekday or weekend
    if weekday:
        return False #if the function reaches this point then it means that there is no vacation and then that means that if its a weekday we have school and we dont sleep in
    else:
        return True #this last case means that it is not a weekday so that means its the weekend and we will sleep in as well

#Tells you whether or not you're in trouble based on if the monkeys are smiling at you or not      
def monkey_trouble(a_smiles, b_smiles):
    if a_smiles == b_smiles: #because of the way the monkeys act, if they are both smiling or not smiling this means trouble so if they are equal to each other then it will return true
        return True
    else:
        return False #if the test above returns false that means that the monkeys have different expressions and you are not in trouble so it will return false

#Tells you if two numbers make ten. This happens if either one number is ten or the two add up to ten      
def makes10(a, b):
    if (a == 10) or (b == 10): # if just one of the numbers are 10 then you will return true so thats why there is an or because it can be either
        return True
    if (a + b == 10): # this part means that the first case is false and that we have to check if the sum is equal to 10 which if its true it will return true
        return True
    else:
        return False # this last part means that both of the cases above are not true so it will return false

#Challenge problem(using external libraries)
def external_dates_problem():
    from datetime import date #Imports the datetime library to work with dates

    year = int(raw_input('Enter year you were born: ')) #Asks you for the dates that the code will work with
    month = int(raw_input ('Enter month you were born: '))
    day = int(raw_input ('Enter day you were born: '))
    tyear = int(raw_input('Enter year we are currently in: '))
    tmonth = int(raw_input ('Enter month we are currently in:  '))
    tday = int(raw_input ('Enter day we are currently in:  '))

    bday = date(year, month, day) #Sets your birthday based on the given input as a date object
    today = date(tyear, tmonth, tday) #Sets today's date based on the given input as a date object
    total_days = today - bday #Finds the time between today and your birthday
    days_old = total_days.days #total_days includes hours, minutes, seconds, etc. as well so we parse it for only the days

    years_old = int((days_old / 365.25)) #Finds how old you are

    print "You are", days_old, "days old" #Gives you the various outputs
    print "You are", years_old, "years old"

    
#Challenge problem without using external features. Does not work with leap day. Cross references the daysInMonth function
def dates_problem():
    year = int(raw_input('Enter year you were born: ')) #Asks you for the dates that the code will work with
    month = int(raw_input ('Enter month you were born: '))
    day = int(raw_input ('Enter day you were born: '))
    tyear = int(raw_input('Enter year we are currently in: '))
    tmonth = int(raw_input ('Enter month we are currently in:  '))
    tday = int(raw_input ('Enter day we are currently in:  '))

    days_old = 0 #Initializes days_old as a variable equal to zero. it will add over time
    for cur_year in range (year + 1, tyear): #Iterates through each year and month betweeb your birthday and today. If your bday is April, 2002, and today is Feb, 2018. It iterates through all 
                                             #the days in 2003, 2004, 2005 ... 2017
        for cur_month in range (1, 13):
            days_old += daysInMonth(cur_month, cur_year) #Adds the number of days in each month to the days_old variable

    days_old += (daysInMonth(month, year) - day)  #Adds to the days_old variable the number of days between your birthday and the end of the month of your birthday
    days_old += tday #Adds to the days_old variable the number of days betwen the start of the current month and today

    for additional_months in range(month + 1, 13):
        days_old += daysInMonth(additional_months, year) #Adds to the days_old variable the number of days in the months between your birthday and the end of the year. 
        																								 #Ex: If you were born on June, 4, 2002 this will calculate the number of days in July, August... December of that year
          
    for new_months in range(1, tmonth):
        days_old += daysInMonth(new_months, year) #Adds to the days_old variable the number of days between the start of this year and the start of this month
        																					#Ex: if today is July, 4, 2018 it will calculate the number of days in January, Febuary ... June of this year

    years_old = int((days_old / 365.25)) #Finds how old you are
    
    print "You are", days_old, "days old" #Gives you the various outputs
    print "You are", years_old, "years old"
