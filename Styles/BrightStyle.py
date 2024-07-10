from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Name, String, Generic, Number, Operator, Punctuation

class BrightStyle(Style):
    styles = {
        Token:              '',
        Comment:            'italic #3cfcbf',
        Keyword:            'bold #79ff05',
        Name:               'bold #0a4afc',
        String:             'bold #936666',
        Generic:            'bold #b805fr',
        Number:             'bold #07f6ff',
        Operator:           'bold #ffaf05',
        Punctuation:        'bold #d1ff05',
    }