import numpy as np

#sequence_1 = input("Enter sequence 1:")
#sequence_2 = input("Enter sequence 2:")


## Testing for smaller sequences. Fails when priority is given to left gap
# sequence_2 = "CGTG"
# sequence_1 = "GACT"


## Fails when priority is given to diagonal matching
sequence_2 = "GACTGCT"
sequence_1 = "GACTGGCTAGTTCAGTCTGACTGGCTAGCTA"

main_matrix = np.zeros((len(sequence_1)+1,len(sequence_2)+1))
match_checker_matrix = np.zeros((len(sequence_1),len(sequence_2)))

# Defining the scoring matrix
match_reward = 1
mismatch_penalty = -1
gap_penalty = -2

# Initialising the match_checker_matrix which keeps tracks of all the matches
for i in range(len(sequence_1)):
    for j in range(len(sequence_2)):
        if sequence_1[i] == sequence_2[j]:
            match_checker_matrix[i][j]= match_reward
        else:
            match_checker_matrix[i][j]= mismatch_penalty

#print(match_checker_matrix)

#STEP 1 : INITIALISATION
## Matrix is already initialised with zeroes so no need of initialistaion

#STEP 2 : MATRIX FILLING
for i in range(1,len(sequence_1)+1):
    for j in range(1,len(sequence_2)+1):

        # Matrix filling by comparing all three possible cases
        # Converted all negative values to zero using the max function
        main_matrix[i][j] = max(max(main_matrix[i][j-1]+ gap_penalty, 0), max(main_matrix[i-1][j]+gap_penalty, 0), max(main_matrix[i-1][j-1]+match_checker_matrix[i-1][j-1], 0))

print(main_matrix, '\n')

# STEP 3 : TRACEBACK

## For local alignment

def traceback(s1, s2, x, y):

    aligned_1 = ''
    aligned_2 = ''

    while (x > 0 and y > 0 and main_matrix[x][y] != 0):

        if (x >0 and y > 0 and main_matrix[x][y] == main_matrix[x-1][y-1]+ match_checker_matrix[x-1][y-1]):

            aligned_1 = sequence_1[x-1] + aligned_1
            aligned_2 = sequence_2[y-1] + aligned_2

            x = x - 1
            y = y - 1

        elif(x > 0 and main_matrix[x][y] == main_matrix[x-1][y] + gap_penalty):
            aligned_1 = sequence_1[x-1] + aligned_1
            aligned_2 = "-" + aligned_2

            x = x -1
        else:
            aligned_1 = "-" + aligned_1
            aligned_2 = sequence_2[y-1] + aligned_2

            y = y - 1

    return aligned_1, aligned_2


max_value = np.max(main_matrix)
max_positions = np.argwhere(main_matrix == max_value)
#print(max_positions)

for max_position in max_positions:
    x, y = max_position
    aligned_1, aligned_2 = traceback(sequence_1, sequence_2, x,y)
    print(f'Algined Sequences:')
    print(x,y)
    print(aligned_1)
    print(aligned_2)

## for global alignment (Comparing with Needleman-Wunsch)

# aligned_1 = ''
# aligned_2 = ''

# ti = len(sequence_1)
# tj = len(sequence_2)

# # when diagonal matching or unmatching is giving priroity. Which means in the case where all three values are zero, we take the diagonal value which results in a match or mismtach. But this gives inconsitent results in some cases.
# while(ti > 0 and tj > 0):

#     # Comparing for gap from upper side
#     if(ti > 0 and max(main_matrix[ti][tj] == main_matrix[ti-1][tj] + gap_penalty,0)):
#         aligned_1 = sequence_1[ti-1] + aligned_1
#         aligned_2 = "-" + aligned_2

#         ti = ti -1

#     # Comparing for gap from left side
#     elif (tj > 0 and max(main_matrix[ti][tj] == main_matrix[ti][tj-1] + gap_penalty,0)):
#         aligned_1 = "-" + aligned_1
#         aligned_2 = sequence_2[tj-1] + aligned_2

#         tj = tj - 1

#     # Comparing for diagonal match or mismatch (Base case : given priority in case all three values are negative)
#     else:
#         aligned_1 = sequence_1[ti-1] + aligned_1
#         aligned_2 = sequence_2[tj-1] + aligned_2

#         ti = ti - 1
#         tj = tj - 1


# when priority is given to the left gap. Which means in the case where all three values are zero, we take the left value leading to a gap. But this gives inconsitent results in some cases.
# while(ti > 0 and tj > 0):

#     if (ti > 0 and tj > 0 and max(main_matrix[ti][tj] == main_matrix[ti-1][tj-1] + match_checker_matrix[ti-1][tj-1],0)):

#         aligned_1 = sequence_1[ti-1] + aligned_1
#         aligned_2 = sequence_2[tj-1] + aligned_2

#         ti = ti - 1
#         tj = tj - 1

#     elif(ti > 0 and max(main_matrix[ti][tj] == main_matrix[ti-1][tj] + gap_penalty,0)):
#         aligned_1 = sequence_1[ti-1] + aligned_1
#         aligned_2 = "-" + aligned_2

#         ti = ti -1
#     else:
#         aligned_1 = "-" + aligned_1
#         aligned_2 = sequence_2[tj-1] + aligned_2

#         tj = tj - 1
#     print(aligned_1)
#     print(aligned_2)


print(aligned_1)
print(aligned_2)
