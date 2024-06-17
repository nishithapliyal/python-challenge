import os
import pandas as pd
import csv

election = pd.read_csv('Resources/election_data.csv') #read in csv using pd.read_csv
totalvotes = len(election.index) # total votes in dataset
candidates = election['Candidate'].unique().tolist() #the candidates of the election stored in a list


def votecounts(x): #define a function that will calculate the number and percentage of votes each candidate got
    candidate_name = candidates[x] #get the candidate name 
    votes = len(election[election['Candidate'] == candidate_name]) #see how many votes the candidate got
    votes_percentage = round(100*votes/totalvotes,3) #find the percentage
    return votes, votes_percentage

votes = []
vote_percentages = []

for i in range(len(candidates)): #iterate through the list of candidates 
    results = votecounts(i) #use the function defined above - the result is a series
    votes.append(results[0]) #results[0] has the total votes per candidate
    vote_percentages.append(results[1]) #results[1] has the total vote percentage per candidate
    
winner = candidates[votes.index(max(votes))] #find the number of max votes and match that to the candidate

print('Election Results')
print('-------------------------')
print(f'Total Votes: {totalvotes}')
print('-------------------------')
print(f'{candidates[0]}: %{vote_percentages[0]} ({votes[0]})')
print(f'{candidates[1]}: %{vote_percentages[1]} ({votes[1]})')
print(f'{candidates[2]}: %{vote_percentages[2]} ({votes[2]})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

results = os.path.join('analysis','results.txt') #create txt file
        
with open(os.path.join('analysis','results.txt'), 'w') as file:
#write all the info in using new lines and change all variables to string date types
    file.write('Election Results'+'\n')
    file.write('-------------------------' + '\n')
    file.write('Total Votes: ' + str(totalvotes) + '\n')
    file.write('-------------------------' + '\n')
    file.write(str(candidates[0]) + ': %' + str(vote_percentages[0]) + ' (' + str(votes[0]) + ')' + '\n')
    file.write(str(candidates[1]) + ': %' + str(vote_percentages[1]) + ' (' + str(votes[1]) + ')' + '\n')
    file.write(str(candidates[2]) + ': %' + str(vote_percentages[2]) + ' (' + str(votes[2]) + ')' + '\n')
    file.write('-------------------------' + '\n')
    file.write('Winner: ' + str(winner) + '\n')
    file.write('-------------------------')