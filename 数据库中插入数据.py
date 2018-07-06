import MySQLdb
import random
import time

        
        
    
import MySQLdb
import random
def insertData():
    conn = MySQLdb.connect(
    host = "127.0.0.1", 
    port = 3306,
    user = "root", 
    db = "gloryroad", 
    charset = "utf8")
    cur = conn.cursor()
    conn.select_db('gloryroad')
    courseList = ['python', 'java', 'mysql', 'linux', '接口测试', '性能测试', '自动化测试','数据结构与算法']
    for i in xrange(1, 101):
        student_id = '201605' + '0' * (3 - len(str(i))) + str(i)
        name = random.choice(['Lucy','Tom','Lily','Amy','Dave','Aaron','Baron']) + str(i)
        tel = '1' + str(random.choice([3, 5, 7, 8])) + str(random.random())[2:11]
        sex = random.choice(['女', '男'])
        stuinfo_sql = "insert into studentInfo(student_id, name, sex, tel, AdmissionDate) \
        values('%s', '%s', '%s', '%s', date_sub(now(),interval %s day))" \
        %(student_id, name, sex, tel, random.randint(90, 120))
        cur.execute(stuinfo_sql)
        conn.commit()
        for j in courseList:
            grade_sql = "insert into grade(stuID,course,score) values('%s','%s',%s)" %(student_id,j,random.randint(80, 100))
            cur.execute(grade_sql)
    conn.commit()
    cur.close()
    conn.commit()
    conn.close()

insertData()
