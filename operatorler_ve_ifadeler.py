hour = int(input("starting time (hours): "))
mins = int(input("starting time (minute): "))
dura = int(input("starting duration (minutes): "))
total_mins = mins+ dura
end_hour = (hour + total_mins // 60) % 24
end_mins = total_mins %60
print(str(end_hour) +":" + str(end_mins))
