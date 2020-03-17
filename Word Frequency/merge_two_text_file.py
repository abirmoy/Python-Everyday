
import re



document_word_list_alphabet = open('word_list_By_alphabet.txt', 'r')
text_string_word_list_alphabet = document_word_list_alphabet.readlines()


# CHINESE TRANSLATION
document_word_list_alphabet_chinese = open('word_list_by_alphabet_Chinese.txt', 'r', encoding='utf8')
text_string_word_list_alphabet_chinese = document_word_list_alphabet_chinese.readlines()
print(len(text_string_word_list_alphabet_chinese))
print(type(text_string_word_list_alphabet_chinese))

merge_text_file_alphabet = open("merge_text_file_alphabet.txt", "w", encoding='utf8')


for i in range(len(text_string_word_list_alphabet_chinese)):
    merge_text_file_alphabet.write(text_string_word_list_alphabet_chinese[i] + text_string_word_list_alphabet[i] + '\n')
    print(text_string_word_list_alphabet_chinese[i] + text_string_word_list_alphabet[i])
merge_text_file_alphabet.close()