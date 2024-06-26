# Diamond Data Analysis Tool
Overview
This Python program provides a command-line interface for analyzing a dataset of diamonds. It allows users to perform various operations to gain insights into the diamond data provided in a CSV file.

# Features
The program supports the following operations, which can be selected from a menu:
•  Find Maximum Price: Determine the highest price of a diamond in the dataset.

•  Calculate Average Price: Compute the average price of all diamonds.

•  Count Ideal Diamonds: Count the number of diamonds with an 'Ideal' cut.

•  List Unique Colors: Display the number of unique diamond colors and list them.

•  Find Median Carat Size for Premium Diamonds: Calculate the median carat size of diamonds with a 'Premium' cut.

•  Average Carat Weight by Cut: Compute the average carat weight for each type of diamond cut.

•  Average Price by Color: Calculate the average price for each diamond color.

•  Exit: Terminate the program.

# How to Use
1. 
Ensure you have Python installed on your system.
2. 
Place your diamond data CSV file in the same directory as the program.
3. 
Run the program using the command python diamond_analysis.py.
4. 
When prompted, choose an action from the menu by entering the corresponding number.
5. 
The program will display the result of the selected operation.
6. 
To exit the program, select the 'Exit' option from the menu.

# CSV File Format
The CSV file should have the following columns:
•  price: The price of the diamond.

•  cut: The cut quality of the diamond (e.g., 'Ideal', 'Premium').

•  color: The color of the diamond.

•  carat: The carat weight of the diamond.

# Dependencies
•  csv: For reading CSV files.

•  enum: For creating the Operations enumeration.

•  rich: For enhanced console printing capabilities.

•  statistics: For calculating median values.

•  collections: For using defaultdict for aggregation tasks.

# Note
This program is designed for educational purposes and as a demonstration of basic data analysis operations in Python.