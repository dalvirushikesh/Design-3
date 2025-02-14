#Time Complexity = O(n) 
# Space Complexity = O(d) d is depth of the nested list

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.result = []
        self.index = 0
        self.dfs(nestedList)
    def dfs(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.result.append(item.getInteger())
            else:
                self.dfs(item.getList())
    def next(self) -> int:
        if self.hasNext():
            val = self.result[self.index]
            self.index += 1
            return val
        return None
    def hasNext(self):
        return self.index < len(self.result)

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())