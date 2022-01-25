# not yet finished 

from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image
import os

class app:

    def __init__(self):
        self.hiddenthing = Tk()
        self.hiddenthing.withdraw()
        self.homepage()

    def homepage(self):
        self.mainpage = Tk()
        self.mainpage.title("home page")
        self.mainpage.resizable(width=False, height=False)
        self.mainpage.configure(width=350, height=500)
        self.firstbutton = Button(self.mainpage, text="Format converstion", command=lambda: self.newlayout())
        self.firstbutton.place(height=50, width=200, relx=0.2, rely=0.1)
        self.secondbutton = Button(self.mainpage, text="Resizing", command=lambda: self.resizingpage())
        self.secondbutton.place(height=50, width=200, relx=0.2, rely=0.2)
        self.thirdbutton  = Button(self.mainpage, text="Quit", command=lambda: quit())
        self.thirdbutton.place(height=50, width=200, relx=0.2, rely=0.3)
        self.mainpage.mainloop()

    def newlayout(self):

        self.mainpage.destroy()
        self.formateconverstion = Tk()
        self.formateconverstion.title("Format Converstion")
        self.formateconverstion.resizable(width=False, height=False)
        self.formateconverstion.configure(width=350, height=500)
        self.label1 = Label(self.formateconverstion, text="Enter image name with formate : ")
        self.label1.place(relx=0.2, rely=0.05)
        self.entry1 = Entry(self.formateconverstion)
        self.entry1.place(height=30, width=180, relx=0.2, rely=0.1)
        self.selectbutton = Button(self.formateconverstion, text="Select file", command=lambda: self.selectfile())
        self.selectbutton.place(relx=0.2, rely=0.2)
        foramat_types = [".png", ".jpeg", ".gif", ".jfif", ".bmp", ".dib", ".sgi", ".ico", ".pcx", ".ppm", ".tiff", ".im", ".eps", ".tga", ".webp"]
        self.aaa = StringVar(self.formateconverstion)
        self.aaa.set("Select formate")
        self.optionsel = OptionMenu(self.formateconverstion, self.aaa, *foramat_types)
        self.optionsel.place(relx=0.2, rely=0.3)
        self.submit1 = Button(self.formateconverstion, text="Convert", command=lambda: self.gettingimagenamefromuse(self.entry1.get(), self.aaa.get()))
        self.submit1.place(height=50, width=200, relx=0.2, rely=0.4)

        self.formateconverstion.mainloop()

    # selecting file function
    def selectfile(self):
         filename = askopenfilename(title="select your file")
         self.entry1.insert(0, filename)

    def gettingimagenamefromuse(self, name, type):
        a = Image.open(name)
        a.save(name+type)
        self.formateconverstion.destroy()
        self.homepage()
        
 """ def resizingpage(self):
        self.mainpage.destroy()
        self.resize = Tk()
        self.resize.title("Resizing")
        self.resize.resizable(width=False, height=False)
        self.resize.configure(width=350, height=500)
        self.label2 = Label(self.resize, text="Resize :")
        self.label2.place(relx=0.1, rely=0.3)
        #width
        self.entry2 = Entry(self.resize)
        self.entry2.place(width=40, height=20, relx=0.245, rely=0.3)
        self.label3 = Label(self.resize, text="width  X")
        self.label3.place(relx=0.35, rely=0.3)
        #height
        self.entry3 = Entry(self.resize)
        self.entry3.place(width=40, height=20, relx=0.51, rely=0.3)
        self.label4 = Label(self.resize, text="height")
        self.label4.place(relx=0.625, rely=0.3)
        self.label5 = Label(self.resize, text="Enter image name with formate : ")
        self.label5.place(relx=0.2, rely=0.05)
        #image name
        self.entry4 = Entry(self.resize)
        self.entry4.place(height=30, width=180, relx=0.2, rely=0.1)
        self.submit2 = Button(self.resize, text="Resize", command=lambda: self.resize001(self.entry2.get(), self.entry3.get(), self.entry4.get(), self.aaa11.get()))
        self.submit2.place(relx=0.2, rely=0.5, width=100, height=40)
        #size label

        foramat_types = [".png", ".jpeg", ".gif", ".jfif", ".bmp", ".dib", ".sgi", ".ico", ".pcx", ".ppm", ".tiff",
                         ".im", ".eps", ".tga", ".webp"]
        self.aaa11 = StringVar(self.resize)
        self.aaa11.set("Select formate")
        self.optionsel = OptionMenu(self.resize, self.aaa11, *foramat_types)
        self.optionsel.place(relx=0.2, rely=0.4)

        self.resize.mainloop()

    def resize001(self, w, h, name, type):
        fielname = random.randint(100, 10000000)
        aaa = Image.open("imagedb/"+name)
        aaa.resize((int(w), int(h)), Image.ANTIALIAS)
        aaa.save("imagedb/"+str(fielname)+type)
        self.label6 = Label(self.resize, text="size of image = " + str((os.stat("imagedb/"+str(fielname)+type).st_size)/1024) + " KB")
        self.label6.place(relx=0.2, rely=0.6)                                """



app()
