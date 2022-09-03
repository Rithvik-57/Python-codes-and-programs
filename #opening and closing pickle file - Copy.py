#opening and closing pickle file 

import pickle
# char=['n','l','i','e']
# file='mchars.pkl'
# fileobj=open(file, 'wb')
# pickle.dump(char,fileobj)
# fileobj.close()

file='mchars.pkl'
fileobj=open(file,'rb')
mchar=pickle.load(fileobj)
print(mchar)
print(type(mchar))