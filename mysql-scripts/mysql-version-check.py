from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def query_with_fetchall(sqlquery):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(sqlquery)
        rows = cursor.fetchall()

        # print('Total Row(s):', cursor.rowcount)
        for row in rows:
            # a = row[0]
            # print(str(row))
            # print(str(a))
            return row[1]
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    a = query_with_fetchall("SHOW variables where Variable_name = 'Version';")
    b = query_with_fetchall("SHOW GLOBAL STATUS LIKE 'Uptime';")
    c = query_with_fetchall("SHOW variables where Variable_name = 'Hostname';")
    print("Server  : " + str(c) + "\nVersion : " + str(a) + "\nUptime  : " + str(int(int(b) / 86400)) + " giorni.")
