from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox as mb
from pathlib import Path
import os
from werkzeug.security import check_password_hash, generate_password_hash
from PIL import ImageTk, Image
import logging
logging.getLogger('PIL').setLevel(logging.WARNING)

class Page:
    def __init__(self, window, db):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Records Management System')
        self.db = db
        self.login_labels = []
        self.errors = []
        
        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)
        self.login_labels.append(self.lgn_frame)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)
        self.login_labels.append(self.heading)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)
        self.login_labels.append(self.sign_in_image_label)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)
        self.login_labels.append(self.sign_in_label)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground="#FFFFFF")
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)
        self.login_labels.extend((self.username_label, self.username_entry, self.username_line, self.username_icon_label))

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.submit)
        self.login.place(x=20, y=10)
        self.login_labels.extend((self.lgn_button_label, self.login))
    
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground="#FFFFFF")
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.login_labels.extend((self.password_label, self.password_entry, self.password_icon_label, 
                                    self.show_button, self.password_line))

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')
        self.login_labels.append(self.hide_button)

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def submit(self):
        user = self.username_entry.get()
        password = self.password_entry.get()

        for error_label in self.errors:
            error_label.destroy()

        # Check for username and password
        if len(user) == 0:
            self.error("Enter username!")
            return
        if password == "":
            self.error("Enter password!")
            return
    
        # Query database for username
        rows = self.db.execute("SELECT * FROM users WHERE username = ?", user)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            self.error("Invalid username or password")
            return
        
        for label in self.login_labels:
            label.destroy()

        self.mainmenu()

    def mainmenu(self):
        # ====== Main Menu Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=1050, height=600)
        self.lgn_frame.place(x=150, y=50)
               
        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "MAIN MENU"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=350, y=20, width=300, height=30)

        # Configure the style Treeview widget
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview.Heading', background="#E8E8E8", font=('Calibri', 13,'bold'))
        s.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        s.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        
        # Tree
        self.tree = ttk.Treeview(self.lgn_frame, height=100, selectmode=BROWSE, 
                   columns=('ID', "Name", "File Type", "Timestamp"))
        X_scroller = Scrollbar(self.tree, orient=HORIZONTAL, command=self.tree.xview)
        Y_scroller = Scrollbar(self.tree, orient=VERTICAL, command=self.tree.yview)
        X_scroller.pack(side=BOTTOM, fill=X)
        Y_scroller.pack(side=RIGHT, fill=Y)
        self.tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
        self.tree.heading('ID', text='ID', anchor=CENTER, )
        self.tree.heading('Name', text='Name', anchor=CENTER)
        self.tree.heading('File Type', text='File Type', anchor=CENTER)
        self.tree.heading('Timestamp', text='Timestamp', anchor=CENTER)
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('#1', width=30, stretch=NO)
        self.tree.column('#2', width=350, stretch=NO)
        self.tree.column('#3', width=80, stretch=NO)
        self.tree.place(y=80, relwidth=0.61, relheight=0.8, relx=0.04)

        # ========================================================================
        # ============================A button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=700, y=80)
        self.login = Button(self.lgn_button_label, text='Add form', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.selectpdf)
        self.login.place(x=20, y=10)

        # ========================================================================
        # ============================A button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=700, y=160)
        self.login = Button(self.lgn_button_label, text='Add photo', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.selectphoto)
        self.login.place(x=20, y=10)

        # ========================================================================
        # ============================A button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=700, y=240)
        self.login = Button(self.lgn_button_label, text='Add pdf', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.selectpdf)
        self.login.place(x=20, y=10)

        # ========================================================================
        # ============================A button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=700, y=400)
        self.login = Button(self.lgn_button_label, text='View File', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='red', command=self.view)
        self.login.place(x=20, y=10)

        # ========================================================================
        # ============================A button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=700, y=460)
        self.login = Button(self.lgn_button_label, text='Delete File', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='red', command=self.delete)
        self.login.place(x=20, y=10)
        
        self.display_records()

    def selectpdf(self):
        """Choose pdf file"""
        filetypes = (
            ('pdf', '*.pdf'),
            ('All files', '*.*')
        )

        filenames = filedialog.askopenfilenames(
            title='Open file',
            initialdir='/',
            filetypes=filetypes
        )

        self.save(filenames, "pdf")

    def selectphoto(self):
        """Choose png file"""
        filetypes = (
            ('png', '*.png'), 
            ('All files', '*.*')
        )

        filenames = filedialog.askopenfilenames(
            title='Open file',
            initialdir='/',
            filetypes=filetypes
        )

        self.save(filenames, "png")
 
    def save(self, filenames, filetype):
        """Save file to the database"""
        for file in list(filenames):
            with open(file, "rb") as input_file:
                ablob = input_file.read()
                try:
                    self.db.execute("INSERT INTO records (name, filetype, file) VALUES(?, ?, ?)", Path(file).name, filetype, ablob)
                except:
                    mb.showerror('Error!', "Couldn't add file")

        self.display_records()

    def delete(self):
        """Delete file from database"""
        if not self.tree.selection():
            mb.showerror('Error!', 'Please select a file to delete')
            return
       
        row = self.tree.focus()
        temp = self.tree.item(row, 'values')
        id  = int(temp[0])
        try:
            self.db.execute("DELETE FROM records WHERE id = ?", id)
            mb.showinfo('File deleted', "File was successfully deleted")
            self.display_records()
        except:
            mb.showerror('Error!', "Couldn't delete file")
    
    def view(self):
        """View a file from the database"""
        if not self.tree.selection():
            mb.showerror('Error!', 'Please select a file to view')
            return
        
        row = self.tree.focus()
        temp = self.tree.item(row, 'values')
        id  = int(temp[0])
        try:
            file = self.db.execute("SELECT filetype, file FROM records WHERE id = ?", id)
            with open(f"output.{file[0]['filetype']}", "wb") as output_file:
                    output_file.write(file[0]["file"])
            os.system(f"output.{file[0]['filetype']}")
        except:
            mb.showerror('Error!', "Couldn't retrieve file")
        

    def display_records(self):
        """Display files in the database"""
        self.tree.delete(*self.tree.get_children())
        records = self.db.execute("SELECT id, name, filetype , timestamp FROM records")
        for record in reversed(records):
            record = tuple(record.values())
            self.tree.insert('', END, values=record)
        
   
    def error(self, message):
        """Handle errors"""
        self.error_label = Label(self.lgn_frame, text=message, font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='red')
        self.error_label.place(x=610, y=520)
        self.login_labels.append(self.error_label)
        self.errors.append(self.error_label)