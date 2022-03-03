date1 = (input("Enter a date (mmddyyyy): "))
#date1 = str(date)
res = ''
if date1[0] == '0' and date1[1] == '1':
    res = "January " + date1[2:4] + ", " + date1[4:]
elif date1[0:2] == '02':
    res = "February " + date1[2:4] + ", " + date1[4:]
elif date1[0:2] == '03':
    res = "March " + date1[2:4] + ", " + date1[4:]
elif date1[0:2] == '04':
    res = "April " + date1[2:4] + ", " + date1[4:]
elif date1[0:2] == '05':
    res = "May " + date1[2:4] + ", " + date1[4:]
elif date1[0:2] == '06':
    res = "June " + date1[2:4] + ", " + date1[4:]
elif date1[0:2] == '07':
    res = "July " + date1[2:4] + ", " + date1[4:]
elif date1[0:2] == '08':
    res = "August " + date1[2:4] + ", " + date1[4:]
elif date1[0:2] == '09':
    res = "September " + date1[2:4] + ", " + date1[4:]
elif date1[0:2] == '10':
    res = "October " + date1[2:4] + ", " + date1[4:]
elif date1[0:2] == '11':
    res = "November " + date1[2:4] + ", " + date1[4:]
elif date1[0:2] == '12':
    res = "December " + date1[2:4] + ", " + date1[4:]
else:
    res = "Invalid Date"
print("Date: ", res)