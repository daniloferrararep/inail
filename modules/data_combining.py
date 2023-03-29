import pandas as pd

# The decimal module provides support for decimal floating point arithmetic used in the function
import decimal

# The start() function will be called by the main, then it will call all the functions related to the data combining
def start() :
    
    # Create the empty dataframes which will be passed to the functions and will be replaced by the fruit of the functions, then they will
    # save as csv
    rates_by_region = pd.DataFrame()
    rates_by_sector = pd.DataFrame()
    
    # Load the cleaned dataset of all the accidents (we load it once and will pass it in each function in order to speed the processes)
    total_accidents = pd.read_csv('datasets/__cleaned_datasets/__cleaned_accidents.csv', sep=";" )

    # Safety at work' risk rates by region
    rates_by_region = rates_Region( rates_by_region, total_accidents )
    rates_by_region.to_csv( "datasets/__final_datasets/__rates_by_region.csv", sep=";", index=False )
    
    # Safety at work' risk rates by sector
    rates_by_sector = rates_Sector( rates_by_sector, total_accidents )
    rates_by_sector.to_csv( "datasets/__final_datasets/__rates_by_sector.csv", sep=";", index=False )
    
    print("Data combining finished!")
    
    
def rates_Region( rates_by_region, total_accidents ) :
    
    # Create the list of regions
    regions = ['Abruzzo', 'Basilicata', 'Calabria', 'Campania', 'Emilia Romagna', 'Friuli Venezia Giulia', 'Lazio', 'Liguria', 'Lombardia',
              'Marche', 'Molise', 'Piemonte', 'Puglia', 'Sardegna', 'Sicilia', 'Toscana', 'Trentino Alto Adige', 'Umbria',
               'Valle D\'Aosta', 'Veneto']
     
    # Load the cleaned dataset of the employed people divided by region and by year
    employed_by_region = pd.read_csv( 'datasets/__cleaned_datasets/__cleaned_employed_by_region.csv', sep=";" )
    
    # For each region, for each year count the number of accidents and deaths and create the rate by combining the data with those of the
    # dataset "employed by region"
    for region in regions :
        
        for year in range( 2013, 2019 ) :
                          
            # Count the total number of accidents at work occurred in the current
            n_accidents = total_accidents[ ( ( total_accidents['Region'] == region ) &
                                             ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) ) ].count()['Accident Date']
            
            # Count the number of deaths at work occurred in the current region and year
            n_deaths = total_accidents[ ( ( total_accidents['Region'] == region ) &
                                          ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) &
                                          ( total_accidents['Death Date'].notna() ) ) ].count()['Accident Date']
            
            # Combine the dataset which contains the employed people for the current year in order to compute the rates
            for index, val in employed_by_region.iterrows() :
                               
                # We check only the first six characters of the region' name because it could be slitghly different from those contained
                # in the dataset of the accidents since they have kept from two different sources (INAIL >> accidents | ISTAT >> employed )
                if region[:5] in val[ 0 ] :
                    
                    # Add the rate of the total accidents over the employed people for the current region and year
                    accidents_rate = n_accidents * 100 / val['Total (thousands)']
                    
                    # Add the rate of the deaths over the employed people for the current region and year
                    deaths_rate = n_deaths * 100 / val['Total (thousands)']
                    
            # Transform each rate in a more readable format (the library Decimal helps us to perform a precise approximation)
            accidents_rate = round( decimal.Decimal( accidents_rate * 10 ) , 2 )
            deaths_rate = round( decimal.Decimal( deaths_rate * 1000 ) , 2 )
            
            print("Region:", region, "| Year:", year, "| Accidents:", n_accidents, "- Rate:", accidents_rate,
                  "| Deaths:", n_deaths, "- Rate:", deaths_rate)
            
            # Concatenate a new row to the DataFrame 'rates_by_region' in order to build a normalized visualization of the regions
            # (then we add the appropriate rate obtained by computing the proportion with the number of people employed in that region
            # for that year)
            row = pd.DataFrame( [[ region, year, n_accidents, accidents_rate, n_deaths, deaths_rate ]] )
            rates_by_region = pd.concat( [ rates_by_region, row ] )
        
        # Creating a new line in order to separate each region in the Jupyter Notebook visualization (main.ipynb)
        print()
    
    # Rename the columns
    rates_by_region.columns = ['Region', 'Year', 'Total Accidents', 'Accidents Rate', 'Total Deaths', 'Deaths Rate' ]
    return rates_by_region


def rates_Sector( rates_by_sector, total_accidents ) :

    # Since the macro-category included in the columns of all the accidents group categories in a different manner with respect to thE
    # grouping adoperated by the dataset which contain the number of people employed by sector - i.e. education and healthcare in a
    # classification and education and public serviced in the other - we create a dictionary which will link the micro-sector with the
    # macro-sector according our favourite classification of the sectors - that of the dataset with the number of people employed by sector

    # We build a dictionary which contain as key
    # the macro-sector and as value a list with all its micro-sectors
    
    dic_sectors = {
        
        # KEY
        "agricoltura, silvicoltura e pesca" :
        # __value
        ["Silvicoltura ed utilizzo di aree forestali","Coltivazioni agricole e produzione di prodotti animali, caccia e servizi connessi","Pesca e acquacoltura"],

        # KEY
        "industria" :
        # __value
        ["Industrie alimentari","Fabbricazione di altri prodotti della lavorazione di minerali non metalliferi","Fabbricazione di autoveicoli, rimorchi e semirimorchi","Industria del legno e dei prodotti in legno e sughero (esclusi i mobili), fabbricazione di articoli in paglia e materiali da intreccio","Industrie tessili","Fabbricazione di macchinari ed apparecchiature nca","Fabbricazione di mobili","Fabbricazione di prodotti in metallo (esclusi macchinari e attrezzature)","Fabbricazione di articoli in gomma e materie plastiche","Fabbricazione di carta e di prodotti di carta","Confezione di articoli di abbigliamento, confezione di articoli in pelle e pelliccia","Metallurgia","Altre attivita' di estrazione di minerali da cave e miniere","Fabbricazione di apparecchiature elettriche ed apparecchiature per uso domestico non elettriche","Fabbricazione di computer e prodotti di elettronica e ottica, apparecchi elettromedicali, apparecchi di misurazione e di orologi","Fabbricazione di altri mezzi di trasporto","Fabbricazione di prodotti chimici","Altre industrie manifatturiere","Fabbricazione di prodotti farmaceutici di base e di preparati farmaceutici","Industria delle bevande","Fabbricazione di coke e prodotti derivanti dalla raffinazione del petrolio","Fabbricazione di articoli in pelle e simili","Attivita' dei servizi di supporto all'estrazione","Estrazione di petrolio greggio e di gas naturale","Attivita' di produzione cinematografica, di video e di programmi televisivi, di registrazioni musicali e sonore","Industria del tabacco","Estrazione di minerali metalliferi","Estrazione di carbone (esclusa torba)"],

        # KEY
        "costruzioni" :
        # __value
        ["Lavori di costruzione specializzati","Costruzione di edifici","Ingegneria civile"],
        
        # KEY
        "commercio all'ingrosso e al dettaglio, riparazione di autoveicoli e motocicli" :
        # __value
        ["Commercio all'ingrosso (escluso quello di autoveicoli e di motocicli)","Commercio all'ingrosso e al dettaglio e riparazione di autoveicoli e motocicli","Commercio al dettaglio (escluso quello di autoveicoli e di motocicli)"],
        
        # KEY
        "trasporto e magazzinaggio" :
        # __value
        ["Trasporto terrestre e trasporto mediante condotte","Servizi postali e attivita' di corriere","Magazzinaggio e attivita' di supporto ai trasporti","Trasporto aereo","Trasporto marittimo e per vie d'acqua"],
        
        # KEY
        "attività dei servizi di alloggio e di ristorazione" :
        # __value
        ["Alloggio","Attivita' dei servizi di ristorazione","Attivita' dei servizi delle agenzie di viaggio, dei tour operator e servizi di prenotazione e attivita' connesse"],
        
        # KEY
        "servizi di informazione e comunicazione" :
        # __value
        ["Telecomunicazioni","Attivita' dei servizi d'informazione e altri servizi informatici","Attivita' editoriali","Attivita' di programmazione e trasmissione"],
        
        # KEY
        "attività finanziarie e assicurative" :
        # __value
        ["Attivita' di servizi finanziari (escluse le assicurazioni e i fondi pensione)","Assicurazioni, riassicurazioni e fondi pensione (escluse le assicurazioni sociali obbligatorie)","Attivita' ausiliarie dei servizi finanziari e delle attivita' assicurative"],
        
        # KEY
        "servizi alle imprese" :
        # __value
        ["Attivita' di direzione aziendale e di consulenza gestionale","Attivita' di supporto per le funzioni d'ufficio e altri servizi di supporto alle imprese","Attivita' di ricerca, selezione, fornitura di personale","Pubblicita' e ricerche di mercato"],
        
        # KEY
        "amministrazione pubblica e difesa, assicurazione sociale obbligatoria" :
        # __value
        ["Amministrazione pubblica e difesa, assicurazione sociale obbligatoria"],

        # KEY
        "istruzione e sanità" :
        # __value
        ["Assistenza sanitaria","Istruzione"],

        # KEY
        "altri servizi collettivi e personali" :
        # __value
        ["Altre attivita' professionali, scientifiche e tecniche","Altre attivita' di servizi per la persona","Attivita' di raccolta, trattamento e smaltimento dei rifiuti, recupero dei materiali","Servizi di vigilanza e investigazione","Raccolta, trattamento e fornitura di acqua","Attivita' di servizi per edifici e paesaggio","Attivita' sportive, di intrattenimento e di divertimento","Attivita' di noleggio e leasing operativo","Attivita' di risanamento e altri servizi di gestione dei rifiuti","Riparazione di computer e di beni per uso personale e per la casa","Riparazione, manutenzione ed installazione di macchine ed apparecchiature","Servizi di assistenza sociale residenziale","Assistenza sociale non residenziale","Stampa e riproduzione di supporti registrati","Attivita' immobiliari","Ricerca scientifica e sviluppo","Fornitura di energia elettrica, gas, vapore e aria condizionata","Attivita' di organizzazioni associative","Attivita' di biblioteche, archivi, musei ed altre attivita' culturali","Attivita' di biblioteche, archivi, musei ed altre attivita' culturali","Produzione di software, consulenza informatica e attivita' connesse","Attivita' legali e contabilita'","Attivita' degli studi di architettura e d'ingegneria, collaudi ed analisi tecniche","Attivita' creative, artistiche e di intrattenimento","Gestione delle reti fognarie","Servizi veterinari","Produzione di beni e servizi indifferenziati per uso proprio da parte di famiglie e convivenze","Organizzazioni ed organismi extraterritoriali","Attivita' di famiglie e convivenze come datori di lavoro per personale domestico"]
        
    }
     
    # Load the dataset of the number of people employed by sector and by year
    employed_by_sector = pd.read_csv( 'datasets/others/occupati_settore.csv', sep=";" )
    
    # Transform the number of people employed of the current year from float to int (and multiply them by 1000)
    for year in range( 2013, 2019 ) :
        employed_by_sector[ str( year) ] = employed_by_sector[ str( year) ].apply( lambda x: x*1000 ).astype( int )
        
    
    # Creating a new line in order to separate the combining operation of the regions from that of the sectors in the Jupyter Notebook
    # visualization (main.ipynb)
    print("\n\n")
    
    for key, sector in dic_sectors.items() :

        for year in range( 2013, 2019 ) :
            
            # Count the total number of accidents at work occurred in the current year and in the current macro-sector
            n_accidents = total_accidents[ ( ( total_accidents['Sector'].isin( sector ) ) &
                                             ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) ) ].count()['Accident Date']

            # Count the number of deaths at work occurred in the current region and year
            n_deaths = total_accidents[ ( ( total_accidents['Sector'].isin( sector ) ) &
                                          ( total_accidents['Accident Date'].str.endswith( str( year ) ) ) &
                                          ( total_accidents['Death Date'].notna() ) ) ].count()['Accident Date']

            # Combine the dataset which contains the employed people for the current sector and year in order to compute the rates
            for index, val in employed_by_sector.iterrows() :

                # We check only the first eight characters in order to gain efficiency by making quicker the research
                if key[:8] in val[ 0 ] :
                    
                    # Add the rate of the total accidents over the employed people for the current sector and year
                    accidents_rate = n_accidents * 100 / val[ str( year) ]

                    # Add the rate of the deaths over the employed people for the current sector and year
                    deaths_rate = n_deaths * 100 / val[ str( year ) ]

            # Transform each rate in a more readable format (the library Decimal helps us to perform a precise approximation)
            accidents_rate = round( decimal.Decimal( accidents_rate * 100 ) , 2 )
            deaths_rate = round( decimal.Decimal( deaths_rate * 1000 ) , 2 )

            print("Sector:", key, "| Year:", year, "| Accidents:", n_accidents, "- Rate:", accidents_rate, "| Deaths:", n_deaths,
                  "- Rate:", deaths_rate)

            # Concatenate a new row to the DataFrame 'rates_by_sector' in order to build a normalized visualization of the regions
            # (then we add the appropriate rate obtained by computing the proportion with the number of people employed in that region
            # for that year)
            row = pd.DataFrame( [[ key, year, n_accidents, accidents_rate, n_deaths, deaths_rate ]] )
            rates_by_sector = pd.concat( [ rates_by_sector, row ] )
    
        # Creating a new line in order to separate each sector in the Jupyter Notebook visualization (main.ipynb)
        print()
    
    # Rename the columns
    rates_by_sector.columns = ['Sector', 'Year', 'Total Accidents', 'Accidents Rate', 'Total Deaths', 'Deaths Rate' ]
    return rates_by_sector
    
