"""这里说的是函数调用的顺序"""

def if_function(condition,true_result,false_result):
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    if condition():
        return true_result()
    else:
        return false_result()

def with_if_function():
    return if_function(condition(),true_result(),false_result()) # 这里先运行形参里的函数，然后再调用if_function函数

def condition():
    return False

def true_result():
    print(1)

def false_result():
    print(2)

def hailstone(n):
    length = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)
        length = length + 1
    print(length)
    return length

if __name__ == "__main__":
    # result = with_if_statement()
    # print(result)
    # result2 = with_if_function()
    # print(result2)
    hailstone(10)