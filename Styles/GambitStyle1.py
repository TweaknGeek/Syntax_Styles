from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Name, String, Generic, Number, Operator, Punctuation, Text, Literal, Error
class BrightStyle(Style):
    styles = {
        Token:              '',
        Comment:            'italic #AA9363',
        Keyword:            'bold #FC3411',
        Name:               'bold #11D9FC',
        String:             'bold #712ead',
        Generic:            'bold #2ea9ad',
        Number:             'bold #ac332e',
        Operator:           'bold #1026CA',
        Punctuation:        'bold #CAB510',
        Text:               'bold #10CA58',
        Literal:            'bold #X1083',
        Error:              'bold #FF0507'
    }
