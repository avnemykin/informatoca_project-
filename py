from math import *
from tkinter import *

root=Tk()
root.title('Исследование физической модели')
root.geometry('500x500')

lb_V0=Label(root, text='V_0')
lb_V0.grid(column=0,row=0)
lb_A=Label(root, text='A')
lb_A.grid(column=0,row=1)
lb_S=Label(root, text='S')
lb_S.grid(column=0,row=2)
lb_H=Label(root, text='H')
lb_H.grid(column=0,row=3)

txt_V0=Entry(root, width=5)
txt_V0.grid(column=1,row=0)
txt_A=Entry(root, width=5)
txt_A.grid(column=1, row=1)
txt_S=Entry(root, width=5)
txt_S.grid(column=1,row=2)
txt_H=Entry(root,width=5)
txt_H.grid(column=1,row=3)

lb_ms=Label(root,text='м/с')
lb_ms.grid(column=2,row=0)
lb_gr=Label(root,text='град')
lb_gr.grid(column=2,row=1)
lb_m=Label(root, text='м')
lb_m.grid(column=2,row=2)
lb_M=Label(root,text='м')
lb_M.grid(column=2,row=3)
lb_L=Label(root,text='L')
lb_L.grid(column=4,row=0)

lb_vievs=Label(root,width=15,text='')
lb_vievs.grid(column=5,row=0)
lb_dr=Label(root,width=5)
lb_dr.grid(column=6,row=0)
lb_text=Label(root,width=15)
lb_text.grid(column=5,row=1)

def f_calc(event):
           a=int(txt_A.get())
           v_0=int(txt_V0.get())
           g=9.8
           s=int(txt_S.get())
           h=int(txt_H.get())

but1=Button(root,width=10,text='Вычислить')
but1.grid(column=4,row=3)
but1.bind('<b=Buttom-1>',f_calc)
but2=Button(root,widtgh=10,text='Показать')
but2.grid(column=5,row=3)


canv_h = 300
canv_w = 450

canv = Canvas(root, width = canv_w+10, height = canv_h+10, bg = "white")             
canv.create_line(10,canv_h,canv_w,canv_h,width=2, fill='green',arrow=LAST)  
canv.create_line(10,canv_h,10,10,width=2, fill='green',arrow=LAST)

k_x= (canv_w)//s
k_y =(canv_h)//s

for i in range(0,canv_w-5,k_x*5):
    canv.create_text(i+10, canv_h, text = str(round(int(txt_S.get))*((i)/canv_w))), fill="purple", font=("Helvectica", "10")

for i in range(s//5*k_y,canv_h,s//5*k_y):
    canv.create_text(10, canv_h-(i), text = str(round((int(txt_S.get)(*((i)/canv_h))), fill="purple", font=("Helvectica", "10")
    canv.create_line(k_x*(int(txt_S.get)),canv_h,k_x*(int(txt_S.get)),canv_h,width=2, fill='red')

for i in range(0,100,1):
  y = (v_0*sin(radians(int(txt_A.get))))*(i/10)-g*((i/10)**2)/2); 
  x = v_0*cos(radians(int(txt_A.get))))*(i/10); 

    canv.create_oval( (x*k_x//5),(canv_h-y*k_y), (x*k_x + 1)//5, (canv_h-y*k_y + 1), fill = 'black')

 y = (int(txt_S.get))*tan(radians(int(txt_A.get))) - (g*((int(txt_S.get))**2))/(2*(int(txt_V0.get))**2*cos(radians(int(txt_A.get)))**2)
    if y>0 and h>=y:
        lb_dr["text"] = 'Попадение'
    elif y<0:
        lb_dr["text"] = 'Недолет'
    else:
        lb_dr["text"] = 'Перелет'
root.mainloop()
