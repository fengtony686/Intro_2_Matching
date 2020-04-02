# An Example of Matching
library(tidyverse)
library(Ecdat)
data(Wages)  


Wages <- Wages %>% mutate(ed.coarse = cut(ed, breaks=3),
                          exp.coarse = cut(exp, breaks=3))


union <- Wages %>% filter(union=='yes')


nonunion <- Wages %>% filter(union=='no') %>%
  group_by(ed.coarse,exp.coarse,bluecol,ind,south,smsa,married,sex,black) %>%
  summarize(untreated.lwage = mean(lwage))


union %>% inner_join(nonunion) %>% 
  summarize(union.mean = mean(lwage),nonunion.mean=mean(untreated.lwage))