{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1195a442-e1c5-448e-88ab-58ba0ca4fe4d",
   "metadata": {},
   "source": [
    "# EXPERIMENT 3 - PYTHON DATA ANALYSIS (PANDAS)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f7509b8-29cc-43cc-b352-d63a783c793a",
   "metadata": {},
   "source": [
    "### PROBLEM 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0e45ccd3-e663-4f8a-ba51-4facc687d977",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd # Import the pandas library for data analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "dbed879a-4d5e-4c71-be5b-b0197a8628ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load CSV file\n",
    "cars = pd.read_csv(\"cars.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "73edb067-3d30-449b-b32b-cf8e93a6ed60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The first 5 rows with odd-numbered columns:\n",
      "               Model  cyl   hp     wt  vs  gear\n",
      "0          Mazda RX4    6  110  2.620   0     4\n",
      "1      Mazda RX4 Wag    6  110  2.875   0     4\n",
      "2         Datsun 710    4   93  2.320   1     4\n",
      "3     Hornet 4 Drive    6  110  3.215   1     3\n",
      "4  Hornet Sportabout    8  175  3.440   0     3\n"
     ]
    }
   ],
   "source": [
    "# a. Display the first 5 rows with odd-numbered columns (1, 3, 5, 7…)\n",
    "# iloc[:5, ::2] → take the first 5 rows, and select every 2nd column starting from index 0\n",
    "print(\"The first 5 rows with odd-numbered columns:\")\n",
    "print(cars.iloc[:5, ::2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6926b490-0162-49f1-a9bc-120c4271a073",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The row with Mazda RX4:\n",
      "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
      "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4\n"
     ]
    }
   ],
   "source": [
    "# b. Display the row that contains the Model 'Mazda RX4'\n",
    "# Use boolean indexing to filter rows where Model == 'Mazda RX4'\n",
    "print(\"The row with Mazda RX4:\")\n",
    "print(cars[cars['Model'] == 'Mazda RX4'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c6618b20-4100-4408-8512-b7a04e1194d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cylinders of Camaro Z28: 8\n"
     ]
    }
   ],
   "source": [
    "# c. How many cylinders ('cyl') does the car model 'Camaro Z28' have?\n",
    "# loc[] selects rows by condition, then 'cyl' column; values[0] extracts the single value\n",
    "cyl_camaro = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]\n",
    "print(\"Cylinders of Camaro Z28:\", cyl_camaro)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5b7dd1d4-46ae-40e0-937c-f3f4d352743d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cylinders and Gear type for selected models:\n",
      "             Model  cyl  gear\n",
      "1    Mazda RX4 Wag    6     4\n",
      "18     Honda Civic    4     4\n",
      "28  Ford Pantera L    8     5\n"
     ]
    }
   ],
   "source": [
    "# d. Show cylinders ('cyl') and gear type ('gear') for specific models\n",
    "# isin() checks if the 'Model' column contains any of the given models\n",
    "models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']\n",
    "print(\"Cylinders and Gear type for selected models:\")\n",
    "print(cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
