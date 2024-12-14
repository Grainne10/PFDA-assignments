## Assignment 5 Risk
### Grainne Boyle
#Assignment Description: Write a program called risk.
# The program similates 1000 individual battle rounds using dice, \ each battle round is one shake of dice for the defender \ and one for the attacker.

# in each round, the attacked can put forward up to three of their troops and the defender can put up to two of their defending troops
# The top two dice are compared, if the attackers dice is the same or lower, \
# they lose one troop. If the defenders dice is the same or higher as the attackers,  the defender wins.


import numpy as np
import matplotlib.pyplot as plt

# Define the 6 sided dice
n_sides = 6

# Represent a dice using a numpy array
dice = np.array([i for i in range(1, n_sides+1)])


def roll_dice(n):
    return np.random.choice(dice, size=n, replace=True)
# Define how many battle rounds

# number of Battles

n_battle = 1000



attacker_total = 0
defender_total = 0
tie_total = 0
#Defn: Battle Round is a complete single dice roll comparison.
#Defn: attacker/defender_wins is the number of times attacker/defender won a single die face-value comparison.
# Simulate battle rounds
for _ in range(n_battle):
    attacker_wins = 0 #reset the wins to zero after each dice roll.
    defender_wins = 0
    # Attacker rolls 3 dice
    attacker_rolls = np.sort(roll_dice(3))[::-1]  # Sort in descending order
    # Defender rolls 2 dice
    defender_rolls = np.sort(roll_dice(2))[::-1]  # Sort in descending order
    for i in range(2):
        if attacker_rolls[i] > defender_rolls[i]:
            attacker_wins += 1
        else:
            defender_wins += 1
    if defender_wins & attacker_wins:
        tie_total+=1
    else:
        if defender_wins == 0:
            attacker_total+=1
        else:
            defender_total+=1
    

            
   

print(f"The number of Wins by Attacker : {attacker_total}")
print(f"The number of Wins by Defender : {defender_total}")
print(f"The number of draws : {tie_total}")



if attacker_total > defender_total :
    print("The Attacker won the most.")
elif defender_total > attacker_total :
    print("The Defender won the most.")
else : 
    print("Neither won the most.")

fig, ax = plt.subplots()

ax.pie([attacker_total, defender_total, tie_total],colors=['Pink', 'cyan', 'skyblue'], startangle=90 )

# Add individual win counts in the center of the pie chart
plt.text(-0.5, 0.2, f'Attacker: {attacker_total}', ha='center', fontsize=10, fontweight='bold')
plt.text(0.25, -0.5, f'Defender: {defender_total}', ha='center', fontsize=10, fontweight='bold')
plt.text(0.5, 0, f'Ties: {tie_total}', ha='center', fontsize=10, fontweight='bold')

plt.axis('equal')  
plt.title('Results of Battle ')

plt.savefig('../img/battle_results.png')
plt.show()

# matplotlib.figure.Figure(figsize=None, dpi=None, *, facecolor=None, edgecolor=None, linewidth=0.0, frameon=None, subplotpars=None, tight_layout=None, constrained_layout=None, layout=None, **kwargs)[source]




# Research:

# https://github.com/Ryota-Kawamura/Mathematics-for-Machine-Learning-and-Data-Science-Specialization/blob/main/Course-3/Week-2/C3_W2_Lab_2_Dice_Simulations.ipynb
# https://www.geeksforgeeks.org/how-to-get-the-n-largest-values-of-an-array-using-numpy/
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html

