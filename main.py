import customtkinter 

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("400x220")
app.title("tournament editor")

def login():
    print("test")

frame_1 = customtkinter.CTkFrame(master = app)
frame_1.pack(pady=35, padx=35,fill="both", expand=True)

entry_1 = customtkinter.CTkEntry(master = frame_1, placeholder_text = "Username")
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master = frame_1, placeholder_text = "Password", show = "*")
entry_2.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master = frame_1, command = login)
button_1.pack(pady = 10, padx=10)

app.mainloop()
