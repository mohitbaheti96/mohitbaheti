
def getSquares(le,wid,count=0):
	if (le>0) and (wid>0):
		if le>wid:
			le=le-wid
			count=count+1
			count=getSquares(le,wid,count)
		else:
			wid=wid-le
			count=count+1	
			count=getSquares(le,wid,count)
	return count


l=int(raw_input('enter length:\t'))
b=int(raw_input('enter width:\t'))

print(getSquares(l,b))
