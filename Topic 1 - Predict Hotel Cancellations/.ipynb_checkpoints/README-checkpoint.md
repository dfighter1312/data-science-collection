# Predict Hotel Cancellations

## What this repository do?

Give an exploratory data analysis on the hotel reservation data to give insights of why there exists so many booking cancellations and recommendations to surpass this circumstance.

In general, I do give 2 recommendations:

- We can employ a Random Forest classifier with a testing F1-score of 81% in order to identify a potential threat of cancellation. For these bookings, the staff can make a phone call to confirm their booking. Before implementation, we can done an experiment of calling the customers of potential cancels, and then observe the improvement of this suggestion.
- One can limit the number of lead time (strongest indicator of cancellation), week nights and weekday nights (minor indicators) for first-time customer.

Further details can be accessed on `topic_1.ipynb` and `topic_1_hyp_test.ipynb` notebook.

## Struggle and Derived Tips during implementation

**1. At first stage, follow a workflow**

You can see a really dummy analysis of me on `brainstorming_1.ipynb` when I don't know what to start first. Then I quickly hanging around Google to find some good EDA and gracefully I found one [here](https://github.com/NishadKhudabux/Potential-Customer-Prediction/blob/main/Potential_Customer_Prediction_Classification.ipynb). The great workflow here is to:

- Firstly look at the data, find some inconsistency between data and the description.
- Find missing values and duplicate values and define the strategies with it.
- Perform univariate analysis first by getting descriptive summaries via numbers and plots. Some erroneous data can be found or some new features can be derived from this stage.
- Perform bivariate analysis via plots (box for 2 categorical features, bar for 1 cat - 1 num, scatter for 2 numerical features).
- Perform full analysis between all features (optional, use heatmap or pair plot for this).
- Modeling and hypothesis testing.
- Make conclusion.

**2. Hypothesis testing**

After taking a revision on hypothesis testing, I decided to revisit this problem and add a notebook `topic_1_hyp_test.ipynb` which explain the process of hypothesis testing more precisely. In fact, there is one change happened on among all the tests in the main notebook. However, I will keep the content in `topic_1.ipynb` the same to know what mistake that I made.