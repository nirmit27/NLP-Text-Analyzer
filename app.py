""" Root of the application """

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from mydb2 import DB as myDb
from myapi import MyAPI as myApi


class NLPApp:

    def __init__(self):

        # Initializing the Widgets in __init__ ...
        self.int_result = None
        self.int_input = None
        self.ner_result = None
        self.ner_input = None
        self.sentiment_result = None
        self.sentiment_input = None
        self.name_input = None
        self.pwd_input = None
        self.email_input = None

        # Instantiating the necessary classes ...
        self.apio = myApi()
        self.root = tk.Tk()
        self.root.title('NLP App')
        self.root.geometry('350x550')
        self.root.configure(bg='white')
        self.root.iconbitmap('resources/favicon.ico')

        # Login page loads on startup ...
        self.login_gui()

        # Calling the event loop of Tk ...
        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='white', fg='blue')
        heading.pack(pady=(30, 20))
        heading.configure(font=('Lucida Sans', 24, 'bold'))

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(50, 10))
        label1.configure(bg='white', font=('Arial', 9))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10), ipady=3)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))
        label2.configure(bg='white', font=('Arial', 9))

        self.pwd_input = Entry(self.root, width=30, show='*')
        self.pwd_input.pack(pady=(5, 10), ipady=3)

        login_btn = Button(self.root, text='Log In', width=15,
                           height=2, command=self.login)
        login_btn.pack(pady=(20, 10))
        login_btn.configure(bg='blue', fg='white', font=('Arial', 10, 'bold'))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(70, 10))
        label3.configure(bg='white', font=('Arial', 9))

        redirect_btn = Button(self.root, text='Register Now',
                              width=15, height=1, command=self.register_gui)
        redirect_btn.pack(pady=(0, 10))
        redirect_btn.configure(bg='green', fg='white',
                               font=('Arial', 9, 'bold'))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='white', fg='blue')
        heading.pack(pady=(30, 20))
        heading.configure(font=('Lucida Sans', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))
        label0.configure(bg='white', font=('Arial', 9))

        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(5, 10), ipady=3)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))
        label1.configure(bg='white', font=('Arial', 9))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10), ipady=3)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))
        label2.configure(bg='white', font=('Arial', 9))

        self.pwd_input = Entry(self.root, width=30, show='*')
        self.pwd_input.pack(pady=(5, 10), ipady=3)

        register_btn = Button(self.root, text='Register',
                              width=15, height=2, command=self.registration)
        register_btn.pack(pady=(20, 10))
        register_btn.configure(bg='blue', fg='white',
                               font=('Arial', 10, 'bold'))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(30, 10))
        label3.configure(bg='white', font=('Arial', 9))

        login_btn = Button(self.root, text='Log In',
                           width=15, height=1, command=self.login_gui)
        login_btn.pack(pady=(0, 10))
        login_btn.configure(bg='green', fg='white',
                            font=('Arial', 9, 'bold'))

    # Logic for L O G G I N G  I N ...

    def login(self):
        email = ''
        pwd = ''
        if self.email_input != None and self.pwd_input != None:
            email = self.email_input.get()
            pwd = self.pwd_input.get()

        logged = myDb()
        response = logged.search_creds(email=email, pwd=pwd)
        if response:
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect email or password.')

    # Logic for R E G I S T R A T I O N ...

    def registration(self):
        name, email, pwd = '', '', ''
        if self.email_input != None and self.pwd_input != None and self.name_input != None:
            name = self.name_input.get()
            email = self.email_input.get()
            pwd = self.pwd_input.get()

        register = myDb()
        response = register.add_creds(name=name, email=email, pwd=pwd)
        if response[0] == 0:
            match response[1]:
                case True:
                    messagebox.showerror('Error', 'Email already exists.')
                case False:
                    messagebox.showerror('Error', 'Password already in use.')
        else:
            messagebox.showinfo('Success', 'Registration successful!')
            self.home_gui()

    def home_gui(self):
        self.clear()

        btn_bg_col = '#4681f4'

        heading = Label(self.root, text='NLP App', bg='white', fg='blue')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Lucida Sans', 24, 'bold'))

        label0 = Label(self.root, text='Choose an analysis option.')
        label0.pack(pady=(10, 10))
        label0.configure(bg='white', font=('Arial', 10))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=25,
                               height=2, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(20, 10))
        sentiment_btn.configure(bg=btn_bg_col, fg='white',
                                font=('Arial', 10, 'bold'))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=25,
                         height=2, command=self.ner_gui)
        ner_btn.pack(pady=(20, 10))
        ner_btn.configure(bg=btn_bg_col, fg='white',
                          font=('Arial', 10, 'bold'))

        intent_btn = Button(self.root, text='Intent Classification', width=25,
                            height=2, command=self.intent_gui)
        intent_btn.pack(pady=(20, 10))
        intent_btn.configure(bg=btn_bg_col, fg='white',
                             font=('Arial', 10, 'bold'))

        logout_btn = Button(self.root, text='Logout',
                            width=15, command=self.login_gui)
        logout_btn.pack(pady=(104, 10))
        logout_btn.configure(bg='red', fg='white', font=('Arial', 9, 'bold'))

    # A N A L Y S I S  O P T I O N S ...

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='white', fg='blue')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Lucida Sans', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis',
                         bg='white', fg='black')
        heading2.pack(pady=(0, 30))
        heading2.configure(font=('Lucida Sans', 16, 'bold'))

        label1 = Label(self.root, text='Enter the text for analysis.')
        label1.pack(pady=(10, 10), padx=(0, 130))
        label1.configure(bg='white', font=('Arial', 10))

        self.sentiment_input = Text(
            self.root, height=5, width=40, highlightthickness=1, wrap='word')
        self.sentiment_input.pack(pady=(0, 15), expand=False)
        self.sentiment_input.configure(font=('Arial', 10))

        sentiment_btn = Button(
            self.root, text='Analyze Sentiment', width=30, command=self.senti_analysis)
        sentiment_btn.pack(pady=(10, 0))
        sentiment_btn.configure(bg='blue', fg='white',
                                font=('Arial', 9, 'bold'))

        self.sentiment_result = Label(
            self.root, text='', fg='blue', bg='white')
        self.sentiment_result.pack(pady=(35, 18))
        self.sentiment_result.configure(
            font=('Arial', 11, 'bold'), height=4, justify='left', anchor='w')

        back_btn = Button(self.root, text='Go Back',
                          width=15, command=self.home_gui)
        back_btn.pack(pady=(0, 10))
        back_btn.configure(bg='lightblue', fg='black',
                           font=('Arial', 9, 'bold'))

    def senti_analysis(self):
        if self.sentiment_result != None and self.sentiment_input != None:
            self.sentiment_result['text'] = ''

            text = self.sentiment_input.get('1.0', tk.END)
            req = self.apio.sentiment(text=text)

            res = ''
            for i in req['sentiment']:
                if i == 'negative':
                    res += i.title() + '  :\t' + \
                        f"{round(req['sentiment'][i]*100,2)} %\n"
                else:
                    res += i.title() + '\t  :\t' + \
                        f"{round(req['sentiment'][i]*100,2)} %\n"

            self.sentiment_result['text'] = res

    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='white', fg='blue')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Lucida Sans', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recognition',
                         bg='white', fg='black')
        heading2.pack(pady=(0, 20))
        heading2.configure(font=('Lucida Sans', 14, 'bold'))

        label1 = Label(self.root, text='Enter the text for analysis.')
        label1.pack(pady=(10, 10), padx=(0, 130))
        label1.configure(bg='white', font=('Arial', 10))

        self.ner_input = Text(
            self.root, height=5, width=40, highlightthickness=1, wrap='word')
        self.ner_input.pack(pady=(0, 15), expand=False)
        self.ner_input.configure(font=('Arial', 10))

        ner_btn = Button(
            self.root, text='Recognize Entities', width=30, command=self.ner)
        ner_btn.pack(pady=(10, 0))
        ner_btn.configure(bg='blue', fg='white',
                          font=('Arial', 9, 'bold'))

        self.ner_result = Text(self.root, height=6,
                               width=35, highlightthickness=2, wrap='word')
        self.ner_result.pack(pady=(20, 24))
        self.ner_result.configure(font=('Arial', 9, 'bold'))

        back_btn = Button(self.root, text='Go Back',
                          width=15, command=self.home_gui)
        back_btn.pack(pady=(0, 10))
        back_btn.configure(bg='lightblue', fg='black',
                           font=('Arial', 9, 'bold'))

    def ner(self):
        if self.ner_result != None and self.ner_input != None:
            self.ner_result.delete('1.0', tk.END)

            text = self.ner_input.get('1.0', tk.END)
            req = self.apio.ner(text=text)

            res = ''
            for i in req['entities']:
                res += f"{i['name']} is a {i['category']}.\n"

            self.ner_result.insert("1.0", res)

    def intent_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='white', fg='blue')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Lucida Sans', 24, 'bold'))

        heading2 = Label(self.root, text='Intent Classification',
                         bg='white', fg='black')
        heading2.pack(pady=(0, 30))
        heading2.configure(font=('Lucida Sans', 16, 'bold'))

        label1 = Label(self.root, text='Enter the text for analysis.')
        label1.pack(pady=(10, 10), padx=(0, 130))
        label1.configure(bg='white', font=('Arial', 10))

        self.int_input = Text(
            self.root, height=5, width=40, highlightthickness=1, wrap='word')
        self.int_input.pack(pady=(0, 15), expand=False)
        self.int_input.configure(font=('Arial', 10))

        int_btn = Button(
            self.root, text='Classify Intent', width=30, command=self.intent)
        int_btn.pack(pady=(10, 0))
        int_btn.configure(bg='blue', fg='white',
                          font=('Arial', 9, 'bold'))

        self.int_result = Label(
            self.root, text='', fg='blue', bg='white')
        self.int_result.pack(pady=(20, 33))
        self.int_result.configure(
            font=('Arial', 11, 'bold'), height=4, justify='left', anchor='w')

        back_btn = Button(self.root, text='Go Back',
                          width=15, command=self.home_gui)
        back_btn.pack(pady=(0, 10))
        back_btn.configure(bg='lightblue', fg='black',
                           font=('Arial', 9, 'bold'))

    def intent(self):
        if self.int_result != None and self.int_input != None:
            self.int_result['text'] = ''

            text = self.int_input.get('1.0', tk.END)
            req = self.apio.intentc(text=text).json()["intent"]

            res = ''
            for i, j in req.items():
                if i in ['query', 'spam']:
                    res += i.title() + '\t    :\t' + f'{round(j*100,2)}%\n'
                elif i == 'marketing':
                    res += i.title() + '   :\t' + f'{round(j*100,2)}%\n'
                else:
                    res += i.title() + '   :\t' + f'{round(j*100,2)}%\n'

            self.int_result['text'] = res

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

# ----------------------------------------------- D R I V E R ----------------------------------------------- #


if __name__ == "__main__":

    # Creating the instance of the GUI class ...
    nlp = NLPApp()

# ----------------------------------------------------------------------------------------------------------- #
