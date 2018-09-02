from tkinter import *
import csv

# Import functions
from letterpairs import random_LP, create_output_file, buffer, create_letterpair, choose_type, twist, flip, remove_twistflips
from update_stats import update_stats
from save_to_results import save_to_results
from top_bad_list import bad_list, top_list
from recover_results import recover_results
from cutoff import cutoff_stats
from counts2 import count_stats2
from cutoff_motivation import cutoff_motivation
from load_comms import show_comm
from topflop_output import topflop_output
from group_for_randomization import group_for_rand
from comm_chooser import comm_chooser
from load_words import show_words, show_words2, show_words3

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
        self.words = StringVar(value=None)
        self.words2 = StringVar(value=None)
        self.words3 = StringVar(value=None)
        self.num_tot = IntVar(value=0)
        self.cutoff = DoubleVar(value=0)
        self.cutoff=7.0 #set to 7 as default
        self.above_cutoff = IntVar(value=0)
        self.counts_total = IntVar(value=0)
        self.all_types = choose_type()
        self.comm_type = StringVar(value=None)
        self.buffer = StringVar(value="Corner")
        self.letters = StringVar(value=None)
        self.hint_used = IntVar(value=None)
        self.learning = IntVar(value=0)
        self.learnword = IntVar(value=0)
        self.randlet = StringVar(value=0)

        self.comm_type.set(NONE)
        for a in self.all_types:
            b = Radiobutton(self.topframe, text= a, value = a, variable = self.comm_type, command = self.chosen_type,
                            font=(None,15), indicatoron=0)
            b.pack(side="left", pady=15, padx = 12)
        self.learning_button = Checkbutton(self.topframe, text = "L", variable = self.learning ,font = (None,15, "bold"), indicatoron = 0,
                                           command = self.learningmode)
        self.learnword_button = Checkbutton(self.topframe, text = "W", variable = self.learnword ,font = (None,15, "bold"), indicatoron = 0,
                                           command = self.learnword)
        self.learning_button.pack(pady=15, padx =20,ipadx = 4)
        self.learnword_button.pack(pady=15, padx =20,ipadx = 4)
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
        self.cutoff_box=Spinbox(self.bottomframe, from_=0, to=15, increment=0.5, font=(None,15),width=4)
        self.cutoff_box.delete(0,"end")
        self.cutoff_box.insert(0,7)
        self.cutoff_box.pack(side=LEFT, padx = 10)
        self.cutoff_button=Button(self.bottomframe, text="Update", font=(None,15))
        self.cutoff_button.pack(side=LEFT)
        self.topflop=Button(self.bottomframe, text = "TopFlops", font = (None, 15))
        self.topflop.pack(side=LEFT, padx = 20)
        self.words_button=Button(self.bottomframe, text="Words", font=(None,15))
        self.words_button.pack(side=LEFT)
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
        self.letters = remove_twistflips(create_letterpair(self.buffer, self.comm_type.get()),self.comm_type.get())

        # Create an output file and recover previous results
        create_output_file(self.letters, self.comm_type.get())
        recover_results(self.buffer, self.comm_type.get())

    def learningmode(self):
        if self.learning.get() == 1:
            print("pressed")
        else:
            print("unpressed")

    def learnword(self):
        if self.learnword.get() == 1:
            print("pressed")
        else:
            print("unpressed")

    def createBindings(self):
        self.bind_all("<ButtonPress>",self.eventButtonPress)
        self.bind_all("<KeyPress>",self.eventKeyPress)


    def eventButtonPress(self,event):

        # Generate a letterpair if Start is clicked and start the timer
        if event.widget==self.buttonstart:
            print(self.cutoff)
            comms_groups = group_for_rand(self.cutoff,self.comm_type.get())
            #self.randomletters=StringVar(value = comm_chooser(comms_groups))
            self.randlet = comm_chooser(comms_groups)
            print(self.randlet)
            #print(self.randomletters.get())

            self.letterpair.configure(text = self.randlet, font=(None, 66)) #, "bold"
            if self.learning.get() == 1:
                text_comm = show_comm(self.randlet,self.buffer,self.comm_type.get())
                print(text_comm)
                self.successlabel.configure(text = text_comm)
                print(self.randlet, self.buffer)
                if self.learnword.get() == 1:
                    self.words = show_words(self.randlet, self.buffer)
                    print(show_words(self.randlet,self.buffer))
                    self.words2 = show_words2(self.randlet, self.buffer)
                    self.words3 = show_words3(self.randlet, self.buffer)
                    print(self.words)
                    self.cutoff_output.configure(text = self.words)
                    self.cutoff_output2.configure(text = self.words2)
                    self.cutoff_output3.configure(text = self.words3)
                else:
                    pass
            else:
                pass
            self.result.set(event.time)

        elif event.widget==self.learning_button:
            print("test")
            if self.learning.get() == 0:
                print(self.learning.get())
                self.successlabel.configure(text = "Learning mode on")
            elif self.learning.get() == 1:
                self.successlabel.configure(text = "Learning mode off")
            else:
                pass

        elif event.widget== self.cutoff_button:
            self.cutoff=float(self.cutoff_box.get())
            print(self.cutoff)
            self.counts_total=count_stats2(self.comm_type.get())
            self.above_cutoff=cutoff_stats(self.cutoff,self.buffer,self.comm_type.get())
            self.cutoff_output.configure(text = [self.above_cutoff,"comms","above","and", len(self.letters)-self.above_cutoff-1, "comms","below","the","cutoff"])
            self.cutoff_output3.configure(text = [self.counts_total,"tries","up","to","now"],font=(None,15))
            self.cutoff_output2.configure(text=cutoff_motivation(self.above_cutoff,self.counts_total),fg="Blue",font=(None,15))

        # TO DO
        elif event.widget == self.words_button:
            print(self.randlet, self.buffer)
            self.words = show_words(self.randlet, self.buffer)
            print(show_words(self.randlet,self.buffer))
            self.words2 = show_words2(self.randlet, self.buffer)
            self.words3 = show_words3(self.randlet, self.buffer)
            print(self.words)
            self.cutoff_output.configure(text = self.words)
            self.cutoff_output2.configure(text = self.words2)
            self.cutoff_output3.configure(text = self.words3)

        elif event.widget == self.topflop:
            self.topFive = bad_list(self.buffer, self.comm_type.get())
            self.cutoff_output2.configure(text=topflop_output(self.topFive),fg="Black",font=(None,12))
            self.topFiveGood = top_list(self.buffer, self.comm_type.get())
            self.cutoff_output3.configure(text=topflop_output(self.topFiveGood),font=(None,12))
            self.cutoff_output.configure(text = "Your top and flop comms (letter pair, time, count):")

        else:
            pass

    def eventKeyPress(self,event):
        if event.keysym == "Return":
            if self.hint_used == 1:
                self.d_time = self.d_time + 10
                self.hint_used == 0
            else:
                self.hint_used == 0

            save_to_results(self.randlet,self.d_time, self.comm_type.get())

            [self.times_new, self.counter] = update_stats(self.randlet, self.d_time, self.buffer, self.comm_type.get())
            print(self.times_new)
            print(self.counter)
            self.successlabel.configure(text= [self.randlet, "Avrg:", round(float(self.times_new),2), "Count:", self.counter])

        elif event.keysym == "h":
            text_comm = show_comm(self.randlet,self.buffer,self.comm_type.get())
            print(text_comm)
            self.successlabel.configure(text = text_comm)
            self.hint_used = 1

        elif event.keysym == "Down":
            if self.hint_used == 1:
                self.d_time = self.d_time + 10
                self.hint_used == 0
            else:
                self.hint_used == 0

            save_to_results(self.randlet,self.d_time, self.comm_type.get())

            [self.times_new, self.counter] = update_stats(self.randlet, self.d_time, self.buffer, self.comm_type.get())
            print(self.times_new)
            print(self.counter)
            self.successlabel.configure(text= [self.randlet, "Avrg:", round(float(self.times_new),2), "Count:", self.counter])
            comms_groups = group_for_rand(self.cutoff,self.comm_type.get())


            self.randlet = comm_chooser(comms_groups)
            print(self.randlet)

            self.letterpair.configure(text = self.randlet, font=(None, 66)) #, "bold"
            self.result.set(event.time)

            if self.learning.get() == 1:
                text_comm = show_comm(self.randlet,self.buffer,self.comm_type.get())
                print(text_comm)
                self.successlabel.configure(text = text_comm)
                if self.learnword.get() == 1:
                    self.words = show_words(self.randlet, self.buffer)
                    print(show_words(self.randlet,self.buffer))
                    self.words2 = show_words2(self.randlet, self.buffer)
                    self.words3 = show_words3(self.randlet, self.buffer)
                    print(self.words)
                    self.cutoff_output.configure(text = self.words)
                    self.cutoff_output2.configure(text = self.words2)
                    self.cutoff_output3.configure(text = self.words3)
                else:
                    pass
            else:
                pass

        else:
            self.d_time = IntVar(value=0)
            self.d_time = (event.time - self.result.get())/1000 #in Seconds
            self.timer.configure(text=self.d_time)
            #self.successlabel.configure(text="Press Enter to save the result \n or h to show the comm")
            self.hint_used = 0

root = Tk()
root.title("CommTrainer_Corners")
root.geometry("600x750")
app = MyApp(root)
app.mainloop()
