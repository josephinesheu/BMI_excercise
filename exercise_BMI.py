height = input('請輸入身高(cm): ')
height = float(height)
weight = input('請輸入體重(kg): ')
weight = float(weight)
height=height/100 #換成公尺
BMI= weight/height/height
BMI= float(BMI)
print('你的BMI為:', BMI)
if BMI < 18.5: 
    print('你的BMI屬於體重過輕')
elif BMI >= 18.5 and BMI < 24:
    print('你的BMI屬於正常範圍')
elif BMI >= 24 and BMI < 27:
	print('你的BMI屬於過重')
elif BMI >= 27 and BMI < 30:
	print('你的BMI屬於輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('你的BMI屬於中度肥胖')
elif BMI >= 35:
	print('你的BMI屬於重度肥胖')




