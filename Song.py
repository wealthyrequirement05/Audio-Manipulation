import numpy as np
from scipy.io.wavfile import read
from scipy.fft import fft
from music21 import note

class Song:
    def __init__(self, filename):
        self.song_name = filename
        self.smp_rate, self.audio_data = read(self.song_name)

    def freq_to_midi(self, freq):
        return np.round(69 + 12 * np.log2(freq / 440))

    def get_notes(self):
        freq_data = fft(self.audio_data)
        freqs = np.fft.fftfreq(len(freq_data), 1 / self.smp_rate)
        notes = []
        for freq in freqs:
            if 20 <= freq <= 20000:  # Check if the frequency is within the audible range
                midi_num = self.freq_to_midi(freq)
                n = note.Note(int(midi_num))  # Here is the map step
                notes.append(n)
        return notes

    #def get_notes(self):
        #Here, I'm using a Fourier Transform that returns a complex-valued array. This could have issues for
        #the loop, so I will attempt to use a modified Fourier Transform later
        #freq_data = fft(self.audio_data)
        #notes = []

        #freqs = np.fft.fftfreq(len(freq_data), 1 / self.smp_rate)


        #for freq in freqs:
        #    midi_num = self.freq_to_midi(freq)
        #    n = note.Note(int(midi_num))  # Here is the map step
        #notes.append(n)
        #return notes
        #for freq in freq_data: #Since I'm using a complex-valued array, I tried below to use the absolute value
        #for freq in np.abs(freq_data):

        #    midi_num = self.freq_to_midi(freq)
        #    n = note.Note(midi_num)  # Here is the map step
        #    notes.append(n)
        #return notes



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








