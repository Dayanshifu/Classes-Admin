import os
from sys import *
import time
import random as ran

cmdmod = 0

try:
    import easygui as box
except ImportError:
    cmdmod = 1
    print('必要的运行库未能导入，开启命令行模式')
    sleep = 3
    for i in range(4):
        print('please wait for '+ str(sleep)+'s')
        sleep -= 1
        time.sleep(0.8)

if cmdmod != 1:
    if 'database.txt' not in os.listdir():#检测数据库是否存在
        op = box.ynbox('系统检测到你的文件目录没有 database.txt 文件，是否自动创建？', title='little颜の班级管理系统 Powered by Python310')
        if op == True:
            f = open('database.txt', 'w')
            res = f.write('{}')
            f.close()
            box.msgbox('创建成功！请重新运行本程序', title='little颜の班级管理系统 Powered by Python310')
            quit()
        else:
            box.msgbox('请自行在当前程序所在目录创建database.txt文件，输入一对英文{}并保存', title='little颜の班级管理系统 Powered by Python310')
            quit()
    else:#检测数据库格式并读取
        f = open('database.txt', 'r')
        res = f.read()
        f.close()
        if res == '':
            f = open('database.txt', 'w')
            res = f.write('{}')
            f.close()
            f = open('database.txt', 'r')
            res = eval(f.read())
            f.close()
        else:
            f = open('database.txt', 'r')
            res = eval(f.read())
            f.close()

    if 'admin' not in res:#设置admin密码并加密
        ans = box.enterbox('你还没有管理员账号，请输入将要使用的密码', title='little颜の班级管理系统 Powered by Python310')
        code = []
        for w in str(ans):
            num = ord(w)
            code.append(num)
        res['admin'] = code
        f = open('database.txt', 'w')
        res = f.write(str(res))
        f.close()
        f = open('database.txt', 'r')
        res = eval(f.read())
        f.close()
        code = res['admin']
        key = ''
        for w in code:
            key = key + str(chr(w))
        box.msgbox('请保管好你的管理员密码：\n' + key, title='little颜の班级管理系统 Powered by Python310')

    admin = res['admin']
    res.pop('admin')

    while True:
        op = box.buttonbox('选择你要做什么\n'+ str(res), choices=('计分', '随机', '排行榜', '管理', '退出'), title='little颜の班级管理系统 Powered by Python310')
        if op == '计分':
            lst = []
            for l in res:
                lst.append(l)
            tpl = tuple(lst)
            op = box.buttonbox('选择学生', choices=tpl, title='little颜の班级管理系统 Powered by Python310')
            if op == None:
                continue
            mk = box.buttonbox('选择分数', choices=('1','2','3','4','5','-1','-2','-3','-4','-5'), title='little颜の班级管理系统 Powered by Python310')
            if mk == None:
                continue
            res[op] = res[op] + int(mk)
            res['admin'] = admin
            f = open('database.txt', 'w')
            res = f.write(str(res))
            f.close()
            f = open('database.txt', 'r')
            res = eval(f.read())
            f.close()
            res.pop('admin')
            box.msgbox('加分成功！\n'+ str(res), title='little颜の班级管理系统 Powered by Python310')
        elif op == '管理':
            f = open('database.txt', 'r')
            code = eval(f.read())['admin']
            f.close()
            key = ''
            for w in code:
                key = key + str(chr(w))
            ans = box.enterbox('请输入管理员密码', title='little颜の班级管理系统 Powered by Python310')
            if ans == key:
                while True:
                    op = box.buttonbox('选择你要做什么', choices=('添加', '删除', '清空', '重置', '退出'), title='little颜の班级管理系统 Powered by Python310')
                    if op == '添加':
                        ans = box.enterbox('请输入学生姓名', title='little颜の班级管理系统 Powered by Python310')
                        if str(type(ans)) != "<class 'str'>":
                            box.msgbox('取消', title='little颜の班级管理系统 Powered by Python310')
                            continuenm
                        res[ans] = 0
                        res['admin'] = admin
                        f = open('database.txt', 'w')
                        res = f.write(str(res))
                        f.close()
                        f = open('database.txt', 'r')
                        res = eval(f.read())
                        f.close()
                        res.pop('admin')
                        box.msgbox('创建成功！\n'+ str(res), title='little颜の班级管理系统 Powered by Python310')
                    elif op == '删除':
                        ans = box.enterbox('请输入要删除学生姓名\n'+ str(res), title='little颜の班级管理系统 Powered by Python310')
                        if ans not in res:
                            box.msgbox('没有找到阿巴阿巴', title='little颜の班级管理系统 Powered by Python310')
                            continue
                        op = box.ynbox('你真舍得删掉ta吗', title='little颜の班级管理系统 Powered by Python310')
                        if op != True:
                            box.msgbox('取消', title='little颜の班级管理系统 Powered by Python310')
                            continue
                        res.pop(ans)
                        res['admin'] = admin
                        f = open('database.txt', 'w')
                        res = f.write(str(res))
                        f.close()
                        f = open('database.txt', 'r')
                        res = eval(f.read())
                        f.close()
                        res.pop('admin')
                        box.msgbox('创建成功！\n'+ str(res), title='little颜の班级管理系统 Powered by Python310')
                    elif op == '清空':
                        op = box.ynbox('你真舍得清空吗', title='little颜の班级管理系统 Powered by Python310')
                        if op != True:
                            box.msgbox('取消', title='little颜の班级管理系统 Powered by Python310')
                            continue
                        res.clear()
                        res['admin'] = admin
                        f = open('database.txt', 'w')
                        res = f.write(str(res))
                        f.close()
                        f = open('database.txt', 'r')
                        res = eval(f.read())
                        f.close()
                        res.pop('admin')
                        box.msgbox('清空成功！\n'+ str(res), title='little颜の班级管理系统 Powered by Python310')
                    elif op == '重置':
                        box.msgbox('删除目录下 database.txt 文件即可（三思而后行）', title='little颜の班级管理系统 Powered by Python310')
                    else:
                        break
            else:
                box.msgbox('密码错误', title='little颜の班级管理系统 Powered by Python310')
        elif op == '随机':
            op = int(box.buttonbox('选择人数', choices=('1','2','3','4','5','6','7','8','9','10'), title='little颜の班级管理系统 Powered by Python310'))
            lst = []
            for l in res:
                lst.append(l)
            if op > len(lst):
                box.msgbox('选择的人数太多', title='little颜の班级管理系统 Powered by Python310')
                continue
            box.msgbox(ran.sample(lst, op), title='little颜の班级管理系统 Powered by Python310')
        elif op == '排行榜':
            f = open('database.txt', 'r')
            res = eval(f.read())
            f.close()
            res.pop('admin')
            box.msgbox(sorted(res.items(),  key=lambda d:d[1], reverse=True), title='little颜の班级管理系统 Powered by Python310')
            pass
        else:
            exit()
else:
    if 'database.txt' not in os.listdir():#检测数据库是否存在
        op = input('系统检测到你的文件目录没有 database.txt 文件，是否按 Y 自动创建？')
        if op == 'Y' or op == 'y':
            f = open('database.txt', 'w')
            res = f.write('{}')
            f.close()
            print('创建成功！请重新运行本程序')
            time.sleep(10)
            quit()
        else:
            print('请自行在当前程序所在目录创建database.txt文件，输入一对英文{}并保存')
            time.sleep(10)
            quit()
    else:#检测数据库格式并读取
        f = open('database.txt', 'r')
        res = f.read()
        f.close()
        if res == '':
            f = open('database.txt', 'w')
            res = f.write('{}')
            f.close()
            f = open('database.txt', 'r')
            res = eval(f.read())
            f.close()
        else:
            f = open('database.txt', 'r')
            res = eval(f.read())
            f.close()

    if 'admin' not in res:#设置admin密码并加密
        ans = input('你还没有管理员账号，请输入将要使用的密码')
        code = []
        for w in str(ans):
            num = ord(w)
            code.append(num)
        res['admin'] = code
        f = open('database.txt', 'w')
        res = f.write(str(res))
        f.close()
        f = open('database.txt', 'r')
        res = eval(f.read())
        f.close()
        code = res['admin']
        key = ''
        for w in code:
            key = key + str(chr(w))
        print('请保管好你的管理员密码：\n' + key)

    admin = res['admin']
    res.pop('admin')

    while True:
        op = input('选择你要做什么,\n'+ str(res) + '\n计分0, 随机1, 排行榜2 , 管理3, 退出4 ')
        if op == '0':
            lst = []
            for l in res:
                lst.append(l)
            tpl = tuple(lst)
            op = input('选择学生'+str(tpl))
            if op == None or op not in tpl:
                continue
            mk = input('输入分数，负数前加“-”')
            try:
                mk = int(mk)
                pass
            except ValueError:
                continue
            if mk == None :
                continue
            res[op] = res[op] + int(mk)
            res['admin'] = admin
            f = open('database.txt', 'w')
            res = f.write(str(res))
            f.close()
            f = open('database.txt', 'r')
            res = eval(f.read())
            f.close()
            res.pop('admin')
            print('加分成功！\n'+ str(res))
        elif op == '3':
            f = open('database.txt', 'r')
            code = eval(f.read())['admin']
            f.close()
            key = ''
            for w in code:
                key = key + str(chr(w))
            ans = input('请输入管理员密码')
            if ans == key:
                while True:
                    op = input('选择你要做什么\n,添加 0, 删除 1, 清空 2, 重置 3, 退出 4')
                    if op == '0':
                        ans = input('请输入学生姓名')
                        if str(type(ans)) != "<class 'str'>":
                            print('取消')
                            continue
                        res[ans] = 0
                        res['admin'] = admin
                        f = open('database.txt', 'w')
                        res = f.write(str(res))
                        f.close()
                        f = open('database.txt', 'r')
                        res = eval(f.read())
                        f.close()
                        res.pop('admin')
                        print('创建成功！\n'+ str(res))
                    elif op == '1':
                        ans = input('请输入要删除学生姓名\n'+ str(res))
                        if ans not in res:
                            print('没有找到阿巴阿巴')
                            continue
                        op = print('你真舍得删掉ta吗按1')
                        if op != 1:
                            print('取消')
                            continue
                        res.pop(ans)
                        res['admin'] = admin
                        f = open('database.txt', 'w')
                        res = f.write(str(res))
                        f.close()
                        f = open('database.txt', 'r')
                        res = eval(f.read())
                        f.close()
                        res.pop('admin')
                        print('创建成功！\n'+ str(res))
                    elif op == '2':
                        op = print('你真舍得清空吗按1')
                        if op != '1':
                            print('取消')
                            continue
                        res.clear()
                        res['admin'] = admin
                        f = open('database.txt', 'w')
                        res = f.write(str(res))
                        f.close()
                        f = open('database.txt', 'r')
                        res = eval(f.read())
                        f.close()
                        res.pop('admin')
                        print('清空成功！\n'+ str(res))
                    elif op == '3':
                        print('删除目录下 database.txt 文件即可（三思而后行）')
                    elif op == '4':
                        break
                    else:
                        pass
            else:
                print('密码错误')
        elif op == '1':
            op = input('输入人数')
            try:
                op = int(op)
                pass
            except ValueError:
                continue
            lst = []
            for l in res:
                lst.append(l)
            if op > len(lst):
                print('选择的人数太多')
                continue
            print(ran.sample(lst, op))
        elif op == '2':
            f = open('database.txt', 'r')
            res = eval(f.read())
            f.close()
            res.pop('admin')
            print(sorted(res.items(),  key=lambda d:d[1], reverse=True))
            pass
        elif op == '4':
            exit()
        else:
            pass