import random

# 最小进球数
min = 0
# 最大进球数
max = 4

play = int(input("请选择竞彩足球比分玩法(1:【单场固定】 , 2:【过关方式】)："))

if play == 1:
    session = int(input("请选择场次：(1:【克罗地亚 vs 摩洛哥】 , 2:【阿根廷 vs 法国】)："))
    if session == 1:
        print("开始预测 【克罗地亚 vs 摩洛哥】 比分...")
        print(f"本场比赛的比分为   {(random.randint(min, max))} ：{(random.randint(min, max))}")

    elif session == 2:
        print("开始预测 【阿根廷 vs 法国】 比分...")
        print(f"本场比赛的比分为   {(random.randint(min, max))} ：{(random.randint(min, max))}")

elif play == 2:
    print("开始预测 【全部比赛】 比分...")
    print(f"【克罗地亚 vs 摩洛哥】比分为   {(random.randint(min, max))} ：{(random.randint(min, max))}")
    print(f"【阿根廷 vs 法国】 比分为     {(random.randint(min, max))} ：{(random.randint(min, max))}")