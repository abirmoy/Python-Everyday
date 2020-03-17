import re

  
def listToString(s):  
    '''        
        This Function convert List Data Type to String String Data type
        Input: List
        Return: String
    ''' 

    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1


def find_frequency(file_name, save_file_name1='Chinese_word_list.txt', save_file_name2='word_list_sortby_num.txt'):
    '''
        pass
    '''
    print('*'*50 ,'\n\nTokenizing on progress....\n')
    document_text = open(file_name, 'r', encoding='utf8')
    text_string = document_text.readlines()
    # print(''.join(text_string))


    frequency = {}
    for word in text_string:
        # print(word)
        count = frequency.get(word,0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()
    word_list_alphabet =[] # WORDS FOR SORTING by ALPHABET
    word_list_num =[] # WORDS FOR SORTING By NUMBER

    
    # APPENDING WORDS INTO LIST ALONG WITH FREQUENCY
    for words in frequency_list:        
        # by ALPHABET
        order_alphabet = str(words.strip()) + '\t- ' + str(frequency[words]) + '\n'
        word_list_alphabet.append(order_alphabet)
        # by NUMBER
        order_num = str(frequency[words]) + ' - \t' + str(words.strip())  +  '\n'
        word_list_num.append(order_num)

    # SORTING LIST
    word_list_alphabet.sort()
    word_list_num.sort(reverse=True)


    ## WRITING WORDS TO THE FILE
    text_file_alphabet = open(save_file_name1, 'w', encoding='utf8')
    text_file_alphabet.write(listToString(word_list_alphabet))
    text_file_alphabet.close()

    text_file_num = open(save_file_name2, 'w', encoding='utf8')
    text_file_num.write(listToString(word_list_num))
    text_file_num.close()

    print('*'*50, f'\n\nTask complete, files saved as:\n{save_file_name1}\n{save_file_name2}\n\n', '*'*50)





file_name = 'Tokenized_word.txt'
save_file_name1 = 'Chinese_word_list.txt'
save_file_name2 = 'Chinese_word_sortby_num.txt'


# FINDING FREQUENCY
find_frequency(file_name, save_file_name1, save_file_name2)
