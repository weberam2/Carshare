#!/usr/bin/python3

import sys
import math

#Evo
#0.41 per minute up to and incl 36 mins (which you probably won't need)
#14.99 per hour up to 6 hours
#89.99 after 6hrs

#MODO
#0.4 for first 25k
#0.28 for every km after
#4 per hour

#sys.argv[1] = distance
#sys.argv[2] = time in hours

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

twentyfour = math.floor(num2/24)
twentyfourrem = num2 % 24

#print("twentyfourrem,", twentyfourrem)
#print("twentyfour,", twentyfour)

print("Total distance in kms", sys.argv[1])
print("Total time in hours", sys.argv[2])

print("Evo will come out to:")
if (num2 < 6):
	evocost = 14.99*num2
elif (num2 < 24):
	evocost = 89.99
else:
	#print(twentyfourrem)
	if (twentyfourrem < 6):
		evocost = twentyfour*89.99 + twentyfourrem*14.99
	else:
		evocost = (twentyfour+1)*89.99
	
print(round(evocost,2))

print("Modo will come out to:")
if (num2 < 13):
	modotcost = 4*num2
elif (num2 < 24):
	modotcost = 48
else: 
	if (twentyfourrem < 13):
		modotcost = twentyfour*48 + twentyfourrem*4
	else:
		modotcost = (twentyfour+1)*48

twentyfive = math.floor(num1/25)
twentyfiverem = num1 % 25

#print("twentyfive,", twentyfive)
#print("twentyfiverem,", twentyfiverem)

mododcost = twentyfive*25*0.4 + twentyfiverem*0.28

modocost = modotcost + mododcost

print("Time:", modotcost, "+ Distance:", round(mododcost,2), " = ", modocost)

if evocost < modocost:
	print("\nYou should go with Evo")
else:
	print("\nYou should go with Modo, bro")