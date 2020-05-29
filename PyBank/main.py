# Import modules for creating file paths across operating systems and reading CSV files
import os
import csv

# Map the path where the input csv file is located
csvpath = os.path.join("Resources","budget_data.csv");

# Open the csv file
with open(csvpath) as csvfile:

    # Specify the delimiter for the budget_data.csv file
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Read the header of the budget_data.csv file
    csv_header = next(csvreader)

    # Define the variables needed for the Financial Analysis summary and set them all as zero so we add to them as the loop parses through the budget_data.csv file    
    total_months = 0
    current_revenue = 0
    prior_revenue = 0
    total_revenue = 0
    change_in_revenue = 0
    total_change_in_revenue = 0
    highest_change_in_revenue = 0 
    lowest_change_in_revenue = 0

    # Initiate the loop to analyse each record contained in the budget_data.csv file
    for data in csvreader:

        # As the loop goes through the current revenues and add each occurence to the total revenue
        current_revenue = int(data[1])
        total_revenue = total_revenue + current_revenue
        change_in_revenue = current_revenue - prior_revenue

        # Calculate the change in revenue from the second month onwards by setting the below condition
        if total_months != 0:            
            total_change_in_revenue = total_change_in_revenue + change_in_revenue
        
        # Calculate if the change in revenue in a particular row is greater than the value recorded against this variable so far
        if highest_change_in_revenue < change_in_revenue:
            
        # If the latest change in revenue is greater than the value recorded against this variable so far, record this value as the newest highest change in revenue
            highest_change_in_revenue = change_in_revenue

            # Look for the corresponding month and year with the highest revenue
            highest_change_in_revenue_month_and_year = data[0]      

        # If the latest change in revenue is lesser than the value recorded against this variable so far, record this value as the newest lowest change in revenue
        if lowest_change_in_revenue > change_in_revenue:

        # Calculate if the change in revenue in a particular row is lesser than the value recorded against this variable so far
            lowest_change_in_revenue = change_in_revenue

            # Look for the corresponding month and year with the lowest revenue            
            lowest_change_in_revenue_month_and_year = data[0]            
        
        # Capture the current month's revenue as the previous month's revenue for future loop iterations
        prior_revenue = current_revenue

        # Count each row of revenue data towards total months
        total_months +=1

    # Divide the overall change in revenue by the total months
    # To arrive at the average for the net count of months that have recorded a change in revenue, I have deducted 1 on account of the first month
    average_change = str(round(total_change_in_revenue/(total_months-1),2))

    # Publish the Financial Analysis summary to the terminal as requested
    print (f"----------------------------------------------------")
    print (f"Financial Analysis")
    print (f"----------------------------------------------------")
    print (f"Total Months:", total_months)
    print (f"Total: $", total_revenue) 
    print (f"Average Change: $", average_change)
    print (f"Greatest Increase in Profits:",highest_change_in_revenue_month_and_year,"($",highest_change_in_revenue,")")
    print (f"Greatest Decrease in Profits:",lowest_change_in_revenue_month_and_year,"($",lowest_change_in_revenue,")")
    print (f"----------------------------------------------------")

# Create a text file to publish the Financial Analysis summary as requested
output = "Financial_Analysis.txt"

# Open the text file using "write" mode to publish the Financial Analysis summary results as requested
with open(output, 'w') as textfile:
    textfile.write (f"----------------------------------------------------")
    textfile.write (f"\nFinancial Analysis")
    textfile.write (f"\n----------------------------------------------------")
    textfile.write (f"\nTotal Months: " + str(total_months))
    textfile.write (f"\nTotal: ${total_revenue}")
    textfile.write (f"\nAverage Change:${average_change}")
    textfile.write (f"\nGreatest Increase in Profits: {highest_change_in_revenue_month_and_year} (${highest_change_in_revenue})")
    textfile.write (f"\nGreatest Decrease in Profits: {lowest_change_in_revenue_month_and_year} (${lowest_change_in_revenue})")
    textfile.write (f"\n----------------------------------------------------")