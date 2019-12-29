from easygui import buttonbox
from easygui import multenterbox
import matplotlib.pyplot as plt
from PIL import Image,ImageTk
import numpy as np
from matplotlib.ticker import NullLocator

#msgbox("Hello, world!")
def popUpImage(img):
    #image = "/home/pranjal/Documents/PythonProjects/PyTorch-YOLOv3/data/samples/dog.jpg"
    image=img
    msg = "Do you want to enter bibId?"
    choices = ["Yes","No"]
    boolean=False
    fieldValues = []  # we start with blanks for the values
    while(not boolean):
        reply = buttonbox(msg, image=image, choices=choices)
        print(reply)

        if reply=="Yes":
            msg = "Enter BibId"
            title = "Runner bibId"
            fieldNames = ["BibId"]
            boolean = True

            fieldValues = multenterbox(msg, title, fieldNames)
            if fieldValues==None:
                print('Entered value', 0)
            else:
                print('Entered value', fieldValues[0])


            # make sure that none of the fields was left blank
            while 1:
                if fieldValues == None:
                    fieldValues = []
                    fieldValues.append(0)
                    boolean = False
                    break
                errmsg = ""
                for i in range(len(fieldNames)):
                    if fieldValues[i].strip() == "":
                        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
                if errmsg == "": break  # no problems found
                fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
                #print('Entered value',fieldValues)
                # if(fieldValues is None):
                #     boolean=False
                # else:
                boolean=True
                print("Entered BibId:", fieldValues[0])

        else:
            fieldValues.append(0)
            print("Entered BibId:", fieldValues[0])
            boolean = True
    return fieldValues[0]

def saveImage(image):
    # img = np.array(Image.open(image))
    # plt.figure()
    # fig, ax = plt.subplots(1)
    # ax.imshow(img)
    # # plt.axis("off")
    # # plt.gca().xaxis.set_major_locator(NullLocator())
    # # plt.gca().yaxis.set_major_locator(NullLocator())
    # temp_file = image.split("/")[-1].split(".")[0]
    # plt.savefig(f"output/{temp_file}_temp.png", bbox_inches="tight", pad_inches=0.0)
    # img1 = Image.open("output/" + temp_file + "_temp.png")
    # img1.show()

    temp_file = image.split("/")[-1].split(".")[0]
    #plt.savefig(f"output/{temp_file}_temp.png", bbox_inches="tight", pad_inches=0.0)

    import cv2
    img = cv2.imread(image)
    picName = "output/" + temp_file + "_temp_cv2.png"
    cv2.imwrite(picName, img)

if __name__ == '__main__':
    saveImage('/home/pranjal/Documents/PythonProjects/PyTorch-YOLOv3/data/samples/dog.jpg')
