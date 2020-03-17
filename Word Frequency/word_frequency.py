# https://code.tutsplus.com/tutorials/counting-word-frequency-in-a-file-using-python--cms-25965
import re
import json

def listToString(s):  
    # Function to convert 

    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1

frequency = {}
document_text = open('PG_English.txt', 'r', encoding='utf-8')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
word_frequency =[]
word_list_alphabet =[] # STORING WORDS FOR SORTING
text_file = open("Output.txt", "w", encoding='utf8')
for words in frequency_list:
    
    # ## for save as text
    text_file.write(str(frequency[words])+"  -")
    text_file.write(str(words) + '\n')

    # ## deffault tutorial
#     word_frequency.append(words)
#     word_frequency.append(frequency[words])    
#     # print(words, frequency[words])

#     # SAVE AS LIST FOR SORTING
#     a = str(words) + '-' + str(frequency[words]) + '\n'
#     word_list_alphabet.append(a)

# # print(word_frequency)
# # print(word_list_alphabet.sort())
# print(word_list_alphabet)


# text_file.write(listToString(word_list_alphabet))


text_file.close()