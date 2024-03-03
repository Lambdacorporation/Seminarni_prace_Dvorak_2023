import customtkinter
from PIL import Image
import subprocess
import sys

class L1(customtkinter.CTkFrame):
    def __init__(self, master, nadpis, image_path, **kwargs):
        super().__init__(master, **kwargs)

        self.title = customtkinter.CTkLabel(self, text=nadpis, fg_color="lightgray", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        my_image = customtkinter.CTkImage(dark_image=Image.open(image_path), size=(300, 300))
        self.image_label = customtkinter.CTkLabel(self, image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button = customtkinter.CTkButton(self, text="Spustit křižovatku", command=self.run_program)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    def run_program(self):
        program_path = "C:/Users/domca/Documents/Dominik/Škola/Stáž/l1main.py" #/home/pi/l1main.py
        
        # Spuštění externího Python programu
        subprocess.run(["python", program_path])

class L2(customtkinter.CTkFrame):
    def __init__(self, master, nadpis, image_path, **kwargs):
        super().__init__(master, **kwargs)

        self.title = customtkinter.CTkLabel(self, text=nadpis, fg_color="lightgray", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        my_image = customtkinter.CTkImage(dark_image=Image.open(image_path), size=(300, 300))
        self.image_label = customtkinter.CTkLabel(self, image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button = customtkinter.CTkButton(self, text="Spustit křižovatku", command=self.run_program)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    def run_program(self):
        program_path = "C:/Users/domca/Documents/Dominik/Škola/Stáž/l2main.py" #/home/pi/l2main.py
        
        # Spuštění externího Python programu
        subprocess.run(["python", program_path])

class L3(customtkinter.CTkFrame):
    def __init__(self, master, nadpis, image_path, **kwargs):
        super().__init__(master, **kwargs)

        self.title = customtkinter.CTkLabel(self, text=nadpis, fg_color="lightgray", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        my_image = customtkinter.CTkImage(dark_image=Image.open(image_path), size=(300, 300))
        self.image_label = customtkinter.CTkLabel(self, image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button = customtkinter.CTkButton(self, text="Spustit křižovatku", command=self.run_program)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    def run_program(self):
        program_path = "C:/Users/domca/Documents/Dominik/Škola/Stáž/l3main.py" #/home/pi/l3main.py
        
        # Spuštění externího Python programu
        subprocess.run(["python", program_path])

class L4(customtkinter.CTkFrame):
    def __init__(self, master, nadpis, image_path, **kwargs):
        super().__init__(master, **kwargs)

        self.title = customtkinter.CTkLabel(self, text=nadpis, fg_color="lightgray", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        my_image = customtkinter.CTkImage(dark_image=Image.open(image_path), size=(300, 300))
        self.image_label = customtkinter.CTkLabel(self, image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button = customtkinter.CTkButton(self, text="Spustit křižovatku", command=self.run_program)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    def run_program(self):
        program_path = "C:/Users/domca/Documents/Dominik/Škola/Stáž/l4main.py" #/home/pi/l4main.py
        
        # Spuštění externího Python programu
        subprocess.run(["python", program_path])

class L5(customtkinter.CTkFrame):
    def __init__(self, master, nadpis, image_path, **kwargs):
        super().__init__(master, **kwargs)

        self.title = customtkinter.CTkLabel(self, text=nadpis, fg_color="lightgray", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        my_image = customtkinter.CTkImage(dark_image=Image.open(image_path), size=(300, 300))
        self.image_label = customtkinter.CTkLabel(self, image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button = customtkinter.CTkButton(self, text="Spustit křižovatku", command=self.run_program)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    def run_program(self):
        program_path = "C:/Users/domca/Documents/Dominik/Škola/Stáž/l5main.py" #/home/pi/l5main.py
        
        # Spuštění externího Python programu
        subprocess.run(["python", program_path])

class L6(customtkinter.CTkFrame):
    def __init__(self, master, nadpis, image_path, **kwargs):
        super().__init__(master, **kwargs)

        self.title = customtkinter.CTkLabel(self, text=nadpis, fg_color="lightgray", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        my_image = customtkinter.CTkImage(dark_image=Image.open(image_path), size=(300, 300))
        self.image_label = customtkinter.CTkLabel(self, image=my_image, text="")
        self.image_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button = customtkinter.CTkButton(self, text="Spustit křižovatku", command=self.run_program)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    def run_program(self):
        program_path = "C:/Users/domca/Documents/Dominik/Škola/Stáž/l6main.py" #/home/pi/l6main.py
        
        # Spuštění externího Python programu
        subprocess.run(["python", program_path])

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.title = customtkinter.CTkLabel(self, text="Křižovatky", fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

        # Přidáme tři instance třídy L1 s různými obrázky
        self.l1_1 = L1(self, nadpis="Křižovatka 1", image_path="C:/Users/domca/Documents/Dominik/Škola/Stáž/krizovatky/krizovatka1.jpg", width=150, height=150) #/home/pi/krizovatky/krizovatka1.jpg
        self.l1_1.grid(row=1, column=0, padx=10, pady=10)

        self.l1_2 = L2(self, nadpis="Křižovatka 2",  image_path="C:/Users/domca/Documents/Dominik/Škola/Stáž/krizovatky/krizovatka2_2.jpg", width=150, height=150) #/home/pi/krizovatky/krizovatka2.jpg
        self.l1_2.grid(row=1, column=1, padx=10, pady=10)

        self.l1_3 = L3(self, nadpis="Křižovatka 3",  image_path="C:/Users/domca/Documents/Dominik/Škola/Stáž/krizovatky/krizovatka3_2.jpg", width=150, height=150) #/home/pi/krizovatky/krizovatka3.jpg
        self.l1_3.grid(row=1, column=2, padx=10, pady=10)

        self.l1_1 = L4(self, nadpis="Křižovatka 4",  image_path="C:/Users/domca/Documents/Dominik/Škola/Stáž/krizovatky/krizovatka4.jpg", width=150, height=150) #/home/pi/krizovatky/krizovatka4.jpg
        self.l1_1.grid(row=2, column=0, padx=10, pady=10)

        self.l1_2 = L5(self, nadpis="Křižovatka 5",  image_path="C:/Users/domca/Documents/Dominik/Škola/Stáž/krizovatky/krizovatka5.jpg", width=150, height=150) #/home/pi/krizovatky/krizovatka5.jpg
        self.l1_2.grid(row=2, column=1, padx=10, pady=10)

        self.l1_3 = L6(self, nadpis="Křižovatka 6",  image_path="C:/Users/domca/Documents/Dominik/Škola/Stáž/krizovatky/krizovatka6.jpg", width=150, height=150) #/home/pi/krizovatky/krizovatka6.jpg
        self.l1_3.grid(row=2, column=2, padx=10, pady=10)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Křižovatky")
        self.my_frame = MyFrame(master=self, width=1000, height=600) #1000, 600
        self.my_frame.grid(row=0, column=0, padx=0, pady=0)

app = App()
app.mainloop()
