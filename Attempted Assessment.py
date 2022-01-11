import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
@dataclass
class Holiday:
      
    def __init__(self,name, date):
        Name: str
        Date: str 
        #Your Code Here        
    
    def __str__ (self):
        return self.Name, self.Date
        # String output
        # Holiday output when printed.
          
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
   def __init__(self):
       self.innerHolidays = []
   
    def addHoliday(holidayObj):
        print("Add a Holiday")
        print("=============")
        Name = input(str("Holiday: "))
        Date = input(str("Date (yyyy-mm-dd): "))

        def isValidDate(date):
                year, month, day = Date.split('-')
                isValidDate = True
                try:
                        datetime.datetime(int(year), int(month), int(day))
                        return(date)
                except:
                        isValidDate = False
        isValidDate(Date)
        if(isValidDate):
                print("Success:")
                innerHolidays = 
                innerHolidays.append(holidayObj)
                print(Name + "(" + Date + ") has been added to the holiday list.")
        else:
                while(isValidDate is False):
                        print("Invalid date. Please try again. ")
                        Date = input(str("Date (yyyy-mm-dd): "))
                        isValidDate(Date)
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday

    def findHoliday(HolidayName, Date):
        find_holiday = str(input("What holiday would you like to find? "))
        if find_holiday in innerHolidays:
                Name = find_holiday
                return innerHolidays[Name], innerHolidays[Date]
        else:
            print("Could not find " + find_holiday + " in the list")
        # Find Holiday in innerHolidays
        # Return Holiday

    def removeHoliday(HolidayName, Date):
        print("Remove a Holiday")
        print("================")
        name is False
        while name is False:
                name = str(input("Holiday Name: "))

                if name in innerHolidays:
                        innerHolidays.remove[name]
                        print(name + "has been removed from the holiday list.")
                        name is True
                else:
                        print(name + " not found.")
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday

    def read_json(filelocation):
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.

    def save_to_json(filelocation):
        # Write out json file to selected file.
        
    def scrapeHolidays():
        holidays = []
        for x in range(2019, 2024):
            html = requests.get("https://www.timeanddate.com/calendar/print.html?year=" + str(x) + "&country=1&hol=33554809&holm=1&df=1").text
            soup = BeautifulSoup(html, "html.parser")

            table = soup.find('table', attrs = {'class': 'cht lpad'})


            for row in table.find_all('tr'):
                cells = row.find_all('td')
                holiday = {}
                holiday['date'] = cells[0].string + " " + str(x)
                holiday['date'] = datetime.strptime(holiday['date'], "%b %d %Y")
                holiday['name'] = cells[1].string
            holidays.append(holiday)
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.     

    def numHolidays():
        # Return the total number of holidays in innerHolidays
        print("There are " + str(len(innerHolidays)) + " holidays in the file"
    
    def filter_holidays_by_week(year, week_number):
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays

    def displayHolidaysInWeek(holidayList):
        holidays = []
    for x in range(2019, 2024):
        html = requests.get("https://www.timeanddate.com/calendar/print.html?year=" + str(x) + "&country=1&hol=33554809&holm=1&df=1").text
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find('table', attrs = {'class': 'cht lpad'})


        for row in table.find_all('tr'):
            cells = row.find_all('td')
            holiday = {}
            holiday['date'] = cells[0].string + " " + str(x)
            holiday['date'] = datetime.strptime(holiday['date'], "%b %d %Y")
            holiday['name'] = cells[1].string
        holidays.append(holiday)
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    def getWeather(weekNum):
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek():
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results



def main():
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    # 2. Load JSON file via HolidayList read_json function
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    # 3. Create while loop for user to keep adding or working with the Calender
    # 4. Display User Menu (Print the menu)
    # 5. Take user input for their action based on Menu and check the user input for errors
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


if __name__ == "__main__":
    main();
    #


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.





