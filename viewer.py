from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('This is sample')
root.iconbitmap('E:/Tkinter/sample.ico')




my_img1 = ImageTk.PhotoImage(Image.open("images/img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/img4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/img5.jpg"))

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0,columnspan=3)

image_list = [my_img1, my_img2, my_img3,my_img4, my_img5]

def forward(image_number):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])

    button_forward = Button(root, text=">>", command = lambda: forward(image_number+1))
    button_backward = Button(root, text="<<", command = lambda: backward(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state = DISABLED)      
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_backward.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def backward(image_number):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    
    button_backward = Button(root, text="<<", command = lambda: backward(image_number-1))
    button_forward = Button(root, text=">>", command = lambda: forward(image_number+1))
    
    if image_number == 1:
        button_backward = Button(root, text="<<", state = DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_backward.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    


button_backward = Button(root, text="<<", state=DISABLED)
button_quit = Button(root, text="Exit Button", command=root.quit)
button_forward = Button(root, text=">>", command = lambda: forward(2))

button_backward.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()