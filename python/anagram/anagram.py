def find_anagrams(word, candidates):
    ret_list = []
    word_list = list(word.lower())
    word_list.sort()
    for i in candidates:
        comp_list = list(i.lower())
        comp_list.sort()
        if word_list == comp_list:
            if word.lower() != i.lower():
                ret_list.append(i)
    return ret_list
