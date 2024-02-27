import os
from AudioUtils import ogg_to_audio, create_chunks

# AUDIO_INPUT_DIR = '/kaggle/input'
# CUT_AUDIO_DIR = '/Kaggle/cut_audio'

# for local use and tests
AUDIO_INPUT_DIR = r'..\data\input'
CUT_AUDIO_DIR = r'..\data\cut'


def prepare_files():
    # create directory for the audio files
    if not os.path.exists(CUT_AUDIO_DIR):
        os.makedirs(CUT_AUDIO_DIR)

    # remove all files from the cut files directory
    files = os.listdir(CUT_AUDIO_DIR)
    for f in files:
        os.remove(f)

    # first cut all the data files into 5 seconds audio files
    for dirname, _, filenames in os.walk(AUDIO_INPUT_DIR):
        for ogg in filenames:
            audio = ogg_to_audio(os.path.join(dirname, ogg))
            create_chunks(audio, ogg[:-4], CUT_AUDIO_DIR)


if __name__ == '__main__':
    prepare_files()
