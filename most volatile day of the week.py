import pandas as pd
from matplotlib import pyplot as plt
from persiantools.jdatetime import JalaliDate
from datetime import  datetime

df = pd.read_csv("BTC-USD.csv")
df["Benefit"] = df["Close"] - df["Open"]


df["Jalali"] = df["Date"].apply(lambda d:JalaliDate(datetime.strptime(d, "%Y-%m-%d")))
df["WeekDay"] = df["Date"].apply(lambda d:JalaliDate(datetime.strptime(d, "%Y-%m-%d")).isoweekday())

std_by_day = df.groupby("WeekDay")["Benefit"].std()


plt.figure(figsize=(10, 6))
std_by_day.plot(kind="bar", color='green', alpha=0.7)
plt.xlabel("Day of the Week",fontsize = 20, color= 'darkgreen')
plt.ylabel("Standard Deviation",fontsize = 20, color= 'darkgreen')
plt.title("Average Standard Deviation for Each Day of the Week",fontsize = 25, y= 1.03)
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()



