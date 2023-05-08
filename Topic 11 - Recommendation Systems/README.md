# Recommendation Systems

## What this repository does?

This repository contains a course note from **Building Recommendation Engines in Python** on DataCamp as well as a mini-project to build a recommendation engine with knowledge taken from the course (I am just planning on this, but tend to take a dataset from Kaggle and then build it from collected data).

## Struggle and Derived Tips during implementation

**1. Review on Recommendation System**

For me, it is more likely to be a revision since I have learned about it in the Data Mining and Intelligent Systems courses in the university. But trust me, not so much knowledge is left (:D). But here is the summary from the course on DataCamp first:

- Three types of recommendations that I have learned are non-personalized recommendations (suitable for newcomers, just pick the products with the most usage or highest ratings); content-based recommendations (or item-based, based on the similarities of items, the user who has used one product will likely to be suggested with a similar item, suitable for large firm with lots of product updated every day to suggest user that has never used the product before, since the attributes are fixed); collaborative filtering (or user-based, based on the similarities of users, the user who has similarity with a set of other users will likely to be suggested with a product that the group of users mentioned above gave high ratings, more challenging and less effective than item-based, in general, but does give interesting recommendation).
- User-Item matrices in recommendation systems are really sparse. A method to tackle this problem is to fill missing value with a "neutral" rating.
- K-Nearest Neighbors is used for user-based recommendation.
- Matrix Factorization methods, such as Singular Value Decomposition, can be useful to reduce the number of entries that requires for such large matrices.
- Validation in recommendation systems require a split in chunks (N columns and M rows) where N less than the number of users, and M less than the number of items. Suggested metric from the course is Root Mean Squared Error.

**2. Recommendation Systems on Twitter**

At a high-level perspective, Twitter's recommendation system can be stated briefly as below:

- Input = follow graph + tweet engagement + user data
- Set of models that extract latent features with specific meaning *(e.g., What is the probability you will interact with another user in the future?)*. I believe that this is similar to performing a downstream task to extract new feature, but not sure which type of learning they employed.
- **Candidate Sourcing**: fetch best tweets from difference sources (~1500 candidates)
  - In-network source (50%):
    - A logistic regression model that ranks tweets of users who you follow based on their relevance.
    - A model (Real Graph) that predicts the likelihood of engagement between 2 users.
  - Out-of-network source (50%):
    - Social graph: like a collaborative filtering approach, find tweets that people you recently engaged with & people with similar tweet interests. Use GraphJet to traverse through the engagement graph.
    - Embedding space: SimClusters which use Sparse Binary Factorization (see the references).
- **Ranking**: A neural network with ~48M parameters taking tweet interaction as inputs, probability of ten labels as outputs ==> give a score (I don't know what are the labels in details).
- **Heuristics, Filters, and Product Features**: a bit modifications of the score (?)
  - *Visibility Filtering*: remove tweets from blocked/muted accounts or contains inappropriate contents.
  - *Author Diversity*: avoid multiple tweets from the same author.
  - *Content Balance*: ensure ratio between in-network and out-of-network tweets.
  - *Feedback-based Fatigue*: add penalty to tweets with negative feedback.
  - *Social Proof*: the tweet must be engaged by someone you follow, or the tweet's owner is followed by someone you follow (second degree connection).
  - *Conversations*: Combine reply + original tweet content.
  - *Edited tweets*: "Determine if the Tweets currently on a device are stale, and send instructions to replace them with the edited versions." (Not clear about this).

## References

- [Twitter Recommendation System Outline](https://blog.twitter.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm)
- [SimClusters: Community-Based Representations for Heterogeneous Recommendations at Twitter](https://dl.acm.org/doi/10.1145/3394486.3403370)
- [Sparse Binary Factorization](https://github.com/twitter/sbf)
