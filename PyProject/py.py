#!C:/Python27/python
import urllib2
from bs4 import BeautifulSoup
import MySQLdb
import string
import sys



from  Tkinter import *
import tkMessageBox
master = Tk()
master.geometry("640x480")


def callback():
    quote_page = 'https://en.wikipedia.org/wiki/List_of_programming_languages'
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    listbox = Listbox(master, width=100, height=100)
    listbox.pack(side="left", fill="y")
    scrollbar = Scrollbar(master, orient="vertical")
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side="right", fill="y")

    listbox.config(yscrollcommand=scrollbar.set)
    List1 = soup.find('div', attrs={'class': 'div-col columns column-width'})
    mydb = MySQLdb.connect(host = "127.0.0.1",
                     user = "root",
                     passwd = "",
                     db ="data1")
    cur = mydb.cursor()



    def goto(linenum):
        global line
        line = linenum

    cur.execute("delete from list")




    line = 1
    while True:
        if List1 == None:
            break

        else:
            List_box = List1.find_all('li')

            for b in List_box:
                List = b.text.strip()
                List = List.encode('utf-8') if isinstance(List, unicode) else List
                #print List

                cur.execute('''INSERT INTO list(languages) VALUES( "%s")''' %(List))
                mydb.commit()
                listbox.insert(END, List)

            next_div = List1.find_next('div', attrs={'class': 'div-col columns column-width'})
            List1 = next_div

            listbox.pack(fill=BOTH, expand=YES)

        goto(1)


    cur.execute("select count(*) from list")
    info = cur.fetchone()


    for row in info:
        if row != 0:
            tkMessageBox.showinfo("Information", "List Successfully Inserted to Database")

    cur.close()

b = Button(master, text="List the Languages from en.wikipedia.org/wiki/List_of_programming_languages", command=callback)
b.pack()

master.mainloop()
