import tkinter as tk


class Window:
    text = False

    def add_string(self):
        if not self.text:
            hello_world = tk.Label(text="Hello World!")
            hello_world.pack()
            self.text = not self.text

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("My First GUI Program")
        self.window.minsize(width=500, height=300)
        self.boton = tk.Button(text="Clickame", command=self.add_string)

        self.boton.pack()
        self.window.mainloop()


if __name__ == "__main__":
    Window()
