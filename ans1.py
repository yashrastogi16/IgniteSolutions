str1=str(raw_input("Enter any string"))
str2 = ""
delimiters = [" ", ",", ";", ".", "\n"]
i = 0
for j in range(1, len(str1)):
    if str1[j] in delimiters:
        str2 += str1[i:j][::-1] + str1[j]
        i = j+1
    elif j==len(str1)-1:
        str2 += str1[i:j+1][::-1]

print str2
