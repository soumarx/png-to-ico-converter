import os
import threading
from tkinter import Tk, filedialog, messagebox, Toplevel, Text, Scrollbar, END, RIGHT, Y, LEFT, BOTH
from PIL import Image, UnidentifiedImageError

def convert_png_to_ico(png_files, output_directory, log_callback):
    for png_file in png_files:
        try:
            img = Image.open(png_file)
            ico_file_name = os.path.splitext(os.path.basename(png_file))[0] + '.ico'
            ico_file_path = os.path.join(output_directory, ico_file_name)
            img.save(ico_file_path, format='ICO')
            log_callback(f"Converted: {png_file} -> {ico_file_path}\n")
        except UnidentifiedImageError:
            log_callback(f"Invalid file (not a PNG or is corrupted): {png_file}\n")
        except Exception as e:
            log_callback(f"Error converting {png_file}: {e}\n")

def show_log_window():
    log_win = Toplevel()
    log_win.title("Conversion Log")
    log_win.geometry("700x400")
    text_area = Text(log_win, wrap='word')
    scrollbar = Scrollbar(log_win, command=text_area.yview)
    text_area.configure(yscrollcommand=scrollbar.set)
    text_area.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    return text_area

def main():
    root = Tk()
    root.withdraw()

    png_files = filedialog.askopenfilenames(title="Select PNG files", filetypes=[("PNG files", "*.png")])
    if not png_files:
        messagebox.showinfo("Info", "No PNG files selected.")
        return

    output_directory = filedialog.askdirectory(title="Select output folder")
    if not output_directory:
        messagebox.showinfo("Info", "No output folder selected.")
        return

    log_win = show_log_window()
    def log_callback(msg):
        log_win.insert(END, msg)
        log_win.see(END)
        log_win.update_idletasks()

    def run_conversion():
        convert_png_to_ico(png_files, output_directory, log_callback)
        log_callback("\nConversion finished!\n")
        messagebox.showinfo("Success", "Conversion completed!")

    threading.Thread(target=run_conversion, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    main()