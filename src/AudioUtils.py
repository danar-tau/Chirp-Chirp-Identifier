import librosa
import os
import AudioSegment
import np
import matplotlib.pyplot as plt 


def create_chunks(audio, filename):
    if len(audio) < 10000:
        return "Audio too small"

    chunk_no = 0
    t1 = 0
    for step in range(0, len(audio), 5000):
        t2 = step
        if step == 0:
            t1 = step
            continue

        curr_chunk = audio[t1:t2]
        chunk_no += 1
        curr_chunk.export(filename + '-' + str(chunk_no) + '.ogg', format="ogg")
        t1, t2 = t2, t1


def remove_silence(signal):
    return signal[librosa.effects.split(signal)[0][0] : librosa.effects.split(signal)[0][-1]]


def ogg_to_audio(path):
    return AudioSegment.from_ogg(path)

def mfcc_features(signal,sample_rate, num_mfcc):
    return np.mean(librosa.feature.mfcc(y=signal, sr=sample_rate, n_mfcc=num_mfcc).T,axis=0).tolist()

def mel_spectogram_generator(audio_name,signal,sample_rate,augmentation,target_path):
    # Plot mel-spectrogram
    N_FFT = 1024 #length of the FFT window         
    HOP_SIZE = 1024  #number of samples between successive frames     
    N_MELS = 128 #number of Mel bands to generate                 
    FMIN = 0 #lowest frequency (in Hz)
    # htk - use HTK formula instead of Slaney
    # fmax - highest frequency (in Hz)
    S = librosa.feature.melspectrogram(y=signal,sr=sample_rate,
                                    n_fft=N_FFT,
                                    hop_length=HOP_SIZE, 
                                    n_mels=N_MELS, 
                                    htk=True, 
                                    fmin=FMIN, 
                                    fmax=sample_rate/2) 

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.power_to_db(S**2,ref=np.max), fmin=FMIN,y_axis='linear')
    plt.axis('off')
    plt.savefig(target_path + augmentation + audio_name[:-4] + '.png',bbox_inches='tight',transparent=True, pad_inches=0)
    plt.clf()
    plt.close("all")
  
