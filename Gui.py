import tkinter as tk
from tkinter import *
from CompressandDecompress import compress,decompress


# --------------------------


def compress_f(input, output):
    compress(input, output)


def decompress_f(input, output):
    decompress(input, output)


window = tk.Tk()

# Title
window.title("Compress and Decompress")
# Window Size
window.geometry("500x300")


# -------------------COMPRESS-----------------------------------------
# Initializes the compressed input and output fields
i_entry = tk.Entry(window)
o_entry = tk.Entry(window)

# Initializes the compressed input and output labels
i_label = tk.Label(window,text="Compress File: Existing File")
o_label = tk.Label(window,text="New Compressed File")

# Initializes the compressed button whiles passing the compress function through the button
compress_btn = tk.Button(window, text="Compress", command=lambda: compress_f(i_entry.get(),o_entry.get()))


# Add the fields ,labels and button to the window
i_label.grid(row=0, column=0)
i_entry.grid(row=0, column= 1)
o_label.grid(row=1, column=0)
o_entry.grid(row=1, column= 1)
compress_btn.grid(row=2 ,column=1)


# -------------------DECOMPRESS-----------------------------------------
# Initializes the compressed input and output fields
di_entry = tk.Entry(window)
do_entry = tk.Entry(window)

# Initializes the compressed input and output labels
di_label = tk.Label(window,text="Decompress File: Existing File")
do_label = tk.Label(window,text="New Decompressed File")

# Initializes the decompressed button whiles passing the compress function through the button
decompress_btn = tk.Button(window,text="Decompress", command=lambda: decompress_f(di_entry.get(), do_entry.get()))

# Add the fields ,labels and button to the window
di_label.grid(row=5, column=0)
di_entry.grid(row=5, column= 1)
do_label.grid(row=6, column=0)
do_entry.grid(row=6, column= 1)
decompress_btn.grid(row=7 ,column=1)




window.mainloop()

