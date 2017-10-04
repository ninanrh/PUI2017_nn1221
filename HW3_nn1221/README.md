# Homework 3

Homework 3 consists of 3 assignments.

### Assignment 1
#### Overview
This assignment is to visualize the Central Limit Theorem by generating 100 samples of different size from each different distribution and visualize them.

#### Steps
- I chose Chi Square, Normal, Poisson, Binomial, Rayleigh distribution
- I set mean into 100 which also the same number for degrees of freedom (df)
- I created 2 empty dictionary which later will be filled with the distribution and the mean
- I generate 100 random number with range 10-1800 using this code `np.random.choice(range(10,1800), 100, replace=False)`
- For each distribution I created random distribution for each distribution using `for loop` of the empty dictionary and `np.random` to generate the random distribution. For I set `sigma = 5` for Rayleigh distribution and `p = 0.5`for binomial distribution.
- I plotted the sample means against sample size using code from [here](https://github.com/fedhere/PUI2017_fb55/blob/master/HW3_fb55/Assignment1.ipynb) with loop and described the phenomena I got from the plot, which is larger sample tends to get closer to population means.
- I plotted the distribution of all means
Overall I worked by myself and got help from stackoverflow for the technical stuff such as plotting and understanding the distribution.


### Assignment 2
can not finish the assignment till the due time


### Assignment 3
#### Overview
This assignment is to interpret the z value and use it to reject or accept null hypothesis

#### Steps
- I formulated the null and alternate hypothesis based on lab 3
- I open the raw data using `pd.read_csv()`
- I calculated the z value using `z = (tOldMean - tNewMean)/(tOldStdev/np.sqrt(len(df)))`
- I compared the z value with z critical (which obtained from `st.norm.ppf(.95)`)
- I rejected null hypothesis because z > zcritical, therefore new bus route has shorter commuting time.
Overall I worked by myself and got help from stackoverflow to generate z critical

