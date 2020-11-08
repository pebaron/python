#!/usr/bin/env python3

import numpy as np
import pandas as pd

CheckSum = np.array([1,3,7,9,1,3,7,9,1,3])
Population = 4000000

def CheckPESEL(PESEL):
    checksum = 0
    for i in range(len(CheckSum)):
        checksum+=CheckSum[i]*int(PESEL[i])
    checksum = (10 - (checksum % 10)) % 10
    if (checksum == int(PESEL[10])):
        return True
    else: 
        return False
print("DEBUG 1")

dates = np.array('1800-01-01', dtype=np.datetime64)
dates = dates + np.arange(365*500 + 121)
print("DEBUG 2")
#dates = pd.date_range(start='1/1/1800', end='1/1/2100')
dates = np.datetime_as_string(dates, unit='D')
dates = np.core.defchararray.replace(dates, '-','')
dates = np.array( dates, dtype=np.int)
#CheckDates = dates
print("DEBUG 3")
dates = np.where( (dates >= 18000000)&(dates <= 18999999), dates-18000000 + 8000, dates) 
dates = np.where( (dates >= 19000000)&(dates <= 19999999), dates-19000000       , dates) 
dates = np.where( (dates >= 20000000)&(dates <= 20999999), dates-20000000 + 2000, dates) 
dates = np.where( (dates >= 21000000)&(dates <= 21999999), dates-21000000 + 4000, dates) 
dates = np.where( (dates >= 22000000)&(dates <= 22999999), dates-22000000 + 6000, dates)
print("DEBUG 4")

#print("Real Date: ", CheckDates[1] , " Pesl Date: ", dates[1])
#print("Real Date: ", CheckDates[50000] , " Pesl Date: ", dates[50000])
#print("Real Date: ", CheckDates[100000] , " Pesl Date: ", dates[100000])
#print("Real Date: ", CheckDates[70000] , " Pesl Date: ", dates[70000])
#print("Real Date: ", CheckDates[150000] , " Pesl Date: ", dates[150000])

RandomPESEL = np.random.choice(dates, Population)
#RandomPESEL = dates[:Population] # here
RandomPESEL = np.array( RandomPESEL, dtype=np.str)
RandomPESEL = np.where( np.char.str_len(RandomPESEL) == 3, np.char.add('000',RandomPESEL) , RandomPESEL)
RandomPESEL = np.where( np.char.str_len(RandomPESEL) == 4, np.char.add('00',RandomPESEL) , RandomPESEL)
RandomPESEL = np.where( np.char.str_len(RandomPESEL) == 5, np.char.add('0',RandomPESEL) , RandomPESEL)

print("DEBUG 5")
Z1 = np.random.randint(0,9,size=Population)
Z2 = np.random.randint(0,9,size=Population)
Z3 = np.random.randint(0,9,size=Population)
X4 = np.random.randint(0,9,size=Population)
Z1 = np.array( Z1, dtype=np.str)
Z2 = np.array( Z2, dtype=np.str)
Z3 = np.array( Z3, dtype=np.str)
X4 = np.array( X4, dtype=np.str)
RandomPESEL = np.char.add(RandomPESEL,Z1)
RandomPESEL = np.char.add(RandomPESEL,Z2)
RandomPESEL = np.char.add(RandomPESEL,Z3)
RandomPESEL = np.char.add(RandomPESEL,X4)
print("DEBUG 6")


Digit1 = np.array(RandomPESEL.view('<U1').reshape(RandomPESEL.shape + (-1,))[..., 0], dtype=np.int)
Digit2 = np.array(RandomPESEL.view('<U1').reshape(RandomPESEL.shape + (-1,))[..., 1], dtype=np.int)
Digit3 = np.array(RandomPESEL.view('<U1').reshape(RandomPESEL.shape + (-1,))[..., 2], dtype=np.int)
Digit4 = np.array(RandomPESEL.view('<U1').reshape(RandomPESEL.shape + (-1,))[..., 3], dtype=np.int)
Digit5 = np.array(RandomPESEL.view('<U1').reshape(RandomPESEL.shape + (-1,))[..., 4], dtype=np.int)
Digit6 = np.array(RandomPESEL.view('<U1').reshape(RandomPESEL.shape + (-1,))[..., 5], dtype=np.int)
Digit7 = np.array(RandomPESEL.view('<U1').reshape(RandomPESEL.shape + (-1,))[..., 6], dtype=np.int)
Digit8 = np.array(RandomPESEL.view('<U1').reshape(RandomPESEL.shape + (-1,))[..., 7], dtype=np.int)
Digit9 = np.array(RandomPESEL.view('<U1').reshape(RandomPESEL.shape + (-1,))[..., 8], dtype=np.int)
Digit10 = np.array(RandomPESEL.view('<U1').reshape(RandomPESEL.shape + (-1,))[..., 9], dtype=np.int)
print("DEBUG 7")
#print("Digit1 : ",  Digit1)
#print("Digit2 : ",  Digit2)
#print("Digit3 : ",  Digit3)
#print("Digit4 : ",  Digit4)
#print("Digit5 : ",  Digit5)
#print("Digit6 : ",  Digit6)
#print("Digit7 : ",  Digit7)
#print("Digit8 : ",  Digit8)
#print("Digit9 : ",  Digit9)
#print("Digit10: " , Digit10)
#

SumDigit1 = Digit1  * CheckSum[0]
SumDigit2 = Digit2  * CheckSum[1]
SumDigit3 = Digit3  * CheckSum[2]
SumDigit4 = Digit4  * CheckSum[3]
SumDigit5 = Digit5  * CheckSum[4]
SumDigit6 = Digit6  * CheckSum[5]
SumDigit7 = Digit7  * CheckSum[6]
SumDigit8 = Digit8  * CheckSum[7]
SumDigit9 = Digit9  * CheckSum[8]
SumDigit10 = Digit10 * CheckSum[9]
print("DEBUG 8")
#print("Digit1 : ",  Digit1)
#print("Digit2 : ",  Digit2)
#print("Digit3 : ",  Digit3)
#print("Digit4 : ",  Digit4)
#print("Digit5 : ",  Digit5)
#print("Digit6 : ",  Digit6)
#print("Digit7 : ",  Digit7)
#print("Digit8 : ",  Digit8)
#print("Digit9 : ",  Digit9)
#print("Digit10: " , Digit10)

LastDigit = np.array(SumDigit1 + SumDigit2 + SumDigit3 + SumDigit4 + SumDigit5 + SumDigit6 + SumDigit7 + SumDigit8 + SumDigit9 + SumDigit10)
LastDigit = (10 - (LastDigit % 10)) % 10
LastDigitString = np.array( LastDigit, dtype=np.str)
#print("Last: ", LastDigitString[0])
RandomPESEL = np.char.add(RandomPESEL,LastDigitString)
RandomPESEL = np.unique(RandomPESEL)
#print(RandomPESEL[100])
#print(CheckPESEL(RandomPESEL[100]))
Vibration = np.array(Digit1 + Digit2 + Digit3 + Digit4 + Digit5 + Digit6 + Digit7 + Digit8 + Digit9 + Digit10)
VibrationString = np.array(Vibration, dtype=np.str)
print(VibrationString.shape)
print("DEBUG 9")
VibrationString1 = VibrationString[ np.char.str_len(VibrationString) == 1]
VibrationString2 = VibrationString[ np.char.str_len(VibrationString) == 2]

Vibration1 = np.array(VibrationString1, dtype=np.int)

VibDigit1 = np.array(VibrationString2.view('<U1').reshape(VibrationString2.shape + (-1,))[..., 0], dtype=np.int)
VibDigit2 = np.array(VibrationString2.view('<U1').reshape(VibrationString2.shape + (-1,))[..., 1], dtype=np.int)

Vibration2 = VibDigit1 + VibDigit2

from matplotlib import pyplot as plt
print("DEBUG 10")
plt.hist(np.append(Vibration2, Vibration1)) 
print("DEBUG 11")
plt.xlabel("Vibration of PESEL")
plt.ylabel("Number of PESELs")
plt.title("Vibration distribution of PESEL number from years 1800-2299")
plt.show()