Overview
The MemeGenerator application will generate random memes from system files.  

Meme Quotes can be ingested from .txt, .pdf, .csv, .docx filetypes provided the file contains a single line quote and author in the format of "'quote' - Author".

Meme images can be generated from any filepath to a .jpg or .png file.

Instructions
The application can be run from command line using:
  >> python3 meme.py --path <image_path> --body <quote body> --author <quote author>

Basic unit tests to validate file ingestion and a meme generation can be performed using the command line:
>> python3 tmp_run.py

The application can be run as a web app launced from command line:
>> python3 app.py


Application workflows
The quotes are governed by the QuoteEngine module.  The QuoteModel class is the quote object that maintains the body and author as class instance attributes.  The Ingestor class will ingest files to return a list of QuoteModel objects. It will determine the appropriate ingestor subclass from IngestCSV, IngestDocx, IngestTXT, or IngestPDF based upon the filetype for the file to be ingested.  Each of the subclasses is an instance of the IngestorInterface abstract base class.

The memes are generated from the MemeEngine, and will leverage the QuoteEngine as needed.  The MemeEngine class is instantiated using a director location for the generated memes.  The MemeEngine.make_meme() method generates the meme given the image path, quote body and quote author.  There is also the ability to resize the meme with the default size set to 500.
