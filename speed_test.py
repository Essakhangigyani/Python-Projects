
from tkinter import *
from speedtest_cli  import speedtest_cli

def speedcheak():
    sp = speedtest_cli()
    sp.get_best_server()
    down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="gray")

lab = Label(sp, text="Internet Speed Test", font=("Times New Roman", 25, "bold"), bg="gray", fg="brown")
lab.place(x=60, y=40, height=30, width=380)

lab = Label(sp, text="Download Speed", font=("Times New Roman", 25, "bold"))
lab.place(x=60, y=130, height=30, width=380)

lab_down = Label(sp, text="00", font=("Times New Roman", 25, "bold"))
lab_down.place(x=60, y=200, height=30, width=380)

lab = Label(sp, text="Upload Speed", font=("Times New Roman", 25, "bold"))
lab.place(x=55, y=290, height=30, width=380)

lab_up = Label(sp, text="00", font=("Times New Roman", 25, "bold"))
lab_up.place(x=55, y=360, height=30, width=380)

button = Button(sp, text='Check Speed', font=("Times New Roman", 20, "bold"), relief=RAISED, bg='pink', command=speedcheak)
button.place(x=55, y=460, height=30, width=380)

sp.mainloop()



































# from tkinter import *
# from speedtest import Speedtest

# # from speedtest import speedtest
# def speedcheak():
#     sp = Speedtest()
#     sp.get_best_server()
#     down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
#     up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
#     lab_down.config(text=down)
#     lab_up.config(text=up)

# sp = Tk()
# sp.title("Internet Speed Test")
# sp.geometry("500x700")
# sp.config(bg="gray")

# lab = Label(sp, text="Internet Speed Test", font=("Times New Roman", 25, "bold"), bg="gray", fg="brown")
# lab.place(x=60, y=40, height=30, width=380)

# lab = Label(sp, text="Download Speed", font=("Times New Roman", 25, "bold"))
# lab.place(x=60, y=130, height=30, width=380)

# lab_down = Label(sp, text="00", font=("Times New Roman", 25, "bold"))
# lab_down.place(x=60, y=200, height=30, width=380)

# lab = Label(sp, text="Upload Speed", font=("Times New Roman", 25, "bold"))
# lab.place(x=55, y=290, height=30, width=380)

# lab_up = Label(sp, text="00", font=("Times New Roman", 25, "bold"))
# lab_up.place(x=55, y=360, height=30, width=380)

# button = Button(sp, text='Check Speed', font=("Times New Roman", 20, "bold"), relief=RAISED, bg='pink', command=speedcheak)
# button.place(x=55, y=460, height=30, width=380)

# sp.mainloop()







































# from tkinter import *
# from speedtest import speedtest

# def speedcheak():
#     sp=speedtest.Speedtest()
#     sp.get_servers()
#     down=str(round(sp.download()/(10**6),3))+"mps"
#     up=str(round(sp.upload()/(10**6),3))+"mps"
#     lab_down.config(text=down)
#     lab_up.config(text=up)





# sp=Tk()
# sp.title("Internet Speed Test")
# sp.geometry("500x700")
# sp.config(bg="gray")
# lab = Label(sp,text="Internet Speed Test", font=("Time New Roman",25,"bold"),bg="gray",fg="brown")
# lab.place(x=60,y=40,height=30,width=380)

# lab = Label(sp,text="Download Speed", font=("Time New Roman",25,"bold"))
# lab.place(x=60,y=130,height=30,width=380)

# lab_down = Label(sp,text="00", font=("Time New Roman",25,"bold"))
# lab_down.place(x=60,y=200,height=30,width=380)

# lab = Label(sp,text="Upload speed", font=("Time New Roman",25,"bold"))
# lab.place(x=55,y=290,height=30,width=380)

# lab_up = Label(sp,text="00", font=("Time New Roman",25,"bold"))
# lab_up.place(x=55,y=360,height=30,width=380)

# Button=Button(sp,text='Check Speed', font=("Time New Roman",20,"bold"),relief=RAISED,bg='pink',command=speedcheak)
# Button.place(x=55,y=460,height=30,width=380)
# sp.mainloop()