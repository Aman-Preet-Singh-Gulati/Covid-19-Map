# functions for making a map

def find_top_confirmed(n=15):
  import pandas as pd
  corona_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/07-04-2020.csv')
  by_country = corona_df.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered','Active']]
  cdf = by_country.nlargest(n, 'Confirmed')[['Confirmed']]
  return cdf

cdf = find_top_confirmed()#.to_html()
pairs = [(country, confirmed) for country, confirmed in zip(cdf.index, cdf['Confirmed'])]


import pandas as pd
corona_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/07-04-2020.csv')
corona_df.head(2)
import folium
m = folium.Map(location= [19.449759, 76.108221],
          tiles = 'Stamen toner', zoom_start= 8)
folium.Circle(location= [19.449759, 76.108221], radius=10000, color='red', fill=True, popup='confirmed {}'.format(20)).add_to(m)

def circle_maker(x):
  folium.Circle(location= [x[0], x[1]],
                radius = float(x[2])*2,
                color = 'red',
                fill = True,
                popup = '{}\nConfirmed Cases: {}'.format(x[3], x[2]),).add_to(m)
corona_df[['Lat', 'Long_', 'Confirmed', 'Combined_Key']].dropna().apply(lambda x: circle_maker(x), axis=1)

html_map = m._repr_html_()





from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html', table = cdf, cmap = html_map, pairs=pairs)


if __name__ == "__main__":
    app.run(debug=True)