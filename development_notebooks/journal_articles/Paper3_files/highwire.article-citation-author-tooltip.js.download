/**
 * Highwire Author pop up
 *
 * Copyright (c) 2010-2011 Board of Trustees, Leland Stanford Jr. University
 * This software is open-source licensed under the GNU Public License Version 2 or later
 * The full license is available in the LICENSE.TXT file at the root of this repository
 */
(function ($) {
  Drupal.behaviors.articleAuthorPopup = {
    attach: function(context, settings) {
      // This is a hope-to-be temporary check. This should be loaded together with Cluetip lib. The only known
      // issue can be when markup_cache_object from php caches the wrong JS items. However there is no known way of
      // reproducing it.
      var doesQTipExist = !!jQuery.fn.qtip;
      if (!doesQTipExist) {
        if (window.console) {
          console.error('HW\'s qTip behavior is called without the qTip library loaded. Please investigate.');
        }
        return;
      }
      var instances = (settings.instances != undefined) ? $.parseJSON(settings.instances) : {};
      // JCORE-2366: Add event delegation wrapper around tooltip
      $("body", context).delegate(".has-author-tooltip span.highwire-citation-author:not(.hasTooltip):not(.noTooltip)", "mouseenter", function (event) {
        var elem = $(this);
        var delta = elem.data('delta');
        var parent = elem.parents('.highwire-article-citation');
        var parentId = parent.attr('id');
        var $tooltipElem = $("#hw-article-author-popups-" + parentId + " .author-tooltip-" + delta, parent);
        var instance = elem.data('hw-author-tooltip-instance') ? elem.data('hw-author-tooltip-instance') : 'highwire_author_tooltip';
        var tipSettings = (instances[instance] != undefined) ? instances[instance] : '';
        if (!tipSettings || $tooltipElem.length <= 0) {
          elem.addClass('noTooltip');
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
            focus: function(event, api) {
              // Add class for showing 'active' state on tooltip target.
              api.elements.target.addClass('author-popup-hover');
            },
            blur: function(event, api) {
              // Remove class for showing 'active' state on tooltip target.
              api.elements.target.removeClass('author-popup-hover');
            },
          },
          content: {
            // Add content.
            text: $tooltipElem,
          }
        }
        $.extend(true, tipSettings, addSettings);

        // Initialize tooltip.
        elem.qtip(tipSettings, event).addClass("has-tooltip hasTooltip");
        event.preventDefault();
      });
    }
  };
})(jQuery);
