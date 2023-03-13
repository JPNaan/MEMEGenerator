from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List

import subprocess
import os
import random



class PDFIngest(IngestorInterface):
    """Subclass of IngestorInterface specific for .docx files."""

    ingestMode =['pdf']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Returns a list of formated quote and author from a .pdf file.

        Subclass of IngestorInterface class.
        Will raise an exception if used for file type other than .pdf.
        Parameters: filepath (str)
        """

        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Error')

        quotes = []

        tmp_dir = random.randint(0,1000000000000)
        tmp_filename = random.randint(0,1000000000000)
        tmp_file = f'{os.getcwd()}/{tmp_dir}/{tmp_filename}.txt'
        os.mkdir(f'{tmp_dir}')

        call = subprocess.call(
            ['/Applications/xpdf-tools-mac-4.04/bin64/pdftotext',
            '-layout',
            path,
            tmp_file])

        f = open(tmp_file,'r')

        lines = f.readlines()
        for line in lines:
            if len(line.strip())>0:
                q = line.split('-')[0].strip('" ""\n\r').strip()
                a = line.split('-')[1].strip('" ""\n\r').strip()
                quotes.append(QuoteModel(q,a))

        f.close()
        os.remove(tmp_file)
        os.rmdir(f'{tmp_dir}')

        return(quotes)
