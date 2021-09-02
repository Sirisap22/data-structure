print("*** Election ***")
n = int(input("Enter a number of voter(s) : "))
votes = map(int, list(input().split(' ')))
count = {}
for v in votes:
  if v > 20 or v <= 0:
    continue
  if (v not in count.keys()):
    count[v] = 1
  else:
    count[v] += 1 

if len(count) == 0:
  print("*** No Candidate Wins ***")
else:
  print(max(count, key=count.get))