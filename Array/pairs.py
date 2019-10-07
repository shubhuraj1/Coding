def findpairs(A,B,X):
	for i in A:
		for j in B:
			if (i+j)==X:
				print(i,j)
			else:
				pass
	print("-1")
A=[1,2,4,5,7]
B=[5,6,3,4,8]
findpairs(A,B,9)					