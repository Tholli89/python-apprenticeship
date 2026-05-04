text = "hello world hello python world world"

counts = {}

for word in text.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
