f = []
h = 100
for i in range(1,11):
    if i == 1:
        f.append(h)
    else:
        f.append(h*2)
    h = h/2

print(f'十次落地距离总和: {sum(f)} 米')
print(f'第十次反弹: {h} 米')