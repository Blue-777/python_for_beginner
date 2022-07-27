import sqlite3

## var declaration part
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql=""

## main code part 
con = sqlite3.connect("C:/Users/Donge/OneDrive/Documents/python_for_beginner/python_for_beginner-1/naverDB")  # DB가 저장된 폴더까지 지정
cur = con.cursor()

while (True) :
    data1 = input("사용자ID ==> ")
    if data1 == "" :
        break;
    data2 = input("사용자이름 ==> ")
    data3 = input("이메일 ==> ")
    data4 = input("출생연도 ==> ")
    sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    cur.execute(sql)
    
con.commit()
con.close()
