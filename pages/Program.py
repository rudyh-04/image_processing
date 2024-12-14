import numpy as np
import cv2

image = cv2.imread("C:/Users/rudyp/Alin-thursday/logo.jpg")

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
