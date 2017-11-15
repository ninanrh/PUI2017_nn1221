I created plot for 311 calls that mentioned heating complaint during winter period between 2010 and 2017. 
I downloaded 311 data from [NYC Open Data](https://nycopendata.socrata.com/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/data). 
The data have been filtered by complaint type of heating and heat/hot water between October 1 and May 31, from 2010 - 2017. 
New York City regulation allows complaint regarding residential building that does not have enough heat only between October 1 and May 31 [(source)](http://www1.nyc.gov/site/hpd/owners/heat-hot-water.page), therefore this assignment use data from October 1 to May 31 for each winter term.
I use [seaborn](https://seaborn.pydata.org/generated/seaborn.heatmap.html) package to plot.
