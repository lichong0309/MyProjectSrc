import sys  # 退出程序
import os
from function import user

def menu():
    print("=========================================")
    print("        通讯录管理系统")
    print("             1、信息录入")
    print("             2、信息浏览")
    print("             3、信息查询")
    print("             4、信息修改")
    print("             5、信息删除")
    print("             6、系统退出")
    print("=========================================")
   

def verification():
    i = "i"
    while(i != "exit"):   # 当i是”exit"时退出循环
        log = login()   # 验证返回值，一个是boolean值，一个是用户输入的名字
        
        if log[0] == "True":
            menu()   
            SelectionFunction(log[1])

        else:
            i = input("用户名和密码不匹配，请按下任意键重新输入或者输入exit退出")
            
            if i == "exit":
                try:
                    sys.exit(0)    # 可以捕获退出发生的错误
                except:
                    print("Program is dead")
                finally:
                    print("Clean-up")

    
# 登录
def login():
    print("=========================================")
    UserName = str(input("UserName:"))
    Password = str(input("Password:"))
    # 打开文件
    with open("UsernamePassword.txt","r") as file:
        line = file.readlines()
        for li in line:
            li = li.split(" ")    # 切片，去除读取一行文件中的空格，返回类型为list
            li[0] = str(li[0])
            li[1] = str(li[1]) 
            
            if UserName == li[0] and Password == li[1]:
                return "True", UserName
    
    # 密码或用户名输出错误
    return "False", UserName
                
# 选择功能界面
def SelectionFunction(name):
    SelectionNum = list(range(1,8))
    a = 0
    while(a != 6):
        while(1):
            a = int(input("请输入要进行的操作："))
            if a in SelectionNum:
                break
        function = user(name)  # 实例化类user

        if a == 1:
            function.AddInfo()
        if a == 2:
            function.ReadInfo()
        if a == 3:
            function.FindInfo()
        if a == 4:
            function.ModifyInfo()
        if a == 5:
            function.DeleteInfo()
        if a == 6:
            try:
                print("程序退出成功")
                os._exit(0)
                
            except:
                print("Program is dead")
            

if __name__ == '__main__':
    verification()  
