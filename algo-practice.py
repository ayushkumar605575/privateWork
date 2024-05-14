a= ['cat','bat','tac','bad','atc']
b = {i: 1 for i in 'act'}

def is_anagram(a,b):
    ans = []
    for word in a:
        m = {}
        for w in word:
            m[w] = 1+m.get(w, 0)
        if m == b:
            ans.append(word)
    print(ans)

is_anagram(a,b)