n = 0
while n < 15:
    print("Oh ya!!!!")
    n = n+1
print("看到你太開心了啦")  
print("小哥哥小姊姊你好!我叫做模擬卡!我是你的聊天機器人")
skill = ("我可以陪你聊天～什麼話題都可以哦～")
print(skill)
name = input("阿忘了問你名字!你叫什麼名字啊?:")
print("我叫", name)
print("哈囉",name, "很高興能成為你的朋友")
#
country = input("你喜歡去哪個國家玩啊?：")
print("哦～原來你喜歡",country)
print("好剛好哦～我也喜歡誒～")
文化 = input("那你喜歡那裡的什麼文化啊?:")
print("我也喜歡", 文化)
print("我也是因為這個文化才深深喜歡上這個國家")
#
food= input("那你喜歡那裡的什麼食物啊？")
print("我也喜歡吃",food)
份=int(input("那你都吃幾份？:"))
print("吃好多喔～")
kg=int(input("那你現在幾公斤？"))
kg = int(kg)
kgs = 70-kg
print("我再",kgs,"就要70了!")
#
print("那我順便來幫你檢測一下BMI!")
w = float(input("請輸入您的體重?(kg)"))
h = float(input("請輸入您的身高?(m)"))

bmi = w/(h*h)
print("您的bmi為" , bmi)
if bmi < 18:
    print("體重過輕")
elif bmi < 24:
    print("體重正常 你真棒!")
elif bmi <27:
    print("體重過重")
else:
    print("體重肥胖 吃太多摟!")
print("阿對了！趁暑假我們一起去",country,"吧")