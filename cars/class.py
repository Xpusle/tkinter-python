import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pygame
import pyautogui 
import cv2 as cv
#print(cv.__version__)
from tkinter import filedialog
from tkinter import Message
from tkinter import colorchooser
from PIL import Image,ImageTk

pygame.display.init
#class scrollbar:  
    #def __init__(self,root):
        #self.root=root
# Create a frame to hold the text widget and scrollbars
        #self.frame = tk.Frame(root)
        #self.frame.grid(row=1, column=0, sticky='nsew')
# Configure grid layout weight to allow resizing
        #self.root.grid_columnconfigure(2, weight=2)
        #self.frame.grid_rowconfigure(3, weight=3)
        #self.frame.grid_columnconfigure(4, weight=4)

# Create a Text widget
        #self.text = tk.Text(self.frame, wrap=tk.NONE)
        #self.text.grid(row=1, column=0, sticky='nsew')

# Add a vertical scrollbar to the Text widget
        #self.v_scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.text.yview)
        #self.v_scrollbar.grid(row=2, column=0, sticky='ns')

# Add a horizontal scrollbar to the Text widget
        #self.h_scrollbar = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL, command=self.text.xview)
       # self.h_scrollbar.grid(row=1, column=0, sticky='ew')

# Configure the Text widget to use the scrollbars
        #self.text.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)

# Start the main event loop
        
#class koenigsegg_:
#    def __init__(self,root):
#        self.root=tk.Tk
#        self.root=root
#        imagepath="D:\\cars\\Koenigsegg CC850 - 1.webp"
#        self.image=Image.open(imagepath)
#        self.resized=self.image.resize((300,300))
#        self.tk_image=ImageTk.PhotoImage(self.resized)
#        self.label=tk.Label(self.root,image=self.tk_image)
#        self.label.grid(row=0, column=10, pady=5, padx=5, sticky='w')
#class Ferrari_:
#    def __init__(self,root):
##        self.root=root
#        imagepath="D:\\cars\\photo-1597687190402-bd767ac2ce81.webp"
#        self.image=Image.open(imagepath)
#        self.resized=self.image.resize((300,300))
#        self.tk_image=ImageTk.PhotoImage(self.resized)
#       self.label=tk.Label(self.root,image=self.tk_image)
#        self.label.grid(row=2, column=10, pady=5, padx=5, sticky='w')
#class KTM_:
#    def __init__(self,root):
#        self.root=root
#        imagepath="D:\\cars\\470674-ktm-x-bow-gt-xr-my2023-action-images-action-images-1662741447.webp"
#        self.image=Image.open(imagepath)
#        self.resized=self.image.resize((300,300))
#        self.tk_image=ImageTk.PhotoImage(self.resized)
#        self.label=tk.Label(self.root,image=self.tk_image)
#        self.label.grid(row=3, column=10, pady=5, padx=5, sticky='w')
#class BMWM5_:
#def __init__(self,root):
#    self.root=root
#     imagepath="D:\\cars\\bmw-m5-in-black.webp"
#     self.image=Image.open(imagepath)
#     self.resized=self.image.resize((300,300))
#     self.tk_image=ImageTk.PhotoImage(self.resized)
#      self.label=tk.Label(self.root,image=self.tk_image)
#       self.label.grid(row=4, column=10, pady=5, padx=5, sticky='w')
#class mercedes_benz:
#    def __init__(self,root):
#        self.root=root
#        imagepath="D:\\cars\\photo-1546518071-fddcdda7580a.webp"
#       self.image=Image.open(imagepath)
#        self.resized=self.image.resize((300,300))
#        self.tk_image=ImageTk.PhotoImage(self.resized)
#        self.label=tk.Label(self.root,image=self.tk_image)
#        self.label.grid(row=5, column=10, pady=5, padx=5, sticky='w')


class cars:
    def __init__(self,root):
        self.root=tk.Tk
        self.root=root
        self.root.title("cars")
        self.root.geometry("1920x1080")
        self.car=None
        self.buttons()
        self.setup=None
    def buttons(self):
        #the function of the button is to dispaly the cars based on the name  
        #koenigsegg
        self.koenigsegg_button=tk.Button(self.root,text="koenigsegg jesko",command=self.koenigsegg,bg="black",fg="white",activebackground="red")
        self.koenigsegg_button.grid(row=0, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #Ferrari
        self.Ferrari_button=tk.Button(self.root,text="Ferrari la ferrari",command=self.Ferrari,bg="red",fg="black",activebackground="red")
        self.Ferrari_button.grid(row=2, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #ktm
        self.X_BOW_button=tk.Button(self.root,text="KTMX-BOW",command=self.X_BOW,bg="orange",fg="black",activebackground="red")
        self.X_BOW_button.grid(row=3, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #The BMW M5
        self.The_BMW_M5=tk.Button(self.root,text="BMW M5",command=self.BMW,bg="blue",fg="white",activebackground="red")
        self.The_BMW_M5.grid(row=4, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #mercedes-benz
        self.mercedes_benz=tk.Button(self.root,text="mercedes-AMG",command=self.mercedes_benz,bg="yellow",fg="black",activebackground="red")
        self.mercedes_benz.grid(row=5, column=0, pady=5, padx=5, sticky='w')#chatgtp
        
        #information_koennigsegg
        self.information_koenigsegg=tk.Button(self.root,text="Koenigseggjesko_specs ",command=self.information_koenigsegg,bg="black",fg="white",activebackground="red",border=3.6)
        self.information_koenigsegg.grid(row=6, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #information_ferrari
        self.information_ferrari=tk.Button(self.root,text="Ferrari_specs",command=self.information_ferrari,bg="red",fg="black",activebackground="red",border=3.6,highlightcolor="red",state="active")
        self.information_ferrari.grid(row=7, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #infromation_of_KTM_X_BOW
        self.information_X_BOW=tk.Button(self.root,text="KTM X BOW_specs",command=self.information_X_BOW,bg="orange",fg="black",activebackground="red",border=3.6)
        self.information_X_BOW.grid(row=8, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #information_of_THE_BMW_M5
        self.information_BMW_M5=tk.Button(self.root,text="BMW M5 specs",command=self.information_BMW_M5,bg="blue",fg="white",activebackground="red",border=3.6)
        self.information_BMW_M5.grid(row=9, column=0, pady=5, padx=5, sticky='w')#chatgtp
        #information_about_mercedes_benz
        self.information_mercedes_benz=tk.Button(self.root,text="Mercedes_AMG",command=self.information_mercedes_benz,bg="yellow",fg="black",activebackground="red",border=3.6)
        self.information_mercedes_benz.grid(row=10, column=0, pady=5, padx=5, sticky='w')#chatgtp
   # def showimage(self):
    #    self.root=tk.Tk
    #    self.imagepath="D:\\cars\\Koenigsegg CC850 - 1.webp"   
    #    self.image_=Image.open("D:\\cars\\Koenigsegg CC850 - 1.webp")
    #    self.label=tk.Label(self.root,image=self.image_)
    #    self.label.grid(row=10,column=0,padx=5,pady=5,sticky='W')        
#eroor point eroor:the image not found  but image is present in the "D:\cars"
    #infromation_of_koenigsegg_
    #def setup(self):
    #    self.root.title("koenigsegg")    
    #   self.image=Image.open("D:\\cars\\470674-ktm-x-bow-gt-xr-my2023-action-images-action-images-1662741447.jpg")
    #    self.resizedimage=self.image.resize((200,200))
    #    self.tk_image=ImageTk.PhotoImage(self.resizedimage)
    #    self.label=tk.Label(self.root,image=self.tk_image)
    #    self.label.grid(row=10, column=0, pady=5, padx=5, sticky='w')
    #    self.label.pack(padx=5,pady=5)
    
    def information_koenigsegg(self):
        self.cars="C:\\Users\\sidda\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-06-14 092609.png"
        self.img_read=mpimg.imread(self.cars)
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()

    #information_Ferrari
    def information_ferrari(self):
        self.cars="C:\\Users\\sidda\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-06-14 095413.png"
        self.img_read=mpimg.imread(self.cars)
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
    #information_about_X_BOW
    def information_X_BOW(self):
        self.cars="C:\\Users\\sidda\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-06-14 101108.png"
        self.img_read=mpimg.imread(self.cars)
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
    #information_about_BMW_M5
    def information_BMW_M5(self):
        self.cars="C:\\Users\\sidda\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-06-14 120701.png"
        self.img_read=mpimg.imread(self.cars)
        plt.imshow(self.img_read)
        plt.axis("off")
        plt.show()
    #information_about_mercedes_benz
    def information_mercedes_benz(self):
        self.cars="C:\\Users\\sidda\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-06-14 121422.png"
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
    #koenigsegg_image=koenigsegg_(root)
    #Ferrari_image=Ferrari_(root)
    #KTM_image=KTM_(root)
    #mercedes_benz_image=mercedes_benz(root)
    #BMWM5_image=BMWM5_(root)
    #scrollbar_=scrollbar(root)
    #root.mainloop()
    #root.mainloop()
    #root.mainloop()
    root.mainloop()
    root.mainloop()
    #root.mainloop()
