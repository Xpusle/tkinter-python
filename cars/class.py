import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pygame
from tkinter import filedialog

pygame.display.init
class cars:
    def __init__(self,root):
        self.root=tk.Tk
        self.root=root
        self.root.title("cars")
        self.root.geometry("500x500")
        self.car=None
        self.buttons()
    def buttons(self):
        #the function of the button is to dispaly the cars based on the name  
        #koenigsegg
        self.koenigsegg_button=tk.Button(self.root,text="koenigsegg",command=self.koenigsegg)
        self.koenigsegg_button.pack(pady=10)
        #Ferrari
        self.Ferrari_button=tk.Button(self.root,text="Ferrari",command=self.Ferrari)
        self.Ferrari_button.pack(pady=10)
        #ktm
        self.X_BOW_button=tk.Button(self.root,text="KTMX-BOW",command=self.X_BOW)
        self.X_BOW_button.pack(pady=10)
        #The BMW M5
        self.The_BMW_M5=tk.Button(self.root,text="The BMW M5",command=self.BMW)
        self.The_BMW_M5.pack(pady=10)
        #mercedes-benz
        self.mercedes_benz=tk.Button(self.root,text="mercedes-benz",command=self.mercedes_benz)
        self.mercedes_benz.pack(pady=10)
    #dispalyfuction     
    def koenigsegg(self):
        self.cars="D:\\cars\\Koenigsegg CC850 - 1.webp"
        self.img_read=mpimg.imread(self.cars)
        pygame.display.get_surface()
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
    def X_BOW(self):
        self.cars="D:\\cars\\470674-ktm-x-bow-gt-xr-my2023-action-images-action-images-1662741447.jpg"
        self.img_read=mpimg.imread(self.cars)
        pygame.display.get_surface()
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
    def Ferrari(self):
        self.cars="D:\\cars\\photo-1597687190402-bd767ac2ce81.webp"
        self.img_read=mpimg.imread(self.cars)
        pygame.display.get_surface()
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
    def BMW(self):
        self.cars="D:\\cars\\bmw-m5-in-black.webp"
        self.img_read=mpimg.imread(self.cars)
        pygame.display.get_surface()
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
    def mercedes_benz(self):
        self.cars="D:\\cars\\photo-1546518071-fddcdda7580a.webp"
        self.img_read=mpimg.imread(self.cars)
        pygame.display.get_surface()
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
if __name__ == "__main__":
    root = tk.Tk()
    app = cars(root)
    root.mainloop()
