# Predict Student Performance From Game Play

## What this repository do?

Give an exploratory data analysis on the student gameplay logs and their effects on answer correct questions in class.

I am currently perform 2 ways to make prediction (from logs, can you predict whether 18 questions are answered correctly by the player) as required from Kaggle competition:

- Perform aggregation on every session, then modeling it using Random Forest or any traditional machine learning models. I also made several hypothesis to be tested (in `eda.ipynb`).
- Consider session information, whether each row records an action made by player, as sequential data, and pass it into an RNN model to make prediction (in specific, LSTM). I have uploaded the notebook to Kaggle under [this link](https://www.kaggle.com/code/dungdore1312/session-info-as-sequence-use-lstm-to-predict) or you can see a version in `session-info-as-sequence-use-lstm-to-predict.ipynb` file.

## Struggle and Derived Tips during implementation

**1. LSTM**

Consider what the inputs are for LSTM model is a difficult questions, since there is over 26 millions records, and greedily putting all of it after processing with One Hot Encoding leads to computation overhead. Meanwhile, reducing features also reduces the model performance. Gladly, however, it still reached 73% accuracy in the training set, but it does provide more rooms for improvement.

Pratically speaking, I do believe treating records as sequential data does have its potential in resolving the problem. But the difficulties it made does need someone else's help.
