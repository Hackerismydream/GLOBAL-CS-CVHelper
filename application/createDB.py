import mysql.connector
import json

# 连接到MySQL数据库
cnx = mysql.connector.connect(
    host="localhost", #请更改配置
    user="root", #请更改配置
    password="123456", #请更改配置
    database="global_u"
)

name_map = {

}


# 加载JSON数据
with open('../exp/ALL_DETAIL_FULL.json', 'r', encoding='utf-8') as file:
    DETAIL = json.load(file)

def init_db():
    cursor = cnx.cursor()
    # 删除并重新创建Universities表格
    # 删除外键约束
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

    cursor.execute("DROP TABLE IF EXISTS Universities")
    cursor.execute("""
        CREATE TABLE Universities (
          id INT PRIMARY KEY AUTO_INCREMENT,
          name VARCHAR(255),
          duration VARCHAR(50),
          language VARCHAR(50),
          degree_type VARCHAR(200),
          internship_required VARCHAR(50),
          thesis_required VARCHAR(50),
          scholarship VARCHAR(255),
          other_info TEXT
        )
    """)

    # 删除Pros表格的外键约束

    # 删除并重新创建Pros表格
    cursor.execute("DROP TABLE IF EXISTS Pros")
    cursor.execute("""
        CREATE TABLE Pros (
          id INT PRIMARY KEY AUTO_INCREMENT,
          university_id INT,
          pro VARCHAR(255),
          FOREIGN KEY (university_id) REFERENCES Universities(id)
        )
    """)

    # 删除并重新创建Cons表格
    cursor.execute("DROP TABLE IF EXISTS Cons")
    cursor.execute("""
        CREATE TABLE Cons (
          id INT PRIMARY KEY AUTO_INCREMENT,
          university_id INT,
          con VARCHAR(255),
          FOREIGN KEY (university_id) REFERENCES Universities(id)
        )
    """)

    # 删除并重新创建ApplicationNotes表格
    cursor.execute("DROP TABLE IF EXISTS ApplicationNotes")
    cursor.execute("""
        CREATE TABLE ApplicationNotes (
          id INT PRIMARY KEY AUTO_INCREMENT,
          university_id INT,
          note TEXT,
          FOREIGN KEY (university_id) REFERENCES Universities(id)
        )
    """)

def insert_universities():
    # 创建游标对象
    cursor = cnx.cursor()
    # 插入Universities表格数据
    for entry in DETAIL:
        insert_query = """
                INSERT INTO universities (name, duration, language, degree_type, internship_required, thesis_required, scholarship, other_info)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
        info = DETAIL[entry]['项目介绍']
        values= (
            entry,
            info['项目时长'],
            info['授课语言'],
            info['学位类型'],
            info['是否强制实习'],
            info['毕业是否需要论文'],
            info['奖学金'],
            info['其他信息']
        )
        cursor.execute(insert_query, values)
    # 提交事务
    cnx.commit()


def get_map():
    name_map = {}
    cursor = cnx.cursor()
    query = """
        SELECT id, name FROM universities
    """
    cursor.execute(query)
    for (id, name) in cursor:
        name_map[name] = id
    return name_map

def insert_other():
    # 创建游标对象
    cursor = cnx.cursor()
    # 插入Pros表格数据
    for entry in DETAIL:
        insert_query = """
                INSERT INTO pros (university_id, pro)
                VALUES (%s, %s)
            """
        info = DETAIL[entry]['项目优劣势']['Pros']
        name = entry
        for item in info:
            values = (name_map.get(name), item)
            cursor.execute(insert_query, values)   #insert

    # 插入Cons表格数据
    for entry in DETAIL:
        insert_query = """
                INSERT INTO cons (university_id, con)
                VALUES (%s, %s)
            """
        info = DETAIL[entry]['项目优劣势']['Cons']
        name = entry
        for item in info:
            values = (name_map.get(name), item)
            cursor.execute(insert_query, values)   #insert

    # 插入ApplicationNotes表格数据
    for entry in DETAIL:
        insert_query = """
                INSERT INTO ApplicationNotes (university_id, note)
                VALUES (%s, %s)
            """
        try:
            info = DETAIL[entry]['注意事项']['网申注意事项']
        except:
            print(entry)
            exit()
        # info = DETAIL[entry]['注意事项']['网申注意事项']
        name = entry
        for item in info:
            values = (name_map.get(name), item)
            cursor.execute(insert_query, values)

    # 提交事务
    cnx.commit()

    # 关闭游标和数据库连接
    cursor.close()
    cnx.close()

if __name__ == '__main__':
    init_db()
    insert_universities()
    name_map = get_map()
    insert_other()
    pass