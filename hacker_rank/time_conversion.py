#!/bin/python3

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s[0:8]
    am_or_pm = s[8:10]

    if am_or_pm == "PM" and time[0:2] != "12":
        time = time.replace(time[0:2], str(int(time[0:2]) + 12))
    elif am_or_pm == "AM" and time[0:2] == "12":
        time = time.replace(time[0:2], "0" + str(int(time[0:2]) - 12))

    return time
# 오전 12시
# 오후 12시 함정

# 12 -12 하면 0 이라 문자열 00 으로 만들어줘야함
