import customtkinter as ctk
from tkinter import *
from PIL import Image
import os
from csv import DictReader
#from back_end import import_csv_database
import pandas as pd


# Definer CTk tema
ctk.set_appearance_mode("dark")




# Lav vindue
class App(ctk.CTk):
    width = 1440
    height = 900

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Hakkelademands leksikon")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

       

         # Definer label
        text_label = ctk.CTkLabel(self, state="normal", text="halløjsovs skipper")

        # Indsæt label i vindue
        text_label.place(relx=0.5, rely= 0.5, anchor=CENTER)


        # Definer sort_by_total_score
        alex_button = ctk.CTkButton(self, text="uhh press me daddy", width=120) # indsæt command=command_navn_her

        # Indsæt sort_by_total_score i vindue
        alex_button.place(relx=0.5, rely= 0.4, anchor=CENTER)


        



     

        




       


if __name__ == "__main__":
    app = App()
    app.mainloop()
