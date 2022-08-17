from tkinter import *
from tkinter import messagebox
from tkinter import Button
from tkinter import PhotoImage
from tkinter import Canvas
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from tkinter import ttk
import time
from time import sleep
from PIL import ImageTk, Image

#Class for the scrollbar
class ScrolFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        xxscrollbar = Scrollbar(self, orient="horizontal", command=canvas.xview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        scrollbar.pack(side="right", fill="y")
        xxscrollbar.pack(side="bottom", fill="x")
        canvas.pack(expand=True)

        canvas.configure(yscrollcommand=scrollbar.set,xscrollcommand=xxscrollbar.set)

#Splashscreen
class SplashScreen:
    def __init__(self):
        #self.a = Toplevel()
        self.percentage = 0
        Label(self.top,text="I am loading screen").pack()
        self.load = Label(self.a,text=f"Loading...{self.percentage}%")
        self.load.pack()
        self.load_bar()

    def load_bar(self):
        self.percentage +=5
        self.load.config(text=f"Loading...{self.percentage}%")
        if self.percentage == 100:
            self.a.destroy()
            top.deiconify()
            return
        else:
            top.after(100,self.load_bar)

#auxillary scrollbar
class testss(ttk.Frame):
    def __init__(self):
        self.render_gui()

    def render_gui(self):
        self.main_canvas = Canvas(self)
        vsb = Scrollbar(self, orient="vertical", command=self.main_canvas.yview)
        hsb = Scrollbar(self, orient="horizontal", command=self.main_canvas.xview)
        hsb.pack(side="bottom", fill="x")
        vsb.pack(side="right", fill="y")
        self.main_canvas.pack(expand = True, fill = "both")

        self.main_canvas.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)

#command for continue button
def takeipt():
    ntvar = IntVar()
    #global Entry1
    row__ = Entry1.get()
    __row = int(row__)
    sttr = str(row__)

    #conditions to continue
    if __row > 100:
        messagebox.showerror("Warning", "This might require a higher processor")
        warning_ = "Do you wish to continue?"
        MsgBox = messagebox.askquestion("Warning", warning_)
        if MsgBox == "yes":
            inform = "Your input is:"
            mbox = inform + " " + sttr + " by " + sttr + " matrix"
            messagebox.showinfo("Input Taken",mbox)
            
            percentage = "..."
            #Label(top,text="I am loading screen").pack()
            load = Label(top,text=f"Loading...{percentage}%")
            load.config(background="white")
            load.place(relx=0.219, rely=0.378, height=120, width=300)
            #percentage +=5
            load.config(text=f"Generating Workspace{percentage}%", font="Times 16 italic bold")



            def nextwindow():
                #load.destroy()
                #top.withdraw()
                window = Tk()
                window.title("N by N Matrix Workspace")
                window.geometry("300x300")
                window.resizable(False, False)
                frame = ScrolFrame(window)
                #window(frame.scrollable_frame).pack()
                __column = __row
                data = []
            

                for i in range(1, __row +1):
                    row = []
                    for j in range(1, __column +1):
                        itvar = IntVar()
                        en = Entry(frame.scrollable_frame, width=3, textvariable = itvar)
                        en.grid(row=i+1, column=j+1)
                        row.append(en)
                    data.append(row)

                #command for proceed button
                def display_matrix():
                    A = np.array(data)
                    map_ = np.vectorize(lambda x: int(x.get()))
                    A = map_(A)
                    #frame.pack_forget()
                    #A.astype(np.int)
                    #print(A)
                    #shoia = A
                    #messagebox.showinfo("Input Taken",shoia)

                    #Matrix inversion workspace
                    window.withdraw()
                    window2 = Toplevel()
                    window2.title("N by N Matrix Inversion Workspace")
                    window2.geometry("450x300")
                    window2.resizable(False, False)
                    frame = ScrolFrame(window2)
                
                    #rounds off number to 2 decimal place
                    def round_off(val,digits):
                        return round(val+10**(-len(str(val))-1), digits)

                    def det_matrix():
                        determinant = np.linalg.det(A)
                        determinant10 = str(round_off(determinant,2))
                        screen_.configure(text=determinant10)

                    def trans_matrix():
                        Transp = A.T
                        screen_.configure(text=Transp)

                    def inv_matrix():
                        determinant = np.linalg.det(A)
                        if determinant == 0:
                            inv_error = "This Matrix cannot be inverted"
                            messagebox.showerror("ERROR", inv_error)
                        else:
                            inv_ = np.linalg.inv(A)
                            screen_.configure(text=inv_)
                            

                    def eig_value_matrix():
                        eig_value, eig_vector = np.linalg.eig(A)
                        screen_.configure(text=eig_value)

                    def eig_vector_matrix():
                        eig_value, eig_vector = np.linalg.eig(A)
                        screen_.configure(text=eig_vector)

                    def clear_():
                        window.destroy()
                        window2.destroy()
                        top.wm_deiconify()

                    def invback():
                        window2.destroy()
                        window.wm_deiconify()



                    screen_ = Label(frame.scrollable_frame, text=A) #, background="white")
                    screen_.grid(row=2)

                    detbut = Button(window2, text="Determinant", command=det_matrix)
                    detbut.place(relx=0.79, rely=0.048, height=31, width=88)

                    transbut = Button(window2, text="Transpose", command=trans_matrix)
                    transbut.place(relx=0.79, rely=0.198, height=31, width=88)

                    eig_val_but = Button(window2, text="Eigen Value", command=eig_value_matrix)
                    eig_val_but.place(relx=0.79, rely=0.348, height=31, width=88)

                    eig_vec_but = Button(window2, text="Eigen Vector", command=eig_vector_matrix)
                    eig_vec_but.place(relx=0.79, rely=0.498, height=31, width=88)

                    invbut = Button(window2, text="Invert", command=inv_matrix)
                    invbut.place(relx=0.79, rely=0.648, height=31, width=88)

                    clrbut = Button(window2, text="Home", command=clear_)
                    clrbut.place(relx=0.79, rely=0.88, height=31, width=88)

                    backbut = Button(window2, text="< Back", command=invback)
                    backbut.place(relx=0.022, rely=0.88, height=31, width=85)

            
                    frame.place(relx=0, rely=0, height=250, width=350)
                dispbut = Button(window, text="Proceed >>>", command=display_matrix)
                dispbut.pack(side="bottom")

                frame.pack()
                window.focus_set()
                window.grab_set()
                load.destroy()
                top.withdraw()

            if percentage == 100:
                load.destroy()
                top.deiconify()
                return
            else:
                #load.destroy()
                top.after(5000,nextwindow)

            
    elif __row < 2:
        messagebox.showerror("ERROR", "Invalid Dimension")
    else:
        inform = "Your input is:"
        mbox = inform + " " + sttr + " by " + sttr + " matrix"
        messagebox.showinfo("Input Taken",mbox)
        
        
        percentage = "..."
        #Label(top,text="I am loading screen").pack()
        load = Label(top,text=f"Loading...{percentage}%")
        load.config(background="white")
        load.place(relx=0.219, rely=0.378, height=120, width=300)
        #percentage +=5
        load.config(text=f"Generating Workspace{percentage}%", font="Times 16 italic bold")



        def nextwindow():
            #load.destroy()
            #top.withdraw()
            window = Toplevel()
            window.title("N by N Matrix Workspace")
            window.geometry("300x300")
            window.resizable(False, False)
            frame = ScrolFrame(window)
            #window(frame.scrollable_frame).pack()
            __column = __row
            data = []
        

            for i in range(1, __row +1):
                row = []
                for j in range(1, __column +1):
                    itvar = IntVar()
                    en = Entry(frame.scrollable_frame, width=3, textvariable = itvar)
                    en.grid(row=i+1, column=j+1)
                    row.append(en)
                data.append(row)

            #command for proceed button
            def display_matrix():
                A = np.array(data)
                map_ = np.vectorize(lambda x: int(x.get()))
                A = map_(A)
                #frame.pack_forget()
                #A.astype(np.int)
                #print(A)
                #shoia = A
                #messagebox.showinfo("Input Taken",shoia)

                #Matrix inversion workspace
                window.withdraw()
                window2 = Tk()
                window2.title("N by N Matrix Inversion Workspace")
                window2.geometry("450x300")
                window2.resizable(False, False)
                frame = ScrolFrame(window2)
            
                #rounds off number to 2 decimal place
                def round_off(val,digits):
                    return round(val+10**(-len(str(val))-1), digits)

                def det_matrix():
                    determinant = np.linalg.det(A)
                    determinant10 = str(round_off(determinant,2))
                    screen_.configure(text=determinant10)

                def trans_matrix():
                    Transp = A.T
                    screen_.configure(text=Transp)

                def inv_matrix():
                    determinant = np.linalg.det(A)
                    if determinant == 0:
                        inv_error = "This Matrix cannot be inverted"
                        messagebox.showerror("ERROR", inv_error)
                    else:
                        inv_ = np.linalg.inv(A)
                        screen_.configure(text=inv_)
                        

                def eig_value_matrix():
                    eig_value, eig_vector = np.linalg.eig(A)
                    screen_.configure(text=eig_value)

                def eig_vector_matrix():
                    eig_value, eig_vector = np.linalg.eig(A)
                    screen_.configure(text=eig_vector)

                def clear_():
                    window.destroy()
                    window2.destroy()
                    top.wm_deiconify()

                def invback():
                    window2.destroy()
                    window.wm_deiconify()



                screen_ = Label(frame.scrollable_frame, text=A) #, background="white")
                screen_.grid(row=2)

                detbut = Button(window2, text="Determinant", command=det_matrix)
                detbut.place(relx=0.79, rely=0.048, height=31, width=88)

                transbut = Button(window2, text="Transpose", command=trans_matrix)
                transbut.place(relx=0.79, rely=0.198, height=31, width=88)

                eig_val_but = Button(window2, text="Eigen Value", command=eig_value_matrix)
                eig_val_but.place(relx=0.79, rely=0.348, height=31, width=88)

                eig_vec_but = Button(window2, text="Eigen Vector", command=eig_vector_matrix)
                eig_vec_but.place(relx=0.79, rely=0.498, height=31, width=88)

                invbut = Button(window2, text="Invert", command=inv_matrix)
                invbut.place(relx=0.79, rely=0.648, height=31, width=88)

                clrbut = Button(window2, text="Home", command=clear_)
                clrbut.place(relx=0.79, rely=0.88, height=31, width=88)

                backbut = Button(window2, text="< Back", command=invback)
                backbut.place(relx=0.022, rely=0.88, height=31, width=85)

        
                frame.place(relx=0, rely=0, height=250, width=350)
            dispbut = Button(window, text="Proceed >>>", command=display_matrix)
            dispbut.pack(side="bottom")

            frame.pack()
            window.focus_set()
            window.grab_set()
            load.destroy()
            top.withdraw()

        if percentage == 100:
            load.destroy()
            top.deiconify()
            return
        else:
            #load.destroy()
            top.after(5000,nextwindow)

            

        
        #empty matrix generation window
       


top = Tk()
top.geometry("550x400")
top.title("N by N Matrix Inversion System")
#top.minsize(width=600, height=450)
#top.maxsize(width=)
top.resizable(False,False)

Label1 = Label(top)
Label1.place(relx=0.317, rely=0.044, height=21, width=229)
Label1.configure(text='''Kelvin's Matrix Inversion system''')

Label2 = Label(top)
Label2.place(relx=0.05, rely=0.116, height=21, width=229)
Label2.configure(text='''Enter the size of the matrix:''')

entvar = IntVar()
Entry1 = Entry(top, textvariable = entvar)
Entry1.place(relx=0.442, rely=0.116, height=23, relwidth=0.143)
Entry1.configure(background="white")
Entry1.configure(font="TkFixedFont")

Button1 = Button(top, command=takeipt)
Button1.place(relx=0.665, rely=0.116, height=31, width=71)
Button1.configure(text='''continue''')

top.mainloop()
