# An Example of Extra Explanatory Variables
library(tidyverse)


df <- tibble(R = sample(c(0,1), 500, replace=T)) %>%
    mutate(X = R) %>%
    mutate(X = ifelse(runif(500) > .8, 1-R, R)) %>%  
    mutate(Y = 5*X +rnorm(500))  # X -> Y


df %>% group_by(R) %>% summarize(Y=mean(Y))
