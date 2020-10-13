from die import Die
import pygal

# 创建两个D8骰子
die1 = Die(8)
die2 = Die(8)

# 掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2,max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling two D8 1000 times."
hist.x_labels = [x for x in range(2,17)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8',frequencies)
hist.render_to_file('D8D8.svg')



