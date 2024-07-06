#using libraries sounddevice, scipy , wavio
#import librarries and functions
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wo

#setting frequency
freq=44100

#time duration of recording in seconds.
duration=15

#recording started
print("\n____________________RECORDING STARTED____________________\n")
recording=sd.rec(int(duration*freq),samplerate=freq,channels=2)

#hold of 15 seconds
sd.wait()

#recording is saving on yoyr device
write("recording.wav",freq,recording)

print("\n____________________RECORDING STOPPED____________________\n")