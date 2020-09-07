# import pandas as pd

# filepath = "Resources/election_data.csv"

# election_df = pd.read_csv(filepath)

# #print(election_df.head())

# # print(len(election_df["Candidate"].unique()))
# # print(election_df["Candidate"].value_counts().index[0])
# # print(election_df["Candidate"].value_counts().sum())
# # print(election_df["Candidate"].value_counts()[0])

# total_votes = election_df["Candidate"].value_counts().sum()

# for i in range(len(election_df["Candidate"].unique())):
#     candidate = election_df["Candidate"].value_counts().index[i]
#     num_votes = election_df["Candidate"].value_counts()[i]
#     percent_vote = num_votes / total_votes
#     print(f"{candidate}: {percent_vote:.2f}({num_votes})")

# print("Winner: " + election_df["Candidate"].value_counts().max())

import os
import csv

electionpath = os.path.join(".", "Resources", "election_data.csv")

with open(electionpath) as electionfile:
    csv_reader = csv.reader(electionfile, delimiter = ",")

    csv_header = next(csv_reader)

    database = {}
    total_votes = 0

    for row in csv_reader:

        name = row[2]

        total_votes += 1

        if name not in database:
            database[name] = 1
        else:
            database[name] += 1

print("Election Results")

print(f"Total Votes: {total_votes}")

for candidate in database:
        print(f"{candidate}: {database[candidate]}({database[candidate]/total_votes:.2f})")

print(f"Winner: {max(database, key = database.get)}")

