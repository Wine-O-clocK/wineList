from glob import glob
import pandas as pd

address = '/Users/yen/tori/winegit/'

wine_red = pd.read_csv('wine_red.csv', encoding='utf-8')
wine_white = pd.read_csv('wine_white.csv', encoding='utf-8')
wine_sparkle = pd.read_csv('wine_sparkle.csv', encoding='utf-8')
wine_rose = pd.read_csv('wine_rose.csv', encoding='utf-8')
wine_etc = pd.read_csv('wine_etc.csv', encoding='utf-8')

df = pd.concat(
	[wine_red, wine_white, wine_rose, wine_sparkle, wine_etc]
)


df.to_csv(path_or_buf=address+'wine_list.csv', encoding="utf-8-sig", index=False)