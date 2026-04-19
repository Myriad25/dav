# -----------------------------
# 1. Import Data
# -----------------------------
data <- read.csv("data.csv")

# -----------------------------
# 2. Basic Structure & Summary
# -----------------------------
str(data)
summary(data)

# -----------------------------
# 3. Correlation Analysis (numeric only)
# -----------------------------
# Select numeric columns
numeric_data <- data[, c("age", "income")]

# Correlation matrix
cor_matrix <- cor(numeric_data)
print(cor_matrix)

# -----------------------------
# 4. Scatter Plot (Age vs Income)
# -----------------------------
plot(data$age, data$income,
     main = "Age vs Income",
     xlab = "Age",
     ylab = "Income",
     col = "blue",
     pch = 19)

# Add regression line
abline(lm(income ~ age, data=data), col="red", lwd=2)

# -----------------------------
# 5. Pair Plot (Multiple Relationships)
# -----------------------------
pairs(numeric_data,
      main = "Pairwise Relationships",
      col = "darkgreen",
      pch = 19)

# -----------------------------
# 6. Boxplot (Income by Gender)
# -----------------------------
boxplot(income ~ gender, data = data,
        main = "Income by Gender",
        col = c("pink", "lightblue"))

# -----------------------------
# 7. Bar Plot (Average Income by Gender)
# -----------------------------
avg_income <- tapply(data$income, data$gender, mean)

barplot(avg_income,
        main = "Average Income by Gender",
        col = c("pink", "lightblue"),
        ylab = "Income")