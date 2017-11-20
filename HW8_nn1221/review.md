![](https://github.com/ninanrh/PUI2017_nn1221/blob/master/HW8_nn1221/HW8.png)

**Figure 1.** Heating complaints frequencies through 311 calls data in New York City during Winter period of 2010-2016. 
[(Source code in Jupyter Notebook)](https://github.com/ninanrh/PUI2017_nn1221/blob/master/HW8_nn1221/HW8.ipynb)

I created plot for 311 calls that mentioned heating complaint during winter period between 2010 and 2017. 
I downloaded 311 data from [NYC Open Data](https://nycopendata.socrata.com/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/data). 
The data have been filtered by complaint type of heating and heat/hot water between October 1 and May 31, from 2010 - 2017. 
New York City regulation allows complaint regarding residential building that does not have enough heat only between October 1 and May 31 [(source)](http://www1.nyc.gov/site/hpd/owners/heat-hot-water.page), therefore this assignment use data from October 1 to May 31 for each winter term.

I used sources from [seaborn](https://seaborn.pydata.org/generated/seaborn.heatmap.html) package to plot. In this assignment, I'm working on my own.



----
Review:

This is an amazing plot! I love it!

CLARITY: is the plot easy to read? is it clear or confusing, are the quantities being visualized ambiguous?
The 

Colorblindness: Using Color Oracle to check, only in the very rare type of color blindness (tritanopia) is information lost. The last two months of winter simply look white. To fix this you can change the lightest colors on the scale to slightly more pigmented, if possible. 

ESTHETIC: beautiful is a subjective judgment: you should not judge the plot on the basis of whether you think it is "beautiful", but you should judge whether its esthetic is functional to what it is meant to communicate. Are the colors chosen appropriately? Are the graphical elements used appropriate to represent the quantities being visualized? Are the graphical choices allowing you to focus on the right elements or are they distracting you?


HONESTY: is the plot honestly reproducing the data or is it deforming it, perhaps to emphasize a point?

