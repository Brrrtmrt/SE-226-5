import random
import string
from collections import Counter
passwords = []
dict={}

print("Choose 5 characters (lowercase only) and assign 5 replacement options each:")
while True:
    if len(dict.keys())==5:
        break
    print("Enter a lowercase character:")
    tmp=input()
    dict[tmp]=set()
    while True:
        if len(dict[tmp])==3:
            break
        print("Enter a replacement for "+tmp)
        tmp2=input()
        dict[tmp].add(tmp2)
        
for i in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    password_list = list(password)
    for idx, ch in enumerate(password_list):
        if ch in dict:
            password_list[idx] = random.choice(tuple(dict[ch]))
    password = ''.join(password_list)
    passwords.append(password)

print(passwords)
       

categorized_passwords = {"strong": [], "weak": []}
bonus = {"strong": [], "weak": []}
for password in passwords:
        replaced_count = sum(1 for ch in password if any(ch in replacements for replacements in dict.values()))
        if replaced_count > 4:
            categorized_passwords["strong"].append(password)
        else:
            categorized_passwords["weak"].append(password)





   
    
    
    
    
    
    
    
    
    
