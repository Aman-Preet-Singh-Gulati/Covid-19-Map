<!-- [![Covid19WebAPP](https://img.theweek.in/content/dam/week/news/sci-tech/2020/april/virus-attack-coronavirus-COVID-19-shut.jpg)](https://aman-preet-singh-gulati.github.io/Aman-Preet-Singh-Gulati/) -->


# Covid-19 Dashboard Webapp
## Technologies used :

> Flask : For designing the api for frontend

> HTML, CSS, Boostrap : For frontend design

> Folium : For accessing the maps through Python

> Pandas : For Data Preprocessing and scraping data   from github repo

---



[![Badges](http://img.shields.io/:badges-9/9-ff6799.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger)

***HERE IS THE GLIMPSE OF COVID-19 DASHBOARD APP***

![Covid 19 Dashboard2](https://user-images.githubusercontent.com/66076818/87554080-508b6a80-c6d1-11ea-8ff7-fcbb387e2e3b.png)

- It is sucessfully `DEPLOYED`, in herokuapp platform and I will provide the link here
- There's an issue in the frontend when viewed in mobile it is bit compressed and best suitable in landascape mode

> What this web app will do ?

- This will let you know about the `CONFIRMED` cases around the `WORLD` (`State-wise`)
- This will also let you know the `COUNTRY` leaderbord in terms of their `CONFIRMED` cases
- You should try this and checks the `perk` of `python` and `web-scraping`

> From where did I scraped the data ?

- The data is from John's Hopkins which provides daily updation regarding the `COVID-19` worldwide cases
- Here is the <a href="https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports">`link`</a>  to the official dataset

---


> How did I managed the `Radius` of `Circle` according to the number of cases
```python
# Here's the code

def circle_maker(x):
  folium.Circle(location= [x[0], x[1]],
                radius = float(x[2])*2,
                color = 'red',
                fill = True,
                popup = '{}\nConfirmed Cases: {}'.format(x[3], x[2]),).add_to(m)
corona_df[['Lat', 'Long_', 'Confirmed', 'Combined_Key']].dropna().apply(lambda x: circle_maker(x), axis=1)
```

---


## Table of Contents

> If you don't wanna follow on the complete contents then, you can just `CLICK` the particular content

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

## Installation

- All the `code` required to get started
- Images of what it should look like

> For data preprocessing
```sh
pip install pandas
```
> For accessing maps through python functionality
```sh
pip install folium
```
> For creating a working api for frontend to access the data from github repo
```sh
pip install flask
```

