import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import yt_dlp
import os


# FUNCTIONS
def download_video(url, format_choice, output_dir):
    try:
        options = {}
        if format_choice == 'MP4 (1080p)':
            options = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
                'outtmpl': f'{output_dir}/%(title)s.%(ext)s'
            }
        elif format_choice == 'MP3 (High Quality)':
            options = {
                'format': 'bestaudio/best',
                'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }]
            }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download complete!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_dir.set(folder)

def start_download():
    url = url_entry.get()
    format_choice = format_var.get()
    output_directory = output_dir.get()

# error handling for no link or dir
    if not url or not format_choice or not output_directory:
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return
    download_video(url, format_choice, output_directory)

# MAIN WINDOW
root = tk.Tk()
root.title("Video Converter")
root.geometry("700x400")
root.configure(bg='#1c1c1c')
root.resizable(False, False)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10, background='#444444', foreground='white')
style.configure("TLabel", background='#1c1c1c', foreground='white', font=("Helvetica", 12))
style.configure("TCombobox", font=("Helvetica", 12), padding=10)
style.map("TButton", background=[('active', '#ff9b00')], foreground=[('active', 'black')])

# TITLE AND HEADER
header_label = ttk.Label(root, text="Video Converter", font=("Helvetica", 18, "bold"))
header_label.grid(row=0, column=0, columnspan=3, pady=(20, 10), padx=20, sticky="n")


# URL INPUT
url_label = ttk.Label(root, text="Video URL:")
url_label.grid(row=1, column=0, pady=10, padx=20, sticky="w")
url_entry = ttk.Entry(root, width=50, font=("Helvetica", 12))
url_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew", columnspan=2)


# FORMAT SELECTION
format_label = ttk.Label(root, text="Select Format:")
format_label.grid(row=2, column=0, pady=10, padx=20, sticky="w")
format_var = tk.StringVar(value="MP4 (1080p)")
formats = ["MP4 (1080p)", "MP3 (High Quality)"]
format_dropdown = ttk.Combobox(root, textvariable=format_var, values=formats, state="readonly", font=("Helvetica", 12))
format_dropdown.grid(row=2, column=1, pady=10, padx=10, sticky="ew")


# OUTPUT DIRECTORY SELECTION
output_dir_label = ttk.Label(root, text="Output Directory:")
output_dir_label.grid(row=3, column=0, pady=10, padx=20, sticky="w")
output_dir = tk.StringVar()
output_dir_display = ttk.Label(root, textvariable=output_dir, font=("Helvetica", 12), relief="sunken")
output_dir_display.grid(row=3, column=1, pady=10, padx=10, sticky="ew")
output_button = ttk.Button(root, text="Browse", command=browse_folder)
output_button.grid(row=3, column=2, pady=10, padx=10, sticky="ew")

# CREDITS
nyu_label = ttk.Label(root,text="by Nyu", foreground='orange')
nyu_label.grid(row = 5, column=5, pady=3, padx=3, sticky="w")
nyu_label = tk.StringVar()

# DOWNLOAD BUTTON
download_button = ttk.Button(root, text="Download", command=start_download)
download_button.grid(row=4, column=1, pady=30, padx=10, sticky="ew")

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(4, weight=1)


# START
root.mainloop()
