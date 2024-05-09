from sqlalchemy import create_engine

username = 'OliviaJYang'
password = 'springds2024'
host = '127.0.0.1'
port = '3306'  
database_name = 'rentaldb'

#create SQLAlchemy engine object to connect to database
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}") 

import pandas as pd

query = "SELECT * FROM PropertyDetails"
prop_det_df = pd.read_sql(query, con=engine)
prop_det_df.head()

from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you are quiet'      
    elif 'help' in lowered:
        return '''Welcome to the Property Bot! 
            Use game to start a game where you guess what a random house's residential id is ranging from 1-5 
            with 1-4 indicating how many separate living spaces it's split into and 5 being none
            
            Use price to see the sale price of a house 
            given its property id ranging from 21973 - 26814
            
            Use proptaxrate tp see the property tax rate of a house 
            given its property id ranging from 21973 - 26814'''

    elif 'game' in lowered:
        return "Guess the random house's residential id"
        
    elif 'price' in lowered:
        return 'Enter property id ranging from 21973 - 26814 for its price'
    elif 'proptaxrate' in lowered:
        return 'Enter property id ranging from 21973 - 26814 for its property tax rate'
    else:
        return "Incoherrent input, type help for suggestions"
        