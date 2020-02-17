# import library
import os
import csv
# define csv file path
poll_csv = os.path.join("/Users/shui/Desktop/BSC/UT-TOR-DATA-PT-01-2020-U-C-Master/03-Python/Instructions/python-challenge/PyPoll/Resources/election_data.csv")
# open and read the csv file line by line
with open(poll_csv,'r') as csvfile:
    csvheader = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter = ",")
# create list variables
    candidates = []
# populate the candidates list and find the total votes
    for row in csvreader:
        candidates.append(row[2])
        total_votes = len(candidates)

# print the title block in the terminal
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")

# build a unordered list of unique items
    candidate = set(candidates)
# create a dictionary variable with the candidate names and votes
    summary_result = {}
    for i in candidate:
        summary_result[i] = candidates.count(i)
# extract the names and votes in the dictionary with the descending order of votes
    for key, value in sorted(summary_result.items(),key = lambda x: x[1],reverse = True):
        candidate_vote = value
        candidate_name = key
        candidate_vote_percentage = round(value/total_votes*100,2)
        winning_count = max(summary_result.values())
        winning_candidate = [key for key, value in summary_result.items() if value == winning_count]
        print(f"{candidate_name}: {candidate_vote_percentage}% ({candidate_vote})")   
# print the output in the terminal
    print(f"--------------------------")
    print(f"Winner: {winning_candidate[0]}")
    print(f"--------------------------")
    

# print the output as a text file
# alternatively using python main.py >> output.txt in the terminal 
txtfile_path = "/Users/shui/Desktop/BSC/UT-TOR-DATA-PT-01-2020-U-C-Master/03-Python/Instructions/python-challenge/PyPoll/output.txt"
with open(txtfile_path,"w") as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"-------------------------\n")
    for key, value in sorted(summary_result.items(),key = lambda x: x[1],reverse = True):
        candidate_vote = value
        candidate_name = key
        candidate_vote_percentage = round(value/total_votes*100,2)
        winning_count = max(summary_result.values())
        winning_candidate = [key for key, value in summary_result.items() if value == winning_count]
        txt_file.write(f"{candidate_name}: {candidate_vote_percentage}% ({candidate_vote})\n")  
    txt_file.write(f"--------------------------\n")
    txt_file.write(f"Winner: {winning_candidate[0]}\n")
    txt_file.write(f"--------------------------\n")
    txt_file.close()
    




# solution 1
    #candidate_1_vote = summary_result["Khan"]
    #candidate_2_vote = summary_result["Correy"]
    #candidate_3_vote = summary_result["Li"]
    #candidate_4_vote = summary_result["O'Tooley"]

    #candidate_1_percentage = round(float(candidate_1_vote/total_votes)*100,5)
    #candidate_2_percentage = round(float(candidate_2_vote/total_votes)*100,5)
    #candidate_3_percentage = round(float(candidate_3_vote/total_votes)*100,5)
    #candidate_4_percentage = round(float(candidate_4_vote/total_votes)*100,5)


#solution 2
    #candidate_1_vote = candidates.count("Khan")
    #candidate_2_vote = candidates.count("Correy")
    #candidate_3_vote = candidates.count("Li")
    #candidate_4_vote = candidates.count("O'Tooley")

#solution 3
    #candidate_1 = [candidate for candidate in candidates if candidate == "Khan"]
    #candidate_2 = [candidate for candidate in candidates if candidate == "Correy"]
    #candidate_3 = [candidate for candidate in candidates if candidate == "Li"]
    #candidate_4 = [candidate for candidate in candidates if candidate == "O'Tooley"]

    #candidate_1_vote = len(candidate_1) 
    #candidate_2_vote = len(candidate_2)
    #candidate_3_vote = len(candidate_3)
    #candidate_4_vote = len(candidate_4)