while True:
    v = raw_input('please input your code:')
    if v == 'q':
        break
    if not (v.startswith('+') or v.startswith('-') or v.startswith('(') or v[0].isalnum()):
        print 'input error'
        continue
    if not (v.endswith(')')or v[-1].isalnum()):
        print 'input error'
        continue
    if v.count('(')  != v.count(')'):
        print 'input error'
        continue
    n= v.rfind('(') + 1
    for i in range(n,len(v)):
        if v[i] == ')':
            value_str = v[n:i]
            if "*" in value_str:
                value_chen_list = value_str.split('*')
                for j in range(0,len(value_chen_list)):
                    for x in range(len(value_chen_list[j])):
                        value_chen_list[j][x]

















