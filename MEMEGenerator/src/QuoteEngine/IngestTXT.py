from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TXTIngest(IngestorInterface):
    """Subclass of IngestorInterface specific for .docx files."""

    ingestMode =['txt']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Returns a list of formated quote and author from a .txt file.

        Subclass of IngestorInterface class.
        Will raise an exception if used for file type other than .txt.
        Parameters: filepath (str)
        """

        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Error')

        if path.split('.')[-1] not in cls.ingestMode:
            raise Exception('Exception:  filetype')

        quotes = []

        with open(path, 'r') as f:
            file = f.readlines()

        for line in file:
            if len(line.strip('" ""\n\r').strip()) > 0:
                q = line.split('-')[0].strip('" ""\n\r').strip()
                a = line.split('-')[1].strip('" ""\n\r').strip()
                quotes.append(QuoteModel(q,a))

        return quotes
