## Session 4 Assignment

- Write code to open the text file census_cost.txt and read all lines into a list named "line_list". Print line_list.
- Extract the first two lines and put them in a different list named "top2_list". You will need to use them later. Print the top2_list.
- Put the rest of the lines (containing useful data elements) in a new list named "data_list". Print data_list.
- Extract the column "Census Year" from data_list and assign them to a list named year_list. Remove the "" from the last element "2010". Print the cleansed year_list.
- Extract the "Total Population" column from the data_list and assign them to a list named "pop_list". Remove the "," from the numbers since Python doesn't recognize them. Print the cleansed "pop_list".
- Extract the "Census Cost" column from the data_list and assign them to a list named "cost_list". Remove the ",", and "$", and "Billion". Make sure to add the "0"s to the numbers from which you removed "Billion". Print the cleansed cost_list.
- Extract the "Average Cost per Person" column from the data_list and assign them to a list named "avg_list". Remove the "cents", and "$". Make sure to divide the numbers in cents by 100 so that all numbers are measured in dollar. Print the cleansed avg_list.
- Coalesce the cleansed data and save them to a text file named "census_cost.csv". The new file should look similar to the original source file except that it is in comma-delimited format and the numbers have been cleansed. The top two lines from the original file should be retained in the new file.
- Open the newly-created file "census_cost.csv", read all lines and display them. How does it look?
