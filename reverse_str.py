def reverseString(testString):
  str = ""
  for i in testString:
    str = i + str
  return str
 
testString = input()
print(reverseString(testString))
