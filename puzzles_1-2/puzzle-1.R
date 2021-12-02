## To do this, count the number of times a depth measurement increases from the 
## previous measurement. (There is no measurement before the first measurement.) 
## In the example above, the changes are as follows:

# 199 (N/A - no previous measurement)
# 200 (increased)
# 208 (increased)
# 210 (increased)
# 200 (decreased)
# 207 (increased)
# 240 (increased)
# 269 (increased)
# 260 (decreased)
# 263 (increased)

# In this example, there are 7 measurements that are larger than the previous 
# measurement.

testInput <- c(199, 200, 208, 210, 200, 207, 240, 269, 260, 263)

#### 

findDepthIncrease <- function(arrayOfDepths){
        ## initiate a counter
        counter = 0
        ## loop over the array and pull the current and previous values
        for(index in 2:length(arrayOfDepths)) {
                previousValue = arrayOfDepths[index - 1]
                if(length(previousValue) == 0) {
                        previousValue <- 0
                }
                currentValue = arrayOfDepths[index]
                if(currentValue > previousValue) {
                        counter = counter + 1
                }
        }
        return(counter)
}

findDepthIncrease(input) ##Answer: 1288