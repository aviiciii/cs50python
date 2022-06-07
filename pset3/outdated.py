month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        inpt= input('Date: ')
        if inpt[0].isalpha():
            date = inpt.split()
            # put input into list
            if ',' not in date[1]:
                raise Exception
            date[1]= date[1].replace(',','')
            # check valid month
            if date[0] not in month:
                raise Exception
            if int(date[1]) > 31:
                raise Exception
            date_type = 1
            break
        else:
            date = inpt.split('/')
            # check valid date and month
            if int(date[0]) > 12 or int(date[1]) > 31:
                raise Exception
            date_type = 2
            break
    except:
        pass
elif date_type == 1:
    month_no = str(month.index(date[0])+1)
    print(date[2].zfill(4), month_no.zfill(2), date[1].zfill(2), sep='-')

elif date_type == 2:
    print(date[2].zfill(4), date[0].zfill(2), date[1].zfill(2), sep='-')
