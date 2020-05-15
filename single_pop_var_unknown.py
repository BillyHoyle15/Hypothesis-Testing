# -*- coding: utf-8 -*-
"""
Hypothesis Testing. Testing for the mean when singlepopulation variance 
is unknown

Task: Estimate if our competitor has a higher e-mail opening rate
Your company has 40% email opening rate
You know the last 10 campaign of your opponent and their opening rates

H0 -> Avarage open rate <= 40% 
H1 -> Avarage open rate > 40%

Decision Rule: if absolute value of T_score > positive critical value (z),
                we reject the null hypothesis
                
critical value t can bu found from t-table. We choose t-stat because variance
is unknown and we have small sample size
This is 1 sided test since we only look for term "higher".

Let's test for 5% significance (i.e. 95% confidence interval.)

t = 1.83
"""

import numpy as np


sample = np.array([26, 23, 42, 49, 23, 59, 29, 29, 57, 40])

sample_mean = sample.mean()
sample_std = sample.std()
sample_count = len(sample)

H0 = 40 #null hypothesis

standard_error = sample_std / np.sqrt(sample_count)
T_score = (sample_mean - H0) / standard_error 

'''
We found that T_score is -0.56, absolute of T = 0.56
t = 1.83
T < t so we accept the Null Hyhothesis (H0), opponnent opening rate is equal or
less than our opening rate, which is 40%
'''

'''*****************p-value****************
p-value is the smallest level of significance at which we can still reject the
null hypothesis, given the observed sample statistic

p-value is a universal concept that works with every distribution (normal,
student's T, binomial, uniform etc.)

We should reject the null hypothesis if p-value < significance level
use the link below the calculate p-value for T-score and significance level
p-value calculator: www.socscistatistics.com/pvalues/tdistribution.aspx

Our T_score is -0.56
significance level is 0.05 (95%)
Size of dataframe = 9 (actual size - 1)
we are looking for one sided (tailed) test

result is: 
The p-value is 0.294572
The result is not significant at p < 0.05
We accept the Null Hypothesis because p-value is greater than 
significance level
'''