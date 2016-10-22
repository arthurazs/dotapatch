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
