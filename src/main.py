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
            log_callback(f"Convertido: {png_file} -> {ico_file_path}\n")
        except UnidentifiedImageError:
            log_callback(f"Arquivo inválido (não é PNG ou está corrompido): {png_file}\n")
        except Exception as e:
            log_callback(f"Erro ao converter {png_file}: {e}\n")

def show_log_window():
    log_win = Toplevel()
    log_win.title("Log de Conversão")
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

    png_files = filedialog.askopenfilenames(title="Selecione arquivos PNG", filetypes=[("PNG files", "*.png")])
    if not png_files:
        messagebox.showinfo("Info", "Nenhum arquivo PNG selecionado.")
        return

    output_directory = filedialog.askdirectory(title="Selecione a pasta de destino")
    if not output_directory:
        messagebox.showinfo("Info", "Nenhuma pasta de destino selecionada.")
        return

    log_win = show_log_window()
    def log_callback(msg):
        log_win.insert(END, msg)
        log_win.see(END)
        log_win.update_idletasks()

    def run_conversion():
        convert_png_to_ico(png_files, output_directory, log_callback)
        log_callback("\nConversão finalizada!\n")
        messagebox.showinfo("Sucesso", "Conversão concluída!")

    threading.Thread(target=run_conversion, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    main()