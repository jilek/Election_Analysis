# The data we need to retrieve.
# 1. The total number of votes cast
# 2. The complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
import csv
import os

file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    print(election_data)
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
    #     print(row)


# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("------------------------\n")
#     txt_file.write("Arapahoe\n")
#     txt_file.write("Denver\n")
#     txt_file.write("Jefferson\n")
