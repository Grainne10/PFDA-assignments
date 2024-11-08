## Assignment 5 Risk
### Grainne Boyle
#Assignment Description: Write a program called risk.
# The program similates 1000 individual battle rounds using dice, \ each battle round is one shake of dice for the defender \ and one for the attacker.

# in each round, the attacked can put forward up to three of their troops and the defender can put up to two of their defending troops
# The top two dice are compared, if the attackers dice is the same or lower, \
# they lose one troop. If the defenders dice is the same or higher as the attackers,  the defender wins.

### come back to this to total the battle rounds


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

attacker_wins = 0
defender_wins = 0

attacker_wins_total = []  # Store total of attacker wins
defender_wins_total = []  # Store total of defender wins


for _ in range(n_battle):
    # Attacker rolls 3 dice
    attacker_rolls = np.sort(roll_dice(3))[::-1]  # Sort in descending order
    # Defender rolls 2 dice
    defender_rolls = np.sort(roll_dice(2))[::-1]  # Sort in descending order

# Simulate battle rounds
for _ in range(n_battle):
    # Attacker rolls 3 dice
    attacker_rolls = np.sort(roll_dice(3))[::-1]  # Sort in descending order
    # Defender rolls 2 dice
    defender_rolls = np.sort(roll_dice(2))[::-1]  # Sort in descending order

# Compare the highest rolls
    if attacker_rolls[0] > defender_rolls[0]:
        attacker_wins += 1
    else:
        defender_wins += 1

# Compare the second highest rolls
    if attacker_rolls[1] > defender_rolls[1]:
        attacker_wins += 1
    else:
        defender_wins += 1

    
# Total up each roll
attacker_wins_total.append(attacker_wins)
defender_wins_total.append(defender_wins)


print(f"The number of Wins by Attacker : {attacker_wins_total}")
print(f"The number of Wins by Defender : {defender_wins_total}")


if attacker_wins_total > defender_wins_total :
    print("The Attacker Wins")
elif defender_wins_total > attacker_wins_total :
    print("The Defender Wins")
else : 
    print("The battle ended in a draw")

fig, ax = plt.subplots()

ax.pie([attacker_wins, defender_wins], startangle=90 )

# Add individual win counts in the center of the pie chart
plt.text(-0.5, 0.2, f'Attacker: {attacker_wins}', ha='center', fontsize=10, fontweight='bold')
plt.text(0.5, -0.2, f'Defender: {defender_wins}', ha='center', fontsize=10, fontweight='bold')


plt.axis('equal')  
plt.title('Results of Battle ')



plt.show()

# matplotlib.figure.Figure(figsize=None, dpi=None, *, facecolor=None, edgecolor=None, linewidth=0.0, frameon=None, subplotpars=None, tight_layout=None, constrained_layout=None, layout=None, **kwargs)[source]




# Research:

# https://github.com/Ryota-Kawamura/Mathematics-for-Machine-Learning-and-Data-Science-Specialization/blob/main/Course-3/Week-2/C3_W2_Lab_2_Dice_Simulations.ipynb
# https://www.geeksforgeeks.org/how-to-get-the-n-largest-values-of-an-array-using-numpy/
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html

