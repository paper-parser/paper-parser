/**
 * @file
 * Highwire User Meta Data Additions JS
 *
 * Copyright (c) HighWire Press, Inc.
 * This software is open-source licensed under the GNU Public License Version 2
 * or later. The full license is available in the LICENSE.TXT file at the root
 * of this repository.
 */

(function ($) {
  // Store our function as a property of Drupal.behaviors.
  Drupal.behaviors.jnl_sci_user_data_add = { attach: function (context, settings) {
    var digitalData = JSON.parse(Drupal.settings.highwire.digitalData)

    // Use a callback to look up user data
    $.ajax({
      url: '/highwire/sub-data',
      type: 'POST',
      cache: false,
      dataType: 'json',
      success: function(msg){
        // Grab the data stored in digitalData
        $.extend(true, digitalData['page']['member'], msg)

        var s = document.createElement('script');
        s.type = 'text/javascript'
        s.id = 'digitalData'
        s.text = '<!--//--><![CDATA[//><!--\ndigitalData = ' + JSON.stringify(digitalData) + '\n//--><!]]>'

        // Write the combined data to the page
        if ($('script[id="digitalData"]').length == 0) {
          // This looks gross, but reasonable methods all failed stupidly
          // @SEE https://www.sitepoint.com/community/t/how-can-i-insert-adsense-code-with-jquerys-insertafter/25889/2
          document.getElementById('sci-footer-end').parentNode.insertBefore(s, document.getElementById('sci-footer-end').nextSibling)
        }
        else {
          $('script[id="digitalData"]').text(s.text)
        }
      }
    });

    // Write the combined data to the page
    if ($('script[id="digitalData"]').length == 0) {
      var s = document.createElement('script');
      s.type = 'text/javascript'
      s.id = 'digitalData'
      s.text = '<!--//--><![CDATA[//><!--\ndigitalData = ' + JSON.stringify(digitalData) + '\n//--><!]]>'
      // This looks gross, but reasonable methods all failed stupidly
      // @SEE https://www.sitepoint.com/community/t/how-can-i-insert-adsense-code-with-jquerys-insertafter/25889/2
      document.getElementById('sci-footer-end').parentNode.insertBefore(s, document.getElementById('sci-footer-end').nextSibling)
    }
  }}
}(jQuery));
