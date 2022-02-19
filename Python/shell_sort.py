# https://www.geeksforgeeks.org/shellsort/
"""
Shell sorting is a very interesting sorting method which basically uses insertion sort
 to sort elements. So if it uses insertion sort then how it is better than insertion sort?
 Well that's the interesting part. To get the intuition, shell sort applies insertion sort
 first to small sequences of largely interleaved elements which makes the array kind of
 partially sorted and then it repeatedly reduces the interleaving between the elements of
 sequence and reapplies insertion sort untill we get the sorted array. Already confused ?
 don't worry, It is lot to grasp in one sentence.

Problem with insertion sort
Insertion sort is a great algorithm, because it’s very intuitive and it is easy to implement,
 but the problem is that it makes many exchanges for an element which is very far from its
 correct place. Thus these elements may slow down the performance of insertion sort a lot.
 That is why in 1959 Donald Shell proposed an algorithm that tries to overcome this problem
 by comparing items of the list that lie far apart

Description
First lets define h-sorted list. We say a list is h-sorted if starting from any
 position every hth element is in sorted order. For e.g. 2 1 4 3 is 2-sorted list
 while 3 1 2 4 is not since starting from initial position every second element i.e.
 3 and 2 is not in sorted order.

Shell sort takes a gap sequence (lets call it gap_seq). This sequence must be a decreasing
 sequence and must end with 1. Now for each element gap_seq[i] in the gap sequence, shell
 sorts makes the array gap_seq[i] sorted by sorting every gap_seq[i] interleaved elements.

How to choose gap size
Not a cool thing about Shell sort is that we’ve to choose “the perfect” gap sequence for
 our list. However this is not an easy task, because it depends a lot of the input data.
 The good news is that there are some gap sequences proved to be working well in the general cases.

Shell Sequence
Donald Shell proposes a sequence that follows the formula FLOOR(N/2k),
 then for N = 1000, we get the following sequence: [500, 250, 125, 62, 31, 15, 7, 3, 1]
    Shell sequence for N=1000: (500, 250, 125, 62, 31, 15, 7, 3, 1)

Pratt Sequence
Pratt proposes another sequence that’s growing with a slower pace than the Shell’s sequence.
 He proposes successive numbers of the form 2p3q or [1, 2, 3, 4, 6, 8, 9, 12, …].

Pratt sequence: (1, 2, 3, 4, 6, 8, 9, 12, ...)
Knuth Sequence
 Knuth in other hand proposes his own sequence following the formula (3k – 1) / 2 or 
 [1, 4, 14, 40, 121, …]

Knuth sequence: (1, 4, 13, 40, 121, ...)

Of course there are many other gap sequences, proposed by various developers and
 researchers, but the problem is that the effectiveness of the algorithm strongly
 depends on the input data.
"""

def shell_sort(arr, gaps):
    length = len(arr)
    for gap in gaps:
        for i in range(gap, length):
            j = i
            while j>=gap and arr[j-gap]>arr[j]:
                arr[j-gap], arr[j] = arr[j], arr[j-gap]
                j = j-gap
    return arr

def main():
    arr = [16, 86, -36, 29, 70, -42, 36, -38, -67, 23, -74, -56, -84, 59, 22, -31, -61, -49, -81, -1, 30, -20, -98, -3, 80, -29, 81, -58, -100, -94, -93, -14, 48, 79, -9, -43, 6, 9, -65, -7, -12, 39, -21, -40, 26, -19, -73, 92, -82, 77]
    gaps = [9, 7, 5, 3, 1]
    print(arr)
    shell_sort(arr, gaps)
    print(arr)

if __name__ == '__main__':
    main()
