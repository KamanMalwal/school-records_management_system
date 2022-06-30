from cs50 import SQL
from tkinter import *
import page

        
def main():
    
    # Initialize database
    db = SQL("sqlite:///records.db")
    
    window = Tk()
    page.Page(window, db)
    window.mainloop()


if __name__ == '__main__':
    main()