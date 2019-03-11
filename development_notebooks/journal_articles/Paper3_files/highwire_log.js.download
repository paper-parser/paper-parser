/**
 * @file
 * Highwire Log Javascript
 *
 * Copyright (c) HighWire Press, Inc.
 * This software is open-source licensed under the GNU Public License Version 2
 * or later. The full license is available in the LICENSE.TXT file at the root
 * of this repository.
 */


(function ($) {
  // Store our function as a property of Drupal.behaviors.
  Drupal.behaviors.highwire_log = { attach: function (context, settings) {
    $('.service-links a').each(function() {
      if(!$(this).is('#twitter_widget') && !$(this).is('#facebook_like') && !$(this).is('#google_plus_one')) {
        if (typeof $(this).attr('data-log-redirect-set') == 'undefined') {
          $(this).attr('href', '/highwire_log/share/' + $(this).attr('id') + '?link=' + encodeURIComponent($(this).attr('href')));
          $(this).attr('data-log-redirect-set', true);
        }
      }
    });

    // If advanced logging is enabled, we will have appended an object with appropriate
    // information to Drupal.settings.  It may also have authentication data, if
    // ac_override hasn't been triggered.
    if (typeof(Drupal.settings.highwire_log) != "undefined" && Drupal.settings.highwire_log !== null) {
      // Check for run flag, so we're not submitting the entry multiple times per page
      if (Drupal.settings.highwire_log.has_run != true) {
        requestData = {};
        // Initial logging settings are key => encrypted_value pairs in Drupal.settings
        $.each( Drupal.settings.highwire_log.userdata, function (param, value) {
          requestData[param] = value;
        });
        if (Drupal.settings.highwire_log.auth != null) {
           $.each( Drupal.settings.highwire_log.auth, function (param, value) {
            requestData[param] = value;
          });
        }

        if (requestData) {
          $.ajax({
              url: '/highwire_log/submit',
              type: 'POST',
              cache: false,
              data: requestData,
              dataType: 'json',
              success: function(msg){
                // debug line
                //console.log(msg);
              }
          });
        } else {
          //debug line
          //console.log('No logging request is attached');
        }
        // Add flag
        Drupal.settings.highwire_log.has_run = true;
      }
    }
  }};
}(jQuery));
