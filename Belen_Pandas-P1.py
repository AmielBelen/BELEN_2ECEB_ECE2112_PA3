{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2a8305fe-7bce-4794-ad81-c6a9e52ccb27",
   "metadata": {},
   "source": [
    "# EXPERIMENT 3 - PYTHON DATA ANALYSIS (PANDAS)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51460f2c-f97f-418c-9a35-6b89fc570d7a",
   "metadata": {},
   "source": [
    "### PROBLEM 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e7c6be43-6598-4dd1-8768-4e41e84918e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd # Import the pandas library for data analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0e830f64-2589-45f5-9b7c-0b989823131c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# First, load the CSV file\n",
    "cars = pd.read_csv(\"cars.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cdb5e600-fe52-4b52-92dd-209982f9239a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The First 5 Rows:\n",
      "               Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \\\n",
      "0          Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4   \n",
      "1      Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4   \n",
      "2         Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4   \n",
      "3     Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3   \n",
      "4  Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3   \n",
      "\n",
      "   carb  \n",
      "0     4  \n",
      "1     4  \n",
      "2     1  \n",
      "3     1  \n",
      "4     2  \n"
     ]
    }
   ],
   "source": [
    "# Then, display the first 5 rows\n",
    "print(\"The First 5 Rows:\")\n",
    "\n",
    "print(cars.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e03ba6e8-84e3-4d3c-b386-e1be640d95fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Last 5 Rows:\n",
      "             Model   mpg  cyl   disp   hp  drat     wt  qsec  vs  am  gear  \\\n",
      "27    Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.9   1   1     5   \n",
      "28  Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.5   0   1     5   \n",
      "29    Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.5   0   1     5   \n",
      "30   Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.6   0   1     5   \n",
      "31      Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.6   1   1     4   \n",
      "\n",
      "    carb  \n",
      "27     2  \n",
      "28     4  \n",
      "29     6  \n",
      "30     8  \n",
      "31     2  \n"
     ]
    }
   ],
   "source": [
    "# Lastly, display the last 5 rows\n",
    "print(\"The Last 5 Rows:\")\n",
    "print(cars.tail())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed200bd1-cd04-4a36-9bfb-ce186120d2fe",
   "metadata": {},
   "outputs": [],
   "source": []
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
