###from tensorflow.keras.models import load_model

## please uncomment above code
import numpy as np
from tkinter import *
from tkinter.filedialog import askopenfilename
root = Tk()
import tkinter as Tkin
from tkinter.ttk import *
global w
root.title("Phantom Fury")
filename=''

x=Canvas(root,height=420)


####         functions

def func1():
    
    data = [s1.get(),s2.get(),s3.get(),s4.get(),s5.get(),s6.get(),s7.get(),s8.get(),s9.get(),s10.get(),s11.get(),s12.get()]
    


    if '' in data:
        root2=Tk()
        Label(root2,text='Please Enter all Value' ).pack(fill=Tkin.X,padx=10,pady=10)
        Button(root2, text='OK!', width=25, command=root2.destroy).pack(fill=Tkin.X,padx=10,pady=10) 
        root2.mainloop()
        return

    data = list(map(float,data))
    #print(data)
    root2=Tk()

    
    
    
    
    load_model('spine model.h5')
    a=np.array(data)
    a=a.reshape(1,-1)
    k=model.predict(a)
    k=k.ravel()
    k=np.argmax(k)
    if(k==0):
        string='Normal Spine'
    else:
        string = "Normal"
    
    
    Label(root2,text=string ).pack(fill=Tkin.X,padx=10,pady=10)
    Button(root2, text='OK!', width=25, command=root2.destroy).pack(fill=Tkin.X,padx=10,pady=10) 
    root2.mainloop()
    return
    
    
        

    

###   Instance

g1 = Label(root, text='Spine Abnormility Detection -',font=("Arial Bold", 12)) 
g3=x.create_line(0, 18, 200, 18 ) 
g2=Label(root, text='Please fill the information below',font=("Arial Bold", 10))


t1=Label(root, text='pelvic_incidence')
s1=Entry(root)
t2=Label(root, text='pelvic tilt')
s2=Entry(root)
t3=Label(root, text='lumbar_lordosis_angle')
s3=Entry(root)
t4=Label(root, text='sacral_slope')
s4=Entry(root)
t5=Label(root, text='pelvic_radius')
s5=Entry(root)
t6=Label(root, text='degree_spondylolisthesis')
s6=Entry(root)
t7=Label(root, text='pelvic_slope')
s7=Entry(root)
t8=Label(root, text='Direct_tilt')
s8=Entry(root)
t9=Label(root, text='thoracic_slope')
s9=Entry(root)
t10=Label(root, text='cervical_tilt')
s10=Entry(root)
t11=Label(root, text='sacrum_angle')
s11=Entry(root)
t12=Label(root, text='scoliosis_slope')
s12=Entry(root)




run=Button(root, text='Create graph', width=20, command=func1)




### packing


g1.pack(fill=Tkin.X,padx=10,pady=10)
g2.pack(fill=Tkin.X,padx=10,pady=4)        
x.pack(fill=Tkin.X,padx=0,pady=0)   



t1.place(x=30, y=100)
s1.place(x=170, y=100)
t2.place(x=30, y=130)
s2.place(x=170, y=130)
t3.place(x=30, y=160)
s3.place(x=170,y=160)
t4.place(x=30,y=190)
s4.place(x=170,y=190)
t5.place(x=30,y=220)
s5.place(x=170,y=220)
t6.place(x=30,y=250)
s6.place(x=170,y=250)
t7.place(x=30,y=280)
s7.place(x=170,y=280)
t8.place(x=30,y=310)
s8.place(x=170,y=310)
t9.place(x=30,y=340)
s9.place(x=170,y=340)
t10.place(x=30,y=370)
s10.place(x=170,y=370)
t11.place(x=30,y=400)
s11.place(x=170,y=400)
t12.place(x=30,y=430)
s12.place(x=170,y=430)
run.place(x=85,y=460)
root.mainloop()
print('asd')