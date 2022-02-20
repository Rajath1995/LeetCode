s = 'dbab'

if s == "" or s == len(s) * s[0]:
    print(s)

p = s[0]
l = 1

for i in range(len(s)):
    for j in range(len(s), 0, -1):
        print(j)
        w = s[i:j]

    # Is 'w' longer than our current longest palindrome 'p'?
        if w == w[::-1] and len(w) > l:
            p = w
            l = len(w)
print(p)
