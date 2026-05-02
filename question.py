def calculateyear(age):
    year=2569-int(age);
    return year;
#program start here
a=input("กรุณาใส่ชื่อของคุณ")
print("สวัสดีคุณ" + a )
b=input("คุณอายุเท่าไหร่")
print("อ่อ คุณอายุ "+b+"แล้วหรอคะ")
#คำนวณหาปีเกิด
y=calculateyear(b)
print("คุณเกิดปีพุทธศักราช "+str(y)+" ")