import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

gc_file=pd.read_csv("gc_content_teste.csv")

df = pd.DataFrame(gc_file)

sns.barplot(data=df, x='genoma', y="gc", palette="pastel")

plt.title("Conteúdo GC de cada espécie")
plt.xticks(rotation=45, fontsize=8)
plt.ylabel("Contéudo GC", fontsize=16)

plt.savefig("gc.png", dpi=100)