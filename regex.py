import re


pattern = "022213"

# if re.match(pattern, "022213"):
#     print("Match found")
# else:    
#     print("No match found")
result = 'match' if re.fullmatch(pattern, "022213") else 'no match'
print(result)

text = "abc123def456ghi789"
s = re.sub(r'\d+', '-', text)
print(s)  
r = re.sub(r'[a-zA-Z]','1',text)
print(r)

q= re.split(r'\d+',text)
print(q)

t= re.search(r'\d+', text)
print(t.group())

w = re.findall(r'\d+', text)
print(w)

