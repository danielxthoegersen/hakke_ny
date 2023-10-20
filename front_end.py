import customtkinter
from tkinter import *
from PIL import Image
import os
from csv import DictReader
#from back_end import import_csv_database
import pandas as pd


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



        # --------------------------- film 1 labels ------------------------------------ #
        # Definer film_1_titel
        film_1_titel = customtkinter.CTkLabel(self, state="normal", text="Film_1_titel")

        # Indsæt film_1_titel i vindue
        film_1_titel.place(relx=0.2, rely= film_1_rely, anchor=CENTER)


        # Definer film_1_score_1
        film_1_score_1 = customtkinter.CTkLabel(self, state="normal", text="Film_1_score_1")

        # Indsæt film_1_score_1 i vindue
        film_1_score_1.place(relx=0.3, rely= film_1_rely, anchor=CENTER)


        # Definer film_1_score_2
        film_1_score_2 = customtkinter.CTkLabel(self, state="normal", text="Film_1_score_2")

        # Indsæt film_1_score_2 i vindue
        film_1_score_2.place(relx=0.4, rely= film_1_rely, anchor=CENTER)


        # Definer film_1_score_3
        film_1_score_3 = customtkinter.CTkLabel(self, state="normal", text="Film_1_score_3")

        # Indsæt film_1_score_3 i vindue
        film_1_score_3.place(relx=0.5, rely= film_1_rely, anchor=CENTER)


        # Definer film_1_score_4
        film_1_score_4 = customtkinter.CTkLabel(self, state="normal", text="Film_1_score_4")

        # Indsæt film_1_score_4 i vindue
        film_1_score_4.place(relx=0.6, rely= film_1_rely, anchor=CENTER)


        # Definer film_1_score_5
        film_1_score_5 = customtkinter.CTkLabel(self, state="normal", text="Film_1_score_5")

        # Indsæt film_1_score_5 i vindue
        film_1_score_5.place(relx=0.7, rely= film_1_rely, anchor=CENTER)



        # Definer film_1_total_score
        film_1_total_score = customtkinter.CTkLabel(self, state="normal", text="Film_1_total_score")

        # Indsæt film_1_score_5 i vindue
        film_1_total_score.place(relx=0.8, rely= film_1_rely, anchor=CENTER)

        # ------------------------------------------------------------------------- #



        # --------------------------- film 2 labels ------------------------------------ #
        # Definer film_2_titel
        film_2_titel = customtkinter.CTkLabel(self, state="normal", text="Film_2_titel")

        # Indsæt film_2_titel i vindue
        film_2_titel.place(relx=0.2, rely= film_2_rely, anchor=CENTER)


        # Definer film_2_score_1
        film_2_score_1 = customtkinter.CTkLabel(self, state="normal", text="Film_2_score_1")

        # Indsæt film_2_score_1 i vindue
        film_2_score_1.place(relx=0.3, rely= film_2_rely, anchor=CENTER)


        # Definer film_2_score_2
        film_2_score_2 = customtkinter.CTkLabel(self, state="normal", text="Film_2_score_2")

        # Indsæt film_2_score_2 i vindue
        film_2_score_2.place(relx=0.4, rely= film_2_rely, anchor=CENTER)


        # Definer film_2_score_3
        film_2_score_3 = customtkinter.CTkLabel(self, state="normal", text="Film_2_score_3")

        # Indsæt film_2_score_3 i vindue
        film_2_score_3.place(relx=0.5, rely= film_2_rely, anchor=CENTER)


        # Definer film_2_score_4
        film_2_score_4 = customtkinter.CTkLabel(self, state="normal", text="Film_2_score_4")

        # Indsæt film_2_score_4 i vindue
        film_2_score_4.place(relx=0.6, rely= film_2_rely, anchor=CENTER)


        # Definer film_2_score_5
        film_2_score_5 = customtkinter.CTkLabel(self, state="normal", text="Film_2_score_5")

        # Indsæt film_2_score_5 i vindue
        film_2_score_5.place(relx=0.7, rely= film_2_rely, anchor=CENTER)



        # Definer film_2_total_score
        film_2_total_score = customtkinter.CTkLabel(self, state="normal", text="Film_2_total_score")

        # Indsæt film_2_score_5 i vindue
        film_2_total_score.place(relx=0.8, rely= film_2_rely, anchor=CENTER)

        # ------------------------------------------------------------------------- #



        # --------------------------- film 3 labels ------------------------------------ #
        # Definer film_3_titel
        film_3_titel = customtkinter.CTkLabel(self, state="normal", text="Film_3_titel")

        # Indsæt film_3_titel i vindue
        film_3_titel.place(relx=0.2, rely= film_3_rely, anchor=CENTER)


        # Definer film_3_score_1
        film_3_score_1 = customtkinter.CTkLabel(self, state="normal", text="Film_3_score_1")

        # Indsæt film_3_score_1 i vindue
        film_3_score_1.place(relx=0.3, rely= film_3_rely, anchor=CENTER)


        # Definer film_3_score_2
        film_3_score_2 = customtkinter.CTkLabel(self, state="normal", text="Film_3_score_2")

        # Indsæt film_3_score_2 i vindue
        film_3_score_2.place(relx=0.4, rely= film_3_rely, anchor=CENTER)


        # Definer film_3_score_3
        film_3_score_3 = customtkinter.CTkLabel(self, state="normal", text="Film_3_score_3")

        # Indsæt film_3_score_3 i vindue
        film_3_score_3.place(relx=0.5, rely= film_3_rely, anchor=CENTER)


        # Definer film_3_score_4
        film_3_score_4 = customtkinter.CTkLabel(self, state="normal", text="Film_3_score_4")

        # Indsæt film_3_score_4 i vindue
        film_3_score_4.place(relx=0.6, rely= film_3_rely, anchor=CENTER)


        # Definer film_3_score_5
        film_3_score_5 = customtkinter.CTkLabel(self, state="normal", text="Film_3_score_5")

        # Indsæt film_3_score_5 i vindue
        film_3_score_5.place(relx=0.7, rely= film_3_rely, anchor=CENTER)



        # Definer film_3_total_score
        film_3_total_score = customtkinter.CTkLabel(self, state="normal", text="Film_3_total_score")

        # Indsæt film_3_score_5 i vindue
        film_3_total_score.place(relx=0.8, rely= film_3_rely, anchor=CENTER)

        # ------------------------------------------------------------------------- #


        # --------------------------- film 4 labels ------------------------------------ #
        # Definer film_4_titel
        film_4_titel = customtkinter.CTkLabel(self, state="normal", text="Film_4_titel")

        # Indsæt film_4_titel i vindue
        film_4_titel.place(relx=0.2, rely= film_4_rely, anchor=CENTER)


        # Definer film_4_score_1
        film_4_score_1 = customtkinter.CTkLabel(self, state="normal", text="Film_4_score_1")

        # Indsæt film_4_score_1 i vindue
        film_4_score_1.place(relx=0.3, rely= film_4_rely, anchor=CENTER)


        # Definer film_4_score_2
        film_4_score_2 = customtkinter.CTkLabel(self, state="normal", text="Film_4_score_2")

        # Indsæt film_4_score_2 i vindue
        film_4_score_2.place(relx=0.4, rely= film_4_rely, anchor=CENTER)


        # Definer film_4_score_3
        film_4_score_3 = customtkinter.CTkLabel(self, state="normal", text="Film_4_score_3")

        # Indsæt film_4_score_3 i vindue
        film_4_score_3.place(relx=0.5, rely= film_4_rely, anchor=CENTER)


        # Definer film_4_score_4
        film_4_score_4 = customtkinter.CTkLabel(self, state="normal", text="Film_4_score_4")

        # Indsæt film_4_score_4 i vindue
        film_4_score_4.place(relx=0.6, rely= film_4_rely, anchor=CENTER)


        # Definer film_4_score_5
        film_4_score_5 = customtkinter.CTkLabel(self, state="normal", text="Film_4_score_5")

        # Indsæt film_4_score_5 i vindue
        film_4_score_5.place(relx=0.7, rely= film_4_rely, anchor=CENTER)



        # Definer film_4_total_score
        film_4_total_score = customtkinter.CTkLabel(self, state="normal", text="Film_4_total_score")

        # Indsæt film_4_score_5 i vindue
        film_4_total_score.place(relx=0.8, rely= film_4_rely, anchor=CENTER)

        # ------------------------------------------------------------------------- #


        # --------------------------- film 5 labels ------------------------------------ #
        # Definer film_5_titel
        film_5_titel = customtkinter.CTkLabel(self, state="normal", text="Film_5_titel")

        # Indsæt film_5_titel i vindue
        film_5_titel.place(relx=0.2, rely= film_5_rely, anchor=CENTER)


        # Definer film_5_score_1
        film_5_score_1 = customtkinter.CTkLabel(self, state="normal", text="Film_5_score_1")

        # Indsæt film_5_score_1 i vindue
        film_5_score_1.place(relx=0.3, rely= film_5_rely, anchor=CENTER)


        # Definer film_5_score_2
        film_5_score_2 = customtkinter.CTkLabel(self, state="normal", text="Film_5_score_2")

        # Indsæt film_5_score_2 i vindue
        film_5_score_2.place(relx=0.4, rely= film_5_rely, anchor=CENTER)


        # Definer film_5_score_3
        film_5_score_3 = customtkinter.CTkLabel(self, state="normal", text="Film_5_score_3")

        # Indsæt film_5_score_3 i vindue
        film_5_score_3.place(relx=0.5, rely= film_5_rely, anchor=CENTER)


        # Definer film_5_score_4
        film_5_score_4 = customtkinter.CTkLabel(self, state="normal", text="Film_5_score_4")

        # Indsæt film_5_score_4 i vindue
        film_5_score_4.place(relx=0.6, rely= film_5_rely, anchor=CENTER)


        # Definer film_5_score_5
        film_5_score_5 = customtkinter.CTkLabel(self, state="normal", text="Film_5_score_5")

        # Indsæt film_5_score_5 i vindue
        film_5_score_5.place(relx=0.7, rely= film_5_rely, anchor=CENTER)



        # Definer film_5_total_score
        film_5_total_score = customtkinter.CTkLabel(self, state="normal", text="Film_5_total_score")

        # Indsæt film_5_score_5 i vindue
        film_5_total_score.place(relx=0.8, rely= film_5_rely, anchor=CENTER)

        # ------------------------------------------------------------------------- #





        # ------------------------------- SORT BY TOTAL SCORE-funktion ---------------------------- #
        
        def sort_by_total_score_function():

            colnames=["film_titel", "fede_skurke", "bar_hud", "vilde_våben", "one_liners", "episk_action", "total_score"]

            # Hent data
            df = pd.read_csv("database_dummy.csv", names=colnames, header=None)

            sorted_database = df.sort_values("total_score", ascending=False)
            sorted_line_number = 0
            sorted_column_number = 0

            # --------- FILM 1 ------- #

            # hent data under variable
            film_1_titel_data = sorted_database.iloc[sorted_line_number][sorted_column_number]
            film_1_score_1_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 1]
            film_1_score_2_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 2]
            film_1_score_3_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 3]
            film_1_score_4_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 4]
            film_1_score_5_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 5]
            film_1_total_score_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 6]


            # Opdater tekst i labels
            film_1_titel.configure(text=film_1_titel_data)
            film_1_score_1.configure(text=film_1_score_1_data)
            film_1_score_2.configure(text=film_1_score_2_data)
            film_1_score_3.configure(text=film_1_score_3_data)
            film_1_score_4.configure(text=film_1_score_4_data)
            film_1_score_5.configure(text=film_1_score_5_data)
            film_1_total_score.configure(text=film_1_total_score_data)

            # ---------------------------------- #

             # --------- FILM 2 ------- #

            # hent data under variable
            film_2_titel_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number]
            film_2_score_1_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 1]
            film_2_score_2_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 2]
            film_2_score_3_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 3]
            film_2_score_4_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 4]
            film_2_score_5_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 5]
            film_2_total_score_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 6]


            # Opdater tekst i labels
            film_2_titel.configure(text=film_2_titel_data)
            film_2_score_1.configure(text=film_2_score_1_data)
            film_2_score_2.configure(text=film_2_score_2_data)
            film_2_score_3.configure(text=film_2_score_3_data)
            film_2_score_4.configure(text=film_2_score_4_data)
            film_2_score_5.configure(text=film_2_score_5_data)
            film_2_total_score.configure(text=film_2_total_score_data)

            # ---------------------------------- #


            # --------- FILM 3 ------- #

            # hent data under variable
            film_3_titel_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number]
            film_3_score_1_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 1]
            film_3_score_2_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 2]
            film_3_score_3_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 3]
            film_3_score_4_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 4]
            film_3_score_5_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 5]
            film_3_total_score_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 6]


            # Opdater tekst i labels
            film_3_titel.configure(text=film_3_titel_data)
            film_3_score_1.configure(text=film_3_score_1_data)
            film_3_score_2.configure(text=film_3_score_2_data)
            film_3_score_3.configure(text=film_3_score_3_data)
            film_3_score_4.configure(text=film_3_score_4_data)
            film_3_score_5.configure(text=film_3_score_5_data)
            film_3_total_score.configure(text=film_3_total_score_data)

            # ---------------------------------- #


            # --------- FILM 4 ------- #

            # hent data under variable
            film_4_titel_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number]
            film_4_score_1_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 1]
            film_4_score_2_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 2]
            film_4_score_3_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 3]
            film_4_score_4_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 4]
            film_4_score_5_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 5]
            film_4_total_score_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 6]


            # Opdater tekst i labels
            film_4_titel.configure(text=film_4_titel_data)
            film_4_score_1.configure(text=film_4_score_1_data)
            film_4_score_2.configure(text=film_4_score_2_data)
            film_4_score_3.configure(text=film_4_score_3_data)
            film_4_score_4.configure(text=film_4_score_4_data)
            film_4_score_5.configure(text=film_4_score_5_data)
            film_4_total_score.configure(text=film_4_total_score_data)

            # ---------------------------------- #


            # --------- FILM 5 ------- #

            # hent data under variable
            film_5_titel_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number]
            film_5_score_1_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 1]
            film_5_score_2_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 2]
            film_5_score_3_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 3]
            film_5_score_4_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 4]
            film_5_score_5_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 5]
            film_5_total_score_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 6]


            # Opdater tekst i labels
            film_5_titel.configure(text=film_5_titel_data)
            film_5_score_1.configure(text=film_5_score_1_data)
            film_5_score_2.configure(text=film_5_score_2_data)
            film_5_score_3.configure(text=film_5_score_3_data)
            film_5_score_4.configure(text=film_5_score_4_data)
            film_5_score_5.configure(text=film_5_score_5_data)
            film_5_total_score.configure(text=film_5_total_score_data)

            # ---------------------------------- #








 # ------------------------------- SORT BY FEDE SKURKE-funktion ---------------------------- #
        
        def sort_by_fede_skurke_function():

            colnames=["film_titel", "fede_skurke", "bar_hud", "vilde_våben", "one_liners", "episk_action", "total_score"]

            # Hent data
            df = pd.read_csv("database_dummy.csv", names=colnames, header=None)

            sorted_database = df.sort_values("fede_skurke", ascending=False)
            sorted_line_number = 0
            sorted_column_number = 0

            # --------- FILM 1 ------- #

            # hent data under variable
            film_1_titel_data = sorted_database.iloc[sorted_line_number][sorted_column_number]
            film_1_score_1_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 1]
            film_1_score_2_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 2]
            film_1_score_3_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 3]
            film_1_score_4_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 4]
            film_1_score_5_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 5]
            film_1_total_score_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 6]


            # Opdater tekst i labels
            film_1_titel.configure(text=film_1_titel_data)
            film_1_score_1.configure(text=film_1_score_1_data)
            film_1_score_2.configure(text=film_1_score_2_data)
            film_1_score_3.configure(text=film_1_score_3_data)
            film_1_score_4.configure(text=film_1_score_4_data)
            film_1_score_5.configure(text=film_1_score_5_data)
            film_1_total_score.configure(text=film_1_total_score_data)

            # ---------------------------------- #

             # --------- FILM 2 ------- #

            # hent data under variable
            film_2_titel_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number]
            film_2_score_1_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 1]
            film_2_score_2_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 2]
            film_2_score_3_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 3]
            film_2_score_4_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 4]
            film_2_score_5_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 5]
            film_2_total_score_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 6]


            # Opdater tekst i labels
            film_2_titel.configure(text=film_2_titel_data)
            film_2_score_1.configure(text=film_2_score_1_data)
            film_2_score_2.configure(text=film_2_score_2_data)
            film_2_score_3.configure(text=film_2_score_3_data)
            film_2_score_4.configure(text=film_2_score_4_data)
            film_2_score_5.configure(text=film_2_score_5_data)
            film_2_total_score.configure(text=film_2_total_score_data)

            # ---------------------------------- #


            # --------- FILM 3 ------- #

            # hent data under variable
            film_3_titel_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number]
            film_3_score_1_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 1]
            film_3_score_2_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 2]
            film_3_score_3_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 3]
            film_3_score_4_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 4]
            film_3_score_5_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 5]
            film_3_total_score_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 6]


            # Opdater tekst i labels
            film_3_titel.configure(text=film_3_titel_data)
            film_3_score_1.configure(text=film_3_score_1_data)
            film_3_score_2.configure(text=film_3_score_2_data)
            film_3_score_3.configure(text=film_3_score_3_data)
            film_3_score_4.configure(text=film_3_score_4_data)
            film_3_score_5.configure(text=film_3_score_5_data)
            film_3_total_score.configure(text=film_3_total_score_data)

            # ---------------------------------- #


            # --------- FILM 4 ------- #

            # hent data under variable
            film_4_titel_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number]
            film_4_score_1_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 1]
            film_4_score_2_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 2]
            film_4_score_3_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 3]
            film_4_score_4_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 4]
            film_4_score_5_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 5]
            film_4_total_score_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 6]


            # Opdater tekst i labels
            film_4_titel.configure(text=film_4_titel_data)
            film_4_score_1.configure(text=film_4_score_1_data)
            film_4_score_2.configure(text=film_4_score_2_data)
            film_4_score_3.configure(text=film_4_score_3_data)
            film_4_score_4.configure(text=film_4_score_4_data)
            film_4_score_5.configure(text=film_4_score_5_data)
            film_4_total_score.configure(text=film_4_total_score_data)

            # ---------------------------------- #


            # --------- FILM 5 ------- #

            # hent data under variable
            film_5_titel_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number]
            film_5_score_1_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 1]
            film_5_score_2_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 2]
            film_5_score_3_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 3]
            film_5_score_4_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 4]
            film_5_score_5_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 5]
            film_5_total_score_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 6]


            # Opdater tekst i labels
            film_5_titel.configure(text=film_5_titel_data)
            film_5_score_1.configure(text=film_5_score_1_data)
            film_5_score_2.configure(text=film_5_score_2_data)
            film_5_score_3.configure(text=film_5_score_3_data)
            film_5_score_4.configure(text=film_5_score_4_data)
            film_5_score_5.configure(text=film_5_score_5_data)
            film_5_total_score.configure(text=film_5_total_score_data)

            # ---------------------------------- #







 # ------------------------------- SORT BY BAR HUD-funktion ---------------------------- #
        
        def sort_by_bar_hud_function():

            colnames=["film_titel", "fede_skurke", "bar_hud", "vilde_våben", "one_liners", "episk_action", "total_score"]

            # Hent data
            df = pd.read_csv("database_dummy.csv", names=colnames, header=None)

            sorted_database = df.sort_values("bar_hud", ascending=False)
            sorted_line_number = 0
            sorted_column_number = 0

            # --------- FILM 1 ------- #

            # hent data under variable
            film_1_titel_data = sorted_database.iloc[sorted_line_number][sorted_column_number]
            film_1_score_1_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 1]
            film_1_score_2_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 2]
            film_1_score_3_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 3]
            film_1_score_4_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 4]
            film_1_score_5_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 5]
            film_1_total_score_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 6]


            # Opdater tekst i labels
            film_1_titel.configure(text=film_1_titel_data)
            film_1_score_1.configure(text=film_1_score_1_data)
            film_1_score_2.configure(text=film_1_score_2_data)
            film_1_score_3.configure(text=film_1_score_3_data)
            film_1_score_4.configure(text=film_1_score_4_data)
            film_1_score_5.configure(text=film_1_score_5_data)
            film_1_total_score.configure(text=film_1_total_score_data)

            # ---------------------------------- #

             # --------- FILM 2 ------- #

            # hent data under variable
            film_2_titel_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number]
            film_2_score_1_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 1]
            film_2_score_2_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 2]
            film_2_score_3_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 3]
            film_2_score_4_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 4]
            film_2_score_5_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 5]
            film_2_total_score_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 6]


            # Opdater tekst i labels
            film_2_titel.configure(text=film_2_titel_data)
            film_2_score_1.configure(text=film_2_score_1_data)
            film_2_score_2.configure(text=film_2_score_2_data)
            film_2_score_3.configure(text=film_2_score_3_data)
            film_2_score_4.configure(text=film_2_score_4_data)
            film_2_score_5.configure(text=film_2_score_5_data)
            film_2_total_score.configure(text=film_2_total_score_data)

            # ---------------------------------- #


            # --------- FILM 3 ------- #

            # hent data under variable
            film_3_titel_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number]
            film_3_score_1_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 1]
            film_3_score_2_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 2]
            film_3_score_3_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 3]
            film_3_score_4_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 4]
            film_3_score_5_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 5]
            film_3_total_score_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 6]


            # Opdater tekst i labels
            film_3_titel.configure(text=film_3_titel_data)
            film_3_score_1.configure(text=film_3_score_1_data)
            film_3_score_2.configure(text=film_3_score_2_data)
            film_3_score_3.configure(text=film_3_score_3_data)
            film_3_score_4.configure(text=film_3_score_4_data)
            film_3_score_5.configure(text=film_3_score_5_data)
            film_3_total_score.configure(text=film_3_total_score_data)

            # ---------------------------------- #


            # --------- FILM 4 ------- #

            # hent data under variable
            film_4_titel_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number]
            film_4_score_1_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 1]
            film_4_score_2_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 2]
            film_4_score_3_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 3]
            film_4_score_4_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 4]
            film_4_score_5_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 5]
            film_4_total_score_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 6]


            # Opdater tekst i labels
            film_4_titel.configure(text=film_4_titel_data)
            film_4_score_1.configure(text=film_4_score_1_data)
            film_4_score_2.configure(text=film_4_score_2_data)
            film_4_score_3.configure(text=film_4_score_3_data)
            film_4_score_4.configure(text=film_4_score_4_data)
            film_4_score_5.configure(text=film_4_score_5_data)
            film_4_total_score.configure(text=film_4_total_score_data)

            # ---------------------------------- #


            # --------- FILM 5 ------- #

            # hent data under variable
            film_5_titel_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number]
            film_5_score_1_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 1]
            film_5_score_2_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 2]
            film_5_score_3_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 3]
            film_5_score_4_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 4]
            film_5_score_5_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 5]
            film_5_total_score_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 6]


            # Opdater tekst i labels
            film_5_titel.configure(text=film_5_titel_data)
            film_5_score_1.configure(text=film_5_score_1_data)
            film_5_score_2.configure(text=film_5_score_2_data)
            film_5_score_3.configure(text=film_5_score_3_data)
            film_5_score_4.configure(text=film_5_score_4_data)
            film_5_score_5.configure(text=film_5_score_5_data)
            film_5_total_score.configure(text=film_5_total_score_data)

            # ---------------------------------- #








# ------------------------------- SORT BY VILDE VÅBEN-funktion ---------------------------- #
        
        def sort_by_vilde_våben_function():

            colnames=["film_titel", "fede_skurke", "bar_hud", "vilde_våben", "one_liners", "episk_action", "total_score"]

            # Hent data
            df = pd.read_csv("database_dummy.csv", names=colnames, header=None)

            sorted_database = df.sort_values("vilde_våben", ascending=False)
            sorted_line_number = 0
            sorted_column_number = 0

            # --------- FILM 1 ------- #

            # hent data under variable
            film_1_titel_data = sorted_database.iloc[sorted_line_number][sorted_column_number]
            film_1_score_1_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 1]
            film_1_score_2_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 2]
            film_1_score_3_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 3]
            film_1_score_4_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 4]
            film_1_score_5_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 5]
            film_1_total_score_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 6]


            # Opdater tekst i labels
            film_1_titel.configure(text=film_1_titel_data)
            film_1_score_1.configure(text=film_1_score_1_data)
            film_1_score_2.configure(text=film_1_score_2_data)
            film_1_score_3.configure(text=film_1_score_3_data)
            film_1_score_4.configure(text=film_1_score_4_data)
            film_1_score_5.configure(text=film_1_score_5_data)
            film_1_total_score.configure(text=film_1_total_score_data)

            # ---------------------------------- #

             # --------- FILM 2 ------- #

            # hent data under variable
            film_2_titel_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number]
            film_2_score_1_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 1]
            film_2_score_2_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 2]
            film_2_score_3_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 3]
            film_2_score_4_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 4]
            film_2_score_5_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 5]
            film_2_total_score_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 6]


            # Opdater tekst i labels
            film_2_titel.configure(text=film_2_titel_data)
            film_2_score_1.configure(text=film_2_score_1_data)
            film_2_score_2.configure(text=film_2_score_2_data)
            film_2_score_3.configure(text=film_2_score_3_data)
            film_2_score_4.configure(text=film_2_score_4_data)
            film_2_score_5.configure(text=film_2_score_5_data)
            film_2_total_score.configure(text=film_2_total_score_data)

            # ---------------------------------- #


            # --------- FILM 3 ------- #

            # hent data under variable
            film_3_titel_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number]
            film_3_score_1_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 1]
            film_3_score_2_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 2]
            film_3_score_3_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 3]
            film_3_score_4_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 4]
            film_3_score_5_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 5]
            film_3_total_score_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 6]


            # Opdater tekst i labels
            film_3_titel.configure(text=film_3_titel_data)
            film_3_score_1.configure(text=film_3_score_1_data)
            film_3_score_2.configure(text=film_3_score_2_data)
            film_3_score_3.configure(text=film_3_score_3_data)
            film_3_score_4.configure(text=film_3_score_4_data)
            film_3_score_5.configure(text=film_3_score_5_data)
            film_3_total_score.configure(text=film_3_total_score_data)

            # ---------------------------------- #


            # --------- FILM 4 ------- #

            # hent data under variable
            film_4_titel_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number]
            film_4_score_1_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 1]
            film_4_score_2_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 2]
            film_4_score_3_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 3]
            film_4_score_4_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 4]
            film_4_score_5_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 5]
            film_4_total_score_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 6]


            # Opdater tekst i labels
            film_4_titel.configure(text=film_4_titel_data)
            film_4_score_1.configure(text=film_4_score_1_data)
            film_4_score_2.configure(text=film_4_score_2_data)
            film_4_score_3.configure(text=film_4_score_3_data)
            film_4_score_4.configure(text=film_4_score_4_data)
            film_4_score_5.configure(text=film_4_score_5_data)
            film_4_total_score.configure(text=film_4_total_score_data)

            # ---------------------------------- #


            # --------- FILM 5 ------- #

            # hent data under variable
            film_5_titel_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number]
            film_5_score_1_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 1]
            film_5_score_2_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 2]
            film_5_score_3_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 3]
            film_5_score_4_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 4]
            film_5_score_5_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 5]
            film_5_total_score_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 6]


            # Opdater tekst i labels
            film_5_titel.configure(text=film_5_titel_data)
            film_5_score_1.configure(text=film_5_score_1_data)
            film_5_score_2.configure(text=film_5_score_2_data)
            film_5_score_3.configure(text=film_5_score_3_data)
            film_5_score_4.configure(text=film_5_score_4_data)
            film_5_score_5.configure(text=film_5_score_5_data)
            film_5_total_score.configure(text=film_5_total_score_data)

            # ---------------------------------- #




# ------------------------------- SORT BY ONELINERS-funktion ---------------------------- #
        
        def sort_by_oneliners_function():

            colnames=["film_titel", "fede_skurke", "bar_hud", "vilde_våben", "one_liners", "episk_action", "total_score"]

            # Hent data
            df = pd.read_csv("database_dummy.csv", names=colnames, header=None)

            sorted_database = df.sort_values("one_liners", ascending=False)
            sorted_line_number = 0
            sorted_column_number = 0

            # --------- FILM 1 ------- #

            # hent data under variable
            film_1_titel_data = sorted_database.iloc[sorted_line_number][sorted_column_number]
            film_1_score_1_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 1]
            film_1_score_2_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 2]
            film_1_score_3_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 3]
            film_1_score_4_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 4]
            film_1_score_5_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 5]
            film_1_total_score_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 6]


            # Opdater tekst i labels
            film_1_titel.configure(text=film_1_titel_data)
            film_1_score_1.configure(text=film_1_score_1_data)
            film_1_score_2.configure(text=film_1_score_2_data)
            film_1_score_3.configure(text=film_1_score_3_data)
            film_1_score_4.configure(text=film_1_score_4_data)
            film_1_score_5.configure(text=film_1_score_5_data)
            film_1_total_score.configure(text=film_1_total_score_data)

            # ---------------------------------- #

             # --------- FILM 2 ------- #

            # hent data under variable
            film_2_titel_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number]
            film_2_score_1_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 1]
            film_2_score_2_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 2]
            film_2_score_3_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 3]
            film_2_score_4_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 4]
            film_2_score_5_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 5]
            film_2_total_score_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 6]


            # Opdater tekst i labels
            film_2_titel.configure(text=film_2_titel_data)
            film_2_score_1.configure(text=film_2_score_1_data)
            film_2_score_2.configure(text=film_2_score_2_data)
            film_2_score_3.configure(text=film_2_score_3_data)
            film_2_score_4.configure(text=film_2_score_4_data)
            film_2_score_5.configure(text=film_2_score_5_data)
            film_2_total_score.configure(text=film_2_total_score_data)

            # ---------------------------------- #


            # --------- FILM 3 ------- #

            # hent data under variable
            film_3_titel_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number]
            film_3_score_1_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 1]
            film_3_score_2_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 2]
            film_3_score_3_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 3]
            film_3_score_4_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 4]
            film_3_score_5_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 5]
            film_3_total_score_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 6]


            # Opdater tekst i labels
            film_3_titel.configure(text=film_3_titel_data)
            film_3_score_1.configure(text=film_3_score_1_data)
            film_3_score_2.configure(text=film_3_score_2_data)
            film_3_score_3.configure(text=film_3_score_3_data)
            film_3_score_4.configure(text=film_3_score_4_data)
            film_3_score_5.configure(text=film_3_score_5_data)
            film_3_total_score.configure(text=film_3_total_score_data)

            # ---------------------------------- #


            # --------- FILM 4 ------- #

            # hent data under variable
            film_4_titel_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number]
            film_4_score_1_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 1]
            film_4_score_2_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 2]
            film_4_score_3_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 3]
            film_4_score_4_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 4]
            film_4_score_5_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 5]
            film_4_total_score_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 6]


            # Opdater tekst i labels
            film_4_titel.configure(text=film_4_titel_data)
            film_4_score_1.configure(text=film_4_score_1_data)
            film_4_score_2.configure(text=film_4_score_2_data)
            film_4_score_3.configure(text=film_4_score_3_data)
            film_4_score_4.configure(text=film_4_score_4_data)
            film_4_score_5.configure(text=film_4_score_5_data)
            film_4_total_score.configure(text=film_4_total_score_data)

            # ---------------------------------- #


            # --------- FILM 5 ------- #

            # hent data under variable
            film_5_titel_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number]
            film_5_score_1_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 1]
            film_5_score_2_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 2]
            film_5_score_3_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 3]
            film_5_score_4_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 4]
            film_5_score_5_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 5]
            film_5_total_score_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 6]


            # Opdater tekst i labels
            film_5_titel.configure(text=film_5_titel_data)
            film_5_score_1.configure(text=film_5_score_1_data)
            film_5_score_2.configure(text=film_5_score_2_data)
            film_5_score_3.configure(text=film_5_score_3_data)
            film_5_score_4.configure(text=film_5_score_4_data)
            film_5_score_5.configure(text=film_5_score_5_data)
            film_5_total_score.configure(text=film_5_total_score_data)

            # ---------------------------------- #








# ------------------------------- SORT BY EPISK ACTION-funktion ---------------------------- #
        
        def sort_by_episk_action_function():

            colnames=["film_titel", "fede_skurke", "bar_hud", "vilde_våben", "one_liners", "episk_action", "total_score"]

            # Hent data
            df = pd.read_csv("database_dummy.csv", names=colnames, header=None)

            sorted_database = df.sort_values("episk_action", ascending=False)
            sorted_line_number = 0
            sorted_column_number = 0

            # --------- FILM 1 ------- #

            # hent data under variable
            film_1_titel_data = sorted_database.iloc[sorted_line_number][sorted_column_number]
            film_1_score_1_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 1]
            film_1_score_2_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 2]
            film_1_score_3_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 3]
            film_1_score_4_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 4]
            film_1_score_5_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 5]
            film_1_total_score_data = sorted_database.iloc[sorted_line_number][sorted_column_number + 6]


            # Opdater tekst i labels
            film_1_titel.configure(text=film_1_titel_data)
            film_1_score_1.configure(text=film_1_score_1_data)
            film_1_score_2.configure(text=film_1_score_2_data)
            film_1_score_3.configure(text=film_1_score_3_data)
            film_1_score_4.configure(text=film_1_score_4_data)
            film_1_score_5.configure(text=film_1_score_5_data)
            film_1_total_score.configure(text=film_1_total_score_data)

            # ---------------------------------- #

             # --------- FILM 2 ------- #

            # hent data under variable
            film_2_titel_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number]
            film_2_score_1_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 1]
            film_2_score_2_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 2]
            film_2_score_3_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 3]
            film_2_score_4_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 4]
            film_2_score_5_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 5]
            film_2_total_score_data = sorted_database.iloc[sorted_line_number + 1][sorted_column_number + 6]


            # Opdater tekst i labels
            film_2_titel.configure(text=film_2_titel_data)
            film_2_score_1.configure(text=film_2_score_1_data)
            film_2_score_2.configure(text=film_2_score_2_data)
            film_2_score_3.configure(text=film_2_score_3_data)
            film_2_score_4.configure(text=film_2_score_4_data)
            film_2_score_5.configure(text=film_2_score_5_data)
            film_2_total_score.configure(text=film_2_total_score_data)

            # ---------------------------------- #


            # --------- FILM 3 ------- #

            # hent data under variable
            film_3_titel_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number]
            film_3_score_1_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 1]
            film_3_score_2_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 2]
            film_3_score_3_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 3]
            film_3_score_4_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 4]
            film_3_score_5_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 5]
            film_3_total_score_data = sorted_database.iloc[sorted_line_number + 2][sorted_column_number + 6]


            # Opdater tekst i labels
            film_3_titel.configure(text=film_3_titel_data)
            film_3_score_1.configure(text=film_3_score_1_data)
            film_3_score_2.configure(text=film_3_score_2_data)
            film_3_score_3.configure(text=film_3_score_3_data)
            film_3_score_4.configure(text=film_3_score_4_data)
            film_3_score_5.configure(text=film_3_score_5_data)
            film_3_total_score.configure(text=film_3_total_score_data)

            # ---------------------------------- #


            # --------- FILM 4 ------- #

            # hent data under variable
            film_4_titel_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number]
            film_4_score_1_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 1]
            film_4_score_2_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 2]
            film_4_score_3_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 3]
            film_4_score_4_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 4]
            film_4_score_5_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 5]
            film_4_total_score_data = sorted_database.iloc[sorted_line_number + 3][sorted_column_number + 6]


            # Opdater tekst i labels
            film_4_titel.configure(text=film_4_titel_data)
            film_4_score_1.configure(text=film_4_score_1_data)
            film_4_score_2.configure(text=film_4_score_2_data)
            film_4_score_3.configure(text=film_4_score_3_data)
            film_4_score_4.configure(text=film_4_score_4_data)
            film_4_score_5.configure(text=film_4_score_5_data)
            film_4_total_score.configure(text=film_4_total_score_data)

            # ---------------------------------- #


            # --------- FILM 5 ------- #

            # hent data under variable
            film_5_titel_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number]
            film_5_score_1_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 1]
            film_5_score_2_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 2]
            film_5_score_3_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 3]
            film_5_score_4_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 4]
            film_5_score_5_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 5]
            film_5_total_score_data = sorted_database.iloc[sorted_line_number + 4][sorted_column_number + 6]


            # Opdater tekst i labels
            film_5_titel.configure(text=film_5_titel_data)
            film_5_score_1.configure(text=film_5_score_1_data)
            film_5_score_2.configure(text=film_5_score_2_data)
            film_5_score_3.configure(text=film_5_score_3_data)
            film_5_score_4.configure(text=film_5_score_4_data)
            film_5_score_5.configure(text=film_5_score_5_data)
            film_5_total_score.configure(text=film_5_total_score_data)

            # ---------------------------------- #







        # ------------------------------- Sort_by_total_score-knap ---------------------------- #

        # Definer sort_by_total_score
        sort_by_total_score = customtkinter.CTkButton(self, text="TOTAL SCORE", width=120, command=sort_by_total_score_function)

        # Indsæt sort_by_total_score i vindue
        sort_by_total_score.place(relx=0.8, rely= sorted_row_rely, anchor=CENTER)

        # ------------------------------------------------------------------------------------- #






        # ------------------------------- sort_by_fede_skurke-knap ---------------------------- #

        # Definer sort_by_total_score
        sort_by_fede_skurke = customtkinter.CTkButton(self, text="FEDE SKURKE", width=120, command=sort_by_fede_skurke_function)

        # Indsæt sort_by_total_score i vindue
        sort_by_fede_skurke.place(relx=0.3, rely= sorted_row_rely, anchor=CENTER)

        # ------------------------------------------------------------------------------------- #      
        


        # ------------------------------- sort_by_bar_hud-knap ---------------------------- #

        # Definer sort_by_total_score
        sort_by_bar_hud = customtkinter.CTkButton(self, text="BAR HUD", width=120, command=sort_by_bar_hud_function)

        # Indsæt sort_by_total_score i vindue
        sort_by_bar_hud.place(relx=0.4, rely= sorted_row_rely, anchor=CENTER)

        # --------------------------------------------------------------------------------- #          
    






        # ------------------------------- sort_by_vilde_våben-knap ---------------------------- #

        # Definer sort_by_total_score
        sort_by_vilde_våben = customtkinter.CTkButton(self, text="VILDE VÅBEN", width=120, command=sort_by_vilde_våben_function)

        # Indsæt sort_by_total_score i vindue
        sort_by_vilde_våben.place(relx=0.5, rely= sorted_row_rely, anchor=CENTER)

        # ------------------------------------------------------------------------------------- #     



        # ------------------------------- sort_by_oneliners-knap ---------------------------- #

        # Definer sort_by_total_score
        sort_by_oneliners = customtkinter.CTkButton(self, text="ONELINERS", width=120, command=sort_by_oneliners_function)

        # Indsæt sort_by_total_score i vindue
        sort_by_oneliners.place(relx=0.6, rely= sorted_row_rely, anchor=CENTER)

        # ----------------------------------------------------------------------------------- #     



        # ------------------------------- sort_by_episk_action-knap ---------------------------- #

        # Definer sort_by_total_score
        sort_by_episk_action = customtkinter.CTkButton(self, text="ONELINERS", width=120, command=sort_by_episk_action_function)

        # Indsæt sort_by_total_score i vindue
        sort_by_episk_action.place(relx=0.7, rely= sorted_row_rely, anchor=CENTER)

        # ----------------------------------------------------------------------------------- #   




       


if __name__ == "__main__":
    app = App()
    app.mainloop()
