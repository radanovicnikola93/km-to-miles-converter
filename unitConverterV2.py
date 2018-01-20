# /usr/bin/env python
# -*- coding: utf-8 -*-

print "Hi! :) This is a unit converter that convertes kilometres to miles."
print ''

while True:
    print "Enter a number of kilometers that you'd like to convert into miles. Enter only numbers!"
    km = float(raw_input("Kilometres: "))
    miles = km * 0.621371
    print("%s km is %s miles.") % (km, miles)

    question = raw_input("Would you like to convert km to miles again? Y/N")

    if question.upper() != "Y" and question.upper() != "YES":
        print("Thank you and goodbye!")
        break

