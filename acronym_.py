def acronym(s):
    return ''.join([x[0] for x in s.split(' ')])

#here split(' ') will break all the words into a list.
#x[0] will take the first letters of all words.
#finally join will again convert it to a string from a list

print(acronym('The State Department'))
'TSD'

