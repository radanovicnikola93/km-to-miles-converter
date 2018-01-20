# /usr/bin/env python
# -*- coding: utf-8 -*-

print "Hi. This is a unit converter. Convertes kilometres to miles."

km = float(raw_input("Please enter km:"))
miles = km * 0.621371

print ("%s is %s miles.") % (km, miles)


while True:
    question = raw_input("Do you want to convert kilometres to miles again? Y/N")

    if question == "Y":
        km = float(raw_input("Please enter km: "))
        miles = "%s is %s miles." % (km, miles)

        print miles

    elif question == "N":
        print ("Thanks for trying the unit converter!")
        break

    else:
        print("Please answer with capitalized Y or N")
