class user(object):
    # 初始化
    def __init__(self,name):
        self.name = name

    #　信息录入功能
    def AddInfo(self):
        self.name = str(input("请输入名字："))
        PhoneNum = input("请输入电话号码：")
        age = input("请输入年龄：")
        address = str(input("请输入地址："))
        Email = str(input("请输入电子邮箱："))
        remarks = str(input("请输入备注："))
        with open("AddressBook.txt","a+") as file:
            file.write(self.name + " ")
            file.write(PhoneNum + " ")
            file.write(age + " ")
            file.write(address + " ")
            file.write(Email + " ")
            file.write(remarks + "\n")
        print("录入成功")

    # 信息浏览功能
    def ReadInfo(self):
        print("通讯录的所有信息为：")
        with open("AddressBook.txt","r") as file:
            line = file.readlines()
            for li in line:
                li = li.split(" ")      # 切片，去除空格，返回list类型的数据
                print("{:30}".format("姓名") + "{:30}".format("电话号码") + 
                        "{:30}".format("年龄") + "{:30}".format("地址") + 
                        "{:30}".format("电子邮件") + "{:30}".format("备注")
                     )
                print("{:30}".format(li[0]) + "{:30}".format(li[1]) + 
                    "{:30}".format(li[2]) + "{:30}".format(li[3]) + 
                    "{:30}".format(li[4]) + "{:30}".format(li[5]))

    
    # 信息查询功能
    def FindInfo(self):
        name = str(input("请输入要查询的姓名："))
        with open("AddressBook.txt","r") as file:
            line = file.readlines()
            for li in line:
                li = li.split(" ")     # 切片，去除空格，返回list类型的数据
                if name == li[0]:
                    print("查询的信息如下：")
                    print("{:30}".format("姓名"),"{:30}".format("电子号码"),
                    "{:30}".format("年龄"),"{:30}".format("地址"),
                    "{:30}".format("电子邮件"),"{:30}".format("备注"))
                    print("{:30}".format(li[0]),"{:30}".format(li[1]),
                    "{:30}".format(li[2]),"{:30}".format(li[3]),
                    "{:30}".format(li[4]),"{:30}".format(li[5]))
                    return   # 退出函数，不执行下面的内容
            
        print("通讯录中没有该用户的信息")
            
    # 信息修改功能
    def ModifyInfo(self):
        name = str(input("请输入要修改的联系人的姓名："))
        with open("AddressBook.txt","r") as file:
            line = file.readlines()
            for li in line:
                li = li.split(" ")   # 切片
                if li[0] == name:
                    print("目前该联系人的信息如下：")
                    print("{:30}".format("姓名"),"{:30}".format("电子号码"),
                    "{:30}".format("年龄"),"{:30}".format("地址"),
                    "{:30}".format("电子邮件"),"{:30}".format("备注"))
                    print("{:30}".format(li[0]),"{:30}".format(li[1]),
                    "{:30}".format(li[2]),"{:30}".format(li[3]),
                    "{:30}".format(li[4]),"{:30}".format(li[5]))
                    
                    print("请输入要修改的内容：")
                    name = str(input("姓名:"))
                    PhoneNum = input("电子号码：")
                    age = input("年龄：")
                    address = input("地址：")
                    email = input("电子邮件：")
                    remarks = input("备注：")
                    
                    name = name + " "
                    PhoneNum = PhoneNum + " "
                    age = age + " "
                    address = address + " "
                    email = email + " "
                    remakrs = remarks 

                    # 文件指向修改的那行，可以向改行写入，覆盖该内容
                    with open("AddressBook.txt","w") as f:
                        f.write(name + PhoneNum + age + address + email + remarks + "\n")
                    
                    print("修改过后的该联系人的信息为：")
                    
                    self.ReadInfo()

                    return
        print("通讯录中没有该用户的信息")
            

    
    # 信息删除功能
    def DeleteInfo(self):
        name = input("请输入要删除信息的联系人的名字：")
        with open("AddressBook.txt","r") as file:
            for li in file.readlines():
                li = li.split(" ")
                if li[0] == name:
                    print("该联系人的信息为：")
                    print("{:30}".format("姓名"),"{:30}".format("电子邮件"),
                    "{:30}".format("年龄"),"{:30}".format("地址"),"{:30}".format("电子邮件"),"{:30}".format("备注"))
                    print("{:30}".format(li[0]),"{:30}".format(li[1]),
                    "{:30}".format(li[2]),"{:30}".format(li[3]),"{:30}".format(li[4]),"{:30}".format(li[5]))
                    li = ""
                    with open("AddressBook.txt","w") as f:
                        f.write(li) 
                    print("修改成功")
                    return
        print("通讯录中没有该用户的信息")

        
    
    # 信息排序功能
    def SortInfo(self):
        pass
        
if __name__ == '__main__':
    pass