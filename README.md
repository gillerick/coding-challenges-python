### Problems

1. [Time Delta](https://www.hackerrank.com/challenges/python-time-delta) [Medium]
2. [Word Order](https://www.hackerrank.com/challenges/word-order) [Medium]
3. [Runner Up Score](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list) [Easy]
4. [Words Score](https://www.hackerrank.com/challenges/words-score) [Medium]
5. [Birthday Cake Candles](https://www.hackerrank.com/challenges/birthday-cake-candles) [Easy]
6. [Mini Max Sum](https://www.hackerrank.com/challenges/mini-max-sum) [Easy]
7. [Time Conversion](https://www.hackerrank.com/challenges/time-conversion) [Easy]
8. [Fraudulent Activity Notifications](https://www.hackerrank.com/challenges/fraudulent-activity-notifications) [Medium]
9. [Text Wrap](https://www.hackerrank.com/challenges/text-wrap) [Easy]
10. [Merge the Tools](https://www.hackerrank.com/challenges/merge-the-tools) [Medium]
11. [Capitalize](https://www.hackerrank.com/challenges/capitalize) [Easy]
12. [Minimum Bribes](https://www.hackerrank.com/challenges/new-year-chaos) [Medium]
13. [Minimum Swaps 2](https://www.hackerrank.com/challenges/minimum-swaps-2) [Medium]
14. [Compare the Triplets](https://www.hackerrank.com/challenges/compare-the-triplets/) [Easy]
15. [An Interesting Game](https://www.hackerrank.com/challenges/an-interesting-game-1) [Medium]
16. [Two Sub-arrays](https://www.hackerrank.com/challenges/two-subarrays/) [Expert]
17. [Sherlock and Anagrams](https://www.hackerrank.com/challenges/sherlock-and-anagrams) [Medium]
18. [Hackerland Radio Transmitters](https://www.hackerrank.com/challenges/hackerland-radio-transmitters) [Medium]
19. [Minimum Loss](https://www.hackerrank.com/challenges/minimum-loss/) [Medium]
20. [Missing Numbers](https://www.hackerrank.com/challenges/missing-numbers) [Easy]
21. [Pairs](https://www.hackerrank.com/challenges/pairs/) [Medium]
22. [Sherlock and Arrays](https://www.hackerrank.com/challenges/sherlock-and-array) [Easy]
23. [Maximum Sub-array Sum](https://www.hackerrank.com/challenges/maximum-subarray-sum) [Hard]
24. [Compress the String](https://www.hackerrank.com/challenges/compress-the-string/) [Medium]
25. [Playing with Numbers](https://www.hackerrank.com/challenges/playing-with-numbers) [Hard]

#### DSA Designs

#### 1. Array-Based Stack Implementation (Data Structures & Algorithms in Python, page 234)

- The implementations for _top_, _is_empty_, and _len_ use constant time in the worst case. The O(1) time for push and
  pop are **amortized** bounds a typical call to either of these methods uses constant time, but there is occasionally
  an O(n)-time worst case, where n is the current number of elements in the stack, when an operation causes the list to
  resize its internal array.

#### 2. Reversing Data Using a Stack (Data Structures & Algorithms in Python, page 235)

- One technical detail worth noting is that we intentionally strip trailing newlines from lines as they are read, and
  then re-insert newlines after each line when writing the resulting file. The reason for doing this is to handle a
  special case in which the original file does not have a trailing newline for the final line.
- If we exactly echoed the lines read from the file in reverse order, then the original last line would be followed
  (without newline) by the original second-to-last line. In our implementation, we ensure that there will be a
  separating newline in the result.


