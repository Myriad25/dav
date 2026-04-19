# Install packages (run once)
install.packages("tidyverse")
install.packages("data.table")
install.packages("caret")

# Load libraries
library(tidyverse)    # includes dplyr, ggplot2, tidyr, readr
library(data.table)
library(caret)

# -------------------------------
# 1. Load Dataset
# -------------------------------
data <- read.csv("data.csv")

# -------------------------------
# 2. Data Cleaning (dplyr, tidyr)
# -------------------------------
clean_data <- data %>%
  filter(!is.na(age)) %>%             # remove NA values
  mutate(income = income * 1.1) %>%   # modify column
  select(age, income, gender)         # select columns

# -------------------------------
# 3. Data Summary
# -------------------------------
summary(clean_data)

# -------------------------------
# 4. Visualization (ggplot2)
# -------------------------------
ggplot(clean_data, aes(x = age, y = income)) +
  geom_point(color = "blue") +
  ggtitle("Age vs Income")

# -------------------------------
# 5. Using data.table (fast ops)
# -------------------------------
dt <- as.data.table(clean_data)

# Calculate average income by gender
dt[, .(avg_income = mean(income)), by = gender]

# -------------------------------
# 6. Machine Learning (caret)
# -------------------------------
# Split data into training and testing
set.seed(123)
trainIndex <- createDataPartition(clean_data$income, p = 0.8, list = FALSE)

trainData <- clean_data[trainIndex, ]
testData  <- clean_data[-trainIndex, ]

# Train a linear regression model
model <- train(income ~ age + gender, data = trainData, method = "lm")

# Predictions
predictions <- predict(model, newdata = testData)

# Model performance
postResample(predictions, testData$income)