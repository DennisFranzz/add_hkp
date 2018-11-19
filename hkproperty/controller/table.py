import locale

from flask_table import Col


class PriceCol(Col):
    def td_format(self, content):
        if content is not None and content != '':
            return format_price(content)
        else:
            return content


def format_price(text):
    locale.setlocale( locale.LC_ALL, '' )
    text = locale.currency( text, grouping=True )
    return text;