 Given a 2D matrix m, of just 0s and 1s,
 count the number of islands in the matrix.
 in this case an island is just a group of 1s or a 1 by itself.
 The 1s need to be connected either horizontally or vertically to count as an island.
 
 
 ```python
 from collection import deque
 
 def islandCount(m):
	if m==None or m == [[]]:
		return 0
	islands = 0
	c = len(m[0])
	r = len(m)
	for i in range(0,r):
		for j in range(0,c):
			if m[i][j]==1:
				islands ++
				findPairsOfIsland(m,i,j,r,c)
	return islands
 def findPairsOfIsland(m,i,j,r,c):
	q = deque()
	q.append([i,j])
	while(len(q)!=0):
		i = q.pop()
		x = i[0]
		y = i[1]
		if m[x][y]==1:
			m[x][y]=2
			appendIf(q,r,c,x+1,y)
			appendIf(q,r,c,x,y+1)
			appendIf(q,r,c,x-1,y)
			appendIf(q,r,c,x,y-1)
			
def appendIf(q,r,c,x,y):
	if(x>0 and x<c and y>0 and y<r):
		q.append(x,y)
 ```