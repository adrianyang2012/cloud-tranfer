import sys
file = "example.txt"
with open(file,"r") as data:
  words = data.readlines()
words = words.split()
donotwant = ["virus"]
for i in range(0,len(donotwant):
  while donotwant[i] in words:
    words.remove("donotwant")
print(data)
print(words)
