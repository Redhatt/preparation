# if n == 0:
#     return 'Zero'

a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen']
b =  ['_', '_', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
c = ['thousand', 'million', 'billion', 'trillion']
d = [3, 6, 9, 12]

def rec(n):
    if n == 0: return []
    if n < 20: return [a[n]]
    if n < 100: return [b[n//10]] + rec(n%10)
    if n < 1000: return [a[n//100], "Hundred"] + rec(n%100)

    s = []
    for v, p in zip(reversed(c), reversed(d)):
        if n >= 10**p:
            print((v, p, n, n//(10**p)))
            s += rec(n//(10**p)) + [v]
            n = n%(10**p)
    s += rec(n)
    
    return s


n = 832418
print(rec(n))