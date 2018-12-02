import math
letterCounts = []

while True:
  solution = 0
  letterCounts = []
  newWord = []
  
  try:
      word = input()
  except EOFError:
     break
   
  for x in word:
    if x not in newWord:
      newWord.append(x)
  #print(newWord)
        
  for x in newWord:
    letterCounts.append(word.count(x))
        
  solution = math.factorial(len(word))
  
  for i in range(len(letterCounts)):
      solution //= math.factorial(letterCounts[i])
      
  print(solution)
