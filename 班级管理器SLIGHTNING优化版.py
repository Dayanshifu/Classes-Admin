import os
import random as ran
import re

try:
    import easygui as box
except ImportError:
    print("GUI库导入失败，将使用命令行模式")

windowTitle = "little颜の班级管理系统 Powered by Python310"
databaseFile = "database.txt"
admin = ""

def quitIfNone(value):
    if value is None:
        quit()
    return value


def interactyn(msg, choices = ("确定", "取消")):
    try:
        return quitIfNone(box.ynbox(msg, choices = choices, title=windowTitle))
    except Exception:
        reply = input(msg + "(y/n)")
        return reply == "" or reply.lower() == "y" or reply.lower() == "yes"

def interactmsg(msg, ok_button = "确定"):
    try:
        quitIfNone(box.msgbox(msg, ok_button = ok_button, title=windowTitle))
    except Exception:
        input(str(msg) + "，按下回车键" + ok_button)
        
def interactenter(msg):
    try:
        return box.enterbox(msg, title=windowTitle)
    except Exception:
        return input(msg + "：")

def interactbutton(msg, choices):
    try:
        return quitIfNone(box.buttonbox(msg, choices = choices, title=windowTitle))
    except Exception:
        for i in range(len(choices)):
            print(str(i) + ". " + choices[i])
        while True:
            reply = input("请输入你的选择：")
            try:
                return choices[int(reply)]
            except Exception:
                pass

noDatabase = lambda :"database.txt" not in os.listdir()

def writeDatabase(res):
    res["admin"] = admin
    f = open(databaseFile, "w")
    f.write(str(res))
    f.close()
    res.pop("admin")

def readDatabase():
    f = open(databaseFile, "r")
    res = f.read()
    f.close()
    return res

if noDatabase():#检测数据库是否存在
    op = interactyn("系统检测到你的文件目录没有数据库文件（database.txt），是否创建？")
    if op == True:
        f = open(databaseFile, "w")
        f.write("{}")
        f.close()
        interactmsg("创建成功！")
    else:
        #interactmsg("请自行在当前程序所在目录创建database.txt文件)
        quit()
        """
            程序的存在就是为了帮助人执行一些可以自动处理的内容
        """

def loadDatabase():
    res = readDatabase()
    if res == "":
        res = "{}"
        writeDatabase(res)
    res = eval(res)
    return res

#设置admin密码并加密
def setAdmin(res):
    global admin

    if "admin" not in res:
        ans = interactenter("你还没有管理员账号，请输入将要使用的密码")
        code = []
        for w in str(ans):
            num = ord(w)
            code.append(num)
        admin = code
        writeDatabase(res)
        code = admin
        key = ""
        for w in code:
            key = key + str(chr(w))
        interactmsg("请保管好你的管理员密码：" + key)
    else:
        admin = res.pop("admin")


def main():
    global admin

    res = loadDatabase()
    setAdmin(res)

    while True:
        op = interactbutton("选择你要做什么\n"+ str(res), choices=("计分", "随机", "排行榜", "管理", "退出"))
        if op == "计分":
            lst = []
            for l in res:
                lst.append(l)
            tpl = tuple(lst)
            op = interactbutton("选择学生", choices = tpl)
            mk = interactbutton("选择分数",
            choices = ("1","2","3","4","5","-1","-2","-3","-4","-5"))
            res[op] = res[op] + int(mk)
            writeDatabase(res)
            interactmsg("加分成功！\n" + str(res))
        elif op == "管理":
            f = open("database.txt", "r")
            code = eval(f.read())["admin"]
            f.close()
            key = ""
            for w in code:
                key = key + str(chr(w))
            ans = interactenter("请输入管理员密码")
            if ans == key:
                while True:
                    op = interactbutton("选择你要做什么", choices=("添加", "删除", "清空", "重置", "返回"))
                    if op == "添加":
                        ans = interactenter("请输入学生姓名")
                        res[ans] = 0
                        writeDatabase(res)
                        interactmsg("创建成功！\n"+ str(res))
                    elif op == "删除":
                        ans = interactenter("请输入要删除学生姓名\n"+ str(res))
                        if ans not in res:
                            interactmsg("没有找到学生 " + ans)
                            continue
                        if not interactyn("你真舍得删掉该学生吗"):
                            interactmsg("操作已取消")
                            continue
                        res.pop(ans)
                        writeDatabase(res)
                        interactmsg("删除成功！\n"+ str(res))
                    elif op == "清空":
                        if not interactyn("你真舍得清空吗"):
                            interactmsg("操作已取消")
                            continue
                        res.clear()
                        writeDatabase(res)
                        interactmsg("清空成功！\n"+ str(res))
                    elif op == "重置":
                        interactmsg("删除目录下 database.txt 文件即可（三思而后行）")
                    else:
                        break
            else:
                interactmsg("密码错误")
        elif op == "随机":
            op = int(interactbutton("选择人数", choices=("1","2","3","4","5","6","7","8","9","10")))
            lst = []
            for l in res:
                lst.append(l)
            if op > len(lst):
                interactmsg("选择的人数太多")
                continue
            interactmsg(ran.sample(lst, op))
        elif op == "排行榜":
            interactmsg(sorted(res.items(),  key=lambda d:d[1], reverse=True))
            pass
        else:
            break

if __name__ == "__main__":
    main()
