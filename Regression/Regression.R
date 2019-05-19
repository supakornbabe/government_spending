library(readr)
feature <- read_csv("feature_without_outlier.csv")

year = feature$Year
Department_of_Local_Administration = feature$Department_of_Local_Administration
Department_of_Provincial_Administration = feature$Department_of_Provincial_Administration
Bangkok =  feature$Bangkok
Department_of_Lands =  feature$Department_of_Lands
Community_Development_Department = feature$Community_Development_Department
Department_of_Disaster_Prevention_and_Mitigation = feature$Department_of_Disaster_Prevention_and_Mitigation
Pattaya = feature$Pattaya
`Department_of_Public_Works_and_Town_&_Country_Planning` = feature$`Department_of_Public_Works_and_Town_&_Country_Planning`
Office_of_the_Permanent_Secretary_for_Interior = feature$Office_of_the_Permanent_Secretary_for_Interior
Usage = feature$Usage

model = lm(Usage ~ Department_of_Local_Administration)
summary(model)
predict(model)

plot(
  year,
  main = "Predicted vs Expected Usage of Ministry on Interior on Thailand",
  Usage/1000000,
  ylab = "Million THB",
  xlab = "Year",
  col = "blue"
)
lines(year, predict(model)/1000000, col = "red")

legend("topleft",
       c("Expected Usage", "Predicted Usage"),
       fill = c("blue", "red"))
