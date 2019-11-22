import tkinter.ttk as ttk
from tkinter import *
import pandas as pd
from PrepareData import *


class AppWindow(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.master = master
        self.master.maxsize(700, 500)
        self.master.minsize(700, 500)
        self.master.title("DDSM images processor")
        self.pack(fill="both", expand=True)

        self.density_1 = IntVar()
        self.density_2 = IntVar()
        self.density_3 = IntVar()
        self.density_4 = IntVar()
        self.var_1 = IntVar()
        self.var_2 = IntVar()
        self.var_3 = IntVar()
        self.var_n = IntVar()
        self.var_c = IntVar()
        self.var_b = IntVar()

        self.den_1_check = Checkbutton(self.master, text="1", variable=self.density_1)
        self.den_2_check = Checkbutton(self.master, text="2", variable=self.density_2)
        self.den_3_check = Checkbutton(self.master, text="3", variable=self.density_3)
        self.den_4_check = Checkbutton(self.master, text="4", variable=self.density_4)

        self.norm_check = Checkbutton(self.master, text="normal", variable=self.var_n)
        self.canc_check = Checkbutton(self.master, text="cancer", variable=self.var_c)
        self.ben_check = Checkbutton(self.master, text="benign", variable=self.var_b)

        self.c1 = Checkbutton(self.master, text="SHAPE IRREGULAR", variable=self.var_1)
        self.c2 = Checkbutton(self.master, text="SHAPE ARCHITECTURAL_DISTORTION", variable=self.var_2)
        self.c3 = Checkbutton(self.master, text="MARGINS SPICULATED", variable=self.var_3)

        # subtlety
        # assesment
        # rozdzielic zmiany od normalnych

        self.all_data = LoadData()

        self.layout()

    def layout(self):

        title = ttk.Label(self, text="Select images", style="title.TLabel")
        title.place(x=0, y=30)

        w = Label(self.master, text="Density", font=("Helvetica", 10))
        w.place(x=30, y=110)

        self.den_1_check.place(x=30, y=140)
        self.den_2_check.place(x=30, y=170)
        self.den_3_check.place(x=30, y=200)
        self.den_4_check.place(x=30, y=230)

        w = Label(self.master, text="Normal / Abnormality", font=("Helvetica", 10))
        w.place(x=170, y=110)

        self.norm_check.place(x=170, y=140)
        self.canc_check.place(x=250, y=140)
        self.ben_check.place(x=250, y=170)

        w = Label(self.master, text="Shape & Lesion Type", font=("Helvetica", 10))
        w.place(x=400, y=110)

        self.c1.place(x=400, y=140)
        self.c2.place(x=400, y=170)
        self.c3.place(x=400, y=200)

        selected_option_var = StringVar(self.master)
        selected_option_var.set("one")  # initial value

        b3 = ttk.Button(self, text="Select images", command = lambda: self.select_images())
        b3.place(x=165, y=290)

        # ----------- STYLES ------------

        style = ttk.Style()

        style.configure("TFrame",
                        background="#607D8B"
                        )
        style.configure("title.TLabel",
                        background="#455A64",
                        foreground="#42A5F5",
                        font="Arial 20 bold",
                        width=500,
                        padding=10
                        )

        style.configure("txt.TLabel",
                        background="#607D8B",
                        foreground="#B0BEC5",
                        font="Arial 12",
                        )


    def select_images(self):

        df = pd.DataFrame()

        if (self.var_n.get() and self.var_c.get()) or (self.var_n.get() and self.var_b.get()):
            pass # popup window

        if self.var_n.get():
            df = self.all_data.normals_df
        if self.var_c.get():
            df = self.all_data.cancers_abnormalities_df
        if self.var_b.get():
            df = self.all_data.benigns_abnormalities_df
        if self.var_c.get() and self.var_b.get():
            df = pd.concat([self.all_data.cancers_abnormalities_df, self.all_data.benigns_abnormalities_df], sort=True)

        conditions = []

        if self.var_1.get():
            conditions.append(self.c1.cget("text"))
        if self.var_2.get():
            conditions.append(self.c2.cget("text"))
        if self.var_3.get():
            conditions.append(self.c3.cget("text"))

        if self.density_check.get():
            if len(conditions) > 0:
                stats = PrepareData(df, density=4, lesion_type_list=conditions).count_values()
            else:
                stats = PrepareData(df, density=4).count_values()
        else:
            if len(conditions) > 0:
                stats = PrepareData(df, lesion_type_list=conditions).count_values()
            else:
                stats = PrepareData(df).count_values()

        print(stats)

