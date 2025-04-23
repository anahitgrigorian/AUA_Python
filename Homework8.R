set.seed(42)   
cities <- c("New York", "Los Angeles", "Chicago", "Houston", "Phoenix")
days <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

#random weather data
generate_weather <- function(n, min_val, max_val) {
  round(runif(n, min_val, max_val), 1)
}

n_cities <- length(cities)
n_days <- length(days)

#data for each parameter
temp_matrix <- matrix(generate_weather(n_cities * n_days, -5, 35), nrow = n_cities, byrow = TRUE)
prec_matrix <- matrix(generate_weather(n_cities * n_days, 0, 20), nrow = n_cities, byrow = TRUE)
wind_matrix <- matrix(generate_weather(n_cities * n_days, 0, 100), nrow = n_cities, byrow = TRUE)

rownames(temp_matrix) <- cities
rownames(prec_matrix) <- cities
rownames(wind_matrix) <- cities

colnames(temp_matrix) <- days
colnames(prec_matrix) <- days
colnames(wind_matrix) <- days

#3D array [cities x days x parameters]
weather_array <- array(c(temp_matrix, prec_matrix, wind_matrix),
                       dim = c(n_cities, n_days, 3),
                       dimnames = list(cities, days, c("Temperature", "Precipitation", "WindSpeed")))


#Temperature avg per city
avg_temp <- rowMeans(temp_matrix)
highest_avg_temp_city <- cities[which.max(avg_temp)]

#Precipitation total per city
total_precip <- rowSums(prec_matrix)
most_rain_city <- cities[which.max(total_precip)]

#Wind speed day with highest average wind across cities
avg_wind_per_day <- colMeans(wind_matrix)
windiest_day <- days[which.max(avg_wind_per_day)]

# list of matrices
weather_list <- list(Temperature = temp_matrix,
                     Precipitation = prec_matrix,
                     WindSpeed = wind_matrix)

#overall averages
overall_avg_temp <- mean(weather_list$Temperature)
overall_total_precip <- sum(weather_list$Precipitation)
overall_avg_wind <- mean(weather_list$WindSpeed)

#days with temp > 30C in more than one city
high_temp_days <- sapply(1:n_days, function(d) sum(weather_list$Temperature[, d] > 30))
days_above_30C <- days[high_temp_days > 1]

selected_city <- "Phoenix"
city_index <- which(cities == selected_city)

#original temperature
original_avg_temp <- mean(temp_matrix[city_index, ])

#days with 0 mm precipitation
zero_precip_days <- which(prec_matrix[city_index, ] == 0)

#increase temperatures by 10% on those days
temp_matrix[city_index, zero_precip_days] <- temp_matrix[city_index, zero_precip_days] * 1.10

weather_array[,, "Temperature"] <- temp_matrix
new_avg_temp <- mean(temp_matrix[city_index, ])


cat("City with highest average temperature:", highest_avg_temp_city, "\n")
cat("City with most precipitation:", most_rain_city, "\n")
cat("Day with highest average wind speed:", windiest_day, "\n")
cat("Overall average temperature:", round(overall_avg_temp, 2), "\n")
cat("Total precipitation over the week:", round(overall_total_precip, 2), "mm\n")
cat("Overall average wind speed:", round(overall_avg_wind, 2), "km/h\n")
cat("Days with >30°C in more than one city:", paste(days_above_30C, collapse = ", "), "\n")
cat("Avg temperature in", selected_city, "before adjustment:", round(original_avg_temp, 2), "\n")
cat("Avg temperature in", selected_city, "after adjustment:", round(new_avg_temp, 2), "\n")
