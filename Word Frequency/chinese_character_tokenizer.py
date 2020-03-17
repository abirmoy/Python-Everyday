# ### SOURCE https://github.com/fxsjy/jieba
import jieba

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

def concat(list, symbol='\n'):
    '''
        This function takes a list and concatenates '\n' after each item in the list
        Input: list
        Return: list    
    '''
    concatenated_list = []
    for i in list:
        word = str(i) + symbol
        concatenated_list.append(word)
    return concatenated_list




def tokenize(name_file_to_tokenize, name_tokenized_file='Tokenized_word.txt'):
    ''' 
        This function takes a chinese document and returns a file that contains words in the document
        Input: Name of the file to Tokenize, 
        Output: Tokenized word document
    '''
    # LOADING THE DOCUMENT AS STRING #
    document_text = open(name_file_to_tokenize, 'r', encoding='utf8')
    text_string = document_text.read()
    # TOKENIZING CHARECTERS #
    jieba.enable_paddle()
    seg_list = list(jieba.cut_for_search(text_string))  # cut_all=True finds all possible combination
    # ADDING NEW LING AFTER EACH WORD #
    tokenized_words = concat(seg_list, '\n')
    # SAVING AS TEXT FILE #
    text_file_alphabet = open(name_tokenized_file, 'w', encoding='utf8')
    text_file_alphabet.write(listToString(tokenized_words))
    text_file_alphabet.close()
    print(f'Task complete, Tokenized file saved as {name_tokenized_file}')




file_to_tokenize = 'UG_Chinese.txt'
name_tokenized_file = 'Tokenized_word.txt'

# tokenizing
tokenize(file_to_tokenize, name_tokenized_file)


# # LOADING THE DOCUMENT AS STRING #
# document_text = open('UG_Chinese.txt', 'r', encoding='utf8')
# text_string = document_text.read()


# # TOKENIZING CHARECTERS #
# jieba.enable_paddle()
# seg_list = list(jieba.cut_for_search(text_string))  # cut_all=True finds all possible combination

# # ADDING NEW LING AFTER EACH WORD #
# tokenized_words = concat(seg_list, '\n')


# # SAVING AS TEXT FILE #
# text_file_alphabet = open("Tokenized_word.txt", "w", encoding='utf8')
# text_file_alphabet.write(listToString(tokenized_words))
# text_file_alphabet.close()