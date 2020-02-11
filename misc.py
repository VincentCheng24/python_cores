with open('decrators.py') as fh:
    # count = 0
    # text = fh.read()
    # for character in text:
    #     if character.isupper():
    #         count += 1
    # print(count)

    cnt = sum([1 for line in fh for character in line if character.isupper()])
    print(cnt)
