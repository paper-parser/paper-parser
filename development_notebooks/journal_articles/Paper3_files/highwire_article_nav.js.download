/**
 * Highwire Article Nav
 *
 * Copyright (c) 2010-2011 Board of Trustees, Leland Stanford Jr. University
 * This software is open-source licensed under the GNU Public License Version 2 or later
 * The full license is available in the LICENSE.TXT file at the root of this repository
 */

(function ($) {
  Drupal.behaviors.highwire_article_nav = {
    attach: function (context, settings) {
      $('.highwire-article-nav', context).once('highwire-article-nav', function() {
        $wrapper = $(this);

        $('a', $wrapper).click(function() {
          $link = $(this);
          var panelTarget = $link.data('panel-ajax-tab');
          var href = $link.attr('href');

          if (panelTarget) {
            var $tabLink = $('a.panels-ajax-tab-tab[data-panel-name="' + panelTarget + '"]');
            var $tabTargetId = $tabLink.attr('data-target-id');
            // Get Tab container ID to jump no the top of Tab container.
            var $tabContainer = $('#panels-ajax-tab-container-' + $tabTargetId);

            // If we are on the current tab and we are clicking a anchor, just let it happen
            // If we on the current tab and it is not an anchor, then ignore it.
            if ($tabLink.parent().hasClass('active')) {
              if (href.substring(0, 1) === '#') {
                return true;
              }
              else {
                // Jump to the tab, but don't do anything else
                $('html, body').animate({
                  scrollTop: $tabContainer.offset().top + 'px'
                }, 'fast');
                return false;
              }
            }
            // We need to trigger a tab change
            else {
              // If it's a link to the tab itself (and not a sub-component) then just trigger a click on the tab and jump to the tab
              if (href.substring(0, 1) != '#') {
                $tabLink.trigger('click');

                // Jump to the tab
                $('html, body').animate({
                  scrollTop: $tabContainer.offset().top + 'px'
                }, 'fast');
              }
              // We need to trigger the panel-ajax-tab THEN we need to jump to the anchored content
              else {
                $tabLink.panels_ajax_tabs_trigger(function() {
                  $('html, body').animate({
                    scrollTop: $(href).offset().top + 'px'
                  }, 'fast');
                });
              }
              return false;
            }
          }
        });
      });
    }
  };
})(jQuery);
