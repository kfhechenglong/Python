import json

# 存储学生的信息
students_dict = {}

def init():
    global students_dict
    #   打开student_scores.json文件，并读取json文件数据
    try:
        with open("student_scores.json", "r") as f:
            student_scores_josn = f.read()
        # 反序列化数据
        students_dict = json.loads(student_scores_josn)

    except FileNotFoundError:
        pass

def save():
    file = open("student_scores.json", "w")
    students_json = json.dumps(students_dict)
    file.write(students_json)
    file.close()

def show_students():
    """
        查询所有学生信息
    """
    for sid, stu_dic in students_dict.items():
        name = stu_dic.get("name")
        chinese = stu_dic.get("scores").get("chinese")
        math = stu_dic.get("scores").get("math")
        english = stu_dic.get("scores").get("english")
        print("学号：%4s 姓名：%4s 语文：%4s 数学：%4s 英语：%4s" % (sid, name, chinese,math, english))

def add_student():
    """添加学生的信息"""
    while 1:
        sid = input("请输入学生学号>>>")
        if sid in students_dict:
            print("该学生已存在")
        else:
            break
    
    name = input("请输入学生姓名>>>")
    chinese_score = input("请输入学生语文成绩>>>")
    math_score = input("请输入学生数学成绩>>>")
    english_score = input("请输入学生英语成绩>>>")
    scores_dict = {
        "chinese": chinese_score,
        "math": math_score,
        "english": english_score
    }
    stu_dic = {
        "name": name,
        "scores": scores_dict
    }
    students_dict[sid] = stu_dic

def update_student():
    """更新一个学生的信息"""
    while 1:
        sid = input("请输入学生的学号>>>")
        if sid in students_dict:
            break
    else:
        print("你要修改的信息不存在")
    
    chinese_score = input("请输入学生语文成绩>>>")
    math_score = input("请输入学生数学成绩>>>")
    english_score = input("请输入学生英语成绩>>>")
    scores_dict = {
        "chinses":chinese_score,
        "math":math_score,
        "english":english_score,
    }
    students_dict.get(sid).update({"scores": scores_dict})
    print("信息修改成功！")
    print("students_dict", students_dict)

def delete_student():
    """删除一个学生的信息"""
    while 1:
        sid = input("请输入学生的学号>>>")
        if sid in students_dict:
            break
    else:
        print("你要修改的信息不存在")
    students_dict.pop(sid)
    print("删除成功")

def main():
    init()

    while 1:
        print('''
           1.  查看所有学生成绩
           2.  添加一个学生成绩
           3.  修改一个学生成绩
           4.  删除一个学生成绩
           5.  保存
           6.  退出程序
        ''')
        choice = input("请输入您的选择：")

        if choice == "1":
            show_students()

        elif choice == "2":
            add_student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            save()

        elif choice == "6":
            break
        else:
            print("输入有误！")

main()