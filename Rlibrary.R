# Install dplyr if not already installed (run once)
  if (!require(dplyr)) {
      install.packages("dplyr")
      library(dplyr)
      }
      
# Filter rows where mpg > 20
  filtered_data <- mtcars %>%
      filter(mpg > 20)
  print(filtered_data)
  
# Select mpg and hp columns
  selected_data <- mtcars %>%
      select(mpg, hp)
  print(selected_data)
  
# Create new column: weight in kilograms
  mutated_data <- mtcars %>%
      mutate (wt_kg = wt * 453.592 / 1000 )
  print(mutated_data)
