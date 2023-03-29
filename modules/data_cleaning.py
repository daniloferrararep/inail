import pandas as pd
import modules.region as r

# Create the list of regions to skim in order to get the relative csv (because data are initially divided by region in several csv)
regions = ['Abruzzo','Basilicata','Calabria','Campania','EmiliaRomagna','FriuliVeneziaGiulia','Lazio','Liguria','Lombardia','Marche','Molise','Piemonte','Puglia','Sardegna','Sicilia','Toscana','TrentinoAltoAdige','Umbria','ValledAosta','Veneto']


# The start() function will be called by the main, then it will call all the functions related to the data cleaning
def start() :
    
    # Create the empty dataframes which will be passed to the functions and will be replaced by the fruit of the functions, then they will
    # save as csv
    accidents = pd.DataFrame()
    employed_by_region = pd.DataFrame()
    
    # Clean accidents
    accidents = clean_Accidents( accidents )
    accidents.to_csv( "datasets/__cleaned_datasets/__cleaned_accidents.csv", sep=";", index=False )
    
    # Clean employed by region
    employed_by_region = clean_Employed_Region( employed_by_region )
    employed_by_region.to_csv( "datasets/__cleaned_datasets/__cleaned_employed_by_region.csv", sep=";", index=False )
    
    print("Data cleaning finished!")
    
def clean_Accidents( accidents ) :
       
    for region in regions :
        
        print('\n\nWorking with:', region, '\n' )
        
        # Set the paths related to the iterable 'region' variable
        path_2013_2017 = 'datasets/accidents/cadenza_semestrale (2013-2017)/DatiConCadenzaSemestraleInfortuni' + region + '.csv'
        
        # In the folder "complete_data_2017_2018" are contained all the data relative to all the accidents of 2017 and 2018
        # (for more information read the "MISSING DATA FROM 2018" issue on the report)
        path_2018 = 'datasets/accidents/cadenza_mensile (2018-2019)/complete_data_2017_2018/DatiConCadenzaMensileInfortuni'+ region+ '.csv'
        
        # Load the csv files in two new DataFrames     
        data_2013_2017 = pd.read_csv( path_2013_2017 , sep=";" )
        data_2018 = pd.read_csv( path_2018 , sep=";" )
                
        # Create the object/instance 'Region' in order to clean and reshape the regional dataset
        reg = r.Region( data_2013_2017 )
        
        # Concatenate the dataset related to the last year in a unique dataset
        print("Concatenating the dataset related to the last year in a unique dataset ...")
        reg = reg.add_Last_Year( data_2018 )
        
        # Drop the unwanted columns
        print("Dropping the unwanted columns ...")
        reg = reg.drop_Unwanted_Columns()
        
        # Decodify the 'Province' and add the 'Region' and the 'Area' for each accident
        print("Decodifing the 'Province' and adding the 'Region' and the 'Area' for each accident ...")
        reg = reg.add_Province_Region_Area()
        
        # Decodify the 'BirthPlace' and add the column 'UE' with S if the country is part of the European Union
        print("Decodifing the 'BirthPlace' and adding the column 'UE' with S if the country is part of the European Union ...")
        reg = reg.add_Birth_Place()
        
        # Decodify the 'Sector' in which the worker was employed
        print("Decodifing the 'Sector' in which the worker was employed ...")
        reg = reg.add_Sector()
        
        # Concatenate the dataframe of the current region with that of the total accidents
        accidents = pd.concat( [accidents, reg.getDataFrame()], sort=False )
    
    # Rename all the columns of the complete dataset of accidents
    accidents.columns = ['Accident Date', 'Death Date', 'Province', 'Region', 'Area', 'Sex', 'Age', 'Birth Place', 'EU', 'Modality',
                         'Sector','Category']
    return accidents

def clean_Employed_Region( employed_by_region ) :
    
    # Load the dataset which contains the number of people employed divided by region and by year
    employed_by_region = pd.read_csv('datasets/others/occupati_regione.csv')
    
    # Drop the unwanted columns because not needed for our research
    employed_by_region.drop(['ITTER107','SEXISTAT1','ETA1','Classe di età','Seleziona periodo','Flag Codes','Flags'],axis=1,inplace=True)
    
    # Transform each value of the colum 'Value' in integer and then multiply it by 1000 (in order to avoid some misunderstanding with the
    # dot that could be interpreted as a comma instead of "the thousands' space")
    employed_by_region['Value'] = ( employed_by_region['Value'] * 1000 ).astype('int')

    # Drop the columns which contain in the column 'Sesso' a specific sex, male or female, because we want only the total value of employed
    # in that region (in order to do so we check or the presence of the keys 'maschi' or 'femmine')
    employed_by_region.drop( employed_by_region.loc[( employed_by_region['Sesso'] == 'maschi') |
                                                    ( employed_by_region['Sesso'] == 'femmine') ].index, inplace=True )
    
    # Drop the columns which contain the specific sex (because now there is no more distinction)
    employed_by_region.drop( 'Sesso', axis=1, inplace=True )
            
    # Drop the columns which contain in the column 'TIME' an alphanumeric value (it means that it cointains the data of people employed
    # for each quarter of the year, expressed with the alphanumeric format '2013-Q1')
    employed_by_region.drop( employed_by_region.loc[employed_by_region['TIME'].str.isalnum() == False].index, inplace=True )
    
    # Rename the columns
    employed_by_region.columns = ['Region','Year','Total (thousands)']
    
    return employed_by_region
