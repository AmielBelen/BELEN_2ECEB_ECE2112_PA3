# Experiment 3 - Python Data Analysis (Pandas)  

This repository contains my solutions for **Experiment 3** in Advanced Computer Programming and Algorithms. The experiment focuses on **using the Pandas library for data analysis**, specifically on tasks such as loading datasets, slicing, filtering rows, and subsetting columns.  

## Table of Contents  
- [Problem 1](#problem-1)  
- [Problem 2](#problem-2)  
- [Results](#results)  

### Code Files  
- [View Problem 1 Code](./Belen_Pandas-P1.py)  
- [View Problem 2 Code](./Belen_Pandas-P2.py)  

---

## Problem 1  

In this first problem, I was required to load the dataset `cars.csv` into a Pandas DataFrame and then display both the first five and the last five rows. To start, I imported the Pandas library using `import pandas as pd`, which is the standard convention. I then used the function `pd.read_csv("cars.csv")` to load the dataset and assigned it to a variable called `cars`. This created a DataFrame containing all the data from the file.  

```python
import pandas as pd # Import the pandas library for data analysis

# First, load the CSV file
cars = pd.read_csv("cars.csv")
```

Once the data was loaded, I displayed the first five rows to quickly preview the beginning of the dataset. I did this with the `.head()` method, which by default shows the first five rows. I also included a print statement to label the output for clarity.  

```python
# Then, display the first 5 rows
print("The First 5 Rows:")
print(cars.head())
```

After checking the start of the dataset, I also needed to show the last five rows. For this, I used the `.tail()` method, which by default prints the last five rows of the DataFrame. Just like before, I added a print statement so the output would be properly labeled.  

```python
# Lastly, display the last 5 rows
print("The Last 5 Rows:")
print(cars.tail())
```

This problem was mainly about confirming that I could correctly load the dataset into Pandas and access its rows. By using `.head()` and `.tail()`, I was able to explore both the start and end of the dataset, which is often the first step in any data analysis workflow.  

---

## Problem 2  

For the second problem, I had to extract specific pieces of information from the `cars` dataset using subsetting, slicing, and indexing.  

The first step was to display the first five rows but only the odd-numbered columns. To achieve this, I used the `.iloc` method because it allows selecting rows and columns by position. I wrote `cars.iloc[:5, ::2]`, where `:5` selects the first five rows and `::2` selects every second column starting at index 0. This matched the requirement for odd-numbered columns (1, 3, 5, … in human counting).  

```python
# a. Display the first 5 rows with odd-numbered columns (1, 3, 5, 7…)
# iloc[:5, ::2] → take the first 5 rows, and select every 2nd column starting from index 0
print("The first 5 rows with odd-numbered columns:")
print(cars.iloc[:5, ::2])
```

Next, I needed to find the row containing the model **Mazda RX4**. I approached this by filtering the DataFrame with a condition. Using `cars['Model'] == 'Mazda RX4'`, I created a boolean mask that marks the matching row as `True`. By applying this mask inside the DataFrame, I was able to display only the row corresponding to Mazda RX4.  

```python
# b. Display the row that contains the Model 'Mazda RX4'
# Use boolean indexing to filter rows where Model == 'Mazda RX4'
print("\nRow with Mazda RX4:")
print(cars[cars['Model'] == 'Mazda RX4'])
```

After that, I had to determine how many cylinders the model **Camaro Z28** has. I used the same idea of filtering, but this time I focused only on the `cyl` column. With `cars.loc[cars['Model'] == 'Camaro Z28', 'cyl']`, I isolated the cylinder values for Camaro Z28. Since the result was still a Series, I extracted the actual number using `.values[0]`. This gave me the answer, which was 8 cylinders.  

```python
# c. How many cylinders ('cyl') does the car model 'Camaro Z28' have?
# loc[] selects rows by condition, then 'cyl' column; values[0] extracts the single value
cyl_camaro = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]
print("\nCylinders of Camaro Z28:", cyl_camaro)
```

Finally, I needed both the cylinder count and gear type for three specific models: Mazda RX4 Wag, Ford Pantera L, and Honda Civic. To do this, I created a list of these models and used the `.isin()` method on the `Model` column, which allowed me to filter rows where the model matched any in my list. Then, I selected only the columns `Model`, `cyl`, and `gear` using `.loc`. This gave me a neat table showing just the information required for the three models.  

```python
# d. Show cylinders ('cyl') and gear type ('gear') for specific models
# isin() checks if the 'Model' column contains any of the given models
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print("\nCylinders and Gear type for selected models:")
print(cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']])
```

Through these steps, I was able to practice combining slicing for structured selections, boolean conditions for filtering specific rows, and membership testing for checking multiple models at once. Together, these approaches covered the essential Pandas skills needed for Problem 2.  

---

## Results  

### Problem 1 Output  
- Displayed the **first 5 rows** of the dataset.  
- Displayed the **last 5 rows** of the dataset.  

### Problem 2 Output  
- **a.** Displayed the first 5 rows with odd-numbered columns.  
- **b.** Found the full row of **Mazda RX4**.  
- **c.** Determined that the **Camaro Z28** has `8` cylinders.  
- **d.** Displayed the cylinders and gear types for the selected models:  
  - Mazda RX4 Wag → 6 cylinders, 4 gears  
  - Honda Civic → 4 cylinders, 4 gears  
  - Ford Pantera L → 8 cylinders, 5 gears  

---

This experiment highlights practical Pandas operations: loading datasets, exploring rows, filtering data, and extracting subsets of information.  
