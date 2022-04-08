"""
QN: https://www.hackerrank.com/challenges/new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1from 1at the front of the line to nat the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if n = 8 and Person 5 bribes Person 4,the queue will look like this:

"""


def minimumBribes(q):
    bribes = 0
    q = [i-1 for i in q]
    for i, o in enumerate(q):
        cur = i

        if o - cur > 2:
            print("Too chaotic")
            return
        
        for k in q[max(o - 1, 0):i]:
            if k > o:
                bribes += 1

    print(bribes)


t = int(input("Enter number of test cases: "))
n = list(map(int, input("Enter list separated by space: ").strip().split()))
print(minimumBribes(n))
