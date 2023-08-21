import pandas as pd
from matplotlib import pyplot as plt
from persiantools.jdatetime import JalaliDate
from datetime import  datetime

df = pd.read_csv("BTC-USD.csv")
df["Benefit"] = df["Close"] - df["Open"]


df["Jalali"] = df["Date"].apply(lambda d:JalaliDate(datetime.strptime(d, "%Y-%m-%d")))
df["WeekDay"] = df["Date"].apply(lambda d:JalaliDate(datetime.strptime(d, "%Y-%m-%d")).isoweekday())


grouped = df.groupby("WeekDay")["Benefit"].sum()



plt.plot(grouped.index, grouped.values, marker='o', color="midnightblue")
plt.xlabel('Weekday',fontsize = 20, color= 'midnightblue')
plt.ylabel('Total Benefit',fontsize = 20, color= 'midnightblue')
plt.title('Total Benefit by Weekday',fontsize = 25, y= 1.03)
plt.xticks(range(1, 8), ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
plt.grid(True)
plt.show()
