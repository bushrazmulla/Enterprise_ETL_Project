from sqlalchemy import create_engine
from src.config import *


class DataLoader:

    def load_to_mysql(self, dataframe, table_name):

        connection_string = (
            f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}"
            f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

        engine = create_engine(connection_string)

        dataframe.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        print(f"✅ Loaded {len(dataframe)} records into '{table_name}'")