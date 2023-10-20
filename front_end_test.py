import customtkinter
from tkinter import *
from PIL import Image
import os
from csv import DictReader
#from back_end import import_csv_database
import pandas as pd


# Definer CTk tema
customtkinter.set_appearance_mode("dark")


# definer scroll_frame
class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, rows, columns, **kwargs):
        super().__init__(master, **kwargs)
        self.generate_labels(rows, columns)
        
    def generate_labels(self, rows, columns):
        for row in range(rows):
            for column in range(columns):
                label = customtkinter.CTkLabel(self)
                label.grid(row=row, column=column, padx=20)



# Lav vindue
class App(customtkinter.CTk):
    width = 1440
    height = 900

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Hakkelademands leksikon")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        """
        # Angiv baggrundsbillede til vindue
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/media/highscore.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)
        """




        sorted_row_rely = 0.5
        film_1_rely = 0.55
        film_2_rely = 0.6
        film_3_rely = 0.65
        film_4_rely = 0.7
        film_5_rely = 0.75



     

        scaling_size = 4
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/media/hk_icon_2.png"),
                                               size=( 100 * scaling_size, 100 * scaling_size))

        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
      
        self.bg_image_label.place(relx= 0.5, rely=0.2, anchor=CENTER)




        # Placer scroll_frame i window
        self.my_frame = MyFrame(master=self, width=1000, height=400)
        self.my_frame.place(relx=0.5, rely=0.7, anchor=CENTER)




       


if __name__ == "__main__":
    app = App()
    my_frame = MyFrame(app, rows=3, columns=2)
    my_frame.pack()
    app.mainloop()
