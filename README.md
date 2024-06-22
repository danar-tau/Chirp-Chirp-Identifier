## Chirp-Chirp-Identifier

# Introduction

Our team worked in the non-competitive track of the challenge “BirdCLEF 2022” organized by Cornell Lab of Ornithology. We needed to successfully identify bird calls in soundscapes recorded in Hawaii, in order to help scientists monitor rare bird species in this region. 
This is a formidable task as even obtaining recordings of these rare birds is hard (for example there are only a few thousand individuals remaining globally of the Nene geese, one of the birds included in this challenge).
We needed to solve a classification problem, with a big amount of classes. The train data has 152 different classes, from which only 21 birds are used for scoring. For each recording in the test dataset we needed to determine whether or not the bird in question called during the 5 second window of that specific recording.
This is code competition, which has some important characteristics to remember - 
We submit our notebook which must run offline and produce the submission csv in kaggle’s working directory. Its runtime cannot surpass 9 hours.
We do not have access to the full logs of each run.
We do not have access to the test dataset. We have one test recording as an example, but the full test dataset can be accessed only during runtime of a submission.

# Explaination on the directories 
# Src

birdclef-mels-computer-2022.ipynb - this notebook preprocesses the audio files and creates the mel spectrograms. The output of this notebook is saved as Kaggle-dataset.
training_on_2022_data.ipynb - this is the training kernel, on the pretrained ResNeSt and 2021 data weights.
birdclef-2022-submitting-pretrained-resenet50.ipynb - our inference kernel

# Models 

All the checkpoint weights we used in our inference.

