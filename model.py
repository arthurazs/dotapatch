

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
        <script>
            $( function () {
                var URL = ( location.protocol == 'https:' ) ? 'https://www.dota2.com/' : 'http://www.dota2.com/';
                URL = URL + 'jsfeed/heropediadata?feeds=herodata,itemdata';
                $.ajax(
                    {
                        type:'GET',
                        cache:true,
                        url: URL,
                        dataType:'jsonp',
                        success: function( data )
                        {
                            g_HeroData = data['herodata'];
                            g_ItemData = data['itemdata'];
                            formatHeroAndItemNotes();
                        }
                    }
                );
            } );

            var g_HeroData = false;
            var g_ItemData = false;
            function formatHeroAndItemNotes()
            {
                $.each( ['items','heroes'], function( i, type ) {
                    var containers = ['#Heroes','#Items'];
                    for ( i = 0; i < containers.length; i++ )
                    {
                        container = containers[i];
                        var strContents = $(container).html();
                        if ( strContents )
                        {
                            var foundTags = strContents.match( /\[\[\w+\]\]/g );
                            if ( foundTags )
                            {
                                for ( x = 0; x < foundTags.length; x++ )
                                {
                                    tag = foundTags[x];
                                    tag = tag.substring( 2, tag.length-2 );
                                    bUnfound = false;
                                    if ( g_ItemData[tag] )
                                    {
                                        path = 'items/'+tag+'_lg.png';
                                        name = g_ItemData[tag].dname;
                                        hw = 'width="48" height="36"';
                                    }
                                    else if ( g_HeroData[tag] )
                                    {
                                        path = 'heroes/'+tag+'_sb.png';
                                        name = g_HeroData[tag].dname;
                                        hw = '';
                                    }
                                    else
                                    {
                                        bUnfound = true;
                                    }
                                    if ( !bUnfound )
                                    {
                                        var strHTML = '<div class="ChangeNoteImage"><img src="http://cdn.dota2.com/apps/dota2/images/'+path+'" '+hw+' /></div><br style="clear: left;"/>';
                                        strHTML += '<b>' + name + '</b>';
                                        strContents = strContents.replace( foundTags[x], strHTML );
                                    }
                                }
                                $(container).html( strContents );
                            }
                        }
                    }
                });

                var eCount = 0;
                $( '.ChangeDetailsExtended' ).each( function() {
                    var $extended = $( this );
                    $extended.attr( 'id', 'extended'+eCount );
                    $extended.before( '<a href="#" class="ChangeDetailsEToggle" id="eToggle'+eCount+'" onclick="$(\'#extended'+eCount+'\').show();$(this).hide();return false;">+ Show Details</a>' );
                    $extended.html( '<a href="#" id="eToggleHide'+eCount+'" class="ChangeDetailsEToggle HideButton" onclick="$(\'#extended'+eCount+'\').hide();$(\'#eToggle'+eCount+'\').show();return false;">- Hide Details</a>' + $extended.html() );
                    eCount++;
                } );
                $( '.ChangeDetailsPopup' ).each( function() {
                    var $popup = $( this );
                    var $popupHoverButton = $( '<a href="#">[?]</a>' );
                    $popup.before( $popupHoverButton );
                    $popupHoverButton.hover( function() {
                        $popup.css( "display", "block" );
                    }, function() {
                        $popup.css( "display", "none" );
                    });
                    $popupHoverButton.click( function() {
                        // Suppress the click event
                        return false;
                    });
                } );
            }
        </script>
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
