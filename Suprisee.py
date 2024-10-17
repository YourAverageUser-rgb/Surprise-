import tkinter as tk
import pyautogui
from PIL import Image, ImageTk
import webbrowser
import time
# i wonder who the person will be that finds
# this little suprise feel free to message me 
# why the weird video with data because why not
# Function to handle the click on the rolling cookie
def open_secret_link():
    # Open a funny secret link when clicked
    secret_link = "https://www.omfgdogs.com/"
    webbrowser.open(secret_link)

# Function to minimize the command prompt window
def minimize_cmd():
    pyautogui.hotkey('win', 'down')  # Minimize current window

# Function to animate the cookie rolling across the screen
def roll_cookie(cookie_label, canvas, width):
    for x in range(-200, width + 100, 5):
        canvas.coords(cookie_label, x, 150)  # Move the cookie
        time.sleep(0.02)  # Control the speed of the rolling effect
        window.update()  # Update the window for animation

# Create the main window
window = tk.Tk()
window.title("Congrats!")

# Set the window to be transparent with no background
window.geometry("800x400")
window.configure(bg='white')
window.attributes('-transparentcolor', 'white')  # Set transparency color
window.overrideredirect(True)  # Remove window borders

# Set up the canvas
canvas = tk.Canvas(window, width=800, height=400, bg="white", highlightthickness=0)
canvas.pack()

# Create a fading message (no background for the text)
message = canvas.create_text(400, 100, text="Congrats on finding this, here have a cookie!", font=("Arial", 24), fill="black")

# Load and display the cookie image
cookie_image = Image.open("cookie.png")
cookie_image = cookie_image.resize((100, 100), Image.ANTIALIAS)
cookie_photo = ImageTk.PhotoImage(cookie_image)
cookie_label = canvas.create_image(-100, 150, image=cookie_photo, anchor=tk.NW)

# Set up the secret link when cookie is clicked
canvas.tag_bind(cookie_label, "<Button-1>", lambda e: open_secret_link())

# Minimize the command prompt after 2 seconds
window.after(2000, minimize_cmd)

# Animate the rolling cookie
window.after(2000, lambda: roll_cookie(cookie_label, canvas, 800))

# Start the Tkinter loop
window.mainloop()
