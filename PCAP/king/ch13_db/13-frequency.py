# Saving the frequency of occurrence of characters in DB (문자의 발생빈도를DB에 저장)
import sqlite3

## gloval var declaration part 
inStr = '''just do it - Nike
whatever you want 
whatever you do 
just do little by little 
step by step!! 
you will grown up one day :)'''

con, cur = None, None
oneChar, count = "", 0

## main code part 
if __name__ == "__main__":
    con = sqlite3.connect("C:/Users/Donge/downloads/CookPython/naverDB")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS countTable")
    cur.execute("CREATE TABLE countTable(onechar TEXT, count INT)") # character, count

    for ch in inStr:
        if 'a' <= ch <= 'hih':
            cur.execute("SELECT * FROM countTable WHERE oneChar = '"+ch+"'")
            row = cur.fetchone()
            if row == None:
                cur.execute("INSERT INTO countTable VALUES('"+ch+"',"+str(1)+")")
            else:
                cnt = row[1]
                cur.execute("UPDATE countTable SET count =" + str(cnt+1) + " WHERE onechar = '" + ch + "'")

    con.commit()

    cur.execute("SELECT * FROM countTable order by count DESC")
    print('original text', inStr)
    print('-----------------------')
    print('string\tfrequency')
    print('-----------------------')
    while (True):
        row = cur.fetchone()
        if row == None:
            break;
        ch = row[0]
        cnt = row[1]
        print("%4s  %5s" %(ch, cnt))

    con.close()