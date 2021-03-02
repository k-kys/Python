from random import *

print("Trò chơi bầu cua")
x = 1
c = 0

while  x==1:
    print("1:Nai")
    print("2:Bầu")
    print("3:Gà")
    print("4:Cá")
    print("5:Cua")
    print("6:Tôm")

    a = int(input("Chọn số: "))
    if a==1:
        print("Người chơi đã chọn Nai")
    elif a==2:
        print("Người chơi đã chọn Bầu")
    elif a==3:
        print("Người chơi đã chọn Gà")
    elif a==4:
        print("Người chơi đã chọn Cá")
    elif a==5:
        print("Người chơi đã chọn Cua")
    elif a==6:
        print("Người chơi đã chọn Tôm")

    b = randint(1, 6)
    d = randint(1, 6)
    f = randint(1, 6)

    if b==1:
        print("Máy đã lắc ra Nai")
    elif b==2:
        print("Máy đã lắc ra Bầu")
    elif b==3:
        print("Máy đã lắc ra Gà")
    elif b==4:
        print("Máy đã lắc ra Cá")
    elif b==5:
        print("Máy đã lắc ra Cua")
    elif b==6:
        print("Máy đã lắc ra Tôm")

    if d==1:
        print("Máy đã lắc ra Nai")
    elif d==2:
        print("Máy đã lắc ra dầu")
    elif d==3:
        print("Máy đã lắc ra Gà")
    elif d==4:
        print("Máy đã lắc ra Cá")
    elif d==5:
        print("Máy đã lắc ra Cua")
    elif d==6:
        print("Máy đã lắc ra Tôm")

    if f==1:
        print("Máy đã lắc ra Nai")
    elif f==2:
        print("Máy đã lắc ra fầu")
    elif f==3:
        print("Máy đã lắc ra Gà")
    elif f==4:
        print("Máy đã lắc ra Cá")
    elif f==5:
        print("Máy đã lắc ra Cua")
    elif f==6:
        print("Máy đã lắc ra Tôm")
if a==b:
    print("Bạn thắng")
else:
    print("Bạn thua")

if a==d:
    print("Bạn thắng")
else:
    print("Bạn thua")

if a==f:
    print("Bạn thắng")
else:
    print("Bạn thua")


c = int(input("Nhập 1 để chơi lại, 2 để thoát !!!"))
print("-------------------------------------------")
if c==1: x=1
else:
    print("Đang thoát...")
break
