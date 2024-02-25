---
jupyter:
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.7.1
  nbformat: 4
  nbformat_minor: 2
---

::: {.cell .markdown}
# DATA VISUALIZATION
:::

::: {.cell .markdown}
## Global Trends viz
:::

::: {.cell .markdown}
#### ACCIDENTS & DEATHS {#accidents--deaths}

##### Accidents
:::

::: {.cell .code execution_count="4"}
``` python
import pandas as pd
import matplotlib.pyplot as plt

accidents = pd.read_csv( "datasets/__final_datasets/__accidents_deaths_trend.csv", sep=";" )
accidents.set_index('Year', inplace=True)
accidents["Total Accidents"].plot( title="Total Accidents (2013-2018)", figsize=( 15, 5 ), color = "#CA4D5D")
```

::: {.output .execute_result execution_count="4"}
    <matplotlib.axes._subplots.AxesSubplot at 0x1a540e52978>
:::

::: {.output .display_data}
![](images/77344da997632c0130b84a4fd274150b532734e0.png)
:::
:::

::: {.cell .markdown}
##### Deaths
:::

::: {.cell .code execution_count="5"}
``` python
import matplotlib.pyplot as plt

accidents = pd.read_csv( "datasets/__final_datasets/__accidents_deaths_trend.csv", sep=";" )
accidents.set_index('Year', inplace=True)
accidents["Total Deaths"].plot( title="Total Deaths (2013-2018)", figsize=( 15, 5 ) , color = "#A57ACE" )
```

::: {.output .execute_result execution_count="5"}
    <matplotlib.axes._subplots.AxesSubplot at 0x1a541037e10>
:::

::: {.output .display_data}
![](images/0680624c716cf5743a083d6ba6341d751c2d8807.png)
:::
:::

::: {.cell .markdown}
#### Data Analysis

The complaints presented for accidents at work occurred in 2014
decreased compared to 2013, while as it concerns fatal accidents at
work, there was a decrease compared to the previous year. In 2015 the
decreasing trend in the number of accidents is confirmed, and there was
a decrease compared to 2014. As it concerns fatal accidents at work,
there was a decrease compared to the previous year, due to the
increasing number of firms benefiting from the reduction in INAIL
premiums for prevention merits. In 2016 there was no significant
difference compared to 2015 , while as it concerns fatal accidents at
work, there was a decrease compared to the year 2015. In 2017 there was
no significant difference compared to 2016, while as it concerns fatal
accidents at work, there was an increase compared to the year 2016. In
2017, in fact, 13 multiple fatal accidents occurred in January in
Abruzzo. We can notice that the trend of the accidents is a downtrend,
from 2013 to 2018 the number of accidents has decreased, this due to
factors as technological development and safety courses. However, as it
is possible to notice from the first graph there was an increasing for
the fatal accidents in 2018. The expansion of the tertiary sector is one
of the most significant causes in determining the decrease in the number
of injuries, as it directs the workforce towards less risky occupations.
:::

::: {.cell .markdown}
#### MALE & FEMALE {#male--female}

###### Accidents {#accidents}
:::

::: {.cell .code execution_count="114"}
``` python
import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('datasets/__final_datasets/__male_female.csv', sep=";")

years = [ year for year in range( 2013, 2019 ) ]

for i,year in enumerate( years ) :
    to_plot = pd.DataFrame( [["Males", df.T[i][1]], ["Females", df.T[i][2]]], columns=["Sex","Year"])

    sex_data = to_plot["Sex"]
    year_data = to_plot["Year"]
    colors = ["#CA4D5D", "#FFA500"] 
    plt.pie(year_data, labels=sex_data, colors=colors,
    autopct='%1.1f%%', startangle=140)
    plt.title("Total accidents in " + str(year))
    plt.show()
```

::: {.output .display_data}
![](images/e504a6f2d90a1f41d6e20e5e013fa30433333e01.png)
:::

::: {.output .display_data}
![](images/240bcaddbd0ac873b4d029f57065195e19abc3b3.png)
:::

::: {.output .display_data}
![](images/9f58db81243224f541519f1430f62d7fc905b653.png)
:::

::: {.output .display_data}
![](images/69f1c94f53a0ab0e5361be33b63b2aba3430ed6e.png)
:::

::: {.output .display_data}
![](images/fa92d6705d5af544b974d0ea7fc58900c444bc21.png)
:::

::: {.output .display_data}
![](images/1af6c368157e6d9c7cdc95e5df58806a7db6fee0.png)
:::
:::

::: {.cell .markdown}
###### Deaths {#deaths}
:::

::: {.cell .code execution_count="115"}
``` python
import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('datasets/__final_datasets/__male_female.csv', sep=";")

years = [ year for year in range( 2013, 2019 ) ]

for i,year in enumerate( years ) :
    to_plot = pd.DataFrame( [["Males", df.T[i][3]], ["Females", df.T[i][4]]], columns=["Sex","Year"])

    sex_data = to_plot["Sex"]
    year_data = to_plot["Year"]
    colors = ["#A57ACE", "#4986C6"] 
    plt.pie(year_data, labels=sex_data, colors=colors,
    autopct='%1.1f%%', startangle=140)
    plt.title("Total deaths in " + str(year))
    plt.show()
```

::: {.output .display_data}
![](images/5759268e81e289e8fa26691a9c9ff6973e8fa199.png)
:::

::: {.output .display_data}
![](images/f76dc8ce8dfa94d209f49c74ac4cc2bc2f0ada05.png)
:::

::: {.output .display_data}
![](images/7c906ae7818c88171b63f9c3e8fed34b3ecac045.png)
:::

::: {.output .display_data}
![](images/3ceb871e63e3b2bd8b63d5daf53996c57707351c.png)
:::

::: {.output .display_data}
![](images/74539338346597af55cba12614e6f707db676cfb.png)
:::

::: {.output .display_data}
![](images/0e89fbdf8b036b722b57d82129d6910563a26e42.png)
:::
:::

::: {.cell .markdown}
#### Data Analysis {#data-analysis}

On the basis of the collected results it appears that the percentage of
death at work by sex has remained constant over the years, around 9% for
women and around 91% for men. The reason behind this great disparity is
that there are very few women hired in the sectors most at risk. On the
other hand, the percentage of non-fatal accidents at work is around 35%
for women and round 65% for men. The employment status of women, mainly
engaged in administrative activities of the tertiary sector or with
clerical or managerial tasks in the most dangerous sectors such as
industry, means that the risk of male workers is much higher than that
of female workers.
:::

::: {.cell .markdown}
#### AGES

##### Accidents {#accidents}
:::

::: {.cell .code execution_count="119"}
``` python
ages = pd.read_csv('datasets/__final_datasets/__ages_accidents.csv', sep=";" )
ages.set_index('Year', inplace=True)
ages.plot( kind="barh", rot=45, title="Age", figsize=( 15, 10 ) )
```

::: {.output .execute_result execution_count="119"}
    <matplotlib.axes._subplots.AxesSubplot at 0x12145c1f780>
:::

::: {.output .display_data}
![](images/e01a5839685b5c94b8634e203e0d087cd682aab3.png)
:::
:::

::: {.cell .markdown}
#### Data Analysis {#data-analysis}

As regards the analysis of accidents at work by age group, the data show
that the age groups most affected are those from 45 to 54 years old
workers,with an average of about 170000 injuries per year, followed by
age groups from 35 to 44 years old, for which the number of accidents
fell constantly: from around 170000 accidents in 2013 to around 130000
in 2018. With regard to the age group between 25 and 34 years old, the
number of accidents has steadily decreased to reach an almost unvaried
number of 110000 accidents per year, while as it concerns the age group
between 15 and 24 years old, there has been a constant increase in the
number of injuries up to a level of 110000 injuries in the year 2018.
The data clearly show that if, on one hand, young people pay the price
of precariousness and uncertainty, on the other hand older workers find
themselves having to put up with the weight of often exhausting working
conditions.
:::

::: {.cell .markdown}
##### Deaths {#deaths}
:::

::: {.cell .code execution_count="120"}
``` python
ages = pd.read_csv('datasets/__final_datasets/__ages_deaths.csv', sep=";" )
ages.set_index('Year', inplace=True)
ages.plot( kind="barh", rot=45, title="Age", figsize=( 15, 10 ))
```

::: {.output .execute_result execution_count="120"}
    <matplotlib.axes._subplots.AxesSubplot at 0x12145deed68>
:::

::: {.output .display_data}
![](images/93ad262db625ea8841badf6a457db67578e0120b.png)
:::
:::

::: {.cell .markdown}
#### Data Analysis {#data-analysis}

As regards the analysis of fatal accidents at work by age group, the
data show that the age groups most affected are those from 55 to 64
years old workers, followed by age groups from 45 to 54 years old, for
which the number of accidents fell constantly.
:::

::: {.cell .markdown}
#### ITALIANS AND FOREIGNERS

##### Accidents {#accidents}
:::

::: {.cell .code execution_count="122"}
``` python
import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('datasets/__final_datasets/__it_for.csv', sep=";")

years = [ year for year in range( 2013, 2019 ) ]

for i,year in enumerate( years ) :
    to_plot = pd.DataFrame( [["Italians", df.T[i][1]], ["Foreigners", df.T[i][2]]], columns=["Nationality","Year"])

    nationality_data = to_plot["Nationality"]
    year_data = to_plot["Year"]
    colors = ["#CA4D5D", "#FFA500"] 
    plt.pie(year_data, labels=nationality_data, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("Total accidents in " + str(year) + " by nationality")
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.show()
```

::: {.output .display_data}
![](images/ab6ca6c1aaafcaa6888a136cfdc1c941888e72c6.png)
:::

::: {.output .display_data}
![](images/1a13c675e5f709950761e1596f37d4564f1ee781.png)
:::

::: {.output .display_data}
![](images/9dfcfdf34c7439d6ba44e51d09e2244cdd75dc22.png)
:::

::: {.output .display_data}
![](images/458a3111889948838d3728b6ef64fda11e3b4c75.png)
:::

::: {.output .display_data}
![](images/feb2391f45c503d386a070314a997e2adfb27872.png)
:::

::: {.output .display_data}
![](images/a2f38bf41b6b301d056a604ed4f18fd302b7d5d9.png)
:::
:::

::: {.cell .markdown}
##### Deaths {#deaths}
:::

::: {.cell .code execution_count="123"}
``` python
import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('datasets/__final_datasets/__it_for.csv', sep=";")

years = [ year for year in range( 2013, 2019 ) ]

for i,year in enumerate( years ) :
    to_plot = pd.DataFrame( [["Italians", df.T[i][3]], ["Foreigners", df.T[i][4]]], columns=["Nationality","Year"])

    nationality_data = to_plot["Nationality"]
    year_data = to_plot["Year"]
    colors = ["#A57ACE", "#4986C6"] 
    plt.pie(year_data, labels=nationality_data, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("Total deaths in " + str(year) + " by nationality")
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.show()
```

::: {.output .display_data}
![](images/39de21672d3ccbdba67fec5d5156277d0a7bc0ae.png)
:::

::: {.output .display_data}
![](images/17faff2a8dc1c039e95c2992f63bbcf3ee1d8de7.png)
:::

::: {.output .display_data}
![](images/8f37bfe07f8d55246223a28701b3965cd17736f2.png)
:::

::: {.output .display_data}
![](images/db1d4014a66f4ca73541fbb40e2eac4fe6a3657c.png)
:::

::: {.output .display_data}
![](images/f7ffdc46cb80bf737030f217549ada07b4afe897.png)
:::

::: {.output .display_data}
![](images/8e47b256fff57874ac71310c2500b625b34b0abb.png)
:::
:::

::: {.cell .markdown}
#### Data Analysis {#data-analysis}

By analyzing the data collected, it appears that the percentage of
deaths at work by nationality also remained constant over the years:
about 85% of deaths at work involved Italian citizens, while the
remaining 15% involved foreign workers. As it concerns non-fatal
accidents at work by nationality it appears that about 64% of accidents
at work involved italian citizens, while the remaining 36% involved
foreign workers.
:::

::: {.cell .markdown}
## Region Rates viz

### 1`<sup>`{=html}st`</sup>`{=html} Research Question: {#1st-research-question}

> Which are the **regions** with the highest rate of work-related
> accidents and fatal accidents at work in Italy (with respect to the
> number of employed per region)?`<BR>`{=html}
:::

::: {.cell .markdown}
#### ACCIDENTS RATE BY REGION
:::

::: {.cell .code execution_count="7" scrolled="false"}
``` python
from IPython.display import Image

with open('src/map/gif/__map_accidents_rate_.gif','rb') as file:
    display(Image(file.read()))
```

::: {.output .display_data}
![](images/4a7a641950f6c1af9ebe37e5510a5451e19b2449.png)
:::
:::

::: {.cell .markdown}
#### Data Analysis {#data-analysis}

In 2018 the reports of accidents at work presented to INAIL increased by
0.9%, probably due to the increase in the retirement age which forced
thousands of old people to keep dangerous jobs that are becoming
increasingly difficult to manage due to concentration,ailments and slow
reflexes. In the report presented by INAIL, Trentino Alto Adige is the
region with the highest number of accidents at work reported from 2013
to 2018, followed by Emilia Romagna. The result is given by the greater
job offer, low undeclared employment rate, and a greater propensity to
report compared to the rest of the Italian regions, but also and above
all by the greater number of labor inspectors present in its provinces.
The sectors most at risk of accidents are agriculture and forestry, for
the latter there was in fact an increase in the labor force linked to
the restoration of the conditions of the Trentino forests after the wave
of bad weather that hit Northern Italy in 2018.
:::

::: {.cell .markdown}
#### DEATHS RATE BY REGION
:::

::: {.cell .code execution_count="5" scrolled="false"}
``` python
from IPython.display import Image

with open('src/map/gif/__map_deaths_rate_.gif','rb') as file:
    display(Image(file.read()))
```

::: {.output .display_data}
![](images/55cf52d2f30a3a49576a8a78ced5ef2d4a6242a9.png)
:::
:::

::: {.cell .markdown}
#### Data Analysis {#data-analysis}

Across the years in Italy the rate of accidents at work has fallen by,
and paradoxically the number of victims has increased according to data
provided by INAIL on the basis of the complaints presented to the
Institute. Among the main risk factors is the lack of safety at work, in
agriculture as well as in construction industry, and undeclared work. By
observing and analysing the information from the INAIL dataset we found
a substantial high rate of fatal accidents at work in two Italian
Regions in particular: Molise and Abruzzo. The lack of safety at work is
due especially to the use of old and damaged work vehicles or machinery,
but also devoid of security devices and security courses for workers.
The causes of the injuries are mainly: falls from above, toxic fumes,
crushing. But these are the apparent reasons: deaths often occur because
the safety of workers is not considered a priority, workers are not
adequately trained on the risks they run and lack controls. To this
scenario is added the precariousness of contracts and the difficulty in
finding a new job, factors that make workers more and more
blackmailable.
:::

::: {.cell .markdown}
## Sector Rates viz

### 2`<sup>`{=html}nd`</sup>`{=html} Research Question: {#2nd-research-question}

> Which are **sectors** with the highest risks (with respect to the
> number of employed per region)?`<BR>`{=html}
:::

::: {.cell .markdown}
#### ACCIDENTS RATE BY SECTOR
:::

::: {.cell .code execution_count="80"}
``` python
import pandas as pd
accidents_by_sector = pd.read_csv( "datasets/__final_datasets/__rates_by_sector.csv", sep=";" )

# Nested list comprehension to create a list which contain the data of the sector for each year (one list for each year)
data = [ 
             [
               accidents_by_sector["Accidents Rate"][index_sector] for index_sector in range( len( accidents_by_sector["Sector"] ) ) if accidents_by_sector["Year"][index_sector] == year
             ] # inner loop/comprehension
    
             for year in range( 2013, 2019 )
         ] # outer loop/comprehension

# Create the pandas DataFrame 
accidents_rate_to_plot = pd.DataFrame(data, index = [ year for year in range( 2013, 2019 ) ],
                            columns = [ "primary sector", "industry", "costructions", "trade","transport",
                                       "accomodation", "information", "finance/insurance","business services",
                                       "public sector", "education/healthcare", "other services" ]) 
accidents_rate_to_plot.plot( kind="barh", rot=45, title="Accidents Rate by sector", figsize=(15,20) )
```

::: {.output .execute_result execution_count="80"}
    <matplotlib.axes._subplots.AxesSubplot at 0x12144866940>
:::

::: {.output .display_data}
![](images/ab5d5a9d9601ac7eefee5b609a0028a699bf113e.png)
:::
:::

::: {.cell .markdown}
#### Data Analysis {#data-analysis}

The sectors most at risk include construction, agriculture, wholesale
and retail trade and vehicle repair, warehousing and transport and the
healthcare and social assistance. In the industrial sector, on the other
hand, the manufacturing of metal products, machinery production and the
food industry stand out for the rate of accidents at work.
:::

::: {.cell .markdown}
#### DEATHS RATE BY SECTOR
:::

::: {.cell .code execution_count="118"}
``` python
import pandas as pd
accidents_by_sector = pd.read_csv( "datasets/__final_datasets/__rates_by_sector.csv", sep=";" )

# Nested list comprehension to create a list which contain the data of the sector for each year (one list for each year)
data = [ 
             [
               accidents_by_sector["Deaths Rate"][index_sector] for index_sector in range( 0, len( accidents_by_sector["Sector"] ) ) if accidents_by_sector["Year"][index_sector] == year
             ] # inner loop/comprehension
    
             for year in range( 2013, 2019 )
         ] # outer loop/comprehension

# Create the pandas DataFrame 
accidents_rate_to_plot = pd.DataFrame(data, index = [ year for year in range( 2013, 2019 ) ],
                            columns = [ "primary sector", "industry", "costructions", "trade","transport",
                                       "accomodation", "information", "finance/insurance","business services",
                                       "public sector", "education/healthcare", "other services" ]) 
accidents_rate_to_plot.plot( kind="barh", rot=45, title="Deaths Rate by sector", figsize=(15,20) )
```

::: {.output .execute_result execution_count="118"}
    <matplotlib.axes._subplots.AxesSubplot at 0x12145ad1da0>
:::

::: {.output .display_data}
![](images/a57bae749fdd7149926c3b218a3f29a5cfcc24ef.png)
:::
:::

::: {.cell .markdown}
#### Data Analysis {#data-analysis}

According to data collected by the INAIL, as far as the sectors are
concerned, fatal accidents at work are more common among construction
workers, manufacturing activities, transport and storage, from wholesale
and retail trade, repair of motor vehicles and motorcycles, followed by
accommodation, restaurants and catering services, and the supply of
water, sewage networks, waste management activities and rehabilitation.
:::

::: {.cell .markdown}
## Interest by People viz

### 3`<sup>`{=html}rd`</sup>`{=html} Research Question: {#3rd-research-question}

> How much people **care** about job security when a serious accident
> occurs? (Google Trend)`<BR>`{=html}
:::

::: {.cell .code execution_count="124"}
``` python
import matplotlib.pyplot as plt

google_trend = pd.read_csv( "datasets/others/interest_by_people.csv" )
google_trend.drop("Mese", axis=0, inplace=True)
prova = pd.to_numeric( google_trend["Categoria: Tutte le categorie"] )
prova.plot( title="Interest by people about safety at work (2013-2019)", figsize=( 15, 5 ), color = "#CA4D5D")
```

::: {.output .execute_result execution_count="124"}
    <matplotlib.axes._subplots.AxesSubplot at 0x12144d34048>
:::

::: {.output .display_data}
![](images/78aa0cba598e9105e1afbac69491cad861933921.png)
:::
:::

::: {.cell .markdown}
#### Data Analysis {#data-analysis}

By looking at the Google Trends graph, we can see that the lowest levels
of interest recorded over the years always coincide with the month of
August.This can be explained by the fact that August is a month of
vacation for most Italian companies, so it is understandable that there
is a decrease in the accident rate and consequently also in the degree
of interest. Another drop, although less significant than the previous
one, is also recorded for the month of December.
:::
