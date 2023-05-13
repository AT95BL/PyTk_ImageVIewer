from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap(r'C:\Users\AT95\OneDrive\Desktop\PythonTkinter\slika.ico')

myImage1 = ImageTk.PhotoImage(Image.open('download (8).png'))
myImage2 = ImageTk.PhotoImage(Image.open('download (9).png'))
myImage3 = ImageTk.PhotoImage(Image.open('download (10).png'))
myImage4 = ImageTk.PhotoImage(Image.open('download (11).png'))
myImage5 = ImageTk.PhotoImage(Image.open('download (12).png'))

imageList = [myImage1, myImage2, myImage3, myImage4, myImage5]

myLabel = Label(image = myImage1)
myLabel.grid(row=0, column=0, columnspan=3)

def backward(imageNumber):
    global myLabel
    global buttonForward
    global buttonBackward

    myLabel.grid_forget()
    myLabel = Label(image = imageList[imageNumber-1])
    buttonForward = Button(root, text = ">>", command = lambda : forward(imageNumber+1))
    buttonBackward = Button(root, text = "<<", command = lambda: backward(imageNumber-1))

    if imageNumber == 1:
        buttonBackward = Button(root, text=">>", state = DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBackward.grid(row=1, column=0)
    #buttonExit.grid(row=1, column=1)
    buttonForward.grid(row=1, column=2)

def forward(imageNumber):
    global myLabel
    global buttonForward
    global buttonBackward

    myLabel.grid_forget()
    myLabel = Label(image = imageList[imageNumber-1])
    buttonForward = Button(root, text = ">>", command = lambda : forward(imageNumber+1))
    buttonBackward = Button(root, text = "<<", command = lambda: backward(imageNumber-1))

    if imageNumber == 5:
        buttonForward = Button(root, text=">>", state = DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBackward.grid(row=1, column=0)
    #buttonExit.grid(row=1, column=1)
    buttonForward.grid(row=1, column=2)
    

buttonBackward = Button(root, text = "<<", command = backward, state=DISABLED)
buttonExit = Button(root, text = "EXIT PROGRAM", command = root.quit)
buttonForward = Button(root, text = ">>", command = lambda : forward(2))

buttonBackward.grid(row=1, column=0)
buttonExit.grid(row=1, column=1)
buttonForward.grid(row=1, column=2)

root.mainloop()