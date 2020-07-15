![virus](https://user-images.githubusercontent.com/66076818/87579481-9a854800-c6f3-11ea-986c-9b060e80b171.png)




# Covid-19 Dashboard Webapp

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## The app is `successfully deployed` at : https://covid-19-map-dashboard.herokuapp.com
---


## Here is the Badge of `Code Quality Score` and `Code grade` by `CodeInspector`
![code quality score](https://www.code-inspector.com/project/11052/status/svg)
![code quality score](https://www.code-inspector.com/project/11052/score/svg)
> The parameters of scoring the badge in github 
 - Code design
 - Code readibility
 - Frontend
 - Backend
 - Database (if any)
 - Even `Bad indentation` can decrease the score to some extent.
 - `Best thing` was I got only few `Violations` in Code style
---
## Technologies used :

> Flask : For designing the api for frontend

> HTML, CSS, Boostrap : For frontend design

> Folium : For accessing the maps through Python

> Pandas : For Data Preprocessing and scraping data   from github repo

---


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

[![GitHub issues](https://img.shields.io/github/issues/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/issues/)   [![Open Source Love png2](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)  [![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://github.com/Aman-Preet-Singh-Gulati/)

>## Table of Contents

> If you don't wanna follow on the complete contents then, you can just `CLICK` the particular content

- [Installation](#installation)
- [Contributing](#contributing)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

>## Installation

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

> Or if you wanna install complete required libraries at once
- For Python2
```sh
pip install -r requirements.txt
```
- For Python3
```sh
pip3 install -r requirements.txt
```

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/Aman-Preet-Singh-Gulati/Covid-19-Map.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/Aman-Preet-Singh-Gulati/Covid-19-Map/compare/" target="_blank">`https://github.com/Aman-Preet-Singh-Gulati/Covid-19-Map/compare`</a>.

---

>## FAQ

- **How I did *Data Preprocessing* via pandas**
    - Just drop this query in my mail or other queries
    - Here is the <a href="https://gulatiamanpreetsingh@gmail.com/">`link`</a>  of my gmail account

---
>## Support

Reach out to me at one of the following places!

- Website at <a href="https://aman-preet-singh-gulati.github.io/Aman-Preet-Singh-Gulati/" target="_blank">         `Portfolio|Amanpreet`</a>
- Instagram  at <a href="https://www.instagram.com/_.aman_preet._/" target="_blank">`_.aman_preet._`</a>
- Linkedin  at <a href="https://www.linkedin.com/in/aman-preet-singh-gulati-41ab20169/" target="_blank">`Aman preet Singh gulati`</a>
---
>## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="https://aman-preet-singh-gulati.github.io/Aman-Preet-Singh-Gulati/" target="_blank">Aman Preet Singh Gulati</a>.
---

>## Is repository maintained ?
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/Aman-Preet-Singh-Gulati/)
