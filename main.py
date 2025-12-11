# 1 - misol
lst = [10, -5, 15, 22, 5, -30, 0]
result = {x for x in lst if x > 0 and x % 5 == 0}
print(result)


# 2 - misol
primes = {n for n in range(1, 51)
          if n > 1 and all(n % d != 0 for d in range(2, int(n**0.5)+1))}
print(primes)


# 3 - misol
words = ["olma", "banana", "anor", "uzum", "gilos"]
vowels = "aeiouAOEIU"
result = {w for w in words if w[0] in vowels}
print(result)


# 4 - misol
s = "assalomu alaykum"
result = {ch for ch in s if ch.isalpha()}
print(result)


# 5 - misol
result = {n**3 for n in range(1, 31) if n % 2 == 1}
print(result)

# 6 - misol
word = "python"
result = {ord(ch) for ch in set(word)}
print(result)
