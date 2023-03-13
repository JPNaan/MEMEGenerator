from QuoteEngine import CSVIngest,DocxIngest,TXTIngest,PDFIngest

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    """Subclass of IngestorInterface.

    Interfaces with CSVIngest class as necessary.
    Interfaces with DocxIngest class as necessary.
    Interfaces with TXTIngest class as necessary.
    Interfaces with PDFIngest class as necessary.
    """

    ingestMode = ['csv', 'docx', 'txt', 'pdf']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Returns a formated quote and author from a file.

        Will interface with the appropriate ingestor class and is able to Parse
        .csv, .docx, .txt, .pdf file types.
        Parameters: filepath(str)
        """

        quotes = []

        ext = path.split('.')[2]

        for mode in [CSVIngest, DocxIngest, TXTIngest, PDFIngest]:
            if ext == mode.__name__[:-6].lower():
                quotes = mode.parse(path)

        return quotes
