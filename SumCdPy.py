
def CalPoints(ops):

    tam = len(ops)
    vs = []

    if tam == 1 or tam > 1000:
        print('There must be a minimum of 1 and a maximum of 1000 numbers')
        exit(0)

    for i in range(tam):

        if ops[i] == 'C':   # Remove the last number
            if len(vs) > 0:
                vs.pop()
            else:
                print("Nothing to remove")
                break
        elif ops[i] == 'D':
            if len(vs) > 0:
                vs.append(2 * vs[len(vs) - 1]) # Put 2 * last number
            else:
                print('Nothing to duplicate')
                break
        elif ops[i] == '+':
            if len(vs) > 1:
                vs.append(vs[len(vs) - 1] + vs[len(vs) - 2])   # Put last number + penultimate number
            else:
                print('numbers must be at least 2 numbers')
                break
        else:
            if ops[i].lstrip("-").isdigit(): # if is number or negative number
                vs.append(int(ops[i]))  # Put the number
            else:
                print("Character " + ops[i] + " not apply")
                break

    print(vs)
    return sum(vs)


ops = input('Enter numbers: ').split(' ')
soma = CalPoints(ops)
print('Sum = ' + str(soma))







