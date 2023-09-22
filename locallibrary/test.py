import datetime as dt


today = dt.date.today()
dayname = today.strftime('%A')
day_list = []
day_list.append(today.strftime("%d/%m/%y")+str(" Today"))
for i in range(1,7):
    newdate = today + dt.timedelta(i)
    day_list.append(newdate.strftime("%d/%m/%y"))
day_dict = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
index = day_dict[dayname]-1

context= {}
Ordered_list = [0,0,0,0,0,0,0]
for i in range(index+1):
    Ordered_list[i] = day_list[index+i]
index += 1
for k in range(0,index-1):
    Ordered_list[index+k] = day_list[k]

context["Monday"] = Ordered_list[0]
context["Tuesday"] = Ordered_list[1]
context["Wednesday"] = Ordered_list[2]
context["Thursday"] = Ordered_list[3]
context["Friday"] = Ordered_list[4]
context["Saturday"] = Ordered_list[5]
context["Sunday"] = Ordered_list[6]

print(context)
