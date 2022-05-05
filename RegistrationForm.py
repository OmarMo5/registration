import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#tk._test()
frm = tk.Tk()
frm.title("Registration Form")
w=400
h=450
ws=(frm.winfo_screenwidth()-w)/2
hs=(frm.winfo_screenheight()-h)/2-40
frm.geometry('%dx%d+%d+%d' %(w,h,ws,hs))
lbl1=ttk.Label(frm,text='Registration Form',font=("None 20 bold"),foreground='navy')
lbl=ttk.Label(frm,text='-----------------------------------------',font=("None 20 bold"),foreground='navy')
lbl1.pack()
lbl.pack()
frame1 = ttk.Frame(frm)
svFN = tk.StringVar()
svEM = tk.StringVar()
svPA = tk.StringVar()
lbl2 = ttk.Label(frame1,text='Full Name:',font=("None 15 bold")).grid(row=0,column=0,pady=10)
ent2 = ttk.Entry(frame1,width=35,textvariable=svFN).grid(row=0,column=1,padx=10)
lbl3 = ttk.Label(frame1,text='Email:',font=("None 15 bold")).grid(row=1,column=0)
ent3 = ttk.Entry(frame1,width=35,textvariable=svEM).grid(row=1,column=1,padx=10)
lbl4 = ttk.Label(frame1,text='Password:',font=("None 15 bold")).grid(row=2,column=0)
ent4 = ttk.Entry(frame1,width=35,textvariable=svPA).grid(row=2,column=1,pady=10,padx=10)
frame1.pack()
frame2 = ttk.Frame(frm)
sv1=tk.StringVar()
sv2=tk.StringVar()
lbl5 = ttk.Label(frame2,text='Gender:',font=("None 15 bold")).grid(row=0,column=0)
gen1 = ttk.Radiobutton(frame2,value=0,textvariable=sv1).grid(row=0,column=1,padx=30,pady=10)
gen2 = ttk.Radiobutton(frame2,value=1,textvariable=sv2).grid(row=0,column=2)
sv1.set('Male')
sv2.set('Female')
svch1=tk.StringVar()
svch2=tk.StringVar()
coun = ttk.Label(frame2,text="Country:",font=("None 15 bold")).grid(row=1,column=0)
cmob = ttk.Combobox(frame2,values=("Select Your Country","Egypt","Sudia","Roma","Italia","Rusea","England","France")).grid(row=1,column=1)
lbl6 = ttk.Label(frame2,text='Programming:',font=("None 15 bold")).grid(row=2,column=0)
che1 = tk.Checkbutton(frame2,textvariable=svch1).grid(row=2,column=1)
che2 = tk.Checkbutton(frame2,textvariable=svch2).grid(row=2,column=2)
svch1.set('Java')
svch2.set('Python')
frame2.pack()
def RecordData():
    if svFN.get().strip()=='':
        messagebox.showinfo('Empty','Name Is Empty')
    elif svEM.get().strip()=='':
        messagebox.showinfo('Empty', 'Email Is Empty')
    elif svPA.get().strip()=='':
        messagebox.showinfo('Empty', 'Password Is Empty')
    else:
        f=open("E:\\My Privacy\\All Data","w")
        f.write("Full Name       :"+svFN.get()+"\n")
        f.write("Email           :"+svEM.get()+"\n")
        f.write("Password        :"+svPA.get()+"\n")
        if sv1.get()=='Male':
            f.write("The gender   :"+sv1.get()+"\n")
        if sv2.get()=='Female':
            f.write("The gender   :"+sv2.get()+"\n")
        if svch1.get()=='Java':
            f.write("the Language :"+svch1.get()+"\n")
        if svch2.get()=='Python':
            f.write("The Language :"+svch2.get()+"\n")
        f.close()
        messagebox.showinfo('Successfull',"The Data Is Record...")

btns=ttk.Style()
btns.configure('TButton',background='red',foreground='red',font=('None 15 bold'))
btn1 = ttk.Button(frm,text="Submit",command=RecordData).pack(pady=20)
btn2 = ttk.Button(frm,text="Exit",command=lambda :frm.destroy()).pack()
frm.mainloop()
