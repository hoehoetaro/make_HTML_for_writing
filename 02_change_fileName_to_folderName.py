import os
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image

# Change the working directory to the script directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Get the folder name where the script is located
script_folder_name = os.path.basename(os.getcwd())
new_filename = script_folder_name + "_thumbnail.png"

def drop(event):
    filepath = event.data
    #エラーになる文字を取り除く
    filepath = filepath.strip('{}')
    
    print("ファイルがドロップされました: ", filepath)
    
    # Open the image file
    img = Image.open(filepath)

    # Generate the new file path
    dirname = os.path.dirname(filepath)
    new_filepath = os.path.join(dirname, new_filename)

    # Save the image as PNG
    img.save(new_filepath, "PNG")
    print("画像を保存しました: ", new_filepath)

    # Remove the original file
    os.remove(filepath)
    print("元のファイルを削除しました: ", filepath)

root = TkinterDnD.Tk()
root.title("ドラッグアンドドロップデモ")

new_file_label = tk.Label(root, text="新しいファイル名: " + new_filename, width=100)
new_file_label.pack()

drop_label = tk.Label(root, text="ここに画像ファイルをドロップしてください", width=50, height=10)
drop_label.pack()
drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind('<<Drop>>', drop)

root.mainloop()
