cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
        'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
        'B', 'B', 'F', 'F', 'F', 'F']
cap3 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']


def pleaseConform(caps):
    start = forward = backward = 0
    intervals = []
    for i in range(1, len(caps)):
        if caps[i] == 'H':
            if caps[i-1] != caps[0]:
                intervals.append((start, i-1, caps[start]))
                start = i
                continue

        if caps[start] != caps[i]:
            intervals.append((start, i-1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    intervals.append((start, len(caps)-1, caps[start]))
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            if t[0] != t[1]:
                print('People in positions', t[0], 'through', t[1], 'flip your caps!')
            else:
                print('Person at position {} flip your cap!'.format(t[0]))
    

pleaseConform(cap1)
pleaseConform(cap2)
pleaseConform(cap3)