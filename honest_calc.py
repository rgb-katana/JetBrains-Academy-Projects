msgs = {"msg_0": "Enter an equation",
        "msg_1": "Do you even know what numbers are? Stay focused!",
        "msg_2": "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "msg_3": "Yeah... division by zero. Smart move...",
        "msg_4": "Do you want to store the result? (y / n):",
        "msg_5": "Do you want to continue calculations? (y / n):",
        "msg_6": " ... lazy",
        "msg_7": " ... very lazy",
        "msg_8": " ... very, very lazy",
        "msg_9": "You are",
        "msg_10": "Are you sure? It is only one digit! (y / n)",
        "msg_11": "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "msg_12": "Last chance! Do you really want to embarrass yourself? (y / n)"
        }
good = {"+", "-", "*", "/"}
memory = 0
result = 0


def number(a):
    global memory
    if a == "M":
        a = memory
        return a
    elif not a.isalpha():
        return float(a)
    else:
        return "Not good."


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msgs["msg_6"]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msgs["msg_7"]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msgs["msg_8"]
    if msg != "":
        msg = msgs["msg_9"] + msg
        print(msg)


def calculator_loop():
    calc = input(msgs["msg_0"]).split()
    x = calc[0]
    oper = calc[1]
    y = calc[2]
    global memory
    global result
    x = number(x)
    y = number(y)
    if x != "Not good." and y != "Not good.":
        if oper in good:
            check(v1=float(x), v2=float(y), v3=oper)
            if oper == "+":
                result = (x + y)
                print(result)
            elif oper == "-":
                result = (x - y)
                print(result)
            elif oper == "*":
                result = (x * y)
                print(result)
            elif oper == "/" and int(y) != 0:
                result = (x / y)
                print(result)
            else:
                print(msgs["msg_3"])
                calculator_loop()
        else:
            print(msgs["msg_2"])
            calculator_loop()
    else:
        print(msgs["msg_1"])
        calculator_loop()


def checker():
    msg_index = 10
    while True:
        third_choice = input(msgs[f"msg_{msg_index}"])
        if third_choice == "y":
            if msg_index < 12:
                msg_index += 1
            else:
                return True
        elif third_choice == "n":
            return "Not in memory."
        else:
            continue


def second_part():
    global memory
    global result
    first_choice = input(msgs["msg_4"])
    if first_choice == "y":
        if is_one_digit(float(result)):
            if checker() == "Not in memory.":
                memory = memory
            else:
                memory = result
                return
        else:
            memory = result
    elif first_choice == "n":
        memory = 0
    else:
        second_part()


def third_part():
    second_choice = input(msgs["msg_5"])
    if second_choice == "y":
        return True
    elif second_choice == "n":
        return False
    else:
        third_part()


calculator_loop()
second_part()
while third_part():
    calculator_loop()
    second_part()
