import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/handover_sample_logs.csv')
failure_types = df['handover_type'].value_counts()

plt.bar(failure_types.index, failure_types.values)
plt.title('Handover Failure Distribution (MRO Analysis)')
plt.ylabel('Number of Events')
plt.savefig('output/failure_distribution.png')
print("Saved visualization to output/failure_distribution.png")
