setwd ("/Users/OliviaMartins/Documents/MMSS_311-2/MMSS_311_2")
install.packages("ggplot2")
install.packages("dplyr")
install.packages("stringr")
install.packages("lubridate")

library(ggplot2)
library(dplyr)
library(stringr)
library(lubridate)

url <- "https://www.qogdata.pol.gu.se/data/qog_std_ts_jan19.csv"
qog <-read.csv(url, header=TRUE)
print(dim(qog))

