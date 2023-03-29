import pandas as pd

class Region:
    
    # Create an empty DataFrame which is the object we will use for all the operations inside the class "Region" 
    df = pd.DataFrame()
    
    def __init__( self, df ) :
        
        # Initialize the local DataFrame with the dataframe we pass when creating a new instance
        self.df = df
        
    def __str__( self ) :
        
        # Return the local DataFrame as a string
        return str( self.df )
        
    def add_Last_Year( self, df_2018 ) :
        
        # Drop all the accidents occured in the 2017 or in the 2019
        self.df.drop( self.df.loc[ ( self.df['DataAccadimento'].str.endswith( '2017' ) ) |
                                   ( self.df['DataAccadimento'].str.endswith( '2019' ) ) ].index, inplace=True )
        
        # Concatenate the data of the 2018 with the data of the period 2013-2017
        self.df = pd.concat( [self.df, df_2018], sort=False)
        return self
    
    def drop_Unwanted_Columns( self ) :
        
        # Drop the unwanted columns since they are not relevant for our task
        self.df.drop(['DataRilevazione', 'DataProtocollo', 'DataDefinizione', 'IdentificativoInfortunato', 'ConSenzaMezzoTrasporto',
                      'DefinizioneAmministrativa', 'IdentificativoCaso', 'DefinizioneAmministrativaEsitoMortale', 'GradoMenomazione',
                      'GiorniIndennizzati', 'Indennizzo', 'DecisioneIstruttoriaEsitoMortale', 'PosizioneAssicurativaTerritoriale',
                      'Gestione', 'GestioneTariffaria', 'GrandeGruppoTariffario','IdentificativoDatoreLavoro'],axis=1,inplace=True)
        
        return self
        
    def add_Province_Region_Area( self ) :
        
        # Load the dataset containing all the provinces with the related id, region and area with ";" as a separator
        provinces = pd.read_csv('datasets/others/Provincia.csv', sep=";")
        
        # Add after the third index the new column 'Region', "allow_duplicates()" function doesn't allow to have duplicates
        self.df.insert(3, "Regione", 0, allow_duplicates=False)
        
        # Add after the fourth index the new column 'Area'
        self.df.insert(4, "Area", 0, allow_duplicates=False)
        
        # Create a list with all the provinces
        provinces_name = provinces['DescrProvincia']
        
         # Skim the provinces' names and compare the id of each province with those present in the accidents' dataset 
        for idx, val in provinces_name.iteritems() :
            self.df.loc[self.df['LuogoAccadimento'] == idx, 'LuogoAccadimento'] = val # where the code finds a province with the id = idx
                                                                                      # substitute in the column 'LuogoAccadimento' the
                                                                                      # complete name of the province
                    
        # Add to the fields 'Region' and 'Area' the appropriate value obtained by skimming the provinces' list
        for idx, val in provinces_name.iteritems() :                                                                                
            self.df.loc[self.df['LuogoAccadimento'] == val, 'Regione'] = provinces.at[idx, 'DescrRegione']
            self.df.loc[self.df['LuogoAccadimento'] == val, 'Area'] = provinces.at[idx, 'DescrMacroregione']
        
        return self
        
    def add_Birth_Place( self ) :
        
        # Load the dataset which contains all the nations with the column EU (S means is an EU member, N means is not an EU member)
        nations = pd.read_csv('datasets/others/LuogoNascita.csv', sep=";")
        
        # Add after the index 8 the new column 'EU'
        self.df.insert(8, "EU", 0, allow_duplicates=False)
        
        # Skim each row of the nations' dataframe, decodify the BirthPlace and whether it is part of the EU
        for idx, row in nations.iterrows():
            self.df.loc[self.df['LuogoNascita'] == row['LuogoNascita'],'LuogoNascita'] = nations.at[idx,'DescrNazioneNascita']
            self.df.loc[self.df['LuogoNascita'] == nations.at[idx,'DescrNazioneNascita'],'EU'] = nations.at[idx, 'FlagAppartenenzaUE']
        
        return self
    
    def add_Sector( self ) :
        
        # Load the dataset which contains all the economic sectors with the column which describes the macro-area (category) of the sector
        sectors = pd.read_csv('datasets/others/SettoreAttivitaEconomica.csv', sep=";")
                
        # Rename the column 'SettoreAttivitaEconomica' as 'Sector'
        self.df.rename(index=str, columns={"SettoreAttivitaEconomica": "Sector"}, inplace=True)
        
        # Add after the index 11 a new column called 'Category'
        self.df.insert(11, "Category", 0, allow_duplicates=False)
        
        # Skim each row of the sectors' dataframe, decodify the Sector and add the Category of the sector
        for idx, row in sectors.iterrows():
            self.df.loc[self.df['Sector'] == row['SettoreAttivitaEconomica'],'Sector'] = sectors.at[idx,'DescrAteco']
            self.df.loc[self.df['Sector'] == sectors.at[idx,'DescrAteco'],'Category'] = sectors.at[idx, 'DescrAtecoLiv1']
        
        return self        
        
    def getDataFrame( self ) :
        
        # Return the DataFrame instanced with the class Region        
        return self.df
    