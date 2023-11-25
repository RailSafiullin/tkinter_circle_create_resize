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
        self.radius_display = self.canvas.create_text(
            450, 440, text=f"Радиус: {self.circle_radius}"
        )
        self.help_text = tk.Label(text="Шаг изменения радиуса:")
        self.help_text.pack()

        self.ent1 = tk.Entry(
            self.root, width=5, font=("Calibri 20"), bg='#cdbacc', fg='#000'
        )
        self.ent1.insert(0, 1)
        self.ent1.pack()

        self.root.bind_all("<Right>", self.increase_radius)
        self.root.bind_all("<Left>", self.decrease_radius)

        self.root.bind_all("<Escape>", self.exit_program)
        self.root.bind_all("<Return>", self.focus_root)

        create_circle_button = tk.Button(
            self.root, text="Пересоздать круг", command=self.create_circle
        )
        self.input_dialog = None
        create_circle_button.pack()

    def run(self):
        self.root.mainloop()

    def increase_radius(self, event):
        self.root.focus()
        step = int(self.ent1.get())
        self.circle_radius += step
        self.canvas.coords(
            self.circle,
            self.x - self.circle_radius,
            self.y - self.circle_radius,
            self.x + self.circle_radius,
            self.y + self.circle_radius,
        )
        self.canvas.itemconfig(
            self.radius_display, text=f"Радиус: {self.circle_radius}"
        )

    def decrease_radius(self, event):
        self.root.focus()
        step = int(self.ent1.get())
        if step >= self.circle_radius:
            step = self.circle_radius - 1
        self.circle_radius -= step
        self.canvas.coords(
            self.circle,
            self.x - self.circle_radius,
            self.y - self.circle_radius,
            self.x + self.circle_radius,
            self.y + self.circle_radius,
        )
        self.canvas.itemconfig(
            self.radius_display, text=f"Радиус: {self.circle_radius}"
        )

    def create_circle(self):
        self.input_dialog = tk.Toplevel()
        self.input_dialog.title("Создать круг")

        tk.Label(self.input_dialog, text="X-координата центра:").grid(row=0, column=0)
        tk.Label(self.input_dialog, text="Y-координата центра:").grid(row=1, column=0)
        tk.Label(self.input_dialog, text="Радиус:").grid(row=2, column=0)

        self.x_entry = tk.Entry(self.input_dialog)
        self.y_entry = tk.Entry(self.input_dialog)
        self.radius_entry = tk.Entry(self.input_dialog)

        self.x_entry.insert(0, 450)
        self.y_entry.insert(0, 150)
        self.radius_entry.insert(0, 10)

        self.x_entry.grid(row=0, column=1)
        self.y_entry.grid(row=1, column=1)
        self.radius_entry.grid(row=2, column=1)

        create_button = tk.Button(
            self.input_dialog, text="Создать", command=self.create_circle_action
        )
        create_button.grid(row=3, columnspan=2)

    def create_circle_action(self):
        self.canvas.delete(self.circle)
        self.x = int(self.x_entry.get())
        self.y = int(self.y_entry.get())
        self.circle_radius = int(self.radius_entry.get())

        self.circle = self.canvas.create_oval(
            self.x - self.circle_radius,
            self.y - self.circle_radius,
            self.x + self.circle_radius,
            self.y + self.circle_radius,
            width=1,
        )
        self.input_dialog.destroy()

    def exit_program(self, event):
        self.root.destroy()

    def focus_root(self, event):
        self.root.focus()


if __name__ == "__main__":
    app = CircleApp()
    app.run()
