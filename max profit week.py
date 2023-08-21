import pandas as pd
import matplotlib.pyplot as plt
from persiantools.jdatetime import JalaliDate

df = pd.read_csv("BTC-USD.csv")
df["Benefit"] = df["Close"] - df["Open"]

df["Date"] = pd.to_datetime(df["Date"])
df["JalaliDate"] = df["Date"].apply(lambda x: JalaliDate.to_jalali(x.year, x.month, x.day))


df_weekly = df.groupby(pd.Grouper(key="Date", freq="W-SUN")).last()

df_weekly["Weekly_Profit"] = df_weekly["Benefit"].rolling(window=7, min_periods=1).sum()

max_profit_week = df_weekly["Weekly_Profit"].idxmax()
max_profit_value = df_weekly.loc[max_profit_week, "Weekly_Profit"]


max_profit_week_jalali = JalaliDate.to_jalali(max_profit_week.year, max_profit_week.month, max_profit_week.day)


plt.figure()
plt.plot(df_weekly.index, df_weekly["Weekly_Profit"], label="Weekday profit")
plt.axvline(x=max_profit_week, color="red", linestyle="--", label="max profit week")
plt.xlabel("WeekDay",fontsize = 20)
plt.ylabel("Weekday profit",fontsize = 20)
plt.title("max profit week",fontsize = 25, y= 1.03)
plt.legend()
plt.grid(True)
plt.show()
