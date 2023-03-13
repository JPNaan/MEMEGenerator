class QuoteModel:
    """Returns a formated quote and author."""

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __str__(self):
        return f'"{self.body}" -{self.author}'
