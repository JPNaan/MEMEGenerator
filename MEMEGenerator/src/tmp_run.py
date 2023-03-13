from QuoteEngine import CSVIngest,DocxIngest,TXTIngest,PDFIngest
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

if __name__ == "__main__":
    for mode in [CSVIngest, DocxIngest, TXTIngest, PDFIngest]:
        ext = mode.__name__[:-6].lower()

        print(f'{ext.upper()} Parse: \n _________________')
        quotes = (Ingestor.parse(
                './_data/SimpleLines/SimpleLines.'+ext))

        for quote in quotes:

            print(type(quote),': ',quote)

        print('_________________')


    test_meme = MemeEngine('./tmp')

    test_meme.make_meme('./_data/photos/dog/xander_1.jpg',
                    'Try out a quote.',
                    'me',
                    width=500)
