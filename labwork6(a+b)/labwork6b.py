import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('scores.csv')

df = df.fillna(df.mean(numeric_only=True))

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].scatter(df.index, df['python'], color='blue')
axes[0].set_title('Python Scores')
axes[0].set_xlabel('Student')
axes[0].set_ylabel('Score')

axes[1].scatter(df.index, df['math'], color='green')
axes[1].set_title('Math Scores')
axes[1].set_xlabel('Student')
axes[1].set_ylabel('Score')

axes[2].scatter(df.index, df['database'], color='red')
axes[2].set_title('Database Scores')
axes[2].set_xlabel('Student')
axes[2].set_ylabel('Score')

plt.tight_layout()
plt.savefig('scattered.png')
plt.close()
print("Đã lưu scattered.png")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

df['python'].plot.hist(ax=axes[0], title='Python', color='blue', bins=10)
df['math'].plot.hist(ax=axes[1], title='Math', color='green', bins=10)
df['database'].plot.hist(ax=axes[2], title='Database', color='red', bins=10)

plt.tight_layout()
plt.savefig('histo.png')
plt.close()
print("Đã lưu histo.png")

plt.figure(figsize=(8, 6))
df.boxplot(column=['python', 'math', 'database'])
plt.title('Box Plot of Scores')
plt.savefig('box.png')
plt.close()
print("saved.png")

print("\ncompleted.")