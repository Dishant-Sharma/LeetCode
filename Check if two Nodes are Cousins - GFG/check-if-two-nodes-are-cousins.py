#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
# Returns true if the nodes with values 'a' and 'b' are cousins. Else returns false
def isCousin(root, a, b):
  
    parent=[a,b]
    levels=[a,b]
   
        # 0th index of these two lists will be representing parent of x and level of x while 1st index of these two lists will be representing parent of y and level of y
  
    findParentandLevels(root,Node(-1),0,a,b,parent,levels)
        # here Node(-1) is currentParent which is a dummy node as we cant pass null for root node as its value would be null which is not the case and 0 is currentLevel
    if parent[0] != parent[1] and levels[0] == levels[1]:
        return 1
    else:
        return 0


def findParentandLevels(root,currentParent,currentLevel,x,y,parent,levels):
    if root is None:
        return
        
    if root.data == x:
        parent[0]=currentParent.data
        levels[0]=currentLevel

    if root.data == y:
        parent[1]=currentParent.data
        levels[1]=currentLevel
        
    # if root.data == x:
    #     parent.append(currentParent.data)
    #     levels.append(currentLevel)

    # if root.data == y:
    #     parent.append(currentParent.data)
    #     levels.append(currentLevel)


    findParentandLevels(root.left,root,currentLevel+1,x,y,parent,levels)
    findParentandLevels(root.right,root,currentLevel+1,x,y,parent,levels)
        # calls to left child and right child
    
    return parent,levels
   
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        n1,n2=list(map(int,input().split()))
        ans=isCousin(root,n1,n2)
        if ans:
            print(1)
        else:
            print(0)
        
# } Driver Code Ends