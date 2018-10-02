n, m = map(int,input().split())

'''for i in range(a):
    print('.|.'((i*2) +1) for i in range(int(a)//2))'''

pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
# total string is m long(,. center will place string to center and remaning place will be filled by what ever value we give inside center along with total length
#                top            center                  bottom

'''
sample input
9 27

sample output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''