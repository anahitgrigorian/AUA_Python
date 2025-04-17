#monthly sales
monthly_sales <- c(120, 135, 148, 160, 145, 170, 165, 180, 200, 190, 220, 205)

#total sales for the year
total_sales <- sum(monthly_sales)
cat("Total sales for the year is", total_sales, "\n")

#average monthly sales
average_sales <- mean(monthly_sales)
cat("Average monthly sales is", average_sales, "\n")

#month with the highest sales
max_sales_value <- max(monthly_sales)
max_sales_month_index <- which(monthly_sales == max_sales_value)
cat("Month with highest sales is the month", max_sales_month_index, "with", max_sales_value, "\n")

#growth rate
growth_rate <- diff(monthly_sales) / head(monthly_sales, -1) * 100
cat("Month-over-month growth rates in %:\n")
print(round(growth_rate, 2))

#month with highest growth rate
max_growth <- max(growth_rate)
max_growth_month <- which(growth_rate == max_growth) + 1  # since growth is for change to next month
cat("Month with highest growth rate is the month", max_growth_month, "with", round(max_growth, 2), "%\n")


#adjust first six months by adding 10%
adjusted_sales <- monthly_sales
adjusted_sales[1:6] <- adjusted_sales[1:6] * 1.10

#total and average sales
adjusted_total <- sum(adjusted_sales)
adjusted_avg <- mean(adjusted_sales)
cat("Adjusted total sales:", adjusted_total, "\n")
cat("Adjusted average sales:", adjusted_avg, "\n")

#named vector with month names
month_names <- c("January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December")
named_adjusted_sales <- setNames(adjusted_sales, month_names)

#sales below the annual average 
below_avg_months <- named_adjusted_sales[named_adjusted_sales < adjusted_avg]
cat("Months with below average sales:\n")
print(below_avg_months)

#variance and st. deviation
original_variance <- var(monthly_sales)
original_sd <- sd(monthly_sales)
adjusted_variance <- var(adjusted_sales)
adjusted_sd <- sd(adjusted_sales)

cat("Original Variance is", original_variance, "\n")
cat("Original Standard Deviation is", original_sd, "\n")
cat("Adjusted Variance is", adjusted_variance, "\n")
cat("Adjusted Standard Deviation is", adjusted_sd, "\n")
