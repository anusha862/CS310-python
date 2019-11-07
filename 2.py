score=input('enter score:')
i=float(score)
if i>=0.9:
    print('A')
elif i>=0.8:
    print('B')
elif i>=0.7:
    print('C')
elif i>=0.6:
    print('D')
elif i<0.6:
    print('F')
else:
    print('some error')