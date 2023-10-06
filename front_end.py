import customtkinter
from tkinter import *
from PIL import Image
import os
from csv import DictReader
from back_end import import_csv_database

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





        """
        # Definer text_label
        text_label = customtkinter.CTkLabel(self, 
                                                   state="normal", 
                                                   text="Film_1, 8, 4, 6, 4, 6, 56", 
                                                   width=900, 
                                                   height=400,
                                                   text_color="black", 
                                                   fg_color="white",
                                                   font=("Helvetica", 30)
                                                   )
                                            
    
        # Indsæt text_label i vindue
        text_label.place(relx=0.5, rely=0.7, anchor=CENTER)
        """

        # --------------------------- film 1 labels ------------------------------------ #
        # Definer film_1_titel
        film_1_titel = customtkinter.CTkLabel(self, state="normal", text="Film_1_titel")

        # Indsæt film_1_titel i vindue
        film_1_titel.place(relx=0.2, rely=0.5, anchor=CENTER)


        # Definer film_1_score_1
        film_1_score_1 = customtkinter.CTkLabel(self, state="normal", text="Film_1_score_1")

        # Indsæt film_1_score_1 i vindue
        film_1_score_1.place(relx=0.3, rely=0.5, anchor=CENTER)


        # Definer film_1_score_2
        film_1_score_2 = customtkinter.CTkLabel(self, state="normal", text="Film_1_score_2")

        # Indsæt film_1_score_2 i vindue
        film_1_score_2.place(relx=0.4, rely=0.5, anchor=CENTER)


        # Definer film_1_score_3
        film_1_score_3 = customtkinter.CTkLabel(self, state="normal", text="Film_1_score_3")

        # Indsæt film_1_score_3 i vindue
        film_1_score_3.place(relx=0.5, rely=0.5, anchor=CENTER)


        # Definer film_1_score_4
        film_1_score_4 = customtkinter.CTkLabel(self, state="normal", text="Film_1_score_4")

        # Indsæt film_1_score_4 i vindue
        film_1_score_4.place(relx=0.6, rely=0.5, anchor=CENTER)


        # Definer film_1_score_5
        film_1_score_5 = customtkinter.CTkLabel(self, state="normal", text="Film_1_score_5")

        # Indsæt film_1_score_5 i vindue
        film_1_score_5.place(relx=0.7, rely=0.5, anchor=CENTER)



        # Definer film_1_total_score
        film_1_total_score = customtkinter.CTkLabel(self, state="normal", text="Film_1_total_score")

        # Indsæt film_1_score_5 i vindue
        film_1_total_score.place(relx=0.8, rely=0.5, anchor=CENTER)

        # ------------------------------------------------------------------------- #



        # --------------------------- film 2 labels ------------------------------------ #
        # Definer film_2_titel
        film_2_titel = customtkinter.CTkLabel(self, state="normal", text="Film_2_titel")

        # Indsæt film_2_titel i vindue
        film_2_titel.place(relx=0.2, rely=0.55, anchor=CENTER)


        # Definer film_2_score_1
        film_2_score_1 = customtkinter.CTkLabel(self, state="normal", text="Film_2_score_1")

        # Indsæt film_2_score_1 i vindue
        film_2_score_1.place(relx=0.3, rely=0.55, anchor=CENTER)


        # Definer film_2_score_2
        film_2_score_2 = customtkinter.CTkLabel(self, state="normal", text="Film_2_score_2")

        # Indsæt film_2_score_2 i vindue
        film_2_score_2.place(relx=0.4, rely=0.55, anchor=CENTER)


        # Definer film_2_score_3
        film_2_score_3 = customtkinter.CTkLabel(self, state="normal", text="Film_2_score_3")

        # Indsæt film_2_score_3 i vindue
        film_2_score_3.place(relx=0.5, rely=0.55, anchor=CENTER)


        # Definer film_2_score_4
        film_2_score_4 = customtkinter.CTkLabel(self, state="normal", text="Film_2_score_4")

        # Indsæt film_2_score_4 i vindue
        film_2_score_4.place(relx=0.6, rely=0.55, anchor=CENTER)


        # Definer film_2_score_5
        film_2_score_5 = customtkinter.CTkLabel(self, state="normal", text="Film_2_score_5")

        # Indsæt film_2_score_5 i vindue
        film_2_score_5.place(relx=0.7, rely=0.55, anchor=CENTER)



        # Definer film_2_total_score
        film_2_total_score = customtkinter.CTkLabel(self, state="normal", text="Film_2_total_score")

        # Indsæt film_2_score_5 i vindue
        film_2_total_score.place(relx=0.8, rely=0.55, anchor=CENTER)

        # ------------------------------------------------------------------------- #



        # --------------------------- film 3 labels ------------------------------------ #
        # Definer film_3_titel
        film_3_titel = customtkinter.CTkLabel(self, state="normal", text="Film_3_titel")

        # Indsæt film_3_titel i vindue
        film_3_titel.place(relx=0.2, rely=0.6, anchor=CENTER)


        # Definer film_3_score_1
        film_3_score_1 = customtkinter.CTkLabel(self, state="normal", text="Film_3_score_1")

        # Indsæt film_3_score_1 i vindue
        film_3_score_1.place(relx=0.3, rely=0.6, anchor=CENTER)


        # Definer film_3_score_2
        film_3_score_2 = customtkinter.CTkLabel(self, state="normal", text="Film_3_score_2")

        # Indsæt film_3_score_2 i vindue
        film_3_score_2.place(relx=0.4, rely=0.6, anchor=CENTER)


        # Definer film_3_score_3
        film_3_score_3 = customtkinter.CTkLabel(self, state="normal", text="Film_3_score_3")

        # Indsæt film_3_score_3 i vindue
        film_3_score_3.place(relx=0.5, rely=0.6, anchor=CENTER)


        # Definer film_3_score_4
        film_3_score_4 = customtkinter.CTkLabel(self, state="normal", text="Film_3_score_4")

        # Indsæt film_3_score_4 i vindue
        film_3_score_4.place(relx=0.6, rely=0.6, anchor=CENTER)


        # Definer film_3_score_5
        film_3_score_5 = customtkinter.CTkLabel(self, state="normal", text="Film_3_score_5")

        # Indsæt film_3_score_5 i vindue
        film_3_score_5.place(relx=0.7, rely=0.6, anchor=CENTER)



        # Definer film_3_total_score
        film_3_total_score = customtkinter.CTkLabel(self, state="normal", text="Film_3_total_score")

        # Indsæt film_3_score_5 i vindue
        film_3_total_score.place(relx=0.8, rely=0.6, anchor=CENTER)

        # ------------------------------------------------------------------------- #


        # --------------------------- film 4 labels ------------------------------------ #
        # Definer film_4_titel
        film_4_titel = customtkinter.CTkLabel(self, state="normal", text="Film_4_titel")

        # Indsæt film_4_titel i vindue
        film_4_titel.place(relx=0.2, rely=0.65, anchor=CENTER)


        # Definer film_4_score_1
        film_4_score_1 = customtkinter.CTkLabel(self, state="normal", text="Film_4_score_1")

        # Indsæt film_4_score_1 i vindue
        film_4_score_1.place(relx=0.3, rely=0.65, anchor=CENTER)


        # Definer film_4_score_2
        film_4_score_2 = customtkinter.CTkLabel(self, state="normal", text="Film_4_score_2")

        # Indsæt film_4_score_2 i vindue
        film_4_score_2.place(relx=0.4, rely=0.65, anchor=CENTER)


        # Definer film_4_score_3
        film_4_score_3 = customtkinter.CTkLabel(self, state="normal", text="Film_4_score_3")

        # Indsæt film_4_score_3 i vindue
        film_4_score_3.place(relx=0.5, rely=0.65, anchor=CENTER)


        # Definer film_4_score_4
        film_4_score_4 = customtkinter.CTkLabel(self, state="normal", text="Film_4_score_4")

        # Indsæt film_4_score_4 i vindue
        film_4_score_4.place(relx=0.6, rely=0.65, anchor=CENTER)


        # Definer film_4_score_5
        film_4_score_5 = customtkinter.CTkLabel(self, state="normal", text="Film_4_score_5")

        # Indsæt film_4_score_5 i vindue
        film_4_score_5.place(relx=0.7, rely=0.65, anchor=CENTER)



        # Definer film_4_total_score
        film_4_total_score = customtkinter.CTkLabel(self, state="normal", text="Film_4_total_score")

        # Indsæt film_4_score_5 i vindue
        film_4_total_score.place(relx=0.8, rely=0.65, anchor=CENTER)

        # ------------------------------------------------------------------------- #


        # --------------------------- film 5 labels ------------------------------------ #
        # Definer film_5_titel
        film_5_titel = customtkinter.CTkLabel(self, state="normal", text="Film_5_titel")

        # Indsæt film_5_titel i vindue
        film_5_titel.place(relx=0.2, rely=0.7, anchor=CENTER)


        # Definer film_5_score_1
        film_5_score_1 = customtkinter.CTkLabel(self, state="normal", text="Film_5_score_1")

        # Indsæt film_5_score_1 i vindue
        film_5_score_1.place(relx=0.3, rely=0.7, anchor=CENTER)


        # Definer film_5_score_2
        film_5_score_2 = customtkinter.CTkLabel(self, state="normal", text="Film_5_score_2")

        # Indsæt film_5_score_2 i vindue
        film_5_score_2.place(relx=0.4, rely=0.7, anchor=CENTER)


        # Definer film_5_score_3
        film_5_score_3 = customtkinter.CTkLabel(self, state="normal", text="Film_5_score_3")

        # Indsæt film_5_score_3 i vindue
        film_5_score_3.place(relx=0.5, rely=0.7, anchor=CENTER)


        # Definer film_5_score_4
        film_5_score_4 = customtkinter.CTkLabel(self, state="normal", text="Film_5_score_4")

        # Indsæt film_5_score_4 i vindue
        film_5_score_4.place(relx=0.6, rely=0.7, anchor=CENTER)


        # Definer film_5_score_5
        film_5_score_5 = customtkinter.CTkLabel(self, state="normal", text="Film_5_score_5")

        # Indsæt film_5_score_5 i vindue
        film_5_score_5.place(relx=0.7, rely=0.7, anchor=CENTER)



        # Definer film_5_total_score
        film_5_total_score = customtkinter.CTkLabel(self, state="normal", text="Film_5_total_score")

        # Indsæt film_5_score_5 i vindue
        film_5_total_score.place(relx=0.8, rely=0.7, anchor=CENTER)

        # ------------------------------------------------------------------------- #





        # ------------------------------- SORT BY-funktion ---------------------------- #
        
        def sort_by_total_score_function():
            dict = import_csv_database()

            print(dict[''])

            film_1_titel.configure()
            film_1_score_1.configure()
            film_1_score_2.configure()
            film_1_score_3.configure()
            film_1_score_4.configure()
            film_1_score_5.configure()
            film_1_total_score.configure()








        # ------------------------------- SORT BY-knap ---------------------------- #

        # Definer sort_by_total_score
        sort_by_total_score = customtkinter.CTkButton(self, text="TOTAL SCORE", width=185, command=sort_by_total_score_function)

        # Indsæt sort_by_total_score i vindue
        sort_by_total_score.place(relx=0.5, rely=0.4, anchor=CENTER)

        # -------------------------------------------------------------------- #


        # Definer sort_by_fede_skurke
        

        # Indsæt sort_by_fede_skurke i vindue
    

        # Definer sort_by_bar_hud


        # Definer sort_by_vilde_våben


        # Definer sort_by_oneliners


        # Definer sort_by_episk_action


       


if __name__ == "__main__":
    app = App()
    app.mainloop()
