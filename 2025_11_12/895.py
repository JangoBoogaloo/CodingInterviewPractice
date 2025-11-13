# https://leetcode.com/problems/maximum-frequency-stack/description/
"""
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

* FreqStack() constructs an empty frequency stack.
* void push(int val) pushes an integer val onto the top of the stack.
* int pop() removes and returns the most frequent element in the stack.
  * If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.


stk = [0, 1, 2, 3, 4]

freqStk = [0, 1, 2, 2, |2, 3, 3, 4, 2] 
    2 = freqStk.pop()
    3 = 

    
freqCounter[val] = (freq++, node*)

MRU = double linked list


"""

class FreqStack:

    # MRU node is in the end
    class Node:
        def __init__(self):
            pass
        
    class DLList:
        def __init__(self):
            pass

    def __init__(self):
        self.freqCounter = defaultdict(int)
        self.dll = self.DLList()
        return

    def push(self, val: int) -> None:
        
        # if val exists
        if val in self.freqCounter:
            
            # find the freq and node
            freq, node = self.freqCounter[val]
            freq += 1

            # update dllist
            self.DLList.remove(node)
            self.DLList.append(node) # add to the end of the dll

            
        else: # val not exists
            node = self.Node()

            self.freqCounter[val] = (1, node)
            self.DLList.append(node)
        return

    def pop(self) -> int:

        max(self.freqCounter, lambda x: x[0])

        return -1