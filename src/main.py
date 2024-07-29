import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.button = customtkinter.CTkButton(self, text="Button", command=self.button_callback)
        self.button.pack(padx=20, pady=20)

    def button_callback(self):
        print("button clicked")

def main():
    app = App()
    app.mainloop()

if __name__=="__main__":
    main()