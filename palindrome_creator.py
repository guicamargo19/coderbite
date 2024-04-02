def PalindromeCreator(strParam):
  if strParam == strParam[::-1]:
      return "palindrome"  

  def remove(strParam, letter, index):
      newString = []
      for i in range(len(strParam)):
          if strParam[i] != letter[index]:
              newString.append(strParam[i])
      return ''.join(newString)

  letters = ''.join(set(strParam))
  all_palindromes = {}

  for i in range(len(letters)):
      removed_1 = remove(strParam, letters, i)
      if removed_1 == removed_1[::-1]:
          all_palindromes[removed_1] = letters[i]

      letters_minus_1 = letters[:i] + letters[i+1:]
      for j in range(len(letters_minus_1)):
          removed_2 = remove(removed_1, letters_minus_1, j)
          if removed_2 == removed_2[::-1]:
              all_palindromes[removed_2] = letters_minus_1[j] + letters[i]

  if len(all_palindromes) < 1:
      return "not possible"
  else:
      longest_palindrome = sorted(all_palindromes.keys(), key=lambda x: len(x), reverse=True)[0]
      return "not possible" if len(longest_palindrome) < 3 else all_palindromes[longest_palindrome]


# keep this function call here 
print PalindromeCreator(raw_input())
