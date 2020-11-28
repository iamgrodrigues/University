import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x= np.random.randn(200)
y= np.random.randn(200)

df = pd.DataFrame({"x": x, "y": y})

'''sns.displot(df["x"])
plt.show()'''

'''sns.barplot(df.x, df.y)
plt.show()'''

'''sns.scatterplot(df.x, df.y, hue=df.x)
plt.show()'''

sns.pairplot(data=df, vars= ["x", "y"], hue= "x")
plt.show()