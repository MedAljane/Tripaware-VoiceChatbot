from queue import Queue
from tkinter import *
import tkinter.messagebox

class ChatInterface(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.master.iconbitmap('appIcon.ico')


        # sets default bg for top level windows
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"
        self.font = "Verdana 10"

        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)
        # Menu bar

        # File
        file = Menu(menu, tearoff=0)
        menu.add_cascade(label="Exit",command=self.destroy())
   
        # color theme
        color_theme = Menu(menu, tearoff=0)
        menu.add_cascade(label="Color theme", menu=color_theme)
        color_theme.add_command(label="Default",command=self.color_theme_default) 
        color_theme.add_command(label="Grey",command=self.color_theme_grey) 
        color_theme.add_command(label="Blue",command=self.color_theme_dark_blue) 
        color_theme.add_command(label="Torque",command=self.color_theme_turquoise)
        color_theme.add_command(label="Hacker",command=self.color_theme_hacker)

        help_option = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_option)
        help_option.add_command(label="About CHATTY", command=self.msg)
        help_option.add_command(label="Develpoers", command=self.about)


    def chatexit(self):
        exit()

    def msg(self):
        tkinter.messagebox.showinfo("CHATTY v1.0",'CHATTY  is a chatbot for answering python queries\nIt is based on retrival-based NLP using pythons NLTK tool-kit module\nGUI is based on Tkinter\nIt can answer questions regarding python language for new learners')

    def about(self):
        tkinter.messagebox.showinfo("CHATTY Developers","Hassen Chebil\nMohamed Amine Aljan")
    
    # Default
    def color_theme_default(self):
        self.master.config(bg="#EEEEEE")
        self.textarea.config(bg="#EEEEEE")
        
        self.tl_bg = "#FFFFFF"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"

    # Dark
    def color_theme_dark(self):
        self.master.config(bg="#2a2b2d")
        self.textarea.config(bg="#2a2b2d")
        
        self.tl_bg = "#212121"
        self.tl_bg2 = "#2a2b2d"
        self.tl_fg = "#FFFFFF"

    # Grey
    def color_theme_grey(self):
        self.master.config(bg="#444444")
        self.textarea.config(bg="#444444")
        
        self.tl_bg = "#4f4f4f"
        self.tl_bg2 = "#444444"
        self.tl_fg = "#ffffff"

    # Blue
    def color_theme_dark_blue(self):
        self.master.config(bg="#263b54")
        self.textarea.config(bg="#263b54")
        
        self.tl_bg = "#1c2e44"
        self.tl_bg2 = "#263b54"
        self.tl_fg = "#FFFFFF"

    # Torque
    def color_theme_turquoise(self):
        self.master.config(bg="#003333")
        self.textarea.config(bg="#003333")
        
        self.tl_bg = "#669999"
        self.tl_bg2 = "#003333"
        self.tl_fg = "#FFFFFF"

    # Hacker
    def color_theme_hacker(self):
        self.master.config(bg="#0F0F0F")
        self.textarea.config(bg="#0F0F0F")
        
        self.tl_bg = "#0F0F0F"
        self.tl_bg2 = "#0F0F0F"
        self.tl_fg = "#33FF33"

    # Default font and color theme
    def default_format(self):
        self.font_change_default()
        self.color_theme_default()    


def runInterface(queue):

    root=Tk()

    def checkQueue():
        e = queue.get()
        if e[1].lower() == "exit":
            root.destroy()
        
        textarea.tag_config('bot', background="white", foreground="blue")
        textarea.tag_config('user', background="white", foreground="red")
        if e[0] == "Bot: ":
            textarea.insert(END,e[0], 'bot')
        else:
            textarea.insert(END,e[0], 'user')
            
        textarea.insert(END,e[1]+'\n')
        textarea.see(END)
        root.after(50, checkQueue)

    root.geometry('500x600+100+50')
    root.title('CHATTY')
    root.config(bg="#263b54")

    logoPic=PhotoImage(file='pic.png')

    logoPicLabel=Label(root,image=logoPic,bg="#263b54")
    logoPicLabel.pack(pady=5)

    centerFrame=Frame(root)
    centerFrame.pack()

    scrollbar=Scrollbar(centerFrame, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    global textarea
    textarea=Text(centerFrame, font=("Times", 14, "bold"), height=20, wrap='word', yscrollcommand=scrollbar.set)
    textarea.pack(side=LEFT)
    scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)

    root.after(50, checkQueue)

    a = ChatInterface(root)

    root.mainloop()
    