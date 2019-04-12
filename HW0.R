library(ggplot2)
library(dplyr)
library(stringr)
library(lubridate)
setwd ("/Users/OliviaMartins/Documents/MMSS_311-2/hw0")
data <- read.csv("pums_chicago.csv", header=TRUE)

reg <- lm(WAGP~WKHP, data = data)
summary(reg)

#(k (vii)) plot of residuals on fitted values
fitted<-fitted.values(reg)
res<-residuals(reg)
fit_res<-ggplot(reg)+geom_point(aes(x=fitted, y=res))
fit_res

#(m)
data(mtcars)
mtcars$am<-as.factor(mtcars$am)
mtcars$gear<-as.factor(mtcars$gear)
plot<-ggplot(mtcars, aes(x=mpg, y=wt, color=am)) + geom_point(aes(shape=gear))
plot + labs(x = "Miles Per Gallon", y = "Weight (In Thousands of Pounds)") + 
  theme(
    panel.background = element_rect(fill="pink", color="pink", size=0.5, linetype="solid"),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank()
  )
        

