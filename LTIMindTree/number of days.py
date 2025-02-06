def count_days(year,month):
    is_leap= (year % 400 ==0 )or (year % 4 ==0 and year%100 !=0)
    if(month==2):
        return 29 if is_leap else 28
    
    if (month== 1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        return 31
    else:
        return 30
    
year=2012
month=12
days= count_days(year,month)
print(f" number of days is {days}.")