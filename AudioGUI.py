import tkinter as tk
from tkinter import filedialog
import Song
from PIL import ImageTk, Image
import music21
from music21 import converter, instrument, note, chord, stream

def convert_audio_to_sheet_music(filename):
    # Here is the audio to sheet music method for the user interface
    # This code returns a stream.Stream object
    s1 = Song(filename)
    song_notes = s1.get_notes()
    midi_stream = stream.Stream(song_notes)
    return midi_stream

def display_sheet_music(filename):
    # Convert the audio file to sheet music
    midi_stream = convert_audio_to_sheet_music(filename)

    # Save the sheet music as a MusicXML file
    xml_filename = 'sheet_music.xml'
    midi_stream.write('musicxml', fp=xml_filename)

    # Convert the MusicXML file to an image
    # This requires external software, such as MuseScore
    # Placeholder for your MusicXML to image conversion code
    img_filename = 'sheet_music.png'

    # Display the image in the tkinter window
    global img  # Make img a global variable
    img = ImageTk.PhotoImage(Image.open(img_filename))
    panel = tk.Label(window, image=img)
    panel.image = img  # Keep a reference to the image
    panel.pack(side="bottom", fill="both", expand="yes")

def browse_files():
    filename = filedialog.askopenfilename()
    display_sheet_music(filename)

window = tk.Tk()

button = tk.Button(window, text="Browse files", command=browse_files)
button.pack()

window.mainloop()
