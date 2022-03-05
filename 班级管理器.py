import os
import easygui as box
import random as ran


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
        mk = box.buttonbox('选择分数', choices=('1','2','3','4','5','-1','-2','-3','-4','-5'), title='little颜の班级管理系统 Powered by Python310')
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
                    if op == False:
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
                    if op == False:
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
        break