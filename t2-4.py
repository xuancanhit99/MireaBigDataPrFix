a = input().split()
b = input().split()
c = {}
# Инициализируйте словарь,
# если ключ не существует,
# инициализируйте его нулем и добавьте входное значение,
# если ключ тот же.
for i in range(len(b)):
    c[b[i]] = c.get(b[i], 0) + int(a[i])
print(c)