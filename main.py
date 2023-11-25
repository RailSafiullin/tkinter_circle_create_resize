import tkinter as tk

class CircleApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Геометрические изображения")
        self.root.geometry("900x600")

        self.canvas = tk.Canvas(self.root, width=900, height=450)
        self.canvas.pack()

        self.x, self.y, self.R = 450, 150, 50
        self.circle_radius = 50
        self.circle = self.canvas.create_oval(
            self.x - self.R, self.y - self.R, self.x + self.R, self.y + self.R, width=1
        )

if __name__ == "__main__":
    app = CircleApp()
    app.run()
