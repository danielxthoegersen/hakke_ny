import customtkinter
from tkinter import *
from PIL import Image
import os

# Definer CTk tema
customtkinter.set_appearance_mode("dark")


# Lav vindue
class App(customtkinter.CTk):
    width = 1440
    height = 900

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Hakkelademands leksikon")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # Angiv baggrundsbillede til vindue
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/media/highscore.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)



        # Definer text_label
        text_label = customtkinter.CTkLabel(self, 
                                                   state="normal", 
                                                   text="Film titel 1, 8, 4, 6, 4, 6, 56", 
                                                   width=900, 
                                                   height=400,
                                                   text_color="black", 
                                                   fg_color="white",
                                                   font=("Helvetica", 30)
                                                   )
    
        # Indsæt text_label i vindue
        text_label.place(relx=0.5, rely=0.7, anchor=CENTER)


        # Indsæt sort_by fede_skurke



if __name__ == "__main__":
    app = App()
    app.mainloop()
