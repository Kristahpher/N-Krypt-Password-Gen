import tkinter
import tkinter.messagebox as i
import random
import datetime
import time
import tkinter.messagebox
import clipboard
from tkinter import messagebox
from tkinter import *

def center_window(w=300, h=200):
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root = Tk() 
center_window(387, 330)
root.title("N-Krypt Generator")


def generate_pass1():
        chars = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()'
        s = int(1)
        s2 = s*2
        s3 = s2
        s4 = s3
        s5 = s4
        s6 = s5
        sf = s6
        password = ''
        password2 =''
        password3 =''
        password4 =''
        password5 =''
        password6 =''
        password7 =''

        ##First password generated##
        for a in range(s):
            password += random.choice(chars)

        ##Second password generated##
        password2 = password2
        for b in range(s2):
            password2+=random.choice(chars)

        ##Third password generated##
        password3 = password3
        for c in range(s3):
            password3+=random.choice(chars)

        ##fourth password generated##
        password4 = password4
        for d in range(s4):
            password4+=random.choice(chars)

        ##fifth password generated##
        password5 = password5
        for e in range(s5):
            password5+=random.choice(chars)

        ##sixth password generated##
        password6 = password6
        for f in range(s6):
            password6+=random.choice(chars)
        
        ##seventh password generated##
        password7 = password7
        for g in range(sf):
            password7+=random.choice(chars)

        #password 1 scrambled
        string_one = password
        char_list = list(string_one) # convert string inti list
        random.shuffle(char_list) #shuffle the list
        string_one = ''.join(char_list)

        #password 2 scrambled
        string_two = password2
        char_list = list(string_two) # convert string inti list
        random.shuffle(char_list) #shuffle the list
        string_two = ''.join(char_list)

        #Password three scrambled
        string_three = password3
        char_list = list(string_three) # convert string inti list
        random.shuffle(char_list) #shuffle the list
        string_three = ''.join(char_list)

        #password 4 scrambled
        string_four = password4
        char_list = list(string_four) # convert string inti list
        random.shuffle(char_list) #shuffle the list
        string_four = ''.join(char_list)

        #password 5 scrambled
        string_five = password5
        char_list = list(string_five) # convert string inti list
        random.shuffle(char_list) #shuffle the list
        string_five = ''.join(char_list)

        #password 6 scrambled
        string_six = password6
        char_list = list(string_six) # convert string inti list
        random.shuffle(char_list) #shuffle the list
        string_six = ''.join(char_list)

        #combining password 
        string_seven = [password,password2,password3,password4,password5,password6,password7]
        char_list = list([password,password2,password3,password4,password5,password6,password7]) # convert string inti list
        random.shuffle(char_list) #shuffle the list
        string_seven = ''.join(char_list)

        #first scramble of combined
        string_eight = string_seven
        char_list = list(string_eight) # convert string inti list
        random.shuffle(char_list) #shuffle the list
        string_eight = ''.join(char_list)

        #second scramble of combined
        string_nine = string_eight
        char_list = list(string_eight) # convert string inti list
        random.shuffle(char_list) #shuffle the list
        string_nine = ''.join(char_list)

        #last scramble of combined
        string_ten = string_nine
        char_list = list(string_ten) # convert string inti list
        random.shuffle(char_list) #shuffle the list
        string_ten = ''.join(char_list)

        x = 0
        dt = datetime.datetime.now()
        while x<=0:
                x = x + 1
                with open('nkrypt.txt','a') as f:
                    print(dt.strftime("%Y-%m-%d %H:%M"),"Password: ",string_ten,file=f)

                f.close
        
        clipboard.copy(text = string_ten)
        text = clipboard.paste()
        

def generate_pass2():
        
        chars = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()'
        s = int(1)
        s2 = s*2
        s3 = s2*2
        s4 = s3
        s5 = s4
        s6 = s5
        sf = s6
        password = ''
        password2 =''
        password3 =''
        password4 =''
        password5 =''
        password6 =''
        password7 =''

        ##First password generated##
        for a in range(s):
            password += random.choice(chars)

        ##Second password generated##
        password2 = password2
        for b in range(s2):
            password2+=random.choice(chars)

        ##Third password generated##
        password3 = password3
        for c in range(s3):
            password3+=random.choice(chars)

        ##fourth password generated##
        password4 = password4
        for d in range(s4):
            password4+=random.choice(chars)

        ##fifth password generated##
        password5 = password5
        for e in range(s5):
            password5+=random.choice(chars)

        ##sixth password generated##
        password6 = password6
        for f in range(s6):
            password6+=random.choice(chars)
        
        ##seventh password generated##
        password7 = password7
        for g in range(sf):
            password7+=random.choice(chars)

        #password 1 scrambled
        string_one = password
        char_list = list(string_one) 
        random.shuffle(char_list) 
        string_one = ''.join(char_list)

        #password 2 scrambled
        string_two = password2
        char_list = list(string_two) 
        random.shuffle(char_list) 
        string_two = ''.join(char_list)

        #Password three scrambled
        string_three = password3
        char_list = list(string_three)
        random.shuffle(char_list) 
        string_three = ''.join(char_list)

        #password 4 scrambled
        string_four = password4
        char_list = list(string_four) 
        random.shuffle(char_list) 
        string_four = ''.join(char_list)

        #password 5 scrambled
        string_five = password5
        char_list = list(string_five) 
        random.shuffle(char_list) 
        string_five = ''.join(char_list)

        #password 6 scrambled
        string_six = password6
        char_list = list(string_six) 
        random.shuffle(char_list) 
        string_six = ''.join(char_list)

        #combining password 
        string_seven = [password,password2,password3,password4,password5,password6,password7]
        char_list = list([password,password2,password3,password4,password5,password6,password7]) 
        random.shuffle(char_list) 
        string_seven = ''.join(char_list)

        #first scramble of combined
        string_eight = string_seven
        char_list = list(string_eight) 
        random.shuffle(char_list) 
        string_eight = ''.join(char_list)

        #second scramble of combined
        string_nine = string_eight
        char_list = list(string_eight) 
        random.shuffle(char_list) 
        string_nine = ''.join(char_list)

        #last scramble of combined
        string_ten = string_nine
        char_list = list(string_ten) 
        random.shuffle(char_list) 
        string_ten = ''.join(char_list)


        x = 0
        dt = datetime.datetime.now()
        while x<=0:
                x = x + 1
                with open('nkrypt.txt','a') as f:
                    print(dt.strftime("%Y-%m-%d %H:%M"),"Password: ",string_ten,file=f)

                f.close
        
        clipboard.copy(text = string_ten)
        text = clipboard.paste()

def generate_pass3():

        chars = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()'
        s = int(1)
        s2 = s*2
        s3 = s2*2
        s4 = s3*2
        s5 = s4*2
        s6 = s5
        sf = s6
        password = ''
        password2 =''
        password3 =''
        password4 =''
        password5 =''
        password6 =''
        password7 =''

        ##First password generated##
        for a in range(s):
            password += random.choice(chars)

        ##Second password generated##
        password2 = password2
        for b in range(s2):
            password2+=random.choice(chars)

        ##Third password generated##
        password3 = password3
        for c in range(s3):
            password3+=random.choice(chars)

        ##fourth password generated##
        password4 = password4
        for d in range(s4):
            password4+=random.choice(chars)

        ##fifth password generated##
        password5 = password5
        for e in range(s5):
            password5+=random.choice(chars)

        ##sixth password generated##
        password6 = password6
        for f in range(s6):
            password6+=random.choice(chars)
        
        ##seventh password generated##
        password7 = password7
        for g in range(sf):
            password7+=random.choice(chars)

        #password 1 scrambled
        string_one = password
        char_list = list(string_one) 
        random.shuffle(char_list) 
        string_one = ''.join(char_list)

        #password 2 scrambled
        string_two = password2
        char_list = list(string_two) 
        random.shuffle(char_list) 
        string_two = ''.join(char_list)

        #Password three scrambled
        string_three = password3
        char_list = list(string_three) 
        random.shuffle(char_list) 
        string_three = ''.join(char_list)

        #password 4 scrambled
        string_four = password4
        char_list = list(string_four) 
        random.shuffle(char_list) 
        string_four = ''.join(char_list)

        #password 5 scrambled
        string_five = password5
        char_list = list(string_five) 
        random.shuffle(char_list) 
        string_five = ''.join(char_list)

        #password 6 scrambled
        string_six = password6
        char_list = list(string_six) 
        random.shuffle(char_list) 
        string_six = ''.join(char_list)

        #combining password 
        string_seven = [password,password2,password3,password4,password5,password6,password7]
        char_list = list([password,password2,password3,password4,password5,password6,password7])
        random.shuffle(char_list) 
        string_seven = ''.join(char_list)

        #first scramble of combined
        string_eight = string_seven
        char_list = list(string_eight) 
        random.shuffle(char_list) 
        string_eight = ''.join(char_list)

        #second scramble of combined
        string_nine = string_eight
        char_list = list(string_eight) 
        random.shuffle(char_list) 
        string_nine = ''.join(char_list)

        #last scramble of combined
        string_ten = string_nine
        char_list = list(string_ten) 
        random.shuffle(char_list) 
        string_ten = ''.join(char_list)



        x = 0
        dt = datetime.datetime.now()
        while x<=0:
                x = x + 1
                with open('nkrypt.txt','a') as f:
                    print(dt.strftime("%Y-%m-%d %H:%M"),"Password: ",string_ten,file=f)

                f.close


        clipboard.copy(text = string_ten)
        text = clipboard.paste()

def generate_pass4():

        chars = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()'
        s = int(1)
        s2 = s*2
        s3 = s2*2
        s4 = s3*2
        s5 = s4*2
        s6 = s5*2
        sf = s6*2
        password = ''
        password2 =''
        password3 =''
        password4 =''
        password5 =''
        password6 =''
        password7 =''

        ##First password generated##
        for a in range(s):
            password += random.choice(chars)

        ##Second password generated##
        password2 = password2
        for b in range(s2):
            password2+=random.choice(chars)

        ##Third password generated##
        password3 = password3
        for c in range(s3):
            password3+=random.choice(chars)

        ##fourth password generated##
        password4 = password4
        for d in range(s4):
            password4+=random.choice(chars)

        ##fifth password generated##
        password5 = password5
        for e in range(s5):
            password5+=random.choice(chars)

        ##sixth password generated##
        password6 = password6
        for f in range(s6):
            password6+=random.choice(chars)
        
        ##seventh password generated##
        password7 = password7
        for g in range(sf):
            password7+=random.choice(chars)

        #password 1 scrambled
        string_one = password
        char_list = list(string_one) 
        random.shuffle(char_list) 
        string_one = ''.join(char_list)

        #password 2 scrambled
        string_two = password2
        char_list = list(string_two) 
        random.shuffle(char_list) 
        string_two = ''.join(char_list)

        #Password three scrambled
        string_three = password3
        char_list = list(string_three) 
        random.shuffle(char_list) 
        string_three = ''.join(char_list)

        #password 4 scrambled
        string_four = password4
        char_list = list(string_four) 
        random.shuffle(char_list) 
        string_four = ''.join(char_list)

        #password 5 scrambled
        string_five = password5
        char_list = list(string_five) 
        random.shuffle(char_list) 
        string_five = ''.join(char_list)

        #password 6 scrambled
        string_six = password6
        char_list = list(string_six) 
        random.shuffle(char_list) 
        string_six = ''.join(char_list)

        #combining password 
        string_seven = [password,password2,password3,password4,password5,password6,password7]
        char_list = list([password,password2,password3,password4,password5,password6,password7]) 
        random.shuffle(char_list) 
        string_seven = ''.join(char_list)

        #first scramble of combined
        string_eight = string_seven
        char_list = list(string_eight) 
        random.shuffle(char_list) 
        string_eight = ''.join(char_list)

        #second scramble of combined
        string_nine = string_eight
        char_list = list(string_eight)
        random.shuffle(char_list) 
        string_nine = ''.join(char_list)

        #last scramble of combined
        string_ten = string_nine
        char_list = list(string_ten) 
        random.shuffle(char_list) 
        string_ten = ''.join(char_list)



        x = 0
        dt = datetime.datetime.now()
        while x<=0:
                x = x + 1
                with open('nkrypt.txt','a') as f:
                    print(dt.strftime("%Y-%m-%d %H:%M"),"Password: ",string_ten,file=f)

                f.close

        
        clipboard.copy(text = string_ten)
        text = clipboard.paste()


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(background='black')
        
        self.label_0 = Label(root, text="N-Krypt Generator",width=20,font=("fixedsys", 20),fg='red',borderwidth=10, relief="groove")
        self.label_0.config(bg="black")
        self.label_0.place(x=20,y=0)

        self.label_username = Label(self, text="Username ID:",height=1,width=13,font=("fixedsys", 20),fg='red', bg='black') 
        self.label_password = Label(self, text="Password Key:", height=1,width=13,font=("fixedsys", 20),fg='red',bg='black')

        self.entry_username = Entry(self, show="*",bg='black',fg='white')
        self.entry_password = Entry(self, show="*",bg='black',fg='white')

        self.label_username.grid(row=3)
        self.label_password.grid(row=4)
        self.entry_username.grid(row=3, column=5, pady=70)
        self.entry_password.grid(row=4, column=5, pady=50)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked,bg='red',fg='white',font=("fixedsys", 15))
        self.logbtn.grid(row=5, column=6,pady=20)
        
        self.pack()
                

    def _login_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == 'admin' and password == 'password':
            def center_window(w=300, h=200):
                # get screen width and height
                ws = root.winfo_screenwidth()
                hs = root.winfo_screenheight()
                # calculate position x, y
                x = (ws/2) - (w/2)    
                y = (hs/2) - (h/2)
                root.geometry('%dx%d+%d+%d' % (w, h, x, y))

            root = Tk()
            center_window(800,500)
            root.title("N-Krypt Generator")
            root.configure(background='black')
            label = Label(root, text="<== Click to generate password",font=("fixedsys", 15), fg="red",bg='black',borderwidth=2, relief="sunken")
            label1 = Label(root, text="Generated passwords will be stored in nkrypt.txt",font=("fixedsys", 15), fg="red",bg='black',borderwidth=2, relief="sunken")
            label_0 = Label(root, text="N-Krypt Generator",width=20,font=("fixedsys", 34),fg='red')
            label_0.config(bg="black")
            label_0.place(relx=.5, rely=0.1, anchor="c")
            label.place(relx=.75, rely=0.49, anchor="c")
            label1.place(relx=.75, rely=0.53, anchor="c")
            
            
            button1 = Button(root, text=" Level One N-Kryption ",font=("fixedsys", 20),command=generate_pass1, fg="cyan",bg='black',borderwidth=10, relief="sunken")
            button2 = Button(root, text=" Level Two N-Kryption ",font=("fixedsys", 20),command=generate_pass2, fg="yellow",bg='black',borderwidth=10, relief="sunken")
            button3 = Button(root, text="Level Three N-Kryption",font=("fixedsys", 20),command=generate_pass3, fg="maroon1",bg='black',borderwidth=10, relief="sunken")
            button4 = Button(root, text=" Level Four N-Kryption",font=("fixedsys", 20),command=generate_pass4, fg="white",bg='black',borderwidth=10, relief="sunken")
            button = Button(root, text="Quit",font=("fixedsys", 15),command= quit, fg="red",bg='black')
            button1.place(relx=0.25, rely=.37, anchor="c")
            button2.place(relx=.25, rely=.50, anchor="c")
            button3.place(relx=.25, rely=.62, anchor="c")
            button4.place(relx=.25, rely=.75, anchor="c")
            button.pack(side=TOP, anchor='sw')
        else:
            i.showerror("Login error", "Incorrect Creds")


lf = LoginFrame(root)
root.mainloop()
