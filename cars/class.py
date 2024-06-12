import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pygame
from tkinter import filedialog
from tkinter import Message
from tkinter import colorchooser

pygame.display.init
class cars:
    def __init__(self,root):
        self.root=tk.Tk
        self.root=root
        self.root.title("cars")
        self.root.geometry("1920x1080")
        self.car=None
        self.buttons()
    def buttons(self):
        #the function of the button is to dispaly the cars based on the name  
        #koenigsegg
        self.koenigsegg_button=tk.Button(self.root,text="koenigsegg",command=self.koenigsegg,bg="black",fg="white",activebackground="red")
        self.koenigsegg_button.grid(row=0, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #Ferrari
        self.Ferrari_button=tk.Button(self.root,text="Ferrari",command=self.Ferrari,bg="red",fg="black",activebackground="red")
        self.Ferrari_button.grid(row=1, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #ktm
        self.X_BOW_button=tk.Button(self.root,text="KTMX-BOW",command=self.X_BOW,bg="orange",fg="black",activebackground="red")
        self.X_BOW_button.grid(row=2, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #The BMW M5
        self.The_BMW_M5=tk.Button(self.root,text="The BMW M5",command=self.BMW,bg="blue",fg="white",activebackground="red")
        self.The_BMW_M5.grid(row=3, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #mercedes-benz
        self.mercedes_benz=tk.Button(self.root,text="mercedes-benz",command=self.mercedes_benz,bg="yellow",fg="black",activebackground="red")
        self.mercedes_benz.grid(row=4, column=0, pady=5, padx=5, sticky='w')#chatgtp
        
        #information_koennigsegg
        self.information_koenigsegg=tk.Button(self.root,text="information_about_koenigsegg ",command=self.information_koenigsegg,bg="black",fg="white",activebackground="red",border=3.6)
        self.information_koenigsegg.grid(row=5, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #information_ferrari
        self.information_ferrari=tk.Button(self.root,text="information_about_ferrari",command=self.information_ferrari,bg="red",fg="black",activebackground="red",border=3.6)
        self.information_ferrari.grid(row=6, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #infromation_of_KTM_X_BOW
        self.information_X_BOW=tk.Button(self.root,text="information_about_KTM_X_BOW",command=self.information_X_BOW,bg="orange",fg="black",activebackground="red",border=3.6)
        self.information_X_BOW.grid(row=7, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #information_of_THE_BMW_M5
        self.information_BMW_M5=tk.Button(self.root,text="information_about_THE_BMW_M5",command=self.information_BMW_M5,bg="blue",fg="white",activebackground="red",border=3.6)
        self.information_BMW_M5.grid(row=8, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #information_about_mercedes_benz
        self.information_mercedes_benz=tk.Button(self.root,text="information_mercedes_benz",command=self.information_mercedes_benz,bg="yellow",fg="black",activebackground="red",border=3.6)
        self.information_mercedes_benz.grid(row=9, column=0, pady=5, padx=5, sticky='w')#chatgtp
        
        
        
    #infromation_of_koenigsegg_ 
    def information_koenigsegg(self):
        self.cars="C:\\Users\\sidda\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-06-05 111802.png"
        self.img_read=mpimg.imread(self.cars)
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
    #information_Ferrari
    def information_ferrari(self):
        self.cars="C:\\Users\\sidda\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-06-05 112208.png"
        self.img_read=mpimg.imread(self.cars)
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
    #information_about_X_BOW
    def information_X_BOW(self):
        self.cars="C:\\Users\\sidda\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-06-05 145040.png"
        self.img_read=mpimg.imread(self.cars)
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
    #information_about_BMW_M5
    def information_BMW_M5(self):
        self.cars="C:\\Users\\sidda\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-06-05 150924.png"
        self.img_read=mpimg.imread(self.cars)
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
    #information_about_mercedes_benz
    def information_mercedes_benz(self):
        self.cars="C:\\Users\\sidda\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-06-05 151711.png"
        self.img_read=mpimg.imread(self.cars)
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
        
        
    
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
