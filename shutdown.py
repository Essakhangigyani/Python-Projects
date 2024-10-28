from tkinter import *
import os

def restart():
        os.system("shutdown /r /t 0")
    

def restart_time():
    os.system("shutdown -r -t 20")

def logout(): 
    os.system("shutdown -l")

def shutdown():
    print('shutdown')
    os.system("shutdown -s -t 1")

st = Tk()
st.title('ShutDown App')
st.geometry("500x500")
st.config(bg="purple")

r_button = Button(st, text="Restart", font=('Times New Roman', 20, 'bold'), relief=RAISED, cursor="plus", command=restart)
r_button.place(x=150, y=60, height=50, width=200)

rt_button = Button(st, text="Restart Time", font=('Times New Roman', 20, 'bold'), relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=150, y=170, height=50, width=200)

lg_button = Button(st, text="Log-Out", font=('Times New Roman', 20, 'bold'), relief=RAISED, cursor="plus", command=logout)
lg_button.place(x=150, y=270, height=50, width=200)

st_button = Button(st, text="ShutDown", font=('Times New Roman', 20, 'bold'), relief=RAISED, cursor="plus", command=shutdown)
st_button.place(x=150, y=370, height=50, width=200)

st.mainloop()
