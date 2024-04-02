def StringReduction(string):
  string = list(string)
  stringSet = set(['a', 'b', 'c'])
  repeat = True
  while repeat:
    i = 0
    repeat = False
    while i < len(string) - 1:
      if string[i] != string[i + 1]:
        string[i:i+2] = list(stringSet - set([string[i], string[i+1]]))
        repeat = True
      else:
        i += 1
  return len(string)

# keep this function call here 
print(StringReduction(input()))
