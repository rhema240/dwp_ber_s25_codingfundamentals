scores = [15, 19, 17, 12, 17, 13]
print("Scores = [15, 19, 17, 12, 17, 13]")
#print the first score
print("First score is", scores[0])
#print the last score
print("Last score",scores[-1])
#print the highest score
print("The highest score is",max(scores))
#print the lowest score
print("The lowest score is", min(scores))
#add 21 to the list
scores.append(21)
print("The new list", scores)
#arrange scores in ascending order
scores.sort()
print(scores)
#remove 17
scores.remove(17)
print(scores)

#Muiltiply each figure by 2
for score in scores:
    print(score*2)

#To print the lists step by step
double_scores= []
for score in scores:
    double_scores.append(score*2)
    print(double_scores)

#To print the list in one line


total= 0

for s in scores:
    total= total + s
    print(total)