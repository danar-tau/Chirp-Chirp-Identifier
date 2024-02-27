import librosa
import os
import AudioSegment


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

