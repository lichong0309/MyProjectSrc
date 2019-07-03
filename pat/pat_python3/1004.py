# 1004 成绩排名 (20 分)
# 读入 n（>0）名学生的姓名、学号、成绩，分别输出成绩最高和成绩最低学生的姓名和学号。

# 输入格式：
# 每个测试输入包含 1 个测试用例，格式为

# 第 1 行：正整数 n
# 第 2 行：第 1 个学生的姓名 学号 成绩
# 第 3 行：第 2 个学生的姓名 学号 成绩
#   ... ... ...
# 第 n+1 行：第 n 个学生的姓名 学号 成绩
# 其中姓名和学号均为不超过 10 个字符的字符串，成绩为 0 到 100 之间的一个整数，这里保证在一组测试用例中没有两个学生的成绩是相同的。

# 输出格式：
# 对每个测试用例输出 2 行，第 1 行是成绩最高学生的姓名和学号，第 2 行是成绩最低学生的姓名和学号，字符串间有 1 空格。

# 输入样例：
# 3
# Joe Math990112 89
# Mike CS991301 100
# Mary EE990830 95
# 输出样例：
# Mike CS991301
# Joe Math990112

def Sort(dict):
    item = dict.items()      # 将dict内的元素转为元组，返回值类型为list
    # print(item)
    # 将item中的元素变换位置，对应的dict中的key和value交换位置
    for i in item:
        # tuple的元素只可读，不可写，所以这里转换为list
        i = list(i)
        # print(i)
        temp = i[0]
        i[0] = i[1]
        i[1] = temp
        # print(i)
    # item = [ [i[1],i[0]] for i in item]
    # print(item)
    S = sorted(item,reverse = True)
    return S

num = int(input())    
dict = {}         # 创建字典
for i in range(num):
    InputString = str(input())   # 输入字符串
    InputList = InputString.split(" ")      # 去除字符串中的空格部分，返回值类型为list
    InputKey = tuple(InputList[:2])           # python不支持字典的key的类型为list,所以转换为tuple  
    InputValue = int(InputList[2])
    dict[InputKey] = InputValue
   
S = Sort(dict)
print(S[0][0][0] + ' ' + S[0][0][1])
print(S[num - 1][0][0] + " " + S[num-1][0][1])



