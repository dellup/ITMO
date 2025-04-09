import pandas as pd
import matplotlib.pyplot as plt

intervals = ['[114-119]', '[119-124]', '[124-129]', '[129-134]', '[134-139]', '[139-144]', '[144-149]', '[149-154]', '[154-159]']
frequencies = [3, 11, 37, 59, 47, 24, 7, 1, 1]

data = {
    'Интервал': intervals,
    'Частота (ni)': frequencies
}

df = pd.DataFrame(data)

midpoints = [116.5, 121.5, 126.5, 131.5, 136.5, 141.5, 146.5, 151.5, 156.5]  
plt.figure(figsize=(10, 6))
plt.step(midpoints, frequencies, where='mid', linestyle='-', color='b', linewidth=2)
plt.xlabel('Интервалы')
plt.ylabel('Частота (ni)')
plt.title('Гистограмма частот')
plt.grid(True)
plt.xticks(midpoints)
plt.show()
