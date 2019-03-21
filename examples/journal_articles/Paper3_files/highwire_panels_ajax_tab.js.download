/**
 * @file
 * HW PDF tab treatment.
 *
 * Copyright (c) HighWire Press, Inc.
 * This software is open-source licensed under the GNU Public License Version 2 or later
 * The full license is available in the LICENSE.TXT file at the root of this repository
 */
(function ($) {
  Drupal.behaviors.highwire_panels_ajax_tab = {
    attach: function (context, settings) {
      $('a.panels-ajax-tab-tab', context, settings).once('hw-panels-ajax-tabs-once', function() {
        if (typeof(settings.highwire_panel_tabs) != "undefined") {
          for (var i = settings.highwire_panel_tabs.length -1; i >= 0; i--) {
            var panel_name = settings.highwire_panel_tabs[i].panel_name;
            if ($(this).data('panel-name') == panel_name) {
              $(this).unbind('click').attr('target', '_blank');
            }
          }
        }
      });
      $('a.highwire-article-nav-jumplink', context, settings).once('hw-panels-ajax-tabs-once', function() {
        if (typeof(settings.highwire_panel_tabs) != "undefined") {
          var panel_ajax_tab = settings.highwire_panel_tabs.panel_ajax_tab;
          if ($(this).data('panel-ajax-tab') == panel_ajax_tab) {
            $(this).unbind('click').attr('target', '_blank');
          }
        }
      });
    }
  };
})(jQuery);
