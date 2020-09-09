import tkinter.ttk as ttk
from tkinter import *
from PrepareData import *

class SelectDataWindow(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.master = master
        self.master.maxsize(800, 650)
        self.master.minsize(800, 650)
        self.master.title("DDSM images processor")
        self.pack(fill="both", expand=True)

        self.img_type_categories = ("normal", "cancer", "benign")
        self.density_categories = ("1", "2", "3", "4")
        self.subtlety_categories = ("1", "2", "3", "4", "5")
        self.assessment_categories = ("1", "2", "3", "4", "5")
        self.lesion_categories = ("SHAPE IRREGULAR", "SHAPE ARCHITECTURAL_DISTORTION", "MARGINS SPICULATED")

        self.layout()


    def layout(self):

        title = ttk.Label(self, text="Select images", style="title.TLabel")
        title.place(x=0, y=30)

        img_type_labelframe = LabelFrame(self.master, text="Type")
        density_labelframe = LabelFrame(self.master, text="Density")
        subtlety_labelframe = LabelFrame(self.master, text="Subtlety")
        assesment_labelframe = LabelFrame(self.master, text="Assessment")
        lesion_labelframe = LabelFrame(self.master, text="Lesion type")

        img_type_labelframe.place(x=50, y=110)
        density_labelframe.place(x=160, y=110)
        subtlety_labelframe.place(x=230, y=110)
        assesment_labelframe.place(x=300, y=110)
        lesion_labelframe.place(x=380, y=110)

        self.img_type_var_categories = self.create_checkbox_grid(img_type_labelframe, self.img_type_categories)
        self.den_var_categories = self.create_checkbox_grid(density_labelframe, self.density_categories)
        self.subt_var_categories = self.create_checkbox_grid(subtlety_labelframe, self.subtlety_categories)
        self.assesm_var_categories = self.create_checkbox_grid(assesment_labelframe, self.assessment_categories)
        self.lesion_var_categories = self.create_checkbox_grid(lesion_labelframe, self.lesion_categories)

        b3 = ttk.Button(self.master, text="Select images", command=lambda: self.select_images())
        b3.place(x=525, y=330)

        data = [["val1", "val2", "val3"],
                ["asd1", "asd2", "asd3"],
                ["bbb1", "bbb3", "bbb4"],
                ["ccc1", "ccc3", "ccc4"],
                ["ddd1", "ddd3", "ddd4"],
                ["eee1", "eee3", "eee4"]]


        tree = ttk.Treeview(self.master, columns=(1, 2, 3), height=5, show="headings")
        # tree.place(x=75, y=430)

        tree.heading(1, text="Column 1")
        tree.heading(2, text="Column 2")
        tree.heading(3, text="Column 3")

        tree.column(1, width=100)
        tree.column(2, width=100)
        tree.column(3, width=100)

        #scroll = ttk.Scrollbar(self.master, orient="vertical", command=tree.yview)
        #scroll.place(x=525, y=400)

        #tree.configure(yscrollcommand=scroll.set)

        for val in data:
            tree.insert('', 'end', values=(val[0], val[1], val[2]))


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

    def create_checkbox_grid(self, label, categories):
        iterator = iter(categories)

        var_categories = {}
        chckbx_categories = {}

        for r in range(len(categories)):
            self.master.columnconfigure(1, weight=1)
            self.master.rowconfigure(r, weight=1)

            # for c in range(3):
            item = next(iterator)

            var = IntVar()

            cb = Checkbutton(label, text=item, variable=var, onvalue=1, offvalue=0,
                                font=('Lucida Grande', 15), anchor='w', bg='#FFFFFF')
            cb.grid(row=r, column=1, sticky='news')

            var_categories[item] = var
            chckbx_categories[item] = cb

        return var_categories

    def get_checked_boxes(self, categories, type):

        conditions_list = []

        for key in categories:
            if categories[key].get():
                print(type, key)
                conditions_list.append(key)

        return conditions_list

    def select_images(self):

        all_conditions_list = {"DENSITY": self.get_checked_boxes(self.den_var_categories, "DENSITY"),
                               "SUBTLETY": self.get_checked_boxes(self.subt_var_categories, "SUBTLETY"),
                               "ASSESSMENT": self.get_checked_boxes(self.assesm_var_categories, "ASSESSMENT"),
                               "LESION_TYPE": self.get_checked_boxes(self.lesion_var_categories, "LESION_TYPE")}

        selected_data = PrepareData(all_conditions_list)
        selected_data.count_values()

        return all_conditions_list





