with open('ospd.txt') as inf:
    with open('ospd5.txt','w') as outf:
        for line in inf:
            if len(line) == 6:
                outf.writelines(line)


