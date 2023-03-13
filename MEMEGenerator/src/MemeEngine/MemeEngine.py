from PIL import Image, ImageDraw, ImageFont
from QuoteEngine import QuoteModel
import os
import random

class MemeEngine:
    """Creates a meme from an image and quote."""

    def __init__(self, output_dir:str):
        """Creates a location for Meme generation."""

        if os.path.exists(output_dir) == False:
            os.mkdir(f'./{output_dir}')

        self.output_dir = output_dir

    def make_meme(self, img_path:str,
                    text:str,
                    author:str,
                    width=500)->str:
        """Generates a meme.

        Parameters:
        -img_path (str): Path to image for Meme. Image must be .png
            or .jpeg
        -text (str): Quote text, can interface with QuoteEngine's
            QuoteModel.
        -author (str): Quote text, can interface with QuoteEngine's
            QuoteModel.
        -width (int): Image width.  Defaults to 500.

        Returns path to meme image.
        """

        img = Image.open(img_path)
        ext = img_path.split('.')[-1]
        out_path = f'{self.output_dir}/{random.randint(0,100000000000000)}.{ext}'

        if width is not None:
            ratio = width/ float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width,height),Image.NEAREST)

        meme = ImageDraw.Draw(img)
        message = QuoteModel(text, author)
        location = random.choice([(width//10,int(height*.82)),
                        (width//10,int(height*.12))])
        font = ImageFont.truetype("Chalkduster.ttf",int(height*.03))

        meme.text(location,
                    str(message),
                    font = font,
                    align='center',
                    fill='white' )
        img.save(out_path)
        img.close()

        return(out_path)
