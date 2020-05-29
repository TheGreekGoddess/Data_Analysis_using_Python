# Import modules for creating file paths across operating systems and reading CSV files
import os
import csv

# Map the path where the input csv file is located
# Open the csv file
csvpath = os.path.join("Resources","election_data.csv");
with open(csvpath) as csvfile:

    # Specify the delimiter for the election_data.csv file
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Read the header of the election_data.csv file
    csv_header = next(csvreader)

    # Define the variables needed for the Election Results summary and set them all as zero so we add to them as the loop parses through the election_data.csv file 
    total_votes = 0
    winning_vote_count = 0
    winning_candidate = ""

    # Considering I do not know how many candidates are running, I have created a blank dictionary to hold the candidate names and the count of votes they each received
    candidate_vote_counts = {}

    # Initiate the loop to analyse each record contained in the election_data.csv file
    for data in csvreader:
        if data[2] in candidate_vote_counts.keys():
            candidate_vote_counts[data[2]] = candidate_vote_counts[data[2]] + 1
        else:
            candidate_vote_counts[data[2]] = 1

        # Count each row of data towards total votes cast
        total_votes += 1

    # Print the requested Election Results summary to the console
    print (f"----------------------------")
    print (f"Election Results")
    print (f"----------------------------")
    print (f"Total Votes:", total_votes)
    print (f"----------------------------")
    
    # Calculate the votes and the percentage of total votes that each candidate received
    for candidate_name in candidate_vote_counts.keys():
        percentage_of_votes = candidate_vote_counts[candidate_name]/total_votes*100
        text_percentage = "{number:.3f}".format(number = percentage_of_votes)
        print (candidate_name + ": " + text_percentage + "% (" + str(candidate_vote_counts[candidate_name])+ ")")

        # Determine which candidate received the maximum votes and declare the corresponding candidate as the winner
        if winning_vote_count < candidate_vote_counts[candidate_name]:
            winning_vote_count = candidate_vote_counts[candidate_name]
            winning_candidate = candidate_name 

    print (f"----------------------------")
    print (f"Winner: ", winning_candidate)
    print (f"----------------------------")

# Create a text file to publish the Election Results summary as requested
output = "Election_Results.txt"

# Open the text file using "write" mode to publish the Election Results summary results as requested
with open(output, 'w') as textfile:
    textfile.write (f"----------------------------")
    textfile.write (f"\nElection Results")
    textfile.write (f"\n----------------------------")
    textfile.write (f"\nTotal Votes: " + str(total_votes))
    textfile.write (f"\n----------------------------")

    for candidate_name in candidate_vote_counts.keys():
        percentage_of_votes = candidate_vote_counts[candidate_name]/total_votes*100
        text_percentage = "{number:.3f}".format(number = percentage_of_votes)
        textfile.write (f"\n" + str(candidate_name) + ": " + str(text_percentage) + "% (" + str(candidate_vote_counts[candidate_name])+ ")")

    textfile.write (f"\n----------------------------")
    textfile.write (f"\nWinner: " + (winning_candidate))
    textfile.write (f"\n----------------------------")