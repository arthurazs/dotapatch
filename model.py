class Html (object):
    def __init__(self, title):
        self._title = title
        self._bgStyle = False
        self._content = r'''<!DOCTYPE html>
<html>
    <head>
        <title>dota2patches ''' + self._title + r''' by @arthurazs</title>

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
                <h1>Gameplay Update ''' + self._title + r'''</h1>
                <h3><a href="index.html">Previous changelogs</a></h3>
            </div>
        </div>
'''

    def addHero(self, dictionary):
        self._content = self._content + r'''
        <div class="Container RepeatY BGStyle''' + str(int(self._bgStyle)) + r'''" id="Heroes">
             <div class="Inner">
                <h3>Heroes</h3>'''

        self._content = self._content + r'''
            </div>
        </div>'''
        self._bgStyle = not self._bgStyle

    def close(self):
        self._content = self._content + r'''
        <div class="Container" id="Footer">
            <div class="Inner"></div>
        </div>
    </body>
</html>'''

    def getContent(self):
        return self._content
