


document = open('BJTU- Proff & Associate Proff Email.txt', 'r', encoding='utf8').readlines()
document_mod = open("BJTU- Proff & Associate Proff Email_mod.txt", "w", encoding='utf8')
print(len(document))
print(type(document))



for i in range(len(document)):
    document_mod.write(document[i].strip()+ '\n')
    print(document[i].strip())
document_mod.close()
