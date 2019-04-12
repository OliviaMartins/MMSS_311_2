library(ggplot2)
library(dplyr)
library(stringr)
library(lubridate)
#Exercise 1 
even_odd <-function(num){
  if(num%%2 == 0)
  {
    print("Even")
  }
  else if(num%%2 !=0)
  {
    print("Odd")
  }
  else{
    print("Not an Integer")
  }
}

#Exercise 2 
die_roll<-function(){
  roll = sample(1:6, 1, replace=T)
  if(roll%%2==0){
    roll = 2*roll
  }
  else{
    roll = roll*roll
  }
}

vec<- sapply(1:20, die_roll)

#Exercise 3 




  
