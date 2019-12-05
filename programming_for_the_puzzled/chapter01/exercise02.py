cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
        'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
        'B', 'B', 'F', 'F', 'F', 'F']
cap3 = []

def pleaseConformOnePass(caps):
    if len(caps) == 0:
        print('input caps empty')
        return
    caps = caps + [caps[0]]
    start = 0
    for i in range(1, len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] == caps[0]:
                if i-1 == start:
                    print('Person at position {} flip you cap!'.format(i-1))
                else:
                    print('People in positions {} through {} flip your caps'.format(start, i-1))
            start = i


pleaseConformOnePass(cap1)
pleaseConformOnePass(cap2)
pleaseConformOnePass(cap3)