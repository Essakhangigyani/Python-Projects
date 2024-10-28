from tkinter import *
import datetime 

def date_time():
    # Get the current time from datetime
    current_time = datetime.datetime.now()  
    hr = current_time.strftime('%I')  # Get hour in 12-hour format
    mi = current_time.strftime('%M')  # Get minute
    sec = current_time.strftime('%S')  # Get second
    am = current_time.strftime('%p')   # Get AM/PM
    
    # Get the current date components
    day = current_time.strftime('%d')   # Get day
    month = current_time.strftime('%m') # Get month
    year = current_time.strftime('%Y')  # Get year
    week_day = current_time.strftime('%A') # Get day of the week
    
    # Update the labels with the current time and date
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    
    lab_date.config(text=day)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=week_day)

    # Call the date_time function every 1000 milliseconds (1 second)
    lab_hr.after(1000, date_time)

# Create the main window
clock = Tk()
clock.title('**** Digital Clock ****')
clock.geometry('1000x500')
clock.config(bg='black')

# Create labels for the hour, minute, second, and AM/PM
lab_hr = Label(clock, text='00', font=('Time New Roman', 60, "bold"), bg='red', fg="white")
lab_hr.place(x=120, y=50, height=110, width=100)
lab_hr_txt = Label(clock, text='Hour', font=('Time New Roman', 20, "bold"), bg='red', fg="white")
lab_hr_txt.place(x=120, y=190, height=40, width=100)

lab_min = Label(clock, text='00', font=('Time New Roman', 60, "bold"), bg='red', fg="white")
lab_min.place(x=340, y=50, height=110, width=100)
lab_min_txt = Label(clock, text='Min.', font=('Time New Roman', 20, "bold"), bg='red', fg="white")
lab_min_txt.place(x=340, y=190, height=40, width=100)

lab_sec = Label(clock, text='00', font=('Time New Roman', 60, "bold"), bg='red', fg="white")
lab_sec.place(x=560, y=50, height=110, width=100)
lab_sec_txt = Label(clock, text='Sec.', font=('Time New Roman', 20, "bold"), bg='red', fg="white")
lab_sec_txt.place(x=560, y=190, height=40, width=100)

lab_am = Label(clock, text='AM', font=('Time New Roman', 50, "bold"), bg='red', fg="white")
lab_am.place(x=780, y=50, height=110, width=100)
lab_am_txt = Label(clock, text='AM/PM', font=('Time New Roman', 20, "bold"), bg='red', fg="white")
lab_am_txt.place(x=780, y=190, height=40, width=100)

# Create labels for the date, month, year, and day of the week
lab_date = Label(clock, text='00', font=('Time New Roman', 60, "bold"), bg='red', fg="white")
lab_date.place(x=120, y=270, height=110, width=100)
lab_date_txt = Label(clock, text='Date', font=('Time New Roman', 20, "bold"), bg='red', fg="white")
lab_date_txt.place(x=120, y=410, height=40, width=100)

lab_mo = Label(clock, text='00', font=('Time New Roman', 60, "bold"), bg='red', fg="white")
lab_mo.place(x=340, y=270, height=110, width=100)
lab_mo_txt = Label(clock, text='Month', font=('Time New Roman', 20, "bold"), bg='red', fg="white")
lab_mo_txt.place(x=340, y=410, height=40, width=100)

lab_year = Label(clock, text='00', font=('Time New Roman', 30, "bold"), bg='red', fg="white")
lab_year.place(x=560, y=270, height=110, width=100)
lab_year_txt = Label(clock, text='Year', font=('Time New Roman', 20, "bold"), bg='red', fg="white")
lab_year_txt.place(x=560, y=410, height=40, width=100)

lab_day = Label(clock, text='Sunday', font=('Time New Roman', 20, "bold"), bg='red', fg="white")
lab_day.place(x=780, y=270, height=110, width=100)
lab_day_txt = Label(clock, text='Day', font=('Time New Roman', 20, "bold"), bg='red', fg="white")
lab_day_txt.place(x=780, y=410, height=40, width=100)

# Start the date_time function to initialize the clock
date_time()

# Run the Tkinter event loop
clock.mainloop()
