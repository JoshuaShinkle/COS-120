#L13-1
def divideWithSubtraction(num, denom, quotient):
    if num < denom:
        return quotient
    else:
        num -= denom
        quotient += 1
        print("Recursion New Parameters-> (" + str(num) + "," + str(denom) + ") and Quotient = " + str(quotient)) 
        return divideWithSubtraction(num, denom, quotient)

print("L13-1")
quotient = 0
print("Final Result-> " + str(divideWithSubtraction(22, 7, quotient)))
print()

#L13-2
def modulusWithSubtraction(num, denom):
    if num - denom < denom:
        remainder = num - denom
        return remainder
    else:
        num -= denom
        print("Recursion New Parameters-> (" + str(num) + "," + str(denom) + ")") 
        return modulusWithSubtraction(num, denom)

print("L13-2")
print("Remainder-> " + str(modulusWithSubtraction(28, 7)))
print()

#L13-3
class Time:
    def __init__(self, hours, minutes, seconds):
        if hours >= 0 and hours <= 23:
            self.hours = hours
        else:
            self.hours = 0

        if minutes >= 0 and minutes <= 59:
            self.minutes = minutes
        else:
            self.minutes = 0

        if seconds >= 0 and seconds <= 59:
            self.seconds = seconds
        else:
            self.seconds = 0

    #L13-4
    def getTime(self):
        if len(str(self.hours)) != 2:
            self.hours = "0" + str(self.hours)

        if len(str(self.minutes)) != 2:
            self.minutes = "0" + str(self.minutes)

        if len(str(self.seconds)) != 2:
            self.seconds = "0" + str(self.seconds)

        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    #L13-5
    def getCivilianTime(self):
        ampm = "AM"
        if self.hours > 12:
            ampm = "PM"
            self.hours -= 12

        if len(str(self.hours)) != 2:
                    self.hours = "0" + str(self.hours)

        if len(str(self.minutes)) != 2:
            self.minutes = "0" + str(self.minutes)

        if len(str(self.seconds)) != 2:
            self.seconds = "0" + str(self.seconds)

        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds) + " " + ampm
    
    #L13-6
    def getHours(self):
        return self.hours
    
    def getMinutes(self):
        return self.minutes
    
    def getSeconds(self):
        return self.seconds
    
    #L13-7
    def setHours(self, newHours):
        if newHours >= 0 and newHours <= 23:
            self.hours = newHours
    
    def setMinutes(self, newMinutes):
        if newMinutes >= 0 and newMinutes <= 23:
            self.minutes = newMinutes
    
    def setSeconds(self, newSeconds):
        if newSeconds >= 0 and newSeconds <= 23:
            self.seconds = newSeconds

    #L13-8
    def incrementTime(self):
        if self.seconds + 1 == 60:
            self.seconds = 0
            if self.minutes + 1 == 60:
                self.minutes = 0
                if self.hours + 1 == 24:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

    #L13-10
    def timeDiff(self, time):
        difference = []
        hourDiff = abs(self.hours - time.hours)
        minuteDiff = abs(self.minutes - time.minutes)
        secondDiff = abs(self.seconds - time.seconds)
        difference.append(hourDiff)
        difference.append(minuteDiff)
        difference.append(secondDiff)
        return difference

print("L13-11")
print("L13-3")
time = Time(12,12,12)
print(time.getTime())
time = Time(55,70,80)
print(time.getTime())
print()

print("L13-4")
time = Time(9,3,3)
print(time.getTime())
print()
time = Time(12,12,12)
print(time.getTime())
print()

print("L13-5")
time = Time(21,33,33)
print(time.getCivilianTime())
print()
time = Time(9,3,3)
print(time.getCivilianTime())
print()

print("L13-6")
time = Time(9,3,3)
print(time.getHours())
print(time.getMinutes())
print(time.getSeconds())
print()

print("L13-7")
time = Time(9,3,3)
time.setHours(12)
time.setMinutes(12)
time.setSeconds(12)
print(time.getHours())
print(time.getMinutes())
print(time.getSeconds())
print()

print("L13-8")
time = Time(23,59,58)
time.incrementTime()
print(time.getTime())
print()
time = Time(23,2,59)
time.incrementTime()
print(time.getTime())
print()
time = Time(2,59,59)
time.incrementTime()
print(time.getTime())
print()
time = Time(23,59,59)
time.incrementTime()
print(time.getTime())
print()

print("L13-10")
time = Time(23,24,24)
time2 = Time(12,12,12)
print(time.timeDiff(time2))
print()
time = Time(3,2,2)
time2 = Time(10,12,12)
print(time.timeDiff(time2))
print()