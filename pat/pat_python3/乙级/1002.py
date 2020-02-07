# 1002 写出这个数
# 读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

# 输入格式：
# 每个测试输入包含 1 个测试用例，即给出自然数 n 的值。这里保证 n 小于 10
# ​100
# ​​ 。

# 输出格式：
# 在一行内输出 n 的各位数字之和的每一位，拼音数字间有 1 空格，但一行中最后一个拼音数字后没有空格。

# 输入样例：
# 1234567890987654321123456789
# 输出样例：
# yi san wu

# import time
# start = time.clock()
a = str(input())     # 转换成str
a = map(int, a)     # 使用map做映射，int转换为list
# 创建字典
dic = {
    1 : "yi",
    2 : "er",
    3 : "san",
    4 : "si",
    5 : "wu",
    6 : "liu",
    7 : "qi",
    8 : "ba",
    9 : "jiu",
    0 : "ling"
}

Sum = 0 
# 计算总和
for i in a:
    Sum = Sum + int(i)    
Sum = str(Sum)    # int转为str

# str转为list
SumList = []
for i in Sum:
    SumList.append(int(i))

p = ''
for s in range(len(SumList)):
    if s == len(SumList) - 1:
        p = p + dic[int(SumList[s])]
    else:
        p = p + dic[int(SumList[s])] + " "
print(p)

# end = time.clock()
# print(end - start)    
