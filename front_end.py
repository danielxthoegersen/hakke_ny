import customtkinter
import csv
from tkinter import *
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    width = 875
    height = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Hakkelademands leksikon")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/media/hakke_bkg.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)

    

        button = customtkinter.CTkButton(self, text="HAK!", text_color="black", fg_color="white", hover_color="gray", bg_color="white", border_width=0, width=185)

        score_entry1 = customtkinter.CTkEntry(self, placeholder_text="...", width=40, text_color="black", fg_color="white", bg_color="white", border_width=0, justify="center")
        score_entry2 = customtkinter.CTkEntry(self, placeholder_text="...", width=40, text_color="black", fg_color="white", bg_color="white", border_width=0, justify="center")
        score_entry3 = customtkinter.CTkEntry(self, placeholder_text="...", width=40, text_color="black", fg_color="white", bg_color="white", border_width=0, justify="center")
        score_entry4 = customtkinter.CTkEntry(self, placeholder_text="...", width=40, text_color="black", fg_color="white", bg_color="white", border_width=0, justify="center")
        score_entry5 = customtkinter.CTkEntry(self, placeholder_text="...", width=40, text_color="black", fg_color="white", bg_color="white", border_width=0, justify="center")

        film_entry = customtkinter.CTkEntry(self, placeholder_text="...", text_color="black", fg_color="white", bg_color="white", border_width=0, justify="center")

        total_score_label = customtkinter.CTkLabel(self, state="normal", text="???", width=40, text_color="gray", fg_color="white")

        film_entry.place(relx=0.21, rely=0.7125, anchor=CENTER)
        score_entry1.place(relx=0.387, rely=0.7125, anchor=CENTER)
        score_entry2.place(relx=0.478, rely=0.7125, anchor=CENTER)
        score_entry3.place(relx=0.57, rely=0.7125, anchor=CENTER)
        score_entry4.place(relx=0.657, rely=0.7125, anchor=CENTER)
        score_entry5.place(relx=0.743, rely=0.7125, anchor=CENTER)
        total_score_label.place(relx=0.834, rely=0.712, anchor=CENTER)
        button.place(relx=0.5, rely=0.865, anchor=CENTER)



if __name__ == "__main__":
    app = App()
    app.mainloop()
