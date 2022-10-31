class_day = "월, 화"
class_day = class_day.replace(" ", "")
days = class_day.split(",")
print(days)

class_date = ""
for day in days:
    print(day)
    if day == "월":
        class_date += "2022-10-31, 2022-11-07, 2022-11-14, 2022-11-21, "
        print("class_date")
        print(class_date)            
    elif day == "화":
        class_date += "2022-11-01, 2022-11-08, 2022-11-15, 2022-11-22, "
    elif day == "수":
        class_date += "2022-11-02, 2022-11-09, 2022-11-16, 2022-11-23, "
    elif day == "목":
        class_date += "2022-11-03, 2022-11-10, 2022-11-17, 2022-11-24, "
    elif day == "금":
        class_date += "2022-11-04, 2022-11-11, 2022-11-18, 2022-11-25, "
    
print("class_date")
print(class_date)