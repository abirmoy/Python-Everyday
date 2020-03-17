
import re



document_word_list_num = open('word_list_num.txt', 'r')
text_string_word_list_num = document_word_list_num.readlines()


# CHINESE TRANSLATION
document_word_list_num_Chinese = open('word_list_num_Chinese.txt', 'r', encoding='utf8')
text_string_word_list_num_chinese = document_word_list_num_Chinese.readlines()
print(len(text_string_word_list_num_chinese))
print(type(text_string_word_list_num_chinese))

merge_text_file_num = open("merge_text_file_num.txt", "w", encoding='utf8')


for i in range(len(text_string_word_list_num_chinese)):
    merge_text_file_num.write(text_string_word_list_num_chinese[i] + text_string_word_list_num[i] + '\n')
    print(text_string_word_list_num_chinese[i] + text_string_word_list_num[i])
merge_text_file_num.close()