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

**2. Recommendation Systems from Tiktok and Twitter**

So far, these 2 big guys did publish a part of their recommendation system on papers and source codes. I will take a look at them (if found) and then write a short summary about it here.