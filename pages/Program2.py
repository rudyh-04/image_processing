import cv2
import numpy as np
from tkinter import Tk, filedialog

# Function to select an image file
def select_image_file():
     root = Tk ()
     root.withdraw()  # Hide the root window
     fille_path = filedialog.askopenfilename(
        filetypes=[("Image Files", ".png;.jpeg;*.jpg")],
        title="Select an Image File"
    )
     return fille_path

# Main script
if __name__ == "__main__":
   # Select an image file
    image_path = select_image_file()
    if not image_path:
        print ("No file selected. Exiting.")
        exit ()

 # Load the selected image
    image = cv2.imread(image_path)
    if image is None:
        print ("Failed to load the image. Exiting.")
        exit ()


#Menampilkan image yang sudah dibaca
cv2.imshow("Logo - blue", image[:,:,0])
cv2.imshow("Logo - green", image[:,:,1])
cv2.imshow("Logo - red", image[:,:,2])

#Menampilkan matriks dari image 
print(image)              #menampilkan semua chanel warna
print(image[:,:,0])       #print chanel warna biru
print(image[:,:,1])       #print chanel warna hijau
print(image[:,:,2])       #print chanel warna merah

#Menunggu sampai user menekan tombol
cv2.waitKey()