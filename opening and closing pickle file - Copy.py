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

#example iris

import pickle
with open('iris.txt') as f:
    data = f.read().splitlines()
# Pickling file
with open('iris.pkl', 'wb') as fileobj:
    pickle.dump(data, fileobj)

# Reading Pickled file as list
with open('iris.pkl', 'rb') as fileobj1:
    read = pickle.load(fileobj1)
print(read)