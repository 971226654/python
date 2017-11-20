Days = "星期日星期一星期二星期三星期四星期五星期六"
s1 = input("")
s2 = int(s1)
DayAbbrev = Days[s2*3:(s2+1)*3]
print("{}".format(DayAbbrev))