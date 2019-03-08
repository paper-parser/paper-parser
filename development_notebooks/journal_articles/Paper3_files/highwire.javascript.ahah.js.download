/**
 * @file
 * General HighWire AHAH Callback
 *
 * Copyright (c) 2010-2011 Board of Trustees, Leland Stanford Jr. University
 * This software is open-source licensed under the GNU Public License Version 2 or later
 * The full license is available in the LICENSE.TXT file at the root of this repository
 */

/**
 * Using jQuery, load content via AJAX
 */

(function ($) {
  // Store our function as a property of Drupal.behaviors.
  Drupal.behaviors.highwire_ahah = { attach: function (context, settings) {
    for (i in Drupal.settings.highwire_ahah) {
      $('#'+i+':not(.highwire-ahah-processed)').each(function() {
        $(this).addClass('highwire-ahah-processed');
        $(this).load(Drupal.settings.highwire_ahah[i]);
      });
    }
  }};
}(jQuery));
