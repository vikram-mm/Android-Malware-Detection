import cPickle

common_dict = cPickle.load( open( "15IT201_15IT217_M1_common_dict_300.save", "rb" ) )

for k in sorted(common_dict.keys()):
	
	print k

print len(common_dict)
print type(common_dict)
