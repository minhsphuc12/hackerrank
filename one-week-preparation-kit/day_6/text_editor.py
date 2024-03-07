S = 'abcde'
ops = ['1 fg', '3 6', '2 5', '4', '3 7', '4', '3 4']

def edit_text(S='', ops=[]):
    states = []
    for op in ops:
        # print(S, op)
        op_list = op.split(' ')
        action = int(op_list[0])
        
        if action in [1,2]:
            states.append(S)

        if action == 1:
            data = op_list[1]
            S += data

        if action == 2:
            k = int(op_list[1])
            S = S[:(len(S)-k)]

        if action == 3:
            k = int(op_list[1])
            print(S[k-1])

        if action == 4:
            if len(states) > 0:
                S = states[-1]
                del states[-1]

edit_text(S=S, ops=ops)