from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import re

from docx import Document

class DocxIngest(IngestorInterface):
    """Subclass of IngestorInterface specific for .docx files."""

    ingestMode =['docx']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Returns a list of formated quote and author from a .docx file.

        Subclass of IngestorInterface class.
        Will raise an exception if used for file type other than .docx.
        Parameters: filepath (str)
        """

        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Error')

        quotes = []

        with open(path,'r') as f:
            doc = Document(path)

        for para in doc.paragraphs:
            if len(para.text)>0:
                q = para.text.split('-')[0].strip('" ""\n\r').strip()
                a = para.text.split('-')[1].strip('" ""\n\r').strip()
                quotes.append(QuoteModel(q,a))

        return quotes
