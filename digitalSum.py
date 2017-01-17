def digitalSum(n):
	if n < 10:
		return n
	else:
	    return(n % 10 + digitalSum(n // 10))	


num = int(input("Enter a number: "))
if num >= 1:
      print("The digit sum of", num, "is", digitalSum(num))	    
