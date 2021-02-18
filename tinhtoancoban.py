from IPython.display import clear_output
print("***********TINH TOAN CO BAN*************")

x = []


def inputNum():
    global x
    num = input("Nhap so nguyen: ")
    x.append(num)
    return int(x[-1])


def inputOP():
    op = ''
    while not (op == '+' or op == '-' or op == '*' or op == '/'):
        op = input("Phep tinh: ")
        clear_output()
        if op == "+":
            return lambda num1, num2: num1 + num2
        elif op == "-":
            return lambda num1, num2: num1 - num2
        elif op == "*":
            return lambda num1, num2: num1 * num2
        elif op == "/":
            return lambda num1, num2: num1 / num2


def close():
    return input('Nhap X de dung lai hoac nhan bat ki nut nao de tiep tuc: ').lower().startswith('x')


frst = inputNum()
while True:
    if len(x) % 2 != 0:
        res = inputOP()
        frst = inputNum()
        res2 = res(int(x[0]), int(x[1]))
        x.append(res2)
        x.pop(0)
        x.pop(0)
        print(int(x[0]))
        if not close():
            continue
        else:
            break
