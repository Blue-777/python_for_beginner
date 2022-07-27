import sqlite3

## var declaration part
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = ""

## main code part 
con = sqlite3.connect("C:/Users/Donge/OneDrive/Documents/python_for_beginner/python_for_beginner-1/naverDB")  # DB가 저장된 폴더까지 지정
cur = con.cursor()

cur.execute("SELECT * FROM userTable")

print("UserID       UserName        Email       BirthYear")
print("------------------------------------------------")

while (True) :
    row = cur.fetchone()
    if row == None :
        break;
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s %15s %20s %d"%(data1, data2, data3, data4))

con.close()