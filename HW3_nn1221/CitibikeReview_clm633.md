### a. verify that their Null and alternative hypotheses are formulated correctly
There's a lot going on here. I don't think this is formulated correctly.
- There's no alternative hypothesis. 
- There are two different null hypotheses, I think?


 1) **"The ratio of long distance trips by men is less than or equal to the ratio of long distance trips by women"**

I think this is the main hypothesis as far as I can tell. But then, this does not line up with the "IDEA", the LaTeX (which looks at ratios long distance trips vs. short distance trips on weekend vs. week), or the code, all of which seem to line up with the Idea but not this hypothesis.

 2) **"The ratio of man biking on weekends over man biking on weekdays is _the same_ or _higher_  than the ratio of woman biking over weekends to woman biking on weekdays."**

I don't think this is pursued at all, so we'll ignore it from here on out.


If we consider "the idea" / hypothesis #1 substantively (assuming "weekdays / weekends" was meant rather than "men / women"), there's still an issue of "what is a long distance trip?" which is not explained in any preamble etc... I see it only by examining the code itself. It seems to me this should probably be explicated in the null hypothesis (the number of trips that had as-the-crow-flies distance above the mean).

Last but not least, I think the ratio should be "weekends / total" vs. "weekdays / weekends" (also see below).

Again, from here on out, I'll look at the "IDEA" / analysis rather than the specific hypothesis that was formulated.

### b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

- As-the-crow-flies distance is a choice worth discussing for a "long distance" trip. What about trips that end up being more circuitous? Should we incorporate some time measure as well (e.g. close to the 30-minute limit). That said, I think as-the-crow-flies distance is a fine indicator to look at.
- The data here is for one month - January 2015. I didn't explicate my temporal assumptions in the hypothesis either, but I think it's dangerous to say that usage patterns in January are the same as in May, for example.
- Processing: looks good to me! If I were code-reviewing this, I'd remark on the use of `eval` :P
- I also really like the plots.

### c. chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.
- I think we'd want to use a Z-test of proportion here. There is one caveat: we'd want to take the proportion of short distance on weekend / total rides vs. proportion of long distance on weekend / total rides. This is to make sure we have a correctly normalized proportion.
