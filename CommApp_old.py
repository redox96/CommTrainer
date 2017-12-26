from tkinter import *
import csv

# Import functions
from letterpairs import random_LP, create_output_file, buffer, create_letterpair, choose_type
from update_stats import update_stats
from save_to_results import save_to_results
from top_bad_list import bad_list, top_list
from recover_results import recover_results
from cutoff import cutoff_stats
from counts2 import count_stats2
from group_comms import weigh_comms
from cutoff_motivation import cutoff_motivation
from load_comms import show_comm

class MyApp(Frame):
    def __init__(self, master = None):
        # Add a frame for the radiobuttons to chose the comm type
        self.topframe = Frame(master)
        self.topframe.pack(side=TOP)
        super().__init__(master, width=800, height=800)
        self.pack()

        # Add two frames for the statistics at the bottom of the window
        self.bottomframe2 = Frame(master=None)
        self.bottomframe2.pack(side=BOTTOM,pady=10)
        self.bottomframe = Frame(master=None)
        self.bottomframe.pack(side=BOTTOM,pady=10)

        self.createWidgets()
        self.createBindings()

    def createWidgets(self):
        self.success = IntVar(value=0)
        self.counter = IntVar(value=0)
        self.result = IntVar(value=0)
        self.times_new = IntVar(value=0)
        self.topFive = StringVar(value=None)
        self.topFiveGood = StringVar(value=None)
        self.num_tot = IntVar(value=0)
        self.cutoff = IntVar(value=0)
        self.above_cutoff = IntVar(value=0)
        self.counts_total = IntVar(value=0)
        self.all_types = choose_type()
        self.comm_type = StringVar(value=None)
        self.buffer = StringVar(value="Corner")
        self.letters = StringVar(value=None)
        self.hint_used = IntVar(value=None)

        self.comm_type.set(NONE)
        for a in self.all_types:
            b = Radiobutton(self.topframe, text= a, value = a, variable = self.comm_type, command = self.chosen_type,
                            font=(None,15), indicatoron=0)
            b.pack(side="left", pady=15, padx = 15)

# TODO: Nice representations of the top 5 worst and best comms including times and counts
        self.badfivelabel=Label(self,text="Worst Comms", font=(None,20))
 #       self.badfivelabel.pack(pady = 5)
        self.topfivelabel=Label(self,text="Best Comms", font=(None,20))
 #       self.topfivelabel.pack(pady = 5)
        self.successlabel=Label(self,font=(None,30),pady=30, text="Choose Comm Type", fg="Red")
        self.successlabel.pack()
        self.letterpair=Label(self,text="Letterpair", font=(None, 66))
        self.letterpair.pack(ipady=30)
        self.timer=Label(self, text="TIME", font=(None,40))
        self.timer.pack(pady = 20)
        self.buttonstart=Button(self, text="Start",font=(None,20),bg="Green")
        self.buttonstart.pack(pady = 5)
        self.cutoff_ask=Label(self.bottomframe, text="Cutoff", font=(None,15))
        self.cutoff_ask.pack(side=LEFT, padx = 5)
        self.cutoff_box=Spinbox(self.bottomframe, from_=0, to=10, increment=0.5, font=(None,15),width=4)
        self.cutoff_box.delete(0,"end")
        self.cutoff_box.insert(0,7)
        self.cutoff_box.pack(side=LEFT, padx = 10)
        self.cutoff_button=Button(self.bottomframe, text="Update", font=(None,15))
        self.cutoff_button.pack(side=LEFT)
        self.cutoff_output=Label(self.bottomframe2, text = "Set Comm Type and Cutoff to view Statistics", font=(None, 15))
        self.cutoff_output.pack(side=TOP, pady = 5)
        self.cutoff_output2=Label(self.bottomframe2, text = " ", font=(None, 15),fg="Blue")
        self.cutoff_output2.pack(side=TOP, pady = 5)
        self.cutoff_output3=Label(self.bottomframe2,text = " ", font = (None, 15))
        self.cutoff_output3.pack(side=TOP, pady = 5)


    def chosen_type(self):
        self.successlabel.configure(text = " ")

        # Define buffers for the chosen Comm set
        self.buffer = StringVar(value=None)
        self.buffer = buffer(self.comm_type.get())
        print((self.buffer))

        # Create letterpairs
        self.letters = StringVar(value=None)
        self.letters = create_letterpair(self.buffer)

        # Create an output file and recover previous results
        create_output_file(self.letters, self.comm_type.get())
        recover_results(self.buffer, self.comm_type.get())


    def createBindings(self):
        self.bind_all("<ButtonPress>",self.eventButtonPress)
        self.bind_all("<KeyPress>",self.eventKeyPress)


    def eventButtonPress(self,event):

        # Generate a letterpair if Start is clicked and start the timer
        if event.widget==self.buttonstart:
            self.randomletters=StringVar(value=random_LP(self.buffer,self.letters))
            self.letterpair.configure(text = self.randomletters.get(), font=(None, 66)) #, "bold"
            self.result.set(event.time)

        elif event.widget== self.cutoff_button:
            self.cutoff=float(self.cutoff_box.get())
            print(self.cutoff)
            self.counts_total=count_stats2(self.comm_type.get())
            self.above_cutoff=cutoff_stats(self.cutoff,self.buffer,self.comm_type.get())
            self.cutoff_output.configure(text = [self.above_cutoff,"comms","above","and", len(self.letters)-self.above_cutoff, "comms","below","the","cutoff"])
            self.cutoff_output3.configure(text = [self.counts_total,"tries","up","to","now"])
            self.cutoff_output2.configure(text=cutoff_motivation(self.above_cutoff,self.counts_total))
        else:
            pass

    def eventKeyPress(self,event):
        if event.keysym == "Return":
            randlet = self.randomletters.get()

            if self.hint_used == 1:
                self.d_time = self.d_time + 10
                self.hint_used == 0
            else:
                pass

            save_to_results(randlet,self.d_time, self.comm_type.get())

            [self.times_new, self.counter] = update_stats(randlet, self.d_time, self.buffer, self.comm_type.get())
            print(self.times_new)
            print(self.counter)
        #    self.counter = update_stats(randlet, self.d_time, self.buffer, self.comm_type.get())[1]
            self.successlabel.configure(text= ["Avrg:", round(float(self.times_new),2), "Count:", self.counter])
            self.topFive = bad_list(self.buffer, self.comm_type.get())
            self.badfivelabel.configure(text=self.topFive)
            self.topFiveGood = top_list(self.buffer, self.comm_type.get())
            self.topfivelabel.configure(text=self.topFiveGood)

 #           weigh_comms(self.buffer,self.comm_type.get(),self.cutoff)

            # Reset hints
            #self.hint_used = 0
        elif event.keysym == "h":
            text_comm = show_comm(self.randomletters.get(),self.buffer,self.comm_type.get())
            print(text_comm)
            self.successlabel.configure(text = text_comm)
            self.hint_used = 1

        else:
            self.d_time = IntVar(value=0)
            self.d_time = (event.time - self.result.get())/1000 #in Seconds
            self.timer.configure(text=self.d_time)
            self.successlabel.configure(text="Press Enter to save the result \n or h to show the comm")


root = Tk()
root.title("CommTrainer_Corners")
root.geometry("600x750")
app = MyApp(root)
app.mainloop()
