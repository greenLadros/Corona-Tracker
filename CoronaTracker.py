#ivri korem 2020
"""
This is a corona tracker taking the data from an api,
i built it for practice and fun, hope you enjoy.
"""

#import
import requests
import time
import matplotlib


#defining vars
headers = {
'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
'x-rapidapi-key': "7d9490fb43mshec1d2778be49823p1a7e2ajsn20db3e1c0e68"
}

#define functions
class CoronaTracker():
    #help
    def getAllCountrys(self):
        url = "https://covid-19-data.p.rapidapi.com/help/countries"
        querystring = {"format":"json"}

        return requests.request("GET", url, headers=headers, params=querystring)
    
    #corona world totals
    def getWorldCoronaTotals(self):
        url = "https://covid-19-data.p.rapidapi.com/totals"
        querystring = {"format":"json"}

        return requests.request("GET", url, headers=headers, params=querystring)
    
    def getDailyWorldCoronaTotals(self, date="2020-9-1"):
        url = "https://covid-19-data.p.rapidapi.com/totals"
        querystring = {"date-format":"YYYY-MM-DD","format":"json","date":date}

        return requests.request("GET", url, headers=headers, params=querystring)
    
    #corona country based totals
    def getDailyCountryCoronaTotals(self, date="2020-9-1", country="israel"):
        url = "https://covid-19-data.p.rapidapi.com/report/country/name"
        querystring = {"date-format":"YYYY-MM-DD","format":"json","date":date,"name":country}

        return requests.request("GET", url, headers=headers, params=querystring)
    
    def getAllCountrysCoronaTotals(self):
        url = "https://covid-19-data.p.rapidapi.com/country/all"
        querystring = {"format":"json"}

        return requests.request("GET", url, headers=headers, params=querystring)
    
    def getAllCountrysDailyCoronaTotals(self, date="2020-9-1"):
        url = "https://covid-19-data.p.rapidapi.com/report/country/all"
        querystring = {"date-format":"YYYY-MM-DD","format":"json","date":date}

        return requests.request("GET", url, headers=headers, params=querystring)
    
    def getCountryCoronaTotals(self, country="israel"):
        url = "https://covid-19-data.p.rapidapi.com/country"
        querystring = {"format":"json","name":country}

        return requests.request("GET", url, headers=headers, params=querystring)

def myPrint(obj):
    """iterates through given object, and print keys and values capitalized.
    param: object with dictionary and lists in it.
    return: none.
    """
    for attr, value in obj.items():
        if type(value) == list:
            myPrint(value[0]) # dangerous!
        elif type(value) == dict:
            myPrint(value)
        else:
            print(attr.capitalize(), ":",value.capitalize() if type(value) == str else value)


#setting it
ct = CoronaTracker()

#welcoming
print("""\n\n\n

░█████╗░░█████╗░██╗░░░██╗██╗██████╗░░░░░░░░░███╗░░░█████╗░  ████████╗██████╗░░█████╗░░█████╗░██╗░░██╗██████╗░
██╔══██╗██╔══██╗██║░░░██║██║██╔══██╗░░░░░░░████║░░██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔══██╗
██║░░╚═╝██║░░██║╚██╗░██╔╝██║██║░░██║█████╗██╔██║░░╚██████║  ░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░██████╔╝
██║░░██╗██║░░██║░╚████╔╝░██║██║░░██║╚════╝╚═╝██║░░░╚═══██║  ░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══██╗
╚█████╔╝╚█████╔╝░░╚██╔╝░░██║██████╔╝░░░░░░███████╗░█████╔╝  ░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║░░██║
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝╚═════╝░░░░░░░╚══════╝░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
""")


#program interaction loop
while True:
    #getting user input
    task = input("""\n\n
    what do you want to know?\n
    \n
    +World Totals\n
    (1)The world's corona totals\n
    (2)The world's daily corona totals in a specific date\n
    \n
    +Country Totals\n
    (3)Country's corona totals\n
    (4)Country's daily corona totals in a specific date\n
    (5)All the countrys corona totals (includes payment)\n
    (6)All the countrys daily corona totals in a specific date (includes payment)\n\n
    \n
    +help\n
    (7)All the supported countrys list\n
    (8)Quit\n
    """)

    #action based on input
    if task == "1":
        response = ct.getWorldCoronaTotals().json()[0]
        myPrint(response)

    elif task == "2":
        date = input("in what date? ")
        response = ct.getDailyWorldCoronaTotals(date).json()[0]
        print("")
        myPrint(response)

    elif task == "3":
        country = input("in what country? ")
        response = ct.getCountryCoronaTotals(country).json()[0]
        print("")
        myPrint(response)
    
    elif task == "4":
        country = input("in what country? ")
        date = input("in what date? ")
        response = ct.getDailyCountryCoronaTotals(date, country).json()[0]
        print("")
        myPrint(response)

    elif task == "5":
        response = ct.getWorldCoronaTotals().json()[0]
        myPrint(response)

    elif task == "6":
        date = input("in what date? ")
        response = ct.getDailyWorldCoronaTotals(date).json()[0]
        print("")
        myPrint(response)

    elif task == "7":
        response = ct.getAllCountrys().json()
        for i in response:
            print(str(i["name"]))
        
    elif task == "8":
        break
        #quiting

    else:
        print("please select a valid option")
        #in case of not valid input

    input("\nPress 'Enter' to continue. ")


# quiting with zero problems ;D