#UI using tkinter
import tkinter as tk

class UI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        #make page as big as screen
        self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.master.title("UI")
        self.master.configure(background='black')
        self.master.attributes('-fullscreen', True)
        #make all text color #F9F9F9
        self.master.option_add("*Foreground", "#F9F9F9")
        self.master.bind('<Escape>', lambda e: self.master.destroy())
    #create three sections with equal size divided horizontally
    def create_widgets(self):#1F2B37,#4F76F6,#F9F9F9,#77F2A1*/
        #master font
        self.master.option_add("*Font", "Rokkitt 20 bold")
        self.left = tk.Frame(self.master, width=100, height=100, bg='#1F2B37')
        self.left.pack(side="left", fill="both", expand=True)
        self.middle = tk.Frame(self.master, width=100, height=100, bg='#1F2B37')
        self.middle.pack(side="left", fill="both", expand=True)
        self.right = tk.Frame(self.master, width=100, height=100, bg='#1F2B37')
        self.right.pack(side="left", fill="both", expand=True)
        self.create_left()
        self.create_middle()
        self.create_right()
    #create left section
    def create_left(self):
        #create 3 equal distant vertical buttons that are styled with #77F2A1
        #style text : Rokkitt 20 bold
        self.button1 = tk.Button(self.left, text="Thread Manipulation", font=("Rokkitt", 20, "bold"), bg='#77F2A1', command=self.thread_setting)
        self.button1.pack(side="top", fill="both", expand=True)
        self.button2 = tk.Button(self.left, text="Input/Output Manipulation", font=("Rokkitt", 20, "bold"), bg='#77F2A1', command=self.inpout_setting)
        self.button2.pack(side="top", fill="both", expand=True)
        self.button3 = tk.Button(self.left, text="Console", font=("Rokkitt", 20, "bold") , bg='#77F2A1', command=self.console_setting)
        self.button3.pack(side="top", fill="both", expand=True)

    #create middle section
    def create_middle(self):
        self.label3 = tk.Label(self.middle, text="Middle",bg='#1F2B37',foreground='#F9F9F9')
        self.label3.pack()  
    #create right section
    def create_right(self):
        self.label4 = tk.Label(self.right, text="Right",bg='#1F2B37',foreground='#F9F9F9')
        self.label4.pack()
    #create thread manipulation page that takes up section 2 and 3
    def thread_setting(self):
        self.label3.config(text="Threads")
        self.label4.config(text="Thread Manipulation")
    #create input/output manipulation page that takes up section 2 and 3
    def inpout_setting(self):
        self.label3.config(text="Input/Output Manipulation")
        self.label4.config(text="Input/Output Manipulation")
    #create console page that takes up section 2 and 3
    def console_setting(self):
        self.label3.config(text="Console")
        self.label4.config(text="Console")

    
s = tk.Tk()
app = UI(master=s)
app.mainloop()

    
