def foundnumbers(improved):

    wordnumbers = {'one':'1',
                  'two':'2',
                  'three':'3',
                  'four':'4',
                  'five':'5',
                  'six':'6',
                  'seven':'7',
                  'eight':'8',
                  'nine':'9',
                  }
    
    firstlettersofnumbers="otfsen"

    found_numbers = []
    wordnumber = ''
    for char in improved:
        if char.isnumeric():
            found_numbers.append(char)
            wordnumber = ''
            continue
        if len(wordnumber) == 0:
            if char in firstlettersofnumbers:
                wordnumber = char
                continue
            else:
                wordnumber = ''
                continue
        if len(wordnumber) == 1:
            if wordnumber + char in ['on','tw','th','fo','fi','si','se','ei','ni']:
                wordnumber +=char
                continue
            if char in firstlettersofnumbers:
                wordnumber = char
                continue
            else:
                wordnumber = ''
                continue
        if len(wordnumber) == 2:
            if wordnumber + char in ['one','two','six']:
                found_numbers.append(wordnumbers[wordnumber + char])
                wordnumber = char
                continue
            if wordnumber + char in ['thr','fou','fiv','sev','eig','nin']:
                wordnumber +=char
                continue
            if char in firstlettersofnumbers:
                wordnumber = char
                continue
            else:
                wordnumber = ''
                continue
        if len(wordnumber) == 3:
            if wordnumber + char in ['four','five','nine']:
                found_numbers.append(wordnumbers[wordnumber + char])
                wordnumber = char
                continue
            if wordnumber + char in ['thre','seve','eigh']:
                wordnumber +=char
                continue
            if char in firstlettersofnumbers:
                wordnumber = char
                continue
            else:
                wordnumber = ''
                continue
        if len(wordnumber) == 4:
            if wordnumber + char in ['three','seven','eight']:
                found_numbers.append(wordnumbers[wordnumber + char])
                wordnumber = char
                continue
            if char in firstlettersofnumbers:
                wordnumber = char
                continue
            else:
                wordnumber = ''
                continue
    return found_numbers   


with open('1/ii/test','r') as values:
    sum=0
    for line in values:
        print(f'{foundnumbers(line)}')
        # print(f'{foundnumbers(line)[0]} {foundnumbers(line)[-1]}')
        sum+= int(foundnumbers(line)[0]+foundnumbers(line)[-1])
    print(sum)
