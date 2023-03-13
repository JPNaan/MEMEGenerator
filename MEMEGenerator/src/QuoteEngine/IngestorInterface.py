from typing import List
from abc import ABC
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Abstract class used by specific ingestor classes."""

    ingestMode =[]

    @classmethod
    def can_ingest(cls, path:str) -> bool:
        """Returns true if path filetype can be ingested."""
        file_type = path.split('.')[-1]

        return file_type in cls.ingestMode

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Returns a list of formated quotes with author.

        Implemented at the subclass level.
        """
        
        pass
