import wave
import numpy as np
from scipy.io.wavfile import read
from scipy.fft import fft
from music21 import converter, instrument, note, chord

# Step 1: Load the .wav file

class Song:
    def __init__(self, filename):
        self.song_name = filename
        wav_file = wave.open(filename, 'r')
        smp_rate, amp_data = read(self.song_name)
        audio_data = np.array(data)
    def get_notes(self, audio_data):
        freq_data = fft(audio_data)
        notes = []
        for freq in freq_data:
            n = note.Note(freq) #Here is the map step
            notes.append(n)
        return notes


    #Below is a possible text display, but I think this should go into another class
    #def print_song(self):
        #notes = get_notes(self, audio_data)
        #The appropriate Tkinter method should display the sheet music here
        #returns sheet music object and also returns text to to display in a user interface

        # for element in notes_to_parse:
        #    if isinstance(element, note.Note):
        #        notes.append(str(element.pitch))
        #    elif isinstance(element, chord.Chord):
        #        notes.append('.'.join(str(n) for n in element.normalOrder))

        # Saving sheet music
        # midi_stream = stream.Stream(notes)
        # midi_stream.write('midi', fp='your_output_file.mid')

    #def modify_notes(input_from_UI):
        #The way this should work is that when the user clicks a button after the sheet music is change, the
        #modified sheet music should be read by this method and the notes of the song should change.
