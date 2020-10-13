# sadText (Final Year Project)
Included in this repo are resources I used for the detection of Secondary emotions related to sadness featured in Parrotts (2001) emotion classification. Data was sourced from reddit using PRAW, a Python Reddit API Wrapper. Classification was carried out using a series of different Deep Neural Network Architectures.

# Data
Data was sourced from different subreddits, primarily the r/depression and r/anxiety subreddits, and the scripts for the scraper and annotator can be found in the Reddit Scraper and Annotator file.

Data was annotated with 7 different classifications - Suffering, Sadness, Guilt, Sympathy, Dissapointment, Neglect and Unclassifiable.
Two different datasets are included sadtextv1, which is heavily weighted towards unclassifiable, and sadtextv2 which omits all unclassifiable datapoints.
Due to the circumstances of the project annotation was not carried out by multiple people, however I did carry out multiple passes when annotating the data in an attempt to improve the data quality.

#Neural Networks
A combination of Bi-LSTMs, GRUs and CNNs are used in classification, and hyperparameters for each one were optimised using [Keras Tuner](https://keras-team.github.io/keras-tuner/). The Bi-LSTM + CNN arcitecture achieved the best results, with an F1 Score of 0.60 on sadTextv2.

