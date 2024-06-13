import tkinter as tk
from tkinter import messagebox
import json
import os

# Define the path for the JSON file
data_file = 'library_data.json'

# Function to load the data from JSON file
def load_data():
    if not os.path.exists(data_file):
        with open(data_file, 'w') as file:
            json.dump([], file)
    with open(data_file, 'r') as file:
        return json.load(file)

# Function to save the data to JSON file
def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

# Load initial data
library_data = load_data()

# Function to add a book
def add_book():
    def save_book():
        title = title_entry.get()
        author = author_entry.get()
        if title and author:
            library_data.append({'title': title, 'author': author, 'status': 'available'})
            save_data(library_data)
            messagebox.showinfo('Success', 'Book added successfully!')
            add_book_window.destroy()
        else:
            messagebox.showerror('Error', 'Please provide both title and author.')
    
    add_book_window = tk.Toplevel(root)
    add_book_window.title("Add Book")
    
    tk.Label(add_book_window, text="Title:").pack(pady=5)
    title_entry = tk.Entry(add_book_window)
    title_entry.pack(pady=5)
    
    tk.Label(add_book_window, text="Author:").pack(pady=5)
    author_entry = tk.Entry(add_book_window)
    author_entry.pack(pady=5)
    
    tk.Button(add_book_window, text="Add Book", command=save_book).pack(pady=20)

# Function to borrow a book
def borrow_book():
    def borrow():
        title = title_entry.get()
        for book in library_data:
            if book['title'].lower() == title.lower():
                if book['status'] == 'available':
                    book['status'] = 'borrowed'
                    save_data(library_data)
                    messagebox.showinfo('Success', 'You have borrowed the book!')
                    borrow_book_window.destroy()
                    return
                else:
                    messagebox.showerror('Error', 'Book is already borrowed.')
                    return
        messagebox.showerror('Error', 'Book not found.')
    
    borrow_book_window = tk.Toplevel(root)
    borrow_book_window.title("Borrow Book")
    
    tk.Label(borrow_book_window, text="Title:").pack(pady=5)
    title_entry = tk.Entry(borrow_book_window)
    title_entry.pack(pady=5)
    
    tk.Button(borrow_book_window, text="Borrow Book", command=borrow).pack(pady=20)

# Function to return a book
def return_book():
    def return_bk():
        title = title_entry.get()
        for book in library_data:
            if book['title'].lower() == title.lower():
                if book['status'] == 'borrowed':
                    book['status'] = 'available'
                    save_data(library_data)
                    messagebox.showinfo('Success', 'You have returned the book!')
                    return_book_window.destroy()
                    return
                else:
                    messagebox.showerror('Error', 'This book was not borrowed.')
                    return
        messagebox.showerror('Error', 'Book not found.')
    
    return_book_window = tk.Toplevel(root)
    return_book_window.title("Return Book")
    
    tk.Label(return_book_window, text="Title:").pack(pady=5)
    title_entry = tk.Entry(return_book_window)
    title_entry.pack(pady=5)
    
    tk.Button(return_book_window, text="Return Book", command=return_bk).pack(pady=20)

# Function to show books
def show_books():
    show_books_window = tk.Toplevel(root)
    show_books_window.title("Library Books")
    
    books_text = tk.Text(show_books_window, wrap='word')
    books_text.pack(pady=20, padx=20)
    
    if not library_data:
        books_text.insert(tk.END, "No books in the library.")
    else:
        for book in library_data:
            books_text.insert(tk.END, f"Title: {book['title']}\nAuthor: {book['author']}\nStatus: {book['status']}\n\n")

# Main window
root = tk.Tk()
root.title("Library App")

tk.Button(root, text="Add Book", command=add_book).pack(pady=10)
tk.Button(root, text="Borrow Book", command=borrow_book).pack(pady=10)
tk.Button(root, text="Return Book", command=return_book).pack(pady=10)
tk.Button(root, text="Show Books", command=show_books).pack(pady=10)

root.mainloop()
