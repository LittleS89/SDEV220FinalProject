# Stacey Little
# SDEV220-50P
# Final Project: Grocery Store Search Tool
# This program uses Tkinter GUI to provide a search tool to find products
# based on user input searches. (ex: 'bread', 'Hersheys', 'Milk', etc)

import csv
import tkinter as tk
from tkinter import *

# main function to search the data sheet for user input
def main():
    # take the user entry from window box and use that for product search
    user_input = prod.get()
    # using upper helps find word matches regardless of case user enters
    global prod_search
    prod_search = user_input.upper()
    
    # uses user input to display the product being searched
    print(f"\nYou entered {prod_search}:\n")

    global header, search_results1, search_results2
    search_results1 = []
    search_results2 = []

    with open("LittleStaceyFinalProjectdata.csv", 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if prod_search in row[0].upper():
                search_results1.append(row)
            elif prod_search in row[4].upper():
                search_results2.append(row)

    print("{: <30} {: <15} {: <15} {: <15} {: <15}".format(*header))
    for result in search_results1 + search_results2:
        print("{: <30} {: <15} {: <15} {: <15} {: <15}".format(*result))
        print('------------------------------------------------------------------------')

# window created for second window
class Window(tk.Toplevel):
    def search_results(self):
        Label(self, text=f"Results for '{prod_search}':", font="Arial 14 bold").grid(row=3, column=0, columnspan=4, pady=5)
        Label(self, text="{: <30} {: <15} {: <15} {: <15} {: <15}".format(*header),
              justify="left").grid(row=4, column=0, columnspan=4)

        row_index = 5
        # tests if 'search1' was created in main() function and displays the output
        for result in search_results1:
            Label(self, text="{: <30} {: <15} {: <15} {: <15} {: <15}".format(*result),
                  justify="left").grid(row=row_index, column=0, columnspan=4)
            row_index += 1

        # if 'search1' was not created in main(), this means 'search2' was created instead
        for result in search_results2:
            Label(self, text="{: <30} {: <15} {: <15} {: <15} {: <15}".format(*result),
                  justify="left").grid(row=row_index, column=0, columnspan=4)
            row_index += 1

    # format window
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(background="pink")
        self.geometry('600x500')
        # adds window title
        self.title('Product Input')

        # related image inserted per project requirements
        global image2
        image2 = tk.PhotoImage(file="groceries2.gif")
        tk.Label(self, image=image2).grid()
        # brief instruction provided to user
        Label(self, text="Enter a search term below:", font="Times 12 bold").grid(row=1, column=0, columnspan=3, pady=10)
        # user input area created with label to the side for user direction
        global prod
        prod = Entry(self, width=30)
        prod.grid(row=4, column=0, columnspan=2, pady=10)

        Button(self, text="Search", command=lambda: [main(), self.search_results()]).grid(row=1, column=1, pady=10)
        Button(self, text="Restart", command=self.destroy).grid(row=1, column=3, pady=10)


# window created for the main (opening) window
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # format window to look nicer and fit image
        self.configure(background="pink")
        self.geometry('500x300')
        self.title('Grocery Product Search Tool')

        # related image inserted per project requirements
        global image
        image = tk.PhotoImage(file="groceries1.gif")
        tk.Label(self, image=image).pack()

        # give window a title and some basic text to welcome the user and provide instruction
        Label(self, text="Welcome to the Grocery Search Tool!", font="Times 16 bold").pack(pady=10)
        Label(self, text="Click 'Open Search Input' to start.", font="Arial 12").pack(pady=5)
        # buttons to open the product search tool and to close the program
        Button(self, text='Open Search Input', command=self.open_window).pack(pady=10)
        Button(self, text="Close", command=self.destroy).pack(pady=5)

    # function to open the search window. This function is being called on the 'Open Search Input' button above
    def open_window(self):
        try:
            window = Window(self)
            window.grab_set()
        except Exception as e:
            print(f"An error occurred: {e}")

# run the program
if __name__ == "__main__":
    app = App()
    app.mainloop()
