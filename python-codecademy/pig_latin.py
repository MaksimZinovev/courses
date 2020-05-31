pyg = 'ay'
original = input('Enter a word:')
# string is not empty and contains only letter characters
if len(original) > 0 and original.isalpha():
  #transform to lower case
  word=original.lower()
  #move 1st letter to the end and add 'ay' suffix
  first=word[0]
  new_word=word+first+pyg
  new_word=new_word[1:len(new_word)]
  #print result
  print(new_word)
else:
  print('empty')
