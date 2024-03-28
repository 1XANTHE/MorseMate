import tkinter as tk
from tkinter import messagebox


morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', ' ': '/'
}


reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += ' '
    return morse_code.strip()

def morse_to_text(morse_code):
    words = morse_code.split('/')
    text = ''
    for word in words:
        chars = word.strip().split(' ')
        for char in chars:
            if char in reverse_morse_code_dict:
                text += reverse_morse_code_dict[char]
            else:
                text += ' '
        text += ' '
    return text.strip()

def convert_text_to_morse():
    text_input = text_entry.get()
    morse_output = text_to_morse(text_input)
    output_label.config(text="Morse code: " + morse_output)

def convert_morse_to_text():
    morse_input = morse_entry.get()
    text_output = morse_to_text(morse_input)
    output_label.config(text="Text: " + text_output)

def clear_input():
    text_entry.delete(0, tk.END)
    morse_entry.delete(0, tk.END)
    output_label.config(text="")

def show_about():
    messagebox.showinfo("About", "MorseMate\nA simple tool to convert text to Morse code and vice versa.")


root = tk.Tk()
root.title("MorseMate")
root.geometry("500x300")


bg_color = "#2C3E50"  
fg_color = "#ECF0F1" 
button_bg_color = "#07143F"  
heading_bg_color = "#2A60FF"  


heading_font = ("Cormorant Unicase", 20)
label_font = ("Cormorant Unicase ", 12)
entry_font = ("Cormorant Unicase", 12)
button_font = ("Segoe UI", 12, "bold")


heading_label = tk.Label(root, text="MorseMate", font=heading_font, bg=heading_bg_color, fg=fg_color, padx=20, pady=10)
heading_label.pack(fill="x")

main_frame = tk.Frame(root, bg=bg_color)
main_frame.pack(padx=20, pady=(0, 20))


text_to_morse_frame = tk.LabelFrame(main_frame, text="Text to Morse", bg=bg_color, fg=fg_color, font=label_font)
text_to_morse_frame.grid(row=0, column=0, padx=10, pady=10)

tk.Label(text_to_morse_frame, text="Enter Text:", bg=bg_color, fg=fg_color, font=label_font).grid(row=0, column=0, padx=5, pady=5)
text_entry = tk.Entry(text_to_morse_frame, width=30, font=entry_font)
text_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Button(text_to_morse_frame, text="Convert", command=convert_text_to_morse, bg=button_bg_color, fg=fg_color, font=button_font).grid(row=1, column=0, columnspan=2, pady=5, padx=5, sticky="we")


morse_to_text_frame = tk.LabelFrame(main_frame, text="Morse to Text", bg=bg_color, fg=fg_color, font=label_font)
morse_to_text_frame.grid(row=0, column=1, padx=10, pady=10)

tk.Label(morse_to_text_frame, text="Enter Morse code:", bg=bg_color, fg=fg_color, font=label_font).grid(row=0, column=0, padx=5, pady=5)
morse_entry = tk.Entry(morse_to_text_frame, width=30, font=entry_font)
morse_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Button(morse_to_text_frame, text="Convert", command=convert_morse_to_text, bg=button_bg_color, fg=fg_color, font=button_font).grid(row=1, column=0, columnspan=2, pady=5, padx=5, sticky="we")


output_label = tk.Label(main_frame, text="", wraplength=400, bg=bg_color, fg=fg_color, font=label_font)
output_label.grid(row=1, column=0, columnspan=2, pady=10)


clear_button = tk.Button(main_frame, text="Clear", command=clear_input, bg=button_bg_color, fg=fg_color, font=button_font)
clear_button.grid(row=2, column=0, columnspan=2, pady=5, padx=5, sticky="we")


menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.mainloop()
