"""
Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

Example


-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The  hourglass sums are:

-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18
The highest hourglass sum is  from the hourglass beginning at row , column :

0 4 3
  1
8 6 6
Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Function Description

Complete the function hourglassSum in the editor below.

hourglassSum has the following parameter(s):

int arr[6][6]: an array of integers
Returns

int: the maximum hourglass sum
Input Format

Each of the  lines of inputs  contains  space-separated integers .

Constraints

Output Format

Print the largest (maximum) hourglass sum found in .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explanation

 contains the following hourglasses:

image

The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4


def main():
    a = [list(map(int, input().split())) for _ in range(6)]
    answer = -INF

    for i in range(1, 5):
        for j in range(1, 5):
            total = (sum(a[i - 1][j - 1: j + 2]) +
                     a[i][j] + sum(a[i + 1][j - 1: j + 2]))
            answer = max(answer, total)

    print(answer)
    
"""


def hourglassSum(arr):
    """
    Solution of hourglass
    """
    max_total = -63
    for i in range(4):
        for j in range(4):
            total = (
                arr[i][j]
                + arr[i][j + 1]
                + arr[i][j + 2]
                + arr[i + 1][j + 1]
                + arr[i + 2][j]
                + arr[i + 2][j + 1]
                + arr[i + 2][j + 2]
            )
            max_total = max(max_total, total)
    
    return max_total


ar = [
    [0, 2, 3, 4, 5, 6],
    [2, 1, 4, 9, 6, 7],
    [3, 4, 1, 6, 10, 8],
    [4, 0, 6, 7, 8, 9],
    [5, 6, 0, 8, 9, 10],
    [6, 7, 8, 9, 10, 11],
]
print(hourglassSum(ar))


TOTAL = 12

INF = 101
ANS = -INF
print(ANS)
print(max(ANS, TOTAL))
