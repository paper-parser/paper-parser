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
  Drupal.behaviors.highwire_user_meta_add = { attach: function (context, settings) {
    $.ajax({
      url: '/highwire/sub-data',
      type: 'POST',
      cache: false,
      dataType: 'json',
      success: function(msg){
        // Add the user subscription info.
        if ($('script[id="user"]').length == 0) {
          var s = document.createElement('script');
          s.type = 'application/json'
          s.id = 'user'
          s.text = JSON.stringify(msg)
          // Add user data at the end of the meta tags, so we keep page data tidy
          $(s).insertAfter($('meta').last())
        }
      }
    });
  }}
}(jQuery));
