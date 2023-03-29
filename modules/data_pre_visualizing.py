# Required libraries to install
# !pip install imageio
# !pip install folium
# !pip install selenium

import numpy as np
import pandas as pd
import os

# library to create the maps
import folium

import time

# library to automatically get a screen of the map (previously saved as html) and save it as png
from selenium import webdriver

# import chrome options in order to hide the icon of chrome during the screen capturing operation
from selenium.webdriver.chrome.options import Options 

# library to create the gifs for accidents and deaths by region accross the years
import imageio

# The start() function will be called by the main, then it will call all the functions related to the data pre-visualizing
def start() :
    
    # Create the empty DataFrames
    accidents_deaths = pd.DataFrame()
    male_female = pd.DataFrame()
    ages = pd.DataFrame()
    ages_d = pd.DataFrame()
    it_for = pd.DataFrame()
    
    # Load the cleaned dataset of all the accidents (we load it once and will pass it in each function in order to speed the processes)
    total_accidents = pd.read_csv('datasets/__cleaned_datasets/__cleaned_accidents.csv', sep=";" )
    
    # Safety at work' global trends about accidents and deaths
    accidents_deaths = accidents_Deaths( accidents_deaths, total_accidents )
    accidents_deaths.to_csv( "datasets/__final_datasets/__accidents_deaths_trend.csv", sep=";", index=False )
    
    # Accidents and deaths by sex
    male_female = male_Female( male_female, total_accidents )
    male_female.to_csv( "datasets/__final_datasets/__male_female.csv", sep=";", index=False )
    
    # Accidents by age
    ages = age_Intervals( ages, total_accidents )
    ages.to_csv( "datasets/__final_datasets/__ages_accidents.csv", sep=";", index=False )
    
    # Deaths by age
    ages_d = age_Intervals_d( ages_d, total_accidents )
    ages_d.to_csv( "datasets/__final_datasets/__ages_deaths.csv", sep=";", index=False )
    
    # Accidents and deaths by nationality (italians and foreigners)
    it_for = it_For( it_for, total_accidents )
    it_for.to_csv( "datasets/__final_datasets/__it_for.csv", sep=";", index=False )
    
    
    #
    # START MAPS PREPARATION
    #
    
    # Load 'Rates by Region' to normalize the accidents and deaths rates
    rates_by_region = pd.read_csv('datasets/__final_datasets/__rates_by_region.csv', sep=";")
    
    # Normalize the rates
    rates_by_region['Accidents Rate'] = normalizeRates( rates_by_region["Accidents Rate"] )
    rates_by_region['Deaths Rate'] = normalizeRates( rates_by_region["Deaths Rate"] )
    
    # save it as csv
    rates_by_region.to_csv( "datasets/__final_datasets/__normalized_rates_by_region.csv", sep=";", index=False )
    
    # Create the maps for both accidents and deaths and save them as png
    accidents_map_to_png( rates_by_region )
    deaths_map_to_png( rates_by_region )
    
    # Create the gifs from the png previously created
    accidents_png_to_gif()
    deaths_png_to_gif()
    
    print("Data pre-visualizing finished!")

    
def accidents_Deaths( accidents_deaths, total_accidents ) :
    
    for year in range( 2013, 2019 ) :
            
        # Count the total number of accidents at work occurred in the current year
        n_accidents = total_accidents[ ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) ].count()['Accident Date']
        
        # Count the total number of fatal accidents at work occurred in the current year
        n_deaths = total_accidents[ ( ( total_accidents['Accident Date'].str.endswith( str( year ) ) &
                                      ( total_accidents['Death Date'].notna() ) ) ) ].count()['Accident Date']
        
        # Delete from the accidents the fatal accidents
        n_accidents -= n_deaths
        
        row = pd.DataFrame( [[ year, n_accidents, n_deaths ]] )
        accidents_deaths = pd.concat( [ accidents_deaths, row ] )
        
    accidents_deaths.columns = [ 'Year', 'Total Accidents', 'Total Deaths' ]
    return accidents_deaths


def male_Female( male_female, total_accidents ) :
    
    for year in range( 2013, 2019 ) :
            
        n_accidents_male = total_accidents[ ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) &
                                  ( total_accidents['Sex'] == 'M' ) ].count()['Accident Date']
        
        n_accidents_female = total_accidents[ ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) &
                                  ( total_accidents['Sex'] == 'F' ) ].count()['Accident Date']
        
        n_deaths_male = total_accidents[ ( ( total_accidents['Sex'] == 'M' ) &
                                    ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) &
                                    ( total_accidents['Death Date'].notna() ) ) ].count()['Accident Date']
        
        n_deaths_female = total_accidents[ ( ( total_accidents['Sex'] == 'F' ) &
                                    ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) &
                                    ( total_accidents['Death Date'].notna() ) ) ].count()['Accident Date']
        
        n_accidents_male -= n_deaths_male
        n_accidents_female -= n_deaths_female
        
        row = pd.DataFrame( [[ year, n_accidents_male, n_accidents_female,n_deaths_male,n_deaths_female ]] )
        male_female = pd.concat( [ male_female, row ] )
        
        
    male_female.columns = [ 'Year', 'Total Accidents M', 'Total Accidents F', 'Total Deaths M', 'Total Deaths F' ]
    return male_female


def age_Intervals( ages, total_accidents ) :
    
    for year in range( 2013, 2019 ) :
        
        age_intervals = [ [15,24], [25,34], [35,44], [45,54], [55,64], [65,120] ]
        
        for interval in age_intervals :
            
            n_accidents = total_accidents[ ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) &
                                           ( total_accidents['Age'] >= interval[0] ) &
                                           ( total_accidents['Age'] <= interval[1] ) ].count()['Accident Date']
            
            interval.append( n_accidents )

        row = pd.DataFrame( [[ year, age_intervals[0][2], age_intervals[1][2], age_intervals[2][2], age_intervals[3][2],
                                     age_intervals[4][2], age_intervals[5][2] ]] )

        ages = pd.concat( [ ages, row ] )
        
        
    ages.columns = [ 'Year', '15-24', '25-34', '35-44', '45-54', '55-64', '65+' ]
    return ages


def age_Intervals_d( ages_d, total_accidents ) :
    
    for year in range( 2013, 2019 ) :
        
        age_intervals = [ [15,24], [25,34], [35,44], [45,54], [55,64], [65,120] ]
        
        for interval in age_intervals :
            
            n_deaths = total_accidents[ ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) & 
                                           ( total_accidents['Death Date'].notna() ) &
                                           ( total_accidents['Age'] >= interval[0] ) &
                                           ( total_accidents['Age'] <= interval[1] ) ].count()['Accident Date']
            
            interval.append( n_accidents )

        row = pd.DataFrame( [[ year, age_intervals[0][2], age_intervals[1][2], age_intervals[2][2], age_intervals[3][2],
                                     age_intervals[4][2], age_intervals[5][2] ]] )

        ages_d = pd.concat( [ ages_d, row ] )
        
        
    ages_d.columns = [ 'Year', '15-24', '25-34', '35-44', '45-54', '55-64', '65+' ]
    return ages_d


def it_For( it_for, total_accidents ) :
    
    for year in range( 2013, 2019 ) :
            
        it_acc = total_accidents[ ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) &
                                  ( total_accidents['Birth Place'] == 'ITALIA' ) ].count()['Accident Date']
        
        for_acc = total_accidents[ ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) &
                                  ( total_accidents['Birth Place'] != 'ITALIA' ) ].count()['Accident Date']
        
        it_dea = total_accidents[ ( ( total_accidents['Birth Place'] == 'ITALIA' ) &
                                    ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) &
                                    ( total_accidents['Death Date'].notna() ) ) ].count()['Accident Date']
        
        for_dea = total_accidents[ ( ( total_accidents['Birth Place'] != 'ITALIA' ) &
                                    ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) &
                                    ( total_accidents['Death Date'].notna() ) ) ].count()['Accident Date']
        
        row = pd.DataFrame( [[ year, it_acc, for_acc,it_dea,for_dea ]] )
        it_for = pd.concat( [ it_for, row ] )
        
        
    it_for.columns = [ 'Year', 'Accidents of italians', 'Accidents of foreigner', 'Deaths of italians', 'Deaths of foreigners' ]
    return it_for


def normalizeRates( column ) :
    
    # Create an empty Series, it will replace the actual once the return line is readen by python
    new_column = pd.Series()
    
    # Get the max and min of the column we pass to the function
    min_column = min( column )
    max_column = max( column )
    
    # Compute the size of the step in order to cover the distance between the max and the min through six steps (because six are the
    # colours contained in the palette of the folium map)
    step = round( ( ( max_column - min_column ) / 6 ), 2 )
    
    # Create the intervals with lenght equal to the step (we used np.arange in order to create float ranges)
    intervals = [ [ str( round( i, 2 ) ), str( round( ( step+i ), 2 ) ) ] for i in np.arange( min_column, max_column+0.1, step ) ]
    
    for i, row in enumerate( column ) :
        
        for index, interval in enumerate( intervals ) :
            
            # if the row of our column is in the current interval, then append to the Series we have initially created the
            # index of the interval
            if ( row >= float( interval[0] ) ) and ( row < float( interval[1] ) ) :
            
                to_append = pd.Series( [ index ] )
                new_column = new_column.append( to_append, ignore_index=True )
    
    return new_column 


def accidents_map_to_png( state_data ) :


    state_geo = os.path.join('src','map','sources','italy.json')

    iterable_data = pd.DataFrame()
    
    # Create and save a map for each of our years
    for year in range( 2013, 2019 ) :
        
        # We need an iterable name for the map because otherwise during the next iteration it will be mainteined also the previous legend
        iterable_map_name = ''
        
        # Crate the map with the italian coordinates
        iterable_map_name = folium.Map(location=[41.8719, 12.5674], zoom_start=5, tiles='cartodbpositron')
        
        # Get only the data of the current year
        iterable_data = iterable_data.append(state_data[state_data['Year'] == year])

        folium.Choropleth(
            geo_data=state_geo, # load the polygons of the italian regions
            name='choropleth',
            data=iterable_data, # load the current data
            columns=['Region', 'Accidents Rate'], # set columns' data to display
            key_on='feature.properties.name', # set the region name of the italy.json file as the key which will link the two datasets 
            fill_color='OrRd',
            fill_opacity=1,
            line_opacity=0.2,
            legend_name='Accidents Rate ' + str( year )
        ).add_to( iterable_map_name )

        delay=0.5

        iterable_html = 'src/map/html/__map_accidents_rate/__accidents_rate_' + str(year) + '.html'
        tmpurl_html ='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=iterable_html)
        iterable_google = '__accidents_rate_' + str(year) + '.html'
        tmpurl_google ='file://{path}/src/map/html/__map_accidents_rate/{mapfile}'.format(path=os.getcwd(),mapfile=iterable_google)
        iterable_map_name.save(iterable_html)

        chrome_options = Options()
        chrome_options.add_argument("--headless") # hide the chrome icons during the operation
        browser = webdriver.Chrome('C:/Users/admin/#Coding_Lessons/Intro to Coding 2/inail/src/map/sources/chromedriver.exe',
                                   options=chrome_options)
        browser.get(tmpurl_google)
        time.sleep(delay)
        iterable_png = 'src/map/png/__map_accidents_rate/__map_accidents_rate_' + str(year) + '.png'
        browser.save_screenshot(iterable_png)
        browser.quit()
        

def deaths_map_to_png( state_data ) :

    state_geo = os.path.join('src','map','sources','italy.json')

    iterable_data = pd.DataFrame()

    # Create and save a map for each of our years
    for year in range( 2013, 2019 ) :

        # We need an iterable name for the map because otherwise during the next iteration it will be mainteined also the previous legend
        iterable_map_name = ''
        
        # Crate the map with the italian coordinates
        iterable_map_name = folium.Map(location=[41.8719, 12.5674], zoom_start=5, tiles='cartodbpositron')

        # Get only the data of the current year
        iterable_data = iterable_data.append(state_data[state_data['Year'] == year])

        folium.Choropleth(
            geo_data=state_geo, # load the polygons of the italian regions
            name='choropleth',
            data=iterable_data, # load the current data
            columns=['Region', 'Deaths Rate'], # set columns' data to display
            key_on='feature.properties.name', # set the region name of the italy.json file as the key which will link the two datasets
            fill_color='BuPu',
            fill_opacity=1,
            line_opacity=0.2,
            legend_name='Deaths Rate ' + str( year )
        ).add_to( iterable_map_name )

        delay=0.5

        iterable_html = 'src/map/html/__map_deaths_rate/__deaths_rate_' + str(year) + '.html'
        tmpurl_html ='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=iterable_html)
        iterable_google = '__deaths_rate_' + str(year) + '.html'
        tmpurl_google ='file://{path}/src/map/html/__map_deaths_rate/{mapfile}'.format(path=os.getcwd(),mapfile=iterable_google)
        iterable_map_name.save(iterable_html)

        chrome_options = Options()
        chrome_options.add_argument("--headless") # hide the chrome icons during the operation
        browser = webdriver.Chrome('C:/Users/admin/#Coding_Lessons/Intro to Coding 2/inail/src/map/sources/chromedriver.exe',
                                   options=chrome_options)
        browser.get(tmpurl_google)
        time.sleep(delay)
        iterable_png = 'src/map/png/__map_deaths_rate/__map_deaths_rate_' + str(year) + '.png'
        browser.save_screenshot(iterable_png)
        browser.quit()

        
def accidents_png_to_gif() :
    
    images=[]

    for year in range( 2013, 2019 ) :

        file_name = '__map_accidents_rate_' + str( year ) + '.png'
        file_path = os.path.join('src\map\png\__map_accidents_rate', file_name)
        images.append(imageio.imread(file_path))

    imageio.mimsave('src/map/gif/__map_accidents_rate_.gif', images, duration = 1.2)
    

def deaths_png_to_gif() :

    images=[]

    for year in range( 2013, 2019 ) :

        file_name = '__map_deaths_rate_' + str( year ) + '.png'
        file_path = os.path.join('src\map\png\__map_deaths_rate', file_name)
        images.append(imageio.imread(file_path))

    imageio.mimsave('src/map/gif/__map_deaths_rate_.gif', images, duration = 1.2)
    