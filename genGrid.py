import random
from config import rows, cols
amount_of_obstacles_per_20 = 14

print(2)
for i in range(rows):
    for j in range(cols):
        temp = random.randint(1, 20)
        if (j == 0 and i == 0 or j == cols-1 and i == rows-1) or temp <= amount_of_obstacles_per_20:
            print("-", end=" ")
        else:
            print("#", end=" ")
    print("")