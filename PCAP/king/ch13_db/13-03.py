import sqlite3
from tkinter import * 
from tkinter import messagebox 

## var declaration part
def insertData():
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""

## main code part 
    con = sqlite3.connect("C:/Users/Donge/downloads/CookPython/naverDB")  # DB가 저장된 폴더까지 지정
    cur = con.cursor()

    data1 = edt1.get(); data2 = edt2.get(); data3 = edt3.get(); data4 = edt4.get()
    try:
        sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
        cur.execute(sql)
    except:
        messagebox.showerror('error', "error input data")
    else:
        messagebox.showerror('success', 'success input data')
    con.commit()
    con.close()

def selectData():
    strData1, strData2, strData3, strData4 = [], [], [], [] 
    con = sqlite3.connect("C:/Users/Donge/downloads/CookPython/naverDB")
    cur = con.cursor()
    cur.execute("SELECT * FROM userTable")
    strData1.append("UserID"); strData2.append("UserName"); 
    strData3.append("Email"); strData4.append("BirthYear"); 
    strData1.append("----------"); strData2.append("----------"); 
    strData3.append("----------"); strData4.append("----------"); 
    while(True):
        row = cur.fetchone()
        if row == None: 
            break;
        strData1.append(row[0]); strData2.append(row[1]); 
        strData3.append(row[2]); strData4.append(row[3]); 

    listData1.delete(0, listData1.size()-1); listData2.delete(0, listData2.size()-1); 
    listData3.delete(0, listData3.size()-1); listData4.delete(0, listData4.size()-1); 
    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
        listData1.insert(END, item1); listData2.insert(END, item2); 
        listData3.insert(END, item3); listData4.insert(END, item4); 
    con.close()

## main code part 
window = Tk()
window.geometry("600x300")
window.title("GUI data input")

edtFrame = Frame(window);
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack(side = BOTTOM, fill = BOTH, expand = 1)

edt1 = Entry(edtFrame, width = 10); edt1.pack(side = LEFT, padx = 10, pady = 10)
edt2 = Entry(edtFrame, width = 10); edt2.pack(side = LEFT, padx = 10, pady = 10)
edt3 = Entry(edtFrame, width = 10); edt3.pack(side = LEFT, padx = 10, pady = 10)
edt4 = Entry(edtFrame, width = 10); edt4.pack(side = LEFT, padx = 10, pady = 10)

btnInsert = Button(edtFrame, text = "input", command = insertData)
btnInsert.pack(side = LEFT, padx = 10, pady = 10)
btnSelect = Button(edtFrame, text = "search", command = selectData)
btnSelect.pack(side = LEFT, padx = 10, pady = 10)

listData1 = Listbox(listFrame, bg = 'yellow');
listData1.pack(side = LEFT, fill = BOTH, expand = 1)
listData2 = Listbox(listFrame, bg = 'yellow');
listData2.pack(side = LEFT, fill = BOTH, expand = 1)
listData3 = Listbox(listFrame, bg = 'yellow');
listData3.pack(side = LEFT, fill = BOTH, expand = 1)
listData4 = Listbox(listFrame, bg = 'yellow');
listData4.pack(side = LEFT, fill = BOTH, expand = 1)

window.mainloop()