import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        exit('ValueError')

def convert(s):
    time_result = re.search(r"(\d+)(?::(\d+))? (AM|PM) to (\d+)(?::(\d+))? (AM|PM)",s)

    if time_result:

        temp = list(time_result.groups())

        time_12=[]

        for t in temp:
            if t == None:
                time_12.append('00')
            else:
                time_12.append(t)

        if int(time_12[0])<0 or int(time_12[0])>12:
            raise ValueError
        elif int(time_12[3])<0 or int(time_12[3])>12:
            raise ValueError

        if int(time_12[1])<0 or int(time_12[1])>59:
            raise ValueError
        elif int(time_12[4])<0 or int(time_12[4])>59:
            raise ValueError

        if time_12[2] == 'AM' and str(time_12[0]) == '12':
            time_12[0]='00'
        if time_12[5] == 'AM' and str(time_12[3]) == '12':
            time_12[3] = '00'

        if time_12[2] == 'PM' and str(time_12[0]) != '12':
            time_12[0]=int(time_12[0])+12
        if time_12[5] == 'PM' and str(time_12[3]) != '12':
            time_12[3]=int(time_12[3])+12

        time_24=[time_12[0],time_12[1],time_12[3],time_12[4]]


        time=f'{str(time_24[0]).zfill(2)}:{str(time_24[1]).zfill(2)} to {str(time_24[2]).zfill(2)}:{str(time_24[3]).zfill(2)}'
        return time

    else:
        raise ValueError


if __name__ == "__main__":
    main()