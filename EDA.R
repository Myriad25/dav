# -----------------------------
# 1. Import Data
# -----------------------------
data <- read.csv("data.csv")

# View data
print(data)
head(data)

# -----------------------------
# 2. Check Missing Values (NA)
# -----------------------------
colSums(is.na(data))

# No NA in your dataset, but just in case:
data_clean <- na.omit(data)

# -----------------------------
# 3. Summary Statistics
# -----------------------------
summary(data_clean)
str(data_clean)

# -----------------------------
# 4. Scatter Plot (Age vs Income)
# -----------------------------
plot(data_clean$age, data_clean$income,
     main = "Age vs Income",
     xlab = "Age",
     ylab = "Income",
     col = "blue",
     pch = 19)

# -----------------------------
# 5. Histogram (Age Distribution)
# -----------------------------
hist(data_clean$age,
     main = "Distribution of Age",
     xlab = "Age",
     col = "green",
     border = "black")

# -----------------------------
# 6. Histogram (Income Distribution)
# -----------------------------
hist(data_clean$income,
     main = "Distribution of Income",
     xlab = "Income",
     col = "lightblue",
     border = "black")

# -----------------------------
# 7. Boxplot (Income)
# -----------------------------
boxplot(data_clean$income,
        main = "Income Distribution",
        col = "orange",
        horizontal = TRUE)

# -----------------------------
# 8. Boxplot by Gender
# -----------------------------
boxplot(income ~ gender, data = data_clean,
        main = "Income by Gender",
        col = c("pink", "lightblue"))