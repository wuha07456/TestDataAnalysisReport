import random
import string
a=string.ascii_letters+string.digits
key=[]
def Random_str():
	key=random.sample(a,5)
	keys="".join(key)
	return keys

