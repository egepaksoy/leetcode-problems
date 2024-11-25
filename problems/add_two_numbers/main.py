def addTwoNum(l1, l2):
    n = 0
    l = l2
    lmin = l1

    if len(l1) > len(l2):
        l = l1
        lmin = l2

    kalan = 0
    sum = []

    while n < len(l):
        if len(lmin) > n:
            if l1[n]+l2[n] > 9:
                k = kalan
                kalan = (l1[n] + l2[n]) // 10
                sum.append(l1[n]+l2[n]-kalan*10+k)

            else:
                sum.append(l1[n]+l2[n]+kalan)
                kalan = 0

        else:
            if l[n] + kalan > 9:
                k = kalan
                kalan = (l[n] + k) // 10
                
                sum.append(l[n] - kalan * 10 + k)
            
            else:
                sum.append(l[n] + kalan)
                kalan = 0

        n+=1

    return sum