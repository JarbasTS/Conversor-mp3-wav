from pydub import AudioSegment
import os
import glob 


for filename in glob.glob("audio\*.mp3"):
        
     name, extension = os.path.splitext(filename)
     AudioSegment.from_wav(filename).set_channels(1).export(name + ".wav", format="wav")
   
     