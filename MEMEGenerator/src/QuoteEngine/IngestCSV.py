from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List

import pandas as pd

class CSVIngest(IngestorInterface):
    """Subclass of IngestorInterface specific for .csv files.

    Interfaces with QuoteModel class for quote formatting.
    """

    ingestMode =['csv']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Returns a list of formated quote and author from a .csv file.

        Subclass of IngestorInterface class.
        Interfaces with QuoteModel class for quote formatting.
        Will raise an exception if used for file type other than .csv.
        Parameters: filepath (str)
        """

        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Error')

        if cls.can_ingest(path):
            quotes = []

            data = pd.read_csv(path,header=0)

            for index,row in data.iterrows():
                new_quote = QuoteModel(row['body'], row['author'])
                quotes.append(new_quote)

            return quotes
