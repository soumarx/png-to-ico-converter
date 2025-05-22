def convert_png_to_ico(png_file_path, output_directory):
    from PIL import Image
    import os

    # Load the PNG image
    with Image.open(png_file_path) as img:
        # Define the output ICO file path
        base_name = os.path.splitext(os.path.basename(png_file_path))[0]
        ico_file_path = os.path.join(output_directory, f"{base_name}.ico")
        
        # Convert and save the image as ICO
        img.save(ico_file_path, format='ICO')

def select_png_files():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilenames

    # Hide the root window
    Tk().withdraw()
    # Open file dialog to select multiple PNG files
    file_paths = askopenfilenames(title="Select PNG files", filetypes=[("PNG files", "*.png")])
    return file_paths

def select_output_directory():
    from tkinter import Tk
    from tkinter.filedialog import askdirectory

    # Hide the root window
    Tk().withdraw()
    # Open directory dialog to select output directory
    output_directory = askdirectory(title="Select Output Directory")
    return output_directory