# importing the dependencies 
import tkinter as Tkinter
import customtkinter as ctk

ctk.set_appearance_mode("System")

running = False
hours, minutes, seconds = 0,0,0

def Start():
    global running
    if not running:
         counter_label(stopwatch_label)
         running = True

def Stop():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running= False
   

def Reset(): 
    global running
    if running==False:
        stopwatch_label.after_cancel(update_time)
        global hours, minutes, seconds
        stopwatch_label.config(text='00:00:00')
    
    else:
        stopwatch_label['text']='Starting...'

def counter_label(stopwatch_label):
        display="Starting..."
        global hours, minutes, seconds
        hours, minutes, seconds = 0,0,0

        seconds += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0
        hours_string = f'{hours}' if hours > 9 else f'0{minutes}'
        minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
        seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
        stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
        global update_time

        update_time= stopwatch_label.after(1000, counter_label)
        counter += 1
counter_label()



root = Tkinter.Tk()
root.geometry("500x160")
root.title("Stopwatch")

stopwatch_label = Tkinter.Label( root, text="Press Start", fg="black", font=("Garamond",50))
stopwatch_label.pack(anchor='center', pady=10)
f = Tkinter.Frame(root)
start = ctk.CTkButton(f, text='Start', width = 7, command= Start, fg_color=("black"))
stop = ctk.CTkButton(f, text='Stop', width= 7, command= Stop, fg_color=("black"))
reset = ctk.CTkButton(f, text='Reset', width= 7, command= Reset, fg_color=("black"))
f.pack(anchor='center', pady=15)
start.pack(pady=15)
stop.pack(pady=16)
reset.pack(pady=17)
root.mainloop()

