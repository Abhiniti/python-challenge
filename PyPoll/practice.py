from collections import Counter

cnt = Counter()
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
count = 0
for word in colors:
    if word == 'red':
        count += 1
print(count)