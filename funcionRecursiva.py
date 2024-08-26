def finalcountdown(num):
	if num>0:
		print(num)
		num-=1
		finalcountdown(num)
finalcountdown(10)