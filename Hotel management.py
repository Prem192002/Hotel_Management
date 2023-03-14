from cProfile import label
from re import L
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from time import strftime
from tokenize import String
from unicodedata import name

from numpy import place

root=Tk()
root.geometry("800x800")
root.title("Star Hotel")

separator = ttk.Separator(root, orient='vertical')    #right partition
separator.place(relx=0.83, rely=0, relwidth=0.2, relheight=1)

separator = ttk.Separator(root, orient='horizontal')   #bottom partition
separator.place(relx=0, rely=0.83, relwidth=1, relheight=1)

import os          #refresh button
root.title("refresh button")
def refresh():
    root.destroy()
    os.popen("Hotel management.py") #change refresh.py according to yours program name
button_1 =Button(root,text = "Refresh",command = refresh).place(x=80,y=550)


menubar=Menu(root)
#adding optins to menubar
file=Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New FIle', command=None)
file.add_command(label='Open', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

edit=Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find Again', command=None)

help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

root.config(menu=menubar)

#headiing labels include(booking,checkin,checkin)
a=Label(root,text="****// WELCOME  TO  STAR  HOTEL //****",font=70).place(x=500,y=50)
b=Label(root,text="BOOKING",font=10).place(x=200,y=150)
c=Label(root,text="CHECK-IN",font=10).place(x=600,y=150)
d=Label(root,text="CHECK-OUT",font=10).place(x=930,y=150)

         #entry widgets
         
#booking entry
import mysql.connector
_database_=mysql.connector.connect(
    host="localhost",
    user="root",
    password="prem@2002"
    )
_cursor_=_database_.cursor()
_cursor_.execute("use star_hotel")
numvar=StringVar()
namevar=StringVar()
checkinvar=StringVar()
checkoutvar=StringVar()
roomtypevar=StringVar()
bedtypevar=StringVar()

def submit():
    num=numvar.get()
    name=namevar.get()
    checkin=checkinvar.get()
    checkout=checkoutvar.get()
    roomtype=roomtypevar.get()
    bedtype=bedtypevar.get()
    
    sql="insert into hotel_data (person_count,name,check_in,check_out,room_type,bed_type) values(%s,%s,%s,%s,%s,%s)"
    t=(num,name,checkin,checkout,roomtype,bedtype)
    _cursor_.execute(sql,t)
    _database_.commit()
    
    numvar.set("")
    namevar.set("")
    checkinvar.set("")
    checkoutvar.set("")
    roomtypevar.set("")
    bedtypevar.set("")
    
numlabel=Label(root,text="NO. Of Person").place(x=100,y=200)
numentry=Entry(root,textvariable=numvar,width=27).place(x=220,y=200)

namelabel=Label(root,text="Name Of The Person").place(x=100,y=230)
nameentry=Entry(root,textvariable=namevar,width=27).place(x=220,y=230)

checkinlabel=Label(root,text="Check-In Date").place(x=100,y=260)
checkinentry=Entry(root,textvariable=checkinvar,width=27).place(x=220,y=260)

checkoutlabel=Label(root,text="Check-Out Date").place(x=100,y=290)
checkoutentry=Entry(root,textvariable=checkoutvar,width=27).place(x=220,y=290)

roomtypelabel=Label(root,text="Room (AC/NON-AC)").place(x=100,y=320)
roomtypeentry=Entry(root,textvariable=roomtypevar,width=27).place(x=220,y=320)

bedtypelabel=Label(root,text="Bed Type").place(x=100,y=350)
bedtypeentry=Entry(root,textvariable=bedtypevar,width=27).place(x=220,y=350)

subutton=Button(root, text="Submit", command=submit).place(x=230,y=400)



#chekin entry
import mysql.connector
db_=mysql.connector.connect(
    host="localhost",
    user="root",
    password="prem@2002"
    )
_cu_=db_.cursor()
_cu_.execute("use star_hotel")

name_var=StringVar()
check_invar=StringVar()

def submit():
    name=name_var.get()
    check=check_invar.get()
    
    
    
    sql=("select name,check_in from hotel_data where name=%s and check_in=%s")
    t=(name,check)
    _cu_.execute(sql,t)
    z=_cu_.fetchall()
    
    
    for x in z:
        if name in z:
            print(x,"data found")
        import random
        room=[101,102,103,104,105,106,107,108,109,110]
        roomnumber=random.choice(room)                   
        cmd="update hotel_data set room_num=%s where name=%s"
        val=(roomnumber,name)
        _cu_.execute(cmd,val)
        db_.commit()
        
        
        # Create text widget and specify size.
        T = Text(root, height = 5, width = 52)
        # Create label
        
        Fact = ("""YOUR ROOM NUMBER IS""", roomnumber)
        
        T.pack(side=BOTTOM)
        
        # Insert The Fact.
        T.insert(END, Fact)
     

            
    name_var.set("")
    check_invar.set("")
    
name_label=Label(root,text="Name").place(x=500,y=200)
name_entry=Entry(root,textvariable=name_var,width=27).place(x=600,y=200)

check_inlabel=Label(root,text="Check-In Date").place(x=500,y=230)
check_inentry=Entry(root,textvariable=check_invar,width=27).place(x=600,y=230)

sub_button=Button(root,text="Submit",command=submit).place(x=630,y=400)


#checkout
import mysql.connector
d_b=mysql.connector.connect(
    host="localhost",
    user="root",
    password="prem@2002"
    )
__cur__=d_b.cursor()
__cur__.execute("use star_hotel")


Name_var=StringVar()
check_outvar=StringVar()

def submit():
    Name=Name_var.get()
    check_out=check_outvar.get()
    
    sql="delete from hotel_data where name=%s and check_out=%s"
    t=(Name,check_out)
    __cur__.execute(sql,t)
    d_b.commit()
    for x in __cur__:
        print(x)
        
    # Create text widget and specify size.
    T = Text(root, height = 5, width = 52)
    # Create label
        
    Fact = """you have successfully checkedout from the room"""
        
    T.pack(side=BOTTOM)
        
    # Insert The Fact.
    T.insert(END, Fact)
     

    
    Name_var.set("")
    check_outvar.set("")

Name_label=Label(root,text="Name").place(x=850,y=200)    
Name_entry=Entry(root,textvariable=Name_var,width=27).place(x=950,y=200)

check_outlabel=Label(root,text="Check-Out Date").place(x=850,y=230)
check_outentry=Entry(root,textvariable=check_outvar,width=27).place(x=950,y=230)

submit_button=Button(root,text="Submit",command=submit).place(x=930,y=400)


#prices
ratelabel=Label(root,text="PRICES",font=10).place(x=1250,y=100)
ac_label=Label(root,text="[ NON-AC ]",font=10).place(x=1200,y=140)
singlebed_label=Label(root,text="Single Bed =  Rs.1000").place(x=1150,y=170)
doublebed_label=Label(root,text="Double Bed = Rs.700").place(x=1150,y=200)
royalbed_label=Label(root,text="Royal Bed = Rs.1200").place(x=1150,y=230)
threesharing_label=Label(root,text="Triple Sharing = Rs.500").place(x=1150,y=260)
foursharing_label=Label(root,text="Four Sharing = Rs.300").place(x=1150,y=290)

nonac_label=Label(root,text="[ AC ]",font=10).place(x=1220,y=340)
single_label=Label(root,text="Single Bed = Rs.1500").place(x=1150,y=370)
double_label=Label(root,text="Double Bed = Rs.1000").place(x=1150,y=400)
royal_label=Label(root,text="Royal Bed = Rs.1700").place(x=1150,y=430)
three_label=Label(root,text="Three Sharing = Rs.700").place(x=1150,y=460)
four_label=Label(root,text="Four sharing = Rs500").place(x=1150,y=490)

root.mainloop()

#second commit
