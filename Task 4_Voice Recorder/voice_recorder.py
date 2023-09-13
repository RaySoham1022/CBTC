import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  
seconds = 10  

print("Start Speaking ................ ")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()
print("Finished Recording................ ")  
write('Recording.wav', fs, myrecording)  