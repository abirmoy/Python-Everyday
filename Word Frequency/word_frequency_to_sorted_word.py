# https://code.tutsplus.com/tutorials/counting-word-frequency-in-a-file-using-python--cms-25965
import re

  
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
document_text = open('test.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
word_frequency =[]
word_list_alphabet =[] # WORDS FOR SORTING by ALPHABET
word_list_num =[] # WORDS FOR SORTING BbyY NUMBER

text_file_alphabet = open("word_list_alphabet.txt", "w", encoding='utf8')
text_file_num = open("word_list_num.txt", "w", encoding='utf8')

for words in frequency_list:
    
    # ## deffault tutorial
    word_frequency.append(words)
    word_frequency.append(frequency[words])    
    # print(words, frequency[words])

    # SAVE AS LIST FOR SORTING
    # by ALPHABET
    order_alphabet = str(words) + '-' + str(frequency[words]) + '\n'
    word_list_alphabet.append(order_alphabet)

    # by NUMBER
    order_num = str(frequency[words]) + '-' + str(words)  +  '\n'
    word_list_num.append(order_num)

# SORTING LIST
word_list_alphabet.sort()
word_list_num.sort(reverse=True)


## WRITING WORD TO THE FILE
text_file_alphabet.write(listToString(word_list_alphabet))
text_file_alphabet.close()

text_file_num.write(listToString(word_list_num))
text_file_num.close()

