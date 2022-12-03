""" A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited. """

def solution(A):
    # write your code in Python 3.8.10
    prefix_sum = [0] * len(A)
    prefix_sum[0] = A[0]

    for i in range(1, len(A)):
        prefix_sum[i] = prefix_sum[i-1] + A[i]

    min_avg = float('inf')
    avg = 0
    min_index = 0
    past_sum = 0

    for i in range(len(prefix_sum)-1):
        if i < len(prefix_sum) - 2:
            avg = min((prefix_sum[i+1] - past_sum) / float(2), (prefix_sum[i+2] - past_sum) / float(3))
        else:
            avg = (prefix_sum[i+1] - past_sum)/ float(2)

        if avg < min_avg:
            min_avg = avg
            min_index = i

        past_sum += A[i]

    return min_index

    pass