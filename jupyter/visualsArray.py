from time import sleep
from IPython.display import clear_output, display

from termcolor import colored
color = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']


def render(lis, selector=set(), x='▒', m='▒', b='  ', s=' ', t='⇓', d='|',w=True, depth=None):
    '''
    x: space filler
    b: blank space btw lines
    s: empty space filler
    '''
    
    n = len(lis)
    p = len(color)
    up = max(0, max(lis))
    down = min(0, min(lis))

    depth = (up - down) if depth is None else depth

    for j in range(n):
        if j in selector: print(colored(t, color[j%p]), end=b)
        else: print(colored(s, color[j%p]), end=b)
    print()

    for i in range(depth+1):
        for j in range(n):
            if up - i>=0:
                if lis[j] - (up - i) > 0:
                    print(colored(x, color[j%p]), end=b)
                else:
                    e = d if j in selector else s
                    print(colored(e, color[j%p]), end=b)
            else:
                if up - i > lis[j]:
                    print(colored(m, color[j%p]), end=b)
                else:
                    print(colored(s, color[j%p]), end=b)
        print()
        
if __name__ == '__main__':
    lis = [1,6,-4,7,8,10,-2,4,6,2,-6,8]
    render(lis, selector={2,8,4})