# Write a Python Program to implement Min-Max Algorithm.

import math


def minimax(curDepth, nodeIndex,
            maxTurn, scores,
            targetDepth):

    # base case : targetDepth reached
    if (curDepth == targetDepth):
        return scores[nodeIndex]

    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2,
                           False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                           False, scores, targetDepth))

    else:
        return min(minimax(curDepth + 1, nodeIndex * 2,
                           True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                           True, scores, targetDepth))


# Driver code
# Terminal Node Values
scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.ceil(math.log(len(scores), 2))
print(math.log(len(scores), 2))
print(treeDepth)
print(math.ceil(2.9))

print("The optimal value is : ", end="")
print(minimax(0, 0, False, scores, treeDepth))
