from Tkinter import *

import tkMessageBox


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()


# create the application



class Application(Frame):

    def say_hi(self):
        print"Hello world"
        #os.system('O7.py')


    def createWidgets(self):


        #quit button
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "green"
        self.QUIT["bg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})


        #hi button
        self.hi_johnny = Button(self)
        self.hi_johnny["text"] = "Hello",
        self.hi_johnny["command"] = self.say_hi
        self.hi_johnny["bg"]   = "green"
        self.hi_johnny.pack({"side": "left"})




    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
#app.mainloop()


root = App()
root.master.title("My Do-Nothing Application")
root.master.minsize(1000,600)
root.master.maxsize(4000, 1090)

# start the program
root.mainloop()



root.destroy()