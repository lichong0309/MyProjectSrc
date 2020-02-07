# 参考连接：
# “答案正确”是自动判题系统给出的最令人欢喜的回复。本题属于 PAT 的“答案正确”大派送 —— 
# 只要读入的字符串满足下列条件，系统就输出“答案正确”，否则输出“答案错误”。

# 得到“答案正确”的条件是：

# 字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；
# 任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
# 如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。
# 现在就请你为 PAT 写一个自动裁判程序，判定哪些字符串是可以获得“答案正确”的。

# 输入格式：
# 每个测试输入包含 1 个测试用例。第 1 行给出一个正整数 n (<10)，是需要检测的字符串个数。接下来每个字符串占一行，字符串长度不超过 100，且不包含空格。

# 输出格式：
# 每个字符串的检测结果占一行，如果该字符串可以获得“答案正确”，则输出 YES，否则输出 NO。

# 输入样例：
# 8
# PAT
# PAAT
# AAPATAA
# AAPAATAAAA
# xPATx
# PT
# Whatever
# APAAATAA
# 输出样例：
# YES
# YES
# YES
# YES
# NO
# NO
# NO
# NO

def judge(InputString):

    P_pre = 0 
    T_pre = 0
    P_flag = 0
    T_flag = 0
    for s in InputString:
        # 当字符串中有其他的字符串的时候
        if s != "P" and s !="T" and s !="A":
            OutString = "NO"
            return OutString

        # 当字符串中只有P、A、T的时候
        else:
            for i in range(len(InputString)):
                if InputString[i] == "P":
                    P_flag = i      # 记录P字符第一次出现的地方
                    P_pre = P_pre + 1       # 记录P字符是否出现，1表示出现
            
                if InputString[i] == "T":
                    T_flag = i      # 记录T字符第一次出现的地方
                    T_pre = T_pre + 1       # 记录T字符是否出现，1表示出现
                    
            # P、T不存在或者多余1个,或者P在T的后面
            if P_pre != 1 or T_pre != 1 or (P_flag > T_flag): 
                OutString = "NO"
                return OutString 

            # 当循环检测除P、T同时存在且只有一个的时候
            else:
               
                # 当P在第一位的时候
                if P_flag == 0:
                    # 形如PAT,PAAT这类的
                    if InputString[P_flag + 1] == "A" and T_flag == (len(InputString) - 1):
                        OutString = "YES"
                        return OutString 
                    else:
                        OutString = "NO"
                        return OutString
               
                # 当P不在首位的时候,有结论：len(c) = len(a) * len(b)
                else:
                    InputString = list(InputString)   # 将InputString转换为list
                    # 切片
                    a = InputString[:P_flag]
                    b = InputString[P_flag+1:T_flag]
                    c = InputString[T_flag+1:]
                    
                    if len(c) == len(a) * len(b) :
                        OutString = "YES"
                        return OutString
                    
                    else :
                        OutString = "NO"
                        return OutString
                    

num = int(input())
InputList = []  # 初始化列表，存放输入的字符串

# 输入字符串,存放到列表中
for i in range(num):
    InputString = str(input())
    InputList.append(InputString)

# 循环打印出结果
for i in range(num):
    OutString = judge(InputList[i])
    print(OutString)
