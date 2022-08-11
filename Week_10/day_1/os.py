import os

for i in range(1, 6):
    os.mkdir(f'Week{i}')
    for j in range(1, 6):
        os.makedirs(f'Week{i}/Day{j}/lesson')
        os.mkdir(f'Week{i}/Day{j}/homework')



