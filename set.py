my_str =('GitHub is an AI-powered developer platform that allows developers to create,'
            ' store, and manage their code.'
            ' It uses Git software, providing the distributed version control of Git plus access control,'
            ' bug tracking, software feature requests, task management, continuous integration, and wikis for every project.'
            'Headquartered in California, it has been a subsidiary of Microsoft since 2018.').lower()
#spliting words
my_words= my_str.split(" ")
my_words_set = set(my_words)

#count words
print(f"numbr of all words: {len(my_words)}")

#count unique word
print(f"numbr of unique words: {len(my_words_set)}")

#count tobe verb
my_dic = {'am': 0,'is':0 , 'are':0, 'was':0,'were':0}
total_tobe = 0
for item in my_words:
    if item in my_words_set:
        if item in ('am','is','are','was','were'):
            my_dic[item] +=1
            total_tobe +=1
print(f'Total to be words: {total_tobe}')
for key,value in my_dic.items():
    print(key,":",value)