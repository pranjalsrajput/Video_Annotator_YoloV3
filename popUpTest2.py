# import tkinter as tk
# from PIL import Image,ImageTk
#
#
# root = tk.Tk()
# version = "Version 1.0 -- 10.2018"
# root.title(version)
# root.geometry("675x200")
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
#
# main_options=["Doors EXPORT","ANALYSE","VISUALIZE","Auto-Mode","Configuration"]
#
# tk.Label(root, text="Here is where you message will go from the msg section of your buttonbox").grid(row=0, column=0, columnspan = len(main_options), stick="n", pady=(15,0))
# image = "/home/pranjal/Documents/PythonProjects/PyTorch-YOLOv3/data/samples/dog.jpg"
# img = ImageTk.PhotoImage(Image.open(image))
# tk.Label(root,image=img).grid(row=1, column=0, pady=5)
#
# frame2 = tk.Frame(root)
# frame2.grid(row=2, column=0)
#
# for ndex, item in enumerate(main_options):
#     tk.Button(frame2, text=item).grid(row=0, column=ndex, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
#
# root.mainloop()


import tkinter as tk
from PIL import Image,ImageTk

bibId_Enter=0
bibId_Quit=0
boolean_quit=False
boolean_skip=False
copy_of_image=None
label=None

def show_entry_fields(master1):
    global bibId_Enter
    global boolean_quit
    boolean_quit = False
    if e2.get().isdigit():
        bibId_Enter=e2.get()
        e2.delete(0, tk.END)
        #print("Entered bib: %s" % (bibId))
        #master1.quit()
        master1.destroy()
        master1.quit()
    else:
        e2.delete(0,tk.END)

def quitButton(master1):
    global bibId_Quit, boolean_quit
    boolean_quit=True
    master1.destroy()
    master1.quit()

def skipButton(master):
    global boolean_skip
    boolean_skip=True
    master.destroy()
    master.quit()

def continueButton(master):
    global boolean_skip
    boolean_skip=False
    master.destroy()
    master.quit()

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

def skipFrame(image):
    master = tk.Toplevel()
    image_open = Image.open(image)
    [w,h]= image_open.size
    print(w,h)
    image_open = image_open.resize((1700, 900), Image.ANTIALIAS)
    # if w>1700 or h>900:
    #     image_open = image_open.resize((1700, 900), Image.ANTIALIAS)
    # elif w<850 or h<450:
    #     image_open = image_open.resize((2*w, 2*h), Image.ANTIALIAS)

    #img = ImageTk.PhotoImage(Image.open(image1))
    img = ImageTk.PhotoImage(image_open)
    # image1 = Image.open(image)
    # global copy_of_image, label
    # copy_of_image = image1.copy()
    # label = tk.Label(master, image=img)
    tk.Label(master, image=img).grid(row=0, column=0, pady=5)
    # label.bind('<Configure>', resize_image)
    # label.pack(fill=tk.BOTH, expand=tk.YES)

    tk.Label(master,
             text="Skip frame?").grid(row=1, column=0)
    global e3
    e3 = tk.Frame(master)
    e3.grid(row=0, column=0)
    #e3.pack(fill=tk.BOTH, expand=tk.YES)
    tk.Button(master,
              text='Skip',
              command=lambda: skipButton(master)).grid(row=3,
                                                       column=0,
                                                       sticky=tk.W,
                                                       pady=4)
    tk.Button(master,
              text='Continue', command=lambda: continueButton(master)).grid(row=3,
                                                                            column=1,
                                                                            sticky=tk.W,
                                                                            pady=4)
    tk.mainloop()

def callSkipFrame(image):
    skipFrame(image)
    return boolean_skip



def popUpImage(image):

    master = tk.Toplevel()
    boolean=True
    #image = "/home/pranjal/Documents/PythonProjects/PyTorch-YOLOv3/data/samples/dog.jpg"
    image_open=Image.open(image)
    image_open = image_open.resize((1400, 700), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image_open)
    tk.Label(master,image=img).grid(row=0, column=0, pady=5)

    tk.Label(master,
             text="Enter BibId").grid(row=1,column=0)

    tk.Label(master,
             text="*Enter only numbers").grid(row=3,column=0)

    global e1, e2
    e1= tk.Frame(master)
    e2 = tk.Entry(master)
    #bibId=0

    e1.grid(row=0, column=0)
    e2.grid(row=2, column=0)

    tk.Button(master,
              text='Quit',
              command=lambda: quitButton(master)).grid(row=3,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(master,
              text='Enter', command=lambda: show_entry_fields(master)).grid(row=3,
                                                           column=1,
                                                           sticky=tk.W,
                                                           pady=4)
    tk.mainloop()

def callPopUpImage(image):
    popUpImage(image)
    if boolean_quit:
        return bibId_Quit
    else:
        return bibId_Enter

if __name__ == '__main__':
    # bib=callPopUpImage("/home/pranjal/Documents/PythonProjects/PyTorch-YOLOv3/data/samples/dog.jpg")
    # print("Entered Bib: ", bib)
    flag=callSkipFrame("/home/pranjal/Documents/PythonProjects/PyTorch-YOLOv3/data/samples/dog.jpg")
    print("Skip? ",flag)