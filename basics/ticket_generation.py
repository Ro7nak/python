#for input use:

s = list(map(str,input().split(',')))
#print(s)
a = []
for i in range(len(s)):
  a.append(s[i].split(':'))
#print(a)
su = []
for i in range(len(s)):
 j = 0
 for i in (a[i][2][::2]):
  j += int(i)
 su.append(str(j))
#for i in range(len(s)):
  #print(a[i][0][0:2]+a[i][1][-2:]+su[i]+str(i+1) end = ",")
print(",".join(a[i][0][0:2]+a[i][1][-2:]+su[i]+str(i+1) for i in range(len(s))))

'''
sample input:
Paris:Delhi:9945672345,Berlin:Brussels:9456723456
'''