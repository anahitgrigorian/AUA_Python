#creating the vectors
artistNames <- c("ArtistA", "ArtistB", "ArtistC", "ArtistD")
eventLocations <- c("Location1", "Location2", "Location3")
merchTypes <- c("T-Shirt", "Hat", "Poster", "Sticker")

#creating matrix for artist ratings 
artistRatings <- matrix(sample(1:5, length(artistNames) * length(eventLocations), replace = TRUE), 
                        nrow = length(artistNames), 
                        ncol = length(eventLocations),
                        dimnames = list(artistNames, eventLocations))
#creating 3D array for merch sales 
merchSales <- array(sample(10:500, length(merchTypes) * length(eventLocations) * 2, replace = TRUE), 
                    dim = c(length(merchTypes), length(eventLocations), 2),
                    dimnames = list(merchTypes, eventLocations, c("Price", "Quantity")))


library(dplyr)

#Attendees dataframe
dfAttendees <- data.frame(
  attendeeID = 1:100,
  name = paste0("Attendee", 1:100),
  age = sample(18:50, 100, replace = TRUE),
  eventAttended = sample(eventLocations, 100, replace = TRUE)
)

#Events dataframe
dfEvents <- data.frame(
  location = eventLocations,
  date = as.Date(c("2025-07-01", "2025-07-02", "2025-07-03"))
)

#Artist Ratings dataframe
dfArtistRatings <- as.data.frame(as.table(artistRatings)) %>%
  rename(Artist = Var1, Location = Var2, Rating = Freq)

#Merchandise Sales dataframe
dfMerchSales <- as.data.frame(as.table(merchSales)) %>%
  pivot_wider(names_from = Var3, values_from = Freq) %>%
  rename(MerchType = Var1, Location = Var2, Price = Price, Quantity = Quantity)



#task 1
topArtist <- dfArtistRatings %>%
  group_by(Artist) %>%
  summarise(avgRating = mean(Rating)) %>%
  arrange(desc(avgRating)) %>%
  slice(1)
topArtist

#task 2
attendeesPerLocation <- dfAttendees %>%
  group_by(eventAttended) %>%
  summarise(totalAttendees = n())
attendeesPerLocation

#task3
avgAgePerLocation <- dfAttendees %>%
  group_by(eventAttended) %>%
  summarise(avgAge = mean(age))
avgAgePerLocation

#task4
highestSalesEvent <- dfMerchSales %>%
  group_by(Location) %>%
  summarise(totalQuantity = sum(Quantity)) %>%
  arrange(desc(totalQuantity)) %>%
  slice(1)
highestSalesEvent

#task 5
avgPriceMerch <- dfMerchSales %>%
  group_by(MerchType) %>%
  summarise(avgPrice = mean(Price))
avgPriceMerch

#task 6
highestRatedEvent <- dfArtistRatings %>%
  group_by(Location) %>%
  summarise(avgRating = mean(Rating)) %>%
  arrange(desc(avgRating)) %>%
  slice(1)
highestRatedEvent

#task 7
expensiveMerch <- avgPriceMerch %>%
  filter(avgPrice > 250)
expensiveMerch

#task 8
revenuePerEvent <- dfMerchSales %>%
  mutate(revenue = Price * Quantity) %>%
  group_by(Location) %>%
  summarise(totalRevenue = sum(revenue))
revenuePerEvent

#task 9
priceVariability <- dfMerchSales %>%
  group_by(MerchType) %>%
  summarise(priceSD = sd(Price)) %>%
  arrange(desc(priceSD)) %>%
  slice(1)
priceVariability

#task 10
lowestAttendance <- attendeesPerLocation %>%
  arrange(totalAttendees) %>%
  slice(1)
lowestAttendance

#task 11
oldestAvgAgeEvent <- avgAgePerLocation %>%
  arrange(desc(avgAge)) %>%
  slice(1)
oldestAvgAgeEvent

#task 12
correlationMerch <- dfMerchSales %>%
  group_by(MerchType) %>%
  summarise(correlation = cor(Price, Quantity))
correlationMerch

#task 13
consistentArtist <- dfArtistRatings %>%
  group_by(Artist) %>%
  summarise(ratingSD = sd(Rating)) %>%
  arrange(ratingSD) %>%
  slice(1)
consistentArtist

#task 14
itemsSoldPerEvent <- dfMerchSales %>%
  group_by(Location) %>%
  summarise(totalItems = sum(Quantity))
itemsSoldPerEvent

#task 15
diverseMerchEvent <- dfMerchSales %>%
  group_by(Location) %>%
  summarise(uniqueMerch = n_distinct(MerchType)) %>%
  arrange(desc(uniqueMerch)) %>%
  slice(1)
diverseMerchEvent
