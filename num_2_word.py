def num_2_word (n):
    n = str(n)
    result = []
    main = {'1':'one', '2':'two', '3':'three','4':'four','5':'five','6':'six', '7':'seven','8':'eight','9':'nine','0':'zero'}
    for i in n:
        word = main.get(i)
        result.append(word)
    s = ' '
    s = s.join(result)
    print (s)
        
num_2_word (4721)
        