# Portfolio Risk Management

## What this repository do?

A hands-on project on portfolio risk management, while learn the course **Introduction to Portfolio Risk Management in Python** on DataCamp.

## Struggle and Derived Tips during implementation

**1. Understanding Financial Concepts**

Since my background is Computer Science, this topic is quite hard to grasp at, not because of the formula, but the finance-related concepts.

To summarize, I do know that portfolio is a collection of financial assets (stocks, bonds, cash) and the goal of creating a portfolio is to maximize the return while minimizing the risk.
- The first part taught me what is the return and what distribution is commonly sampled from (not Gaussian, of course). 
- The second part defines ways to pick an efficient portfolio, which is a portfolio with high (annualized) average return, and low volatility. The baseline in this section is equally weighted portfolio, then we improve to weighted, market-cap weighted, Max Sharpe Ratio portfolio and finally Global Minimum Volatility portfolio.
- The third part is modeling the portfolio return based on factors. In CAPM, excess expected return of the designated portfolio is correlated with excess expected return of the broad market portfolio. In 3-factor model, we have exposure to the HML factor, SMB factor and unexplained factor $\alpha$. In 5-factor model, we have RMW (Profitability) and CMW (Investment). I definitely have no idea about those factors, therefore if I can take this further, I would get back to read about the factors later to see how they are computed (the dataset computes them for me so it is kinda confusing).
- The final part is estimating tail risk. In other words, the portfolio has an $x$% chance of getting $y$% return (or loss since $y$ normally negative). Common approaches are Historical drawdowns, Value at Risk, Conditional Value at Risk, which are calculated based on existing sample. Other approach includes Parametric Value at Risk and Monte Carlo simulation, which assume that the return follows a normal distribution, and either get a sample of it then derive VaR (Monte Carlo) or directly compute the VaR from the assumed distribution (Parametric VaR). Note that the mean and volatility of the distribution is taken from the observations.

Yes, I think the summary looks quite nice for me. But in general, I think that the notebook attached in this topic is mostly working with stock data, and of course a portfolio do not only have stocks as all of their assets. So next sessions/courses may take me deeper about risk management in Applied Finance.

**2. Quantile and Percentile**

You have to be careful when using `np.quantile` and `np.percentile`. They both accept the first 2 arguments are `arr` and `q`. But the elements of `q` in `np.quantile` must be between 0 and 1, while `q` in `np.percentile` is scaled up between 0 and 100.

From the courses I have learned, they assume quantile and percentile have the similar meaning, but through this I know that there is a bit difference now.
