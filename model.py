from data import HeropediaData

class Html (object):

    #Initialization
    def __init__(self, title):
        self._title = title
        self._bgStyle = False
        self._content = r'''<!DOCTYPE html>
<html>
    <head>
        <title>dota2patches {0} by @arthurazs</title>

        <link rel="shortcut icon" href="favicon.ico" />

        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=9" />

        <link href="css/global.css" rel="stylesheet" type="text/css" >
        <link href="css/global_english.css" rel="stylesheet" type="text/css" >
        <link href="css/changelog.css" rel="stylesheet" type="text/css" >

        <script type="text/javascript" src="javascript/jquery-1.7.1.min.js"></script>
        <script type="text/javascript">$J = jQuery;</script>
        <script src="javascript/fetch_heropediadata.js"></script>
    </head>

    <body>
        <div class="Container" id="KeyArt">
            <div class="Inner">
                <a href="http://www.dota2.com/"><img src="http://cdn.dota2.com/apps/dota2/images/springcleaning2016/logo.png" /></a>
            </div>
        </div>

        <a class="HiddenAnchor" name="GameplayHeader"> </a>
        <div class="Container" id="Header">
            <div class="Inner" style="text-align:center">
                <h1>Gameplay Update {0}</h1>
                <h3><a href="index.html">Previous changelogs</a></h3>
            </div>
        </div>
'''.format(self._title)

    #Default function for adding content
    def _addContent(self, text):
        self._content = self._content + text

    #Add GENERAL Contents
    def addGeneral(self, lines):
        if(lines):
            self._addContent(r'''
        <div class="Container RepeatY BGStyle{}">
            <div class="Inner">
                <h3>General</h3>'''.format(int(self._bgStyle)))

            self._addContent(r'''

                    <ul>''')
            for line in lines:
                self._addContent(r'''
                    <li>{}</li>'''.format(line))
            self._addContent(r'''
                    </ul>
''')

            self._addContent(r'''
            </div>
        </div>''')
            self._bgStyle = not self._bgStyle

    #Add ITEMS Contents
    def addItems(self, dictionary):
        if(dictionary):
            self._addContent(r'''
        <div class="Container RepeatY BGStyle{}" id="Items">
            <div class="Inner">
                <h3>Item changes</h3>'''.format(int(self._bgStyle)))

            for key, values in sorted(dictionary.items()):
                self._addContent(r'''

                    [[{}]]
                    <ul>'''.format(key))
                for value in values:
                    self._addContent(r'''
                        <li>{}</li>'''.format(value))
                self._addContent(r'''
                    </ul>
''')

            self._addContent(r'''
            </div>
        </div>''')
            self._bgStyle = not self._bgStyle

    #Add HERO Contents
    def addHeros(self, dictionary):
        if(dictionary):
            self._addContent(r'''
        <div class="Container RepeatY BGStyle{}" id="Heroes">
             <div class="Inner">
                <h3>Heroes</h3>'''.format(int(self._bgStyle)))

            for key, values in sorted(dictionary.items(), key=HeropediaData.sort):
                self._addContent(r'''

                    [[{}]]
                    <ul>'''.format(key))
                for value in values:
                    self._addContent(r'''
                        <li>{}</li>'''.format(value))
                self._addContent(r'''
                    </ul>
''')

            self._addContent(r'''
            </div>
        </div>''')
            self._bgStyle = not self._bgStyle

    #Closes the HTML
    def close(self):
        self._addContent(r'''
        <div class="Container" id="Footer">
            <div class="Inner"></div>
        </div>
    </body>
</html>''')

    #Returns HTML Content
    def getContent(self):
        return self._content
