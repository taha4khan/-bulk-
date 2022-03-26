from tkinter import*
form=Tk()
form.title('FEEDBACK FROM')
#form.geometry('800x640')
form.configure(bg='burlywood')
form.attributes('-fullscreen',True)

def save():
    data=(E1.get()+'\n'+E2.get()+'\n'+E3.get()+'\n'+E4.get()+'\n'+E5.get()+'\n'+E6.get()+'\n'+E7.get()+'\n'+E8.get()+'\n'+E9.get()+'\n\n\n')
    with open("form.txt",'w')as f:
        f.writelines(data)

title=Label(form,text='STUDENT INFORMATION',font=('times','30','bold italic'),bg='burlywood',fg='blue',activebackground='pink')
title.grid(row=0,column=2)

line1=Label(form,text='student name:',font=('times','16','bold'),bg='burlywood')
line1.grid(row=1,column=1,padx=20,pady=10,sticky='w')
E1=Entry(form,bd=5,relief=GROOVE)
E1.grid(row=1,column=2,pady=10)

line2=Label(form,text='Father name:',font=('times','16','bold'),bg='burlywood')
line2.grid(row=2,column=1,padx=20,pady=10,sticky='w')
E2=Entry(form,bd=5,relief=GROOVE)
E2.grid(row=2,column=2)

line3=Label(form,text='RollNO.:',font=('times','16','bold'),bg='burlywood')
line3.grid(row=3,column=1,padx=20,pady=10,sticky='w')
E3=Entry(form,bd=5,relief=GROOVE)
E3.grid(row=3,column=2)

line4=Label(form,text='Date of birth:',font=('times','16','bold'),bg='burlywood')
line4.grid(row=4,column=1,padx=20,pady=10,sticky='w')
E4=Entry(form,bd=5,relief=GROOVE)
E4.grid(row=4,column=2)

line5=Label(form,text='Email ID:',font=('times','16','bold'),bg='burlywood')
line5.grid(row=5,column=1,padx=20,pady=10,sticky='w')
E5=Entry(form,bd=5,relief=GROOVE)
E5.grid(row=5,column=2)

line6=Label(form,text='Contact Number:',font=('times','16','bold'),bg='burlywood')
line6.grid(row=6,column=1,padx=20,pady=10,sticky='w')
E6=Entry(form,bd=5,relief=GROOVE)
E6.grid(row=6,column=2)

line7=Label(form,text='Nationality:',font=('times','16','bold'),bg='burlywood')
line7.grid(row=7,column=1,padx=20,pady=10,sticky='w')
E7=Entry(form,bd=5,relief=GROOVE)
E7.grid(row=7,column=2)

line8=Label(form,text='field:',font=('times','16','bold'),bg='burlywood')
line8.grid(row=8,column=1,padx=20,pady=10,sticky='w')
E8=Entry(form,bd=5,relief=GROOVE)
E8.grid(row=8,column=2)

line9=Label(form,text='Resedential Address:',font=('times','16','bold'),bg='burlywood')
line9.grid(row=9,column=1,padx=20,pady=10,sticky='w')
E9=Entry(form,bd=5,relief=GROOVE)
E9.grid(row=9,column=2)

btn=Button(form,text='EXIT',command=form.destroy,bg='brown',fg='blue',activebackground='pink')
btn.grid(row=10,column=1,pady=10,)

submit=Button(form,text='submit',activebackground='yellow',command=save)
submit.grid(row=11,column=2,pady=10)

form.mainloop()

