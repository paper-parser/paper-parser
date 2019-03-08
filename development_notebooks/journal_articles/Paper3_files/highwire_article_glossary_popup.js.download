/**
 * Highwire Article References pop up
 *
 * Copyright (c) HighWire Press, Inc.
 * This software is open-source licensed under the GNU Public License Version 2 or later
 * The full license is available in the LICENSE.TXT file at the root of this repository
 */
 
 (function ($) {
  Drupal.behaviors.articleGloPopup = {
    attach: function(context, settings) {
      var instances = (settings.instances != undefined) ? $.parseJSON(settings.instances) : false;
      if (!instances) {
        return;
      }
      $("body", context).delegate("a.xref-list[href]:not(.hasTooltip):not(.hw-no-reference)", "mouseenter", function (event) {
        var elem = $(this);
        var parent = elem.parents('[data-highwire-glossary-tooltip-instance]');
        var defId = elem.attr("href").replace('#def', 'def-item');
        var defElem = $('#' + defId + '+dd');
        var instance = parent ? parent.data('highwire-glossary-tooltip-instance') : 'highwire_reflinks_tooltip';
        var tipSettings = (instances[instance] != undefined) ? instances[instance] : '';

        if (!tipSettings || !defElem.length) {
          elem.addClass("hw-no-reference");
          return;
        }

        // Merge in additional settings to tooltip instance settings.
        var addSettings = {
          show: {
            // "Ready" makes qTip show as soon as it is bound.
            ready: true,
          },
          position: {
            viewport: $(window),
          },
          events: {
            show: function(event, api) {
              // Disable for mobile
              var activate = true;
              if (Drupal.highwireResponsive) {
                var currentLayout = Drupal.highwireResponsive.getCurrentLayout();
                activate = currentLayout !== 'mobile' ? true : false;
              }
              return activate;
            }
          },
          content: {
            // Add content.
            text: defElem.html(),
          }
        }
        $.extend(true, tipSettings, addSettings);

        // Initialize tooltip.
        elem.qtip(tipSettings, event).addClass("article-glo-popup hasTooltip");
        event.preventDefault();
      });
    }
  };
})(jQuery);
