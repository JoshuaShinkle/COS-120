flightsD={"Delta":{1102:[["IND",1850],["MDW",1955]],
                   1096:[["PHX",900],["MDW",1255]],
                   1445:[["ATL",1135],["LAX",1810]],
                   1776:[["PHL",1350],["RAP",1610]],
                   1226:[["PHX",950],["MDW",1345]],
                   1885:[["ATL",1305],["LAX",2000]],
                   1009:[["MDW",2250],["IND",2355]],
                   9001:[["MDW",2145],["IND",2255]]},
          "Southwestern":{1111:[["SAT",430],["MDW",825]],
                          2121:[["MDW",430],["SAT",825]],
                          4335:[["PHX",450],["MDW",745]],
                          1102:[["MDW",1100],["PHX",1450]]},
          "American":{7765:[["IND",1850],["CHA",2105]],
                   2133:[["BNA",900],["IND",1115]],
                   3321:[["HOU",1335],["ATL",1615]],
                   2100:[["BNA",900],["IND",1115]],
                   4311:[["HOU",905],["ATL",1255]],
                   5577:[["ATL",1100],["HOU",1350]],
                   1102:[["BNA",1100],["HOU",1450]]}}



#L11-1 Write a function def printAirlines(airD): that will print out
#the names of all of the airlines in the dictionary in sorted order(5 points)
def printAirlines(airD):
    for airline, values in sorted(airD.items()):
        print(airline)


#L11-2 Write a function def printAirlinesWithFlight(airD,withFlight): that will
#print out the names of all of the airlines in the dictionary with a
#specified flight number (e.g. 1102) (5 points)
def printAirlinesWithFlight(airD,withFlight):
    for airline, values in sorted(airD.items()):
        for flightNum, moreValues in values.items():
            print("%s %s\n" % (airline, flightNum))
            break


#L11-3 Write a function def printAirlineFlightNums(airD): that will
#print out the names of all of the airlines along with the flight numbers
#for all flights for that airline, flights in sorted order (10 points)
def printAirlineFlightNums(airD):
    for airline, values in airD.items():
        for flightNum, moreValues in sorted(values.items()):
            print("%s %s\n" % (airline, flightNum))


#L11-4 Write a function def printAirlineFlightsDepartFrom(airD,fromCity):
#that will print all Airlines and the flights from that airline that depart
#from a specified city (10 points)
def printAirlineFlightsDepartFrom(airD,fromCity):
    for airline, values in sorted(airD.items()):
        for flightNum, moreValues in sorted(values.items()):
            if moreValues[0][0] == fromCity:
                print("%s %s\n" % (airline, flightNum))


#L11-5 Write a function def printAirlinesSortedFlightNumsSorted(airD): that will
#print out the names of all of the sorted airlines along with the flight numbers
#for all flights for that airline, but with the flights in sorted order per
#airline (10 points)
def printAirlineFlightNumsSorted(airD):
    for airline, values in sorted(airD.items()):
        for flightNum, moreValues in sorted(values.items()):
            print("%s %s\n" % (airline, flightNum))


#L11-6 Write a function def printAirlinesFlightInfo(airD): that will
#print out the names of all of the airlines along with the flight numbers,
#departure city and time, and arrival city and time for all flights for
#that airline.  Be sure the time is formatted in civilian time (am or pm)
#(10 points).  You should write a "milToCivil(tm)" function that takes a
#military time as an argument and returns the civilian time equivalent.
def milToCivil(tm):
    if tm > 1259:
        newTime = tm - 1200
        return newTime
    return tm

def printAirlinesFlightInfo(airD):
    for airline, values in sorted(airD.items()):
        for flightNum, moreValues in sorted(values.items()):
            arrival = milToCivil(moreValues[0][1])
            depart = milToCivil(moreValues[1][1])
            print("%s %s %s %i %s %i\n" % (airline, flightNum, moreValues[0][0], arrival, moreValues[1][0], depart))


#L11-7 Write a function def printSelectedFlight(airD,airline,flightNum):
#that will print out the departure city and time, and arrival city and time
#for the specified flight for the specified airline.  Be sure the time is
#formatted in civilian time(am or pm) (10 points)
def printSelectedFlight(airD,airline,flightNum):
    for airlineKey, values in sorted(airD.items()):
        for flightNumKey, moreValues in sorted(values.items()):
            if airline == airlineKey and flightNum == flightNumKey:
                arrival = milToCivil(moreValues[0][1])
                depart = milToCivil(moreValues[1][1])
                print("%s %s %s %i %s %i\n" % (airline, flightNum, moreValues[0][0], arrival, moreValues[1][0], depart))

#L11-8 Write a function def findFlight(airD,fromCity,toCity): that will
#print out all Airlines and flight numbers and times which match the specified
#fromCity/toCity parameters.  Within Airlines, sort the flights by departure
#time (10 points)
def findFlight(airD,fromCity,toCity):
    for airline, values in sorted(airD.items()):
        for flightNum, moreValues in sorted(values.items()):
            if moreValues[0][0] == fromCity and moreValues[1][0] == toCity:
                arrival = milToCivil(moreValues[0][1])
                depart = milToCivil(moreValues[1][1])
                print("%s %s %s %i %s %i\n" % (airline, flightNum, moreValues[0][0], arrival, moreValues[1][0], depart))


def main():
    test=[1,2,3,4,5,6,7,8]
    for index in test:
        print("TEST",index)
        if index==1:
            printAirlines(flightsD)
        elif index==2:
            printAirlinesWithFlight(flightsD,1102)
        elif index==3:
            printAirlineFlightNums(flightsD)
        elif index==4:
            printAirlineFlightsDepartFrom(flightsD,"IND")
        elif index==5:
            printAirlineFlightNumsSorted(flightsD)
        elif index==6:
            printAirlinesFlightInfo(flightsD)
        elif index==7:
            printSelectedFlight(flightsD,"Delta",1776)
        elif index==8:
            findFlight(flightsD,"MDW","IND")
        print()

main()
