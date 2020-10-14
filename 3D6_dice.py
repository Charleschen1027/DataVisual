from die import Die
import pygal

# 创建3个D6的骰子
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 掷骰子多次，存储结果
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(2,max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling a 3D6 1000 times."
hist.x_labels = [x for x in range(3,19)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('3D6',frequencies)
hist.render_to_file('3D6.svg')
