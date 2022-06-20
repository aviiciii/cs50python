from datetime import date
import inflect
import sys
import re

def main():
    inpt=input('Date of Birth: ')
    print(get_min(inpt))


def get_min(inpt):

    # gets dates from input using regex
    if search := re.search(r'^(\d{4})-(\d{2})-(\d{2})$',inpt):
        inpt=list(search.groups())
    else:
        sys.exit('Invalid date')

    # converts str into int and checks valid date
    inpt_bday = convert_and_check(inpt)

    # today's date
    today = date.today()

    # bday
    bday = date(inpt_bday[0], inpt_bday[1], inpt_bday[2])

    # computes no of days
    diff = bday - today
    no_of_days = -int(diff.days)

    # computes days into minutes
    minutes = no_of_days * 24 * 60

    # converts into words
    inf = inflect.engine()
    min_words = inf.number_to_words(minutes)

    # remove 'and' and capitalize

    min_words = min_words.replace(' and','').capitalize()

    # return
    return min_words + ' minutes'


def convert_and_check(day):
    # convert str to int
    day = list(map(int, day))

    # check valid date and month
    if day[1] < 0 or day[1] > 12:
        sys.exit('Invalid date')

    elif day[2] < 0 or day[2] > 31:
        sys.exit('Invalid date')

    return day



if __name__ == "__main__":
    main()