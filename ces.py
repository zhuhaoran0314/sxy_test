# 新建一个列表，用于存放距离数据
far = []
# 起始高度
high = 100
# for遍历十次，从1到10
for i in range(1,11):
    print(f'第{i}次')
    # 如果遍历到第一次
    if i == 1:
        # 第一次落下100米，添加到距离列表里
        far.append(high)
    # 如果不是第一次，之后每次反弹和落下的距离都是相等，所有要high*2，再添加到距离列表里
    else:
        far.append(high*2)
    print(f'距离记录列表内容:{far}')
    # 每次遍历时的高度 = 上次的遍历的高度/2
    high = high/2
    print(f'反弹距离:{high}米')

print(f'经过的总距离:{sum(far)}米')
print(f'第十次反弹{high}米')


