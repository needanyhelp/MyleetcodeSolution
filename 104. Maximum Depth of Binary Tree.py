import collections

class TreeNode:
    def __init__(self, InputVal=None, leftInput=None, rightInput=None):
        self.val = InputVal
        self.left = leftInput
        self.right = rightInput

    
def solution(startNode):

    queue=collections.deque([startNode])

    visited=[]
    visited.append(startNode)
    depth=0

    while queue:
        depth+=1
        for _ in range(len(queue)):
            next = queue.popleft()
            if next.left and next.left not in visited:
                queue.append(next.left)
                visited.append(next.left)
            if next.right and next.right not in visited:
                queue.append(next.right)
                visited.append(next.right)


    print(depth)


if __name__ =='__main__':
    fourth=TreeNode(15)
    fifth=TreeNode(7)   
    second=TreeNode(9)
    third=TreeNode(20,fourth,fifth)
    first=TreeNode(3,second,third)
    
        
    solution(first)     

