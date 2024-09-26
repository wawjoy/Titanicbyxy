# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# show the title
st.title('Titanic App by Xiaoyu Wang:sunglasses:')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.dataframe(df)
# create a figure with three subplots, size should be (15, 5)
fig, ax = plt.subplots(1, 3, figsize=(15,5))

# show the box plot for ticket price with different classes
df_pclass1 = df[df.Pclass == 1]
df_pclass1.Fare.plot.box(ax=ax[0])
df_pclass2 = df[df.Pclass == 2]
df_pclass2.Fare.plot.box(ax=ax[1])
df_pclass3 = df[df.Pclass == 3]
df_pclass3.Fare.plot.box(ax=ax[2])

# you need to set the x labels and y labels
ax[0].set_xlabel('PClass = 1')
ax[1].set_xlabel('PClass = 2')
ax[2].set_xlabel('PClass = 3')
ax[0].set_ylabel('Fare')
st.pyplot(fig)
# a sample diagram is shown below

