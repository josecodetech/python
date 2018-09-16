#variable local / global
#global
variable='global'
def local():
	#local
	variable='local'
	print('variable dentro ='+variable)
local()
#valor global
print('variable fuera ='+variable)
