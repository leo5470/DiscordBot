import os, random
import sqlite3 as sq3
def tell():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #利用絕對位置定位檔案
    db_path = os.path.join(BASE_DIR, "jokes.db")
    num = random.randint(1, 26)
    with sq3.connect(db_path) as conn:
        cursor = conn.execute('select * from jokes limit 1 offset {}'.format(num - 1)) #利用SQL指令限制並提取資料
        rows = cursor.fetchall()
        for row in rows:
            Q = row[0]
            A = row[1]
    return Q, A