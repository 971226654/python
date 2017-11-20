height = float(input("请输入身高（米）："))
weight = float(input("请输入体重（公斤）："))

bmi = weight/pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))
wto,dom = "",""
if bmi < 18.5:
	wto = "偏瘦"
elif bmi < 25:
	wto = "正常"
elif bmi < 30:
	wto = "偏胖"
else:
	wto = "肥胖"
if bmi < 18.5:
	dom = "偏瘦"
elif bmi < 24:
	dom = "正常"
elif bmi < 28:
	dom = "偏胖"
else:
	dom = "肥胖"
print("BMI指标为：国际'{0}'，国内'{1}'".format(wto,dom))