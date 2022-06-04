def main():
    in_time = input('What time is it? ').strip()
    time = convert(in_time)
    if 7 <= time and time <= 8:
        print('breakfast time')
    elif 12 <= time and time <= 13:
        print('lunch time')
    elif 18 <= time and time <= 19:
        print('dinner time')



def convert(time):
    if time.rfind('a.m.') != -1:
        time= time[:time.rfind('a')]
        hours, minutes = time.split(':')
        converted_time = float(hours)+(float(minutes)/600)
        return converted_time

    elif time.rfind('p.m.') != -1:
        time= time[:time.rfind('p')]
        hours, minutes = time.split(':')
        converted_time = 12+float(hours)+(float(minutes)/600)
        return converted_time

    else :
        hours, minutes = time.split(':')
        converted_time = float(hours)+(float(minutes)/600)
        return converted_time


if __name__ == "__main__":
    main()