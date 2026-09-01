import tkinter as tk
import time
from PIL import Image, ImageTk

# Main Application Window
root = tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

# List of image Paths
image_paths= [
    r"/Users/ayushbharti/Desktop/Album/IMG_1509.JPG",
    r"/Users/ayushbharti/Desktop/Album/IMG_1600.jpeg",
    r"/Users/ayushbharti/Desktop/Album/IMG_1623.JPG",
    r"/Users/ayushbharti/Desktop/Album/IMG_1667.JPG",
    r"/Users/ayushbharti/Desktop/Album/PHOTO-2026-08-18-19-39-39.jpg",
    r"/Users/ayushbharti/Desktop/Album/IMG_1665.JPG",  
]
image_size = (700,800)  # Desired size for the images
images= []
for path in image_paths:
    img=Image.open(path)
    img=img.resize(image_size)
    images.append(img) # Adding each image in the list

# Convert PIL image into Tkinter Compatible image
final_images= []
for img in images:
    photo = ImageTk.PhotoImage(img) 
    final_images.append(photo) 

# Label Widget to keep photo
image_label = tk.Label(root)
image_label.pack(pady=30)

# Slideshow Function
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image = photo
        root.update()
        time.sleep(2)  # Display each image for 2 seconds

# button
play_button = tk.Button(
    root, 
    text="Play The Slideshow",
    font=("Arial",17),
    command=start_slideshow
)

play_button.pack(pady=40)

root.mainloop() # This will keep the window open