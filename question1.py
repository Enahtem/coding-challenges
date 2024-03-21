def solution(i):
    s = ""
    current_prime=2
    while len(s)<=i+5:
        is_prime=True
        for j in range(2, int(current_prime**(0.5)+1)):
            if (current_prime%j==0):
                is_prime=False
                break
        if (is_prime):
            s=s+str(current_prime)
        current_prime+=1
    return s[i:i+5]

print(solution(10000))
