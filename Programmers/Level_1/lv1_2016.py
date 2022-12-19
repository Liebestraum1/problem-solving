#Programmers lv.1, 2016
def solution(a, b):
    month = {1:0, 2: 31, 3: 29, 4: 31, 5:30, 6:31, 7:30, 8:31, 9:31,
          10:30, 11:31, 12:30}
    
    day = {0 : "THU", 1 : "FRI", 2 : "SAT", 3: "SUN",
           4:"MON", 5:"TUE", 6 : "WED"}
    
    for i in range(1, a+1):
        b += month[i]
    return day[b%7]