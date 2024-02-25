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
# ACCIDENTS AT WORK IN ITALY

## GUIDELINES

Our work has the scope to face 3 related **research questions**:

1.  Which are the **regions** with the highest rate of work-related
    accidents and fatal accidents at work in Italy (with respect to the
    number of employed per region)?
2.  Which are **sectors** with the highest risks (with respect to the
    number of employed per region)?
3.  How much people **care** about job security when a serious accident
    occurs? And do these mortal accidents influence the worker\'
    attention during the days after the event?

We used datasets available on <https://dati.inail.it/opendata/>, the
Open-Data section of the INAIL website, the italian organization which
have the role to monitor and support the workers in case of accidents or
diseases. We appreciated a lot these collections because they are pretty
well organised (commented columns, linkable datasets by key, up-to-date
information). In fact we used these additional easy-linkable datasets:

-   <https://dati.inail.it/opendata/elements/Provincia> (to decodify the
    province of the event)
-   <https://dati.inail.it/opendata/elements/LuogoNascita> (to decodify
    the birth place of the worker)
-   <https://dati.inail.it/opendata/elements/SettoreAttivitaEconomica>
    (to decodify the sector of the job)

Datasets are divided by **time** (2013-2017, 2018-2019) and by
**regions**.

Furthermore, in our opinion, the subject of our topic is not taken into
great consideration by our society, which should increase awareness of
the risks we face every day as workers or as citizens.

The other datasets have been gathered by the ISTAT website (Italian
National Institute of Statistics):

-   <http://dati.istat.it/Index.aspx?DataSetCode=DCCV_OCCUPATIT1>
    (number of people employed by region and by sector)

The last dataset has been downloaded from Google Trends:

-   <https://trends.google.it/trends/explore?date=2013-01-01%202018-12-31&geo=IT&q=%2Fm%2F035sx5>

### SOCIAL IMPACT members

• DANILO FERRARA - data cleaning and data combining`<BR>`{=html} •
LEONARDO VENTURINI - data combining and data visualization`<BR>`{=html}
• VALERIA PICCOLI - data analysis and documentation`<BR>`{=html} • CARLO
CREMONA - data visualization and documentation`<BR>`{=html} • FRANCESCO
GHEZZE - data analysis and data visualization`<BR>`{=html}
:::

::: {.cell .markdown}
## STRUCTURE OF THE PUBLIC DATASET

> **Infortuni** - *Accidents at work*`<BR>`{=html}
>
> > **Dati con cadenza semestrale** - *data updated every six months*
> > **(2013-2017)**`<BR>`{=html}
> > <https://dati.inail.it/opendata/default/Daticadenzasemestrale/index.html>
> >
> > > **Abruzzo** - *region 1*`<BR>`{=html} **Basilicata** - *region
> > > 2*`<BR>`{=html} **Calabria** - *region 3*`<BR>`{=html} **\...**
:::

::: {.cell .markdown}
> > **Dati con cadenza mensile** - *data updated every month*
> > **(2018-2019)**`<BR>`{=html}
> > <https://dati.inail.it/opendata/default/Daticadenzamensile/index.html>
> >
> > > **Abruzzo** - *region 1*`<BR>`{=html} **Basilicata** - *region
> > > 2*`<BR>`{=html} **Calabria** - *region 3*`<BR>`{=html} **\...**
:::

::: {.cell .markdown}
## STEPS OF OUR WORK
:::

::: {.cell .markdown}
### 1. DATA CLEANING {#1-data-cleaning}

`<BR>`{=html}

First of all we need to unify the two periods of data for each italian
region (excluding the current year - 2019 - because it is incomplete).
Then we need to remove the columns we are not interested in, decodify
the *province* of the accident by merging our dataset with that of all
the italian provinces
(<https://dati.inail.it/opendata/elements/Provincia>) and add the
associated information *region* and *area* (North, Middle, South of
Italy). Add the *birth place* of the subject involved in the accident
and the sector where his work could be classified. Finally create a get
method which returns the DataFrame we have created and operated with
inside the class.

For all these operations we create the module ***region.py***, an
external source which cointains the class *Region* with the following
methods:`<BR>`{=html}

1.  **add_Last_Year ( df_2018 )** - Merge the data 2013-2017 with those
    of the same region of 2018
2.  **drop_Unwanted_Columns ( )** - Drop the unwanted colummns
3.  **add_Province_Region_Area ( )** - Decodify the \"province\", the
    \"region\" and the \"area\" of the accident (by merging with an
    external source)
4.  **add_Birth_Place ( )** - Decodify the birth place of the person
    involved in the accident (by merging with an external source)
5.  **add_Sector ( )** - Decodify the sector of work (primary, secondary
    or services) in which the worker was imployed
6.  **getDataFrame ( )** - get the DataFrame inside the class (then
    concatenate it into a unique file with all the accidents occurred in
    all the regions)

We will call these functions inside the module ***data_cleaning.py***
launched by the main file (see it below) and which contains the
following functions:`<BR>`{=html}

1.  **start ( )** - Launch the functions which clean the accidents and
    employed datasets and save them to csv
2.  **clean_Accidents ( accidents )** - Create a new instance of the
    class ***Region***, clean each region and concatenate them in a
    unique dataset
3.  **clean_Employed_Region ( employed_by_region )** - Clean the dataset
    related to the number of people employed by region
:::

::: {.cell .markdown}
### 2. DATA COMBINING {#2-data-combining}

`<BR>`{=html}

In order to merge the information we cleaned to build a rate for each
region and for each sector we prepared a set of function inside the
second module we call from the main that is
***data_combining.py***:`<BR>`{=html}

1.  **start ( )** - Launch the three functions which create the rates
    and save them to csv
2.  **rates_Region ( rates_by_region, total_accidents )** - Combine the
    number of accidents with those of people employed for each region
    for each year
3.  **rates_Sector ( rates_by_sector, total_accidents )** - Combine the
    number of accidents with those of people employed for each sector
    for each year
:::

::: {.cell .markdown}
### 3. DATA PRE-VISUALIZING {#3-data-pre-visualizing}

`<BR>`{=html}

In order to prepare the visualizations (plots, maps, gifs, \...) we
prepared a specic module called ***data_visualizing.py*** which has
different functions regarding some operations to do before launch the
final visualizations (**open the file *results.ipynb* in the main
folder**):`<BR>`{=html}

1.  **start ( )** - Launching the ten functions which are related to the
    preparation for visualization
2.  **accidents_Deaths ( accidents_deaths, total_accidents )** - Create
    the optimized dataset to plot the Accidents/Deaths trends over the
    years
3.  **male_Female ( male_female, total_accidents )** - Create the
    optimized dataset to plot the Male/Female percentages for
    accidents/deaths over the years
4.  **age_Intervals ( ages, total_accidents )** - Create the optimized
    dataset to plot the intervals of age related to the accidents at
    work over the year
5.  **age_Intervals_d ( ages_d, total_accidents )** - Create the
    optimized dataset to plot the intervals of age related to the deaths
    at work over the year
6.  **it_For ( it_for, total_accidents )** - Create the optimized
    dataset to plot the Italians/Foreigners percentages for
    accidents/deaths over the years
7.  **normalizeRates ( column )** - Normalize the rates of the columns
    in order to visualize a fair map representation over the years
8.  **accidents_map_to_png ( state_data )** - Create through a cycle a
    map for each year with the normalized data of accidents by region
    and then save it as html, later open the html, get a screenshot
    through the Selenium library and save it as png
9.  **deaths_map_to_png ( state_data )** - Create through a cycle a map
    for each year with the normalized data of deaths by region and then
    save it as html, later open the html, get a screenshot through the
    Selenium library and save it as png
10. **accidents_png_to_gif ( )** - Open the png files previously created
    and save them in a unique gif (deaths)
11. **deaths_png_to_gif ( )** - Open the png files previously created
    and save them in a unique gif (deaths)
:::

::: {.cell .markdown}
### RESULTS AND VISUALIZATIONS (results.ipynb) {#results-and-visualizations-resultsipynb}

All the outcomes of our 3 research questions are shown in the
interactive notebook file ***data_visualizing.ipynb*** which contains
the following visualizations:`<BR>`{=html}

-   **Global Trends viz** - Four plots which give an idea about the
    trends of the phenomenon
-   **Region Rates viz** - Italian maps in which regions are colored
    according its *rate of accidents* or *rate of accidents with death*
-   **Sector Rates viz** - Comparing plots which show which sectors are
    characterised by an high risk
-   **Interest by People viz** - Two plots where are shown how much
    people focus on *safety at work* (decreasing the rate of accident)
    after a serious accident and how much the interest about the
    argument increases on Google Trends during these events

We chose basic plots for non-expert users in order to reach as many
people as possible.
:::

::: {.cell .markdown}
## MAIN - cleaning, combining and preparing the visualizations
:::

::: {.cell .code execution_count="1"}
``` python
%reload_ext autoreload
%autoreload 2

# Import the three modules located inside the folder 'modules' and assign to them an alias
import modules.data_cleaning as clean
# import modules.data_combining as combine
# import modules.data_pre_visualizing as pre_visualize

# Start cleaning the datasets (about 12 minutes)
clean.start()

# Start combining the datasets (about 27 minutes)
combine.start()

# Start preparing the visualizations of the datasets (about 20 minutes)
# pre_visualize.start() (DECOMMENTING WILL ALTERATE RESULTS.IYPNB - see it first - )

# In order to visualize the outcomes of our work open the Jupyter Notebook file "results.ipynb"
```

::: {.output .stream .stdout}


    Working with: Abruzzo 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Basilicata 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Calabria 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Campania 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: EmiliaRomagna 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: FriuliVeneziaGiulia 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Lazio 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Liguria 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Lombardia 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Marche 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Molise 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Piemonte 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Puglia 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Sardegna 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Sicilia 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Toscana 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: TrentinoAltoAdige 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Umbria 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: ValledAosta 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...


    Working with: Veneto 

    Concatenating the dataset related to the last year in a unique dataset ...
    Dropping the unwanted columns ...
    Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...
    Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...
    Decodifing the 'Sector' in which the worker was employed ...
    Data cleaning finished!
:::
:::
