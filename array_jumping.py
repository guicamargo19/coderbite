def ArrayJumping(arr):

  def direita(length, index, number):
    left = number % length
    if left > index:
      left = length + index - left
    else:
      left = index - left
    return left

  def esquerda(length, index, number):
    right = number % length
    if right > length - index - 1:
      right = right + index -length
    else:
      right = right + index
    return right


  size = len(arr)
  maxIndex = arr.index(max(arr))
  ss = {}

  for i in range(size):
    ss[i] = (direita(size, i, arr[i]), esquerda(size, i , arr[i]))

  if maxIndex in ht[maxIndex]:
    return 1
  
  travelSet = set(ss[maxIndex])

  for step in range(2, size+1):
    for value in tuple(travelSet):
      travelSet.add(ss[value][0])
      travelSet.add(ss[value][1])
    if maxIndex in travelSet:
      return step
  return -1
  
print(ArrayJumping(input()))
