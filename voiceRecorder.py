import sounddevice as sd
import soundfile as sf
from tkinter import *

def Voice_rec():
    fs=48000
    time=5
    record=sd.rec(int(time*fs),sample=fs,channel=2)
    sd.wait()

    return sf.write('my_audio_file.flac',record,fs)

root=Tk()
Lable(root,text="Voice Recorder: ").grid(row=0,sticky=W,rowspan=5)

b=Buttom(root,text="Start",command=Voilce_rec)
b.grid(row=0,column=2,columnspan=2,rowspan=2,padx=5,pady=5)

mainloop()
