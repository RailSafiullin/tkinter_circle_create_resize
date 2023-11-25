import pytest
import tkinter as tk
from main import CircleApp

@pytest.fixture
def app():
    app = CircleApp()
    app.root.attributes('-topmost', True)
    app.root.update()
    yield app
    app.root.destroy()

def test_increase_radius(app):
    initial_radius = app.circle_radius
    step = 5

    app.ent1.delete(0, tk.END)
    app.ent1.insert(0, str(step))

    event = tk.Event()
    event.keysym = "Right"
    app.increase_radius(event)

    assert app.circle_radius == initial_radius + step

def test_decrease_radius(app):
    initial_radius = app.circle_radius
    step = 5

    app.ent1.delete(0, tk.END)
    app.ent1.insert(0, str(step))

    event = tk.Event()
    event.keysym = "Left"
    app.decrease_radius(event)

    assert app.circle_radius == initial_radius - step