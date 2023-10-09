import customtkinter
from tkinter import *
from PIL import Image
import os
from csv import DictReader
from back_end import import_csv_database
from varname import nameof

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

        """
        # Angiv baggrundsbillede til vindue
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/media/highscore.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)
        """

        # lav tæller
        def tæl(film_antal,score_antal):
            
            counter_1 = 1
            for i in range(film_antal):
                
                #definer starts counter
                counter_2 = 1
                
                # lav loop, der gentager sig et bestemt antal gange
                for j in range(score_antal):
                    
                    # print counter
                    titel = "film_" + str(counter_1) + "_score_" + str(counter_2)
                                        
                    setattr(self, titel, customtkinter.CTkLabel(self, state="normal", text=titel)) #equivalent to: self.varname= 'something'

                    print(nameof(self.vartitel))

                    x_position = counter_1 / 10 + 0.2

                    self.vartitel.place(relx= x_position, rely=0.5, anchor=CENTER)


                    
                    # Tilføj 1 i slutning af loop.
                    counter_2 = counter_2 + 1


                counter_1 = counter_1 + 1
                
        # Aktiver tæller       
        tæl(2, 5)





       


       


if __name__ == "__main__":
    app = App()
    app.mainloop()
