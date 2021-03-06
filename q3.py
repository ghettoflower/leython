#Let A be an array of n elements (that is, the elements of A are A[0], . . . , A[n−1]).
#An element A[i] is extreme if the following conditions hold regarding A[i]:
#   A[i] is not the first nor the last element of A. That is, 0 < i < n – 1
#   and either A[i − 1] < A[i] > A[i + 1] or A[i − 1] > A[i] < A[i + 1]. For
#   example, the extreme points of an array [0, 5, 3, 6, 8, 7, 15, 9] are
#   5, 3, 8, 7, 15. 

#Write an algorithm that prints the extreme points of the given array. If
#there are no extreme points, the algorithm prints “SORTED”. Do you
#agree that an array has no extreme points if and only if it is sorted?
#Explain your answer.

numlist = [1, 2, 3, 4, 5, 6]
list2 = [0, 5, 3, 6, 8, 7, 15, 9]

#EXTREME = TRUE if i != 0 and i != n-1

def find_extreme(A):
    result = [] #list that will hold the extreme points
  
   #for i in range(1, len(A) - 1) works too
    for i in range(len(A) - 1):
        if (i == 0) or i == (len(A) - 1):
            continue
        if (A[i] > A[i-1] and A[i] > A[i+1]) or (A[i] < A[i-1] and A[i] < A[i+1]):
            result.append(A[i])    
        else:
            continue      

    if result: #Means "if result contains any data"
        print("The extreme points are", result)
    if not result: #Empty lists are considered false
        print("SORTED")

find_extreme(numlist)
print("Now time for list 2. Output should be 5, 3, 8, 7, 15")
find_extreme(list2)