# NLP and Data Science project

Work in a small group to create a complete, reproducible text-classification project.
The main outcome is not a particular accuracy score. It is a project that another
student can open, understand, and run.

You can use {download}`the prepared GoEmotions data <../data/goemotions_workshop.csv>`,
or find another text-classification dataset that interests your group.

## Start with a research question

For the supplied data, you could ask:

> Can patterns in a short comment predict whether a human annotator labelled it as
> anger, fear, joy, or sadness?

If you choose another dataset, write your own question before beginning the analysis.
It should identify the text used as input and the category being predicted.

## Create a project

Make a new folder outside the workshop repository. Give it a meaningful name and
organise it so that code, data, and generated results are not mixed together.

Your project might look like this:

    emotion_project/
    ├── README.md
    ├── requirements.txt
    ├── data/
    │   └── emotions.csv
    ├── scripts/
    │   └── analyse_emotions.py
    └── outputs/
        └── confusion_matrix.png

This is an example rather than a mandatory template. Your group should be able to
explain every folder it creates.

## Write one runnable script

Create a Python script that:

1. locates files with pathlib;
2. loads and inspects the data with pandas;
3. defines the text input X and category target y;
4. creates training and test sets;
5. places text vectorisation and classification in a pipeline;
6. fits the pipeline using the training data;
7. evaluates predictions on the test data;
8. saves at least one useful result in the outputs folder; and
9. contains comments explaining the important analytical decisions.

Use functions where they make the workflow easier to understand. Add a few assertions
that check assumptions which matter to the analysis. The finished script should run
from beginning to end without requiring someone to execute lines manually.

## Make the project understandable

Write a short README containing:

- the research question;
- the source and licence of the data;
- what one row represents;
- instructions for running the script;
- the model and text representation used;
- one result; and
- one important limitation.

Be precise about the target. An emotion classifier predicts labels from text; it does
not directly measure a person's internal emotional state.

## Option: choose your own data

Your group may instead find a text-classification dataset on
[Kaggle Datasets](https://www.kaggle.com/datasets). Sentiment, topic, spam, intent,
authorship, and emotion datasets can all work.

Choose something manageable:

- the data can be downloaded as CSV or converted easily to a DataFrame;
- there is one text column and one clearly documented category column;
- there are enough examples in each category for a train/test split;
- the licence permits educational reuse;
- the content is suitable to share in the classroom; and
- the dataset does not require extensive cleaning before modelling.

Record the dataset page and licence in your README. Do not spend the whole project
searching: if your group has not found a suitable dataset after ten minutes, use the
provided GoEmotions subset.

## Optional reference

If your group gets stuck on the basic scikit-learn structure, consult
{download}`this runnable example <../workshop_scripts/emotion_classification_challenge.py>`.
In your cloned repository, it is at
`book/workshop_scripts/emotion_classification_challenge.py`.

Use it as a reference rather than copying it unchanged: your own script and README
should reflect your dataset and research question.

## Supplied data

The supplied file contains 1,000 screened GoEmotions comments, balanced across anger,
fear, joy, and sadness. It is a small teaching sample and is not representative of
emotion or Reddit users generally. Source: [GoEmotions](https://github.com/google-research/google-research/tree/master/goemotions),
used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
