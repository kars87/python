import soundfile as sf
import pyloudnorm as pyln
import matplotlib.pyplot as plt
import numpy as np

"""
@inproceedings{steinmetz2021pyloudnorm,
        title={pyloudnorm: {A} simple yet flexible loudness meter in Python},
        author={Steinmetz, Christian J. and Reiss, Joshua D.},
        booktitle={150th AES Convention},
        year={2021}}
"""





fileName = "cheer_long.wav"
data, rate = sf.read(fileName) # load audio

# peak normalize audio to -3 dB
peak_normalized_audio = pyln.normalize.peak(data, -3.0)

# measure the loudness first 
meter = pyln.Meter(rate) # create BS.1770 meter
loudness = meter.integrated_loudness(data)
#print(loudness)



# loudness normalize audio to -23 dB LUFS
loudness_normalized_audio = pyln.normalize.loudness(data, loudness, -23.0)
sf.write("newCheer.wav", loudness_normalized_audio, rate)
sf.SoundFile.close()


