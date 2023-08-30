import re

with open ('Jobs.txt', 'r') as f:
    file_data = f.read()

list = re.split(r'\s', file_data)

word_counter={}

word_counter={}

for word in list:
    if word not in word_counter:
        word_counter[word] = 1
    else: 
        word_counter[word]+=1

sorted_ct = sorted(word_counter.items(), key = lambda x:x[1], reverse=True)
convert_ct = dict(sorted_ct)

ats_words = {k: v for k, v in convert_ct.items() if v > 1}

print(ats_words)