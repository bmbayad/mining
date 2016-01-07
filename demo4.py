__author__ = 'bmbayad'

import tkinter as tk

from tkinter import Tk, Text, BOTH, W, N, E, S

import matplotlib

matplotlib.use('TkAgg')

from numpy import arange, linspace, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure


class Example:
    def __init__(self, parent):
        #tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initHeader()
        self.initUI()

    def quit(self):
        self.parent.destroy()

    def clear_frame(self):
        self.frame2.destroy()
        self.initUI()

    def callback(self):

        #print("test")
        # self.area.insert(tk.END, self.e.get())
        # self.area.insert(tk.END, self.e1.get())
        # self.area.insert(tk.END, self.e2.get())
        # self.area.insert(tk.END, self.e3.get())
        # self.area.insert(tk.END, self.e4.get())

        self.frame2.destroy()
        self.initUI()

        seq = []

        counter = 0
        range_skip_num = 1
        count = 1
        seq_counter=1

        if self.e4.get() == "Odd":
            #seq = [x for x in range(2,int(self.e2.get())) if x%2 == 1]
            while(seq_counter <= int(self.e2.get())):
                count+=1
                if(count%2)==1:
                    seq.append(count)
                    seq_counter+=1

        if self.e4.get() == "Even":
            #seq = [x for x in range(2,int(self.e2.get())) if x%2 == 0]
            while(seq_counter <= int(self.e2.get())):
                count+=1
                if(count%2)==0:
                    seq.append(count)
                    seq_counter+=1


        if self.e4.get() == "All" or  self.e4.get() == "" :
            seq = [x for x in range(2,int(self.e2.get()))]

        tk.Label(self.frame2, text="%s" % 1, width=3, borderwidth="1",relief="solid").grid(row=1, column=0)


        f = Figure(figsize=(8, 3), dpi=40)
        a = f.add_subplot(111)
        x = sin(linspace(0, 2*pi*400, int(self.e1.get())))
        a.plot(x, 'r--')
        canvas1 = FigureCanvasTkAgg(f, self.frame2)
        mpl = canvas1.get_tk_widget()
        mpl.grid(row=1, column=1,padx=20)

        acc = x

        print(seq)
        #for row in range(2,int(self.e2.get())+1):
        for row in seq:
            print(row)
            tk.Label(self.frame2, text="%s" % row, width=3, borderwidth="1",relief="solid").grid(row=row, column=0)

            f = Figure(figsize=(8, 3), dpi=40)
            a = f.add_subplot(111)
            x = (1 / row) * sin(linspace(0, 2*400*int(self.e.get()) * row * pi, int(self.e1.get())))
            a.plot(x, 'r--')
            canvas1 = FigureCanvasTkAgg(f, self.frame2)
            mpl = canvas1.get_tk_widget()
            mpl.grid(row=row, column=1,padx=20)

            acc += x

            f = Figure(figsize=(8, 3), dpi=40)
            a = f.add_subplot(111)
            a.plot(acc)
            canvas1 = FigureCanvasTkAgg(f, self.frame2)
            mpl = canvas1.get_tk_widget()
            mpl.grid(row=row, column=2,padx=20)




    def onFrameConfigure(self, canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))
    def initHeader(self):
        self.parent.title("Windows")
        #self.pack(fill=BOTH, expand=True)

        self.parent.columnconfigure(1, weight=1)
        self.parent.columnconfigure(3, pad=30)
        self.parent.rowconfigure(3, weight=1)
        self.parent.rowconfigure(5, pad=7)

        canvas1 = tk.Canvas(self.parent, borderwidth=0, height=120)
        canvas1.grid(sticky=W, pady=2, padx=3)
        frame = tk.Frame(canvas1)
        canvas1.create_window((4, 4), window=frame, anchor="nw")

        lbl = tk.Label(frame, text="Periods")
        lbl.grid(row=0, column=0, padx=5)
        self.e = tk.Entry(frame)
        self.e.grid(row=0, column=1)
        self.e.insert(0,"1")

        lbl = tk.Label(frame, text="Sample")
        lbl.grid(row=1, column=0, padx=5)
        self.e1 = tk.Entry(frame)
        self.e1.grid(row=1, column=1)
        self.e1.insert(0,100)


        lbl = tk.Label(frame, text="# Harmonics")
        lbl.grid(row=2, column=0, padx=5)
        self.e2 = tk.Entry(frame)
        self.e2.grid(row=2, column=1)
        self.e2.insert(0,"10")


        lbl = tk.Label(frame, text="Scale")
        lbl.grid(row=3, column=0, padx=5)
        self.e3 = tk.Entry(frame)
        self.e3.grid(row=3, column=1)

        lbl = tk.Label(frame, text="Odd|Even|All")
        lbl.grid(row=4, column=0, padx=5)
        self.e4 = tk.Entry(frame)
        self.e4.grid(row=4, column=1)
    def initUI(self):




        # area = Text(self)
        # self.area= area

        # area.grid(row=1, column=0, columnspan=2, rowspan=4,padx=5, sticky=E+W+S+N)

        canvas2 = tk.Canvas(self.parent, borderwidth=0, height=90, background="#fffaaa")
        canvas2.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E + W + S + N)
        vsb = tk.Scrollbar(canvas2, orient="vertical", command=canvas2.yview)
        canvas2.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        # vsb.grid(row=1, column=0, columnspan=2, rowspan=4,padx=5, sticky=E)

        frame2 = tk.Frame(canvas2)
        canvas2.create_window((4, 4), window=frame2, anchor="nw")
        frame2.bind("<Configure>", lambda event, canvas=canvas2: self.onFrameConfigure(canvas2))

        self.frame2 = frame2

        abtn = tk.Button(self.parent, text="Generate", width=10, command=self.callback)
        abtn.grid(row=1, column=3)

        cbtn = tk.Button(self.parent, text="clear", width=10, command=self.clear_frame)
        cbtn.grid(row=2, column=3, pady=4)

        obtn = tk.Button(self.parent, text="Close", width=10, command=self.quit)
        obtn.grid(row=5, column=3)


def main():
    root = Tk()
    root.geometry("885x700+10+10")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
