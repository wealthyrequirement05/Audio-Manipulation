import tkinter as tk
from tkinter import filedialog
import Song
from PIL import ImageTk, Image
import music21
from music21 import converter, instrument, note, chord, stream

def convert_audio_to_sheet_music(filename):
    s1 = Song(filename)
    song_notes = s1.get_notes()
    print(song_notes)  # Add this line
    midi_stream = stream.Stream(song_notes)
    return midi_stream

def display_sheet_music(filename):
    midi_stream = convert_audio_to_sheet_music(filename)
    xml_filename = 'sheet_music.xml'
    midi_stream.write('musicxml', fp=xml_filename)
    img_filename = 'sheet_music.png'
    global img
    img = ImageTk.PhotoImage(Image.open(img_filename))
    panel.config(image=img)
    panel.image = img
    filepath_text.delete(1.0, tk.END)
    filepath_text.insert(tk.END, filename)

def browse_files():
    filename = filedialog.askopenfilename()
    display_sheet_music(filename)

def exit_program():
    window.destroy()

window = tk.Tk()

filepath_text = tk.Text(window, height=1, width=40)
filepath_text.pack()

browse_button = tk.Button(window, text="Upload File", command=browse_files)
browse_button.pack()

panel = tk.Label(window)
panel.pack(side="bottom", fill="both", expand="yes")

exit_button = tk.Button(window, text="Exit", command=exit_program)
exit_button.pack()

window.mainloop()
