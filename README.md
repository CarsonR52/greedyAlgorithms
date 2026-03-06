# Cache Eviction Algorithms FIFO/LRU/OPTFF Assignment

## Information
Carson Reis 
UFID: 18459067

## Overview
This program simulates three cache eviction policies:

FIFO (First-In, First-Out)
LRU (Least Recently Used)
OPTFF (Belady's Farthest-in-Future)

The program reads an input file - > runs the 3 policies - > prints the number of cache misses for each

## File Structure:

greedyAlgorithm/
README.md
src/ -> cache_simulator.py
data/ -> ex.in, ex.out, error1.in, error2.in, file1.in, file2.in, file3.in, test2.in, test2.out
tests/ -> notes.txt


## Written Component:

Question 1:

Input File  |   k   |   m   |   FIFO    |   LRU     |   OPTFF   |

File 1      |   3   |   54  |   50      |   50      |   32      |

File 2      |   4   |   60  |   58      |   56      |   33      |

File 3      |   3   |   54  |   46      |   44      |   28      |



Does OPTFF have the fewest misses?
How does FIFO compare to LRU?

Within the 3 test files, OPTFF has the fewest misses. This makes sense due to OPTFF knowing
the full future request sequence. It can always just evict the item that's next use is the furthest away. 
FIFO/LRU performed worse comparatively between all the other files. They exactly tied
in file 1, but LRU did a little better in file 2 and file 3 compared to FIFO. LRU can occasionally
do better than FIFO, but still, OPTFF is still seemingly the best overall.

Question 2: 

Using ex.in data,

3 12
1 2 3 4 1 2 5 1 2 3 4 5

The miss counts were 9 for FIFO, 10 for LRU, and 7 for OPTFF. 

To answer the question asked: yes, there is such a sequence that exists for which OPTFF incurs
strictly fewer misses than LRU or FIFO. For k = 3, the sequence above gives OPTFF strictly fewer 
misses than both LRU and FIFO. On this sequence, FIFO has 9 misses while LRU has 10, and OPTFF has 7.
This occurs due to OPTFF using its knowledge of future requests to, before evicting an item, checking which
item's next use is the furthest down the line. FIFO/LRU only make their decision on eviction solely 
based on past history.

Question 3:

Let OPTFF be Belady’s Farthest-in-Future algorithm.

Let ( A ) be any offline algorithm that knows the full request sequence.

Prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence

Answer:

OPTFF is optimal due to the fact that, whenever there is a miss that happens and the cache is
full, it evicts the item whose next use is the farthest into the future. Suppose some other offline algorithm, A, is
making a different choice at that step and evicts an item that'll be used sooner. Algorithm A is keeping
an item that isn't needed as soon and throwing away one that is needed earlier than that. Replacing algorithm A's
choice with the choice OPTFF would've made can't make the result worse, due to the item OPTFF evicts being
the safest one to remove at that moment. Whenever another offline algorithm disagrees with OPTFF, we can change the
algorithm to match OPTFF at that step without therefore increasing the total number of misses within that algorithm.
By continuing to do this step by step, repeating this argument over and over, it will turn any optimal
offline algorithm into OPTFF without making it worse. Thus, OPTFF has no more misses than any other offline
algorithm, and it must be optimal.


## Implementation explanation:

The program reads the cache size and request sequence from an input file. It then simulates FIFO, LRU, and OPTFF
algorithms all separately and counts the number of misses for each policy. FIFO uses a queue and a set, so the oldest
inserted item can be evicted when it's needed. LRU uses an OrderedDict, which makes it easy to move recently used items
to the end and evict the least recently used item from the front. OPTFF preprocesses the future positions of each request
using a dictionary of queues, so whenever a miss occurs and the cache is full, it evicts the cached item that's next use
is farthest in the future, or that never appears again.

How to run:

After downloading all data files, run them as follows:

Windows PowerShell:
py src/cache_simulator.py data/<filename>.in

Linux/macOS:
python3 src/cache_simulator.py data/<filename>.in

To reproduce `ex.out`, run:

Within powershell:

py src/cache_simulator.py data/ex.in

Expected output:
FIFO  : 9
LRU   : 10
OPTFF : 7

Where <filename> is to be replaced with a .in file from /data, such as file1.in.

## Assumptions and dependencies
- Python 3 is a requirement
- No external libraries are required beyond the Python standard library
- Input files have exactly two lines
- Cache size must satisfy `k >= 1`
- First line contains `k m`
- Second line contains exactly `m` integer requests
