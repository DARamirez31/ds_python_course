f=open("C:/Users/deisy/PycharmProjects/ds_python_course/1_python_basics/10_file_handling/funny.txt","r")
for line in f:
    print(line)
f.close()
# Open a file in read mode and print each line

with open("C:/Users/deisy/PycharmProjects/ds_python_course/1_python_basics/10_file_handling/funny.txt", "r") as f:
    lines = f.readlines()
    print(lines)
# Open a file in read mode and print all lines at once

with open ("love.txt", "w") as f:
    f.write ("I love Python\n")
    f.write ("I love programming\n")
# Open a file in write mode and write multiple lines

with open ("love.txt", "a") as f:
    f.write ("I love data science\n")
    f.write ("I love machine learning\n")
# Open a file in append mode and add more lines

with open ("love.txt", "w") as f:
    f.writelines(["I love data\n",
                 "I love machine learning\n",
                 "I love artificial intelligence\n"])
# Open a file in write mode and write a list of lines

player_scores = {}

with open ("C:/Users/deisy/PycharmProjects/ds_python_course/1_python_basics/10_file_handling/scores.csv","r") as f:
    for line in f:
        player, _, score = line.strip().split(",") #underscore is used to ignore the second value
        score= int(score) # Convert score to integer
        if player in player_scores:
            player_scores[player].append(score) # Append score to existing dictionary entry
        else:
            player_scores[player] = [score] # Create new dictionary entry for player

print(player_scores)

# Calculate the average score for each player
for player, scores in player_scores.items():
    average_score = sum(scores) / len(scores)
    print(f"{player}: {average_score:.2f}")

# remove a file

import os
if os.path.exists("love.txt"):
    os.remove("love.txt")
    print("File deleted successfully")
else:
    print("The file does not exist")