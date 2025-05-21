# 155. Min Stack
# https://leetcode.com/problems/min-stack/

class MinStack(object):
# Stack:LIFO 
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        
        

    def push(self, val):
      self.stack.append(val)

      if not self.min_stack or val<=self.min_stack[-1]:
        self.min_stack.append(val)
        

    def pop(self):
        val=self.stack.pop()
        if val==self.min_stack[-1]:
            self.min_stack.pop()
       
        

    def top(self):
       return  self.stack[-1]
        
        

    def getMin(self):
       return self.min_stack[-1]
        


