import time
import customtkinter
import subprocess
from PIL import Image

class Title(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(0, 0), sticky="ew", columnspan=4)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class L1(customtkinter.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        # Vložení obrázku do nadřazeného okna (App)
        #/home/pi/krizovatky/krizovatka1.jpg
        my_image = customtkinter.CTkImage(dark_image=Image.open("/home/pi/krizovatky/krizovatka1.jpg"), size=(400, 400))
        image_label = customtkinter.CTkLabel(master, image=my_image, text="")  # text is optional
        image_label.grid(row=1, column=0, padx=307, pady=(10, 0), sticky="w")

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class MyRadiobuttonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=4)
        self.grid_columnconfigure((1, 2, 3), weight=1)
        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i+2, column=0, padx=10, pady=(5, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("BRUH")
        self.geometry("1024x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.title = Title(self, "Křižovatka 1", values=["option 1", "option 2", "option 3"])
        self.title.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        self.l1 = L1(self, values=["option 1", "option 2", "option 3"])
        self.l1.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        self.radiobutton_frame = MyRadiobuttonFrame(self, "Options", values=["První pojede zelené auto, a po něm růžové auto", "První pojede růžové auto, a po něm zelené auto", "Obě auta pojedou současně"])
        self.radiobutton_frame.grid(row=2, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="Potvrdit volbu", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=1)

    def button_callback(self):
        print("radiobutton_frame:", self.radiobutton_frame.get())
        selected_option = self.radiobutton_frame.get()
        if selected_option == "":
            print("No option selected")
            return
        for radiobutton in self.radiobutton_frame.radiobuttons:
            if radiobutton.cget("value") == "První pojede zelené auto, a po něm růžové auto":
                radiobutton.configure(fg_color="green", text_color="green")
            else:
                radiobutton.configure(fg_color="red", text_color="red")
        button_new_text = "Přehrát simulaci"
        if selected_option == "První pojede zelené auto, a po něm růžové auto":
            self.button.configure(text=button_new_text, command=self.o1_l1)
        elif selected_option == "První pojede růžové auto, a po něm zelené auto":
            self.button.configure(text=button_new_text, command=self.o2_l1)
        elif selected_option == "Obě auta pojedou současně":
            self.button.configure(text=button_new_text, command=self.o3_l1)
    def o1_l1(self):
        try:
            subprocess.run(["python", "1c.py"])
            time.sleep(5)
            subprocess.run(["python", "1cb.py"])
        except Exception as e:
            print(f"Chyba při spouštění skriptu: {e}")
    def o2_l1(self):
        try:
            subprocess.run(["python", "1s.py"])
            time.sleep(5)
            subprocess.run(["python", "1sb.py"])
        except Exception as e:
            print(f"Chyba při spouštění skriptu: {e}")
    def o3_l1(self):
        try:
            subprocess.run(["python", "1s.py"])
            time.sleep(5)
            subprocess.run(["python", "1sb.py"])
        except Exception as e:
            print(f"Chyba při spouštění skriptu: {e}")
    def menu_port(self):
        print("Nová funkce pro Menu")

app = App()
app.mainloop()

