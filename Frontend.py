"""
A Graphical user interface for library database management system

title, author, year, shelfno

user can: 
    1) view all books 
    2) search an entry 
    3) add an entry
    4) update an entry
    6) delete an entry
    
"""

from tkinter import *
import Database

def view_command():
    list1.delete(0,END)
    for row in Database.view():
        list1.insert(END,row)
        
def search_book():
    list1.delete(0,END)
    for books in Database.search(title_text.get(),author_text.get(),year_text.get(),shelfno_text.get()):
        list1.insert(END,books)

def add_command():
    Database.insert(title_text.get(),author_text.get(),year_text.get(),shelfno_text.get())
    list1.delete(0,END)
    list1.insert(END,title_text.get(),author_text.get(),year_text.get(),shelfno_text.get())

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])    
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])    
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])    
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4]) 
    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])
    

def delete_command():
    Database.delete(selected_tuple[0])
    
def update_command():
    Database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),shelfno_text.get())


window=Tk()
window['background']='#7a8197'
window.wm_title("Library Database Management")
Font=("Comic Sans MS",15,"bold")
Font1=("MS Sans Serif",12,'bold')

l1=Label(window,text="Title",bg='#7a8197',fg='white',font=Font)
l1.grid(row=0,column=0)
l2=Label(window,text="Author  ",bg='#7a8197',fg='white',font=Font)
l2.grid(row=0,column=2)
l3=Label(window,text="Year",bg='#7a8197',fg='white',font=Font)
l3.grid(row=1,column=0)
l4=Label(window,text="Shelfno  ",bg='#7a8197',fg='white',font=Font)
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

shelfno_text=StringVar()
e4=Entry(window,textvariable=shelfno_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=9,width=28,bg='#b8bcc8')
list1.grid(row=13,column=1,rowspan=10,columnspan=1)

sb1=Scrollbar(window)
sb1.grid(row=9,column=2,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all",width=10,font=Font1,fg='#7a8197',command=view_command)
b1.grid(row=14,column=3)

b2=Button(window,text="Search Entry",width=10,font=Font1,fg='#7a8197',command=search_book)
b2.grid(row=15,column=3)

b3=Button(window,text="Add Entry",width=10,font=Font1,fg='#7a8197',command=add_command)
b3.grid(row=16,column=3)

b4=Button(window,text="Update",width=10,font=Font1,fg='#7a8197',command=update_command)
b4.grid(row=17,column=3)

b5=Button(window,text="Delete",width=10,font=Font1,fg='#7a8197',command=delete_command)
b5.grid(row=18,column=3)

window.mainloop()




    

    