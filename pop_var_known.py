# -*- coding: utf-8 -*-
"""
Hypothesis Testing. Testing for the mean when population variance is known
poulation standard deviation (std) = 15.000 USD (remember std = sqrt(var))

We have sample dataset for software developer salaries. 
H0 -> Avarage software developer salary = 113.000 USD
H1 -> Avarage software developer salary != 113.000 USD

Decision Rule: if absolute value of Z_score > positive critical value (z),
                we reject the null hypothesis
                
critical value z can bu found from z-table
This is 2 sided test since we don't look for just greater or smaller value.

Let's test for 5% significance (i.e. 95% confidence interval.)
z = 1.96
"""

import numpy as np


sample = np.array([117313, 104002, 113038, 101936, 84560, 113136, 80740, 
                   100536, 105052, 87201, 91986, 94868, 90745, 102848,
                   85927, 112276, 108637, 96818, 92307, 114564, 109714,
                   108833, 115295, 89279, 81720, 89344, 114426, 90410,
                   95118, 113382])

sample_mean = sample.mean()
sample_count = len(sample)
pop_std = 15000 #population standard deviation
H0 = 113000 #null hypothesis

standard_error = pop_std / np.sqrt(sample_count)
Z_score = (sample_mean - H0) / standard_error 

'''
We found that Z_score is -4.67, absolute of Z = 4.67
z = 1.96
Z > z so we reject the Null Hyhothesis (H0), avarage software developer salary
is not 113000 USD.
'''

'''*****************p-value****************
p-value is the smallest level of significance at which we can still reject the
null hypothesis, given the observed sample statistic

p-value is a universal concept that works with every distribution (normal,
student's T, binomial, uniform etc.)

We should reject the null hypothesis if p-value < significance level
use the link below the calculate p-value for Z-score and significance level
p-value calculator: www.socscistatistics.com/pvalues/normaldistribution.aspx

Our Z_score is -4.67
significance level is 0.05 (95%)
we are looking for two sided (tailed) test

result is: 
The P-Value is < .00001
The result is significant at p < .05
'''
