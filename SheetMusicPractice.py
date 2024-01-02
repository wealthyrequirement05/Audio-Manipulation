from music21 import note, stream
from music21 import environment
us = environment.UserSettings()
us['lilypondPath'] = r'C:\Users...\lilypond.exe' #Be sure to insert the actual path 

s = stream.Stream()  #Using a stream

n = note.Note('C5',quarterLength = 0.5)
s.append(n)
n = note.Note('A4',quarterLength = 0.5)
s.append(n)
n = note.Note('C5',quarterLength = 0.5)
s.append(n)
n = note.Note('A4',quarterLength = 0.5)
s.append(n)
n = note.Note('C5',quarterLength = 0.5)
s.append(n)
n = note.Note('A4',quarterLength = 0.5)
s.append(n)
n = note.Note('C5',quarterLength = 0.5)
s.append(n)
n = note.Note('A4',quarterLength = 0.5)
s.append(n)
c = note.Note('E4',quarterLength = 8)
s.insert(0, c)
out1 = s.makeVoices()
out2 = out1.makeNotation()
out2.show('practice_sheet_music.pdf')
