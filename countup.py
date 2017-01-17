def countup(n):
    if n == 0:
    	print('blastoff!')
    else:
        countup(n-1)
        print(n)	
countup(3)