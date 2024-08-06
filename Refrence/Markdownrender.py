import tkinter as tk
from tkinter import filedialog

# import markdown
import markdown2


def open_md_file():
    file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
    if file_path:
        with open(file_path, "r") as file:
            md_content = file.read()
            html_content = markdown2.markdown(md_content)
            display_html_content(html_content)


def display_html_content(html_content):
    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, html_content)
    text_widget.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Markdown Viewer")

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(expand=1, fill=tk.BOTH)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_md_file)

root.mainloop()
