/**
 * Highwire Article References pop up
 *
 * Copyright (c) 2010-2011 Board of Trustees, Leland Stanford Jr. University
 * This software is open-source licensed under the GNU Public License Version 2 or later
 * The full license is available in the LICENSE.TXT file at the root of this repository
 */
(function ($) {
  Drupal.behaviors.articleRefPopup = {
    attach: function(context, settings) {
      var instances = (settings.instances != undefined) ? $.parseJSON(settings.instances) : false;
      if (!instances) {
        return;
      }

      // JCORE-2366: Use event delegation wrapper around cluetip to speed up domready scripting time
      $("body", context).delegate("a.xref-bibr:not(.hasTooltip):not(.hw-no-refrence), a.xref-ref:not(.hasTooltip):not(.hw-no-refrence)", "mouseenter", function (event) {
        var elem = $(this);
        var parent = elem.parents('[data-highwire-cite-ref-tooltip-instance]');
        var instance = parent ? parent.data('highwire-cite-ref-tooltip-instance') : 'highwire_reflinks_tooltip';
        var tipSettings = (instances[instance] != undefined) ? instances[instance] : '';
        var target = 'a' + elem.attr('href') + '~.ref-cit';

        if (!tipSettings || !$(target).length) {
          elem.addClass('hw-no-refrence');
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
            },
            render: function(event, api) {
              api.elements.content.addClass('highwire-markup');
            },
          },
          content: {
            // Add content but leave referenced element.
            text: $(target).clone(),
          }
        }
        $.extend(true, tipSettings, addSettings);

        // Initialize tooltip.
        elem.qtip(tipSettings, event).addClass("article-ref-popup hasTooltip");
        event.preventDefault();
      });
      
    }
  };
})(jQuery);
