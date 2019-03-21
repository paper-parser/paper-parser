/**
 * Highwire Figure
 *
 * Copyright (c) HighWire Press, Inc.
 * This software is open-source licensed under the GNU Public License Version 2 or later
 * The full license is available in the LICENSE.TXT file at the root of this repository
 */
(function ($) {
  Drupal.behaviors.highwireFiguresMarkupProcessor = {
    attach: function(context, settings) {
      /**
       * Force hide captions for mobile. Can't do this directly with CSS only since ColorboxJS controls visibility.
       */
      $('body').bind('highwireResponsiveLayoutTransition', function(e, d) {
        var mobileLayouts = Drupal.highwireResponsive.getMobileLayouts();
        if(d.from != d.to) {
          // Check if we transitioned into one of the mobile breakpoints.
          if (mobileLayouts.indexOf(d.to) != -1) {
            // .force-hide is display:none !important. See jcore_1/css/global.css
            $('#cboxTitle').addClass('force-hide');
          }
          else {
            $('#cboxTitle').removeClass('force-hide');          
          }
        }
        // Check if we're in one of the mobile breakpoints.
        else if (mobileLayouts.indexOf(d.to) != -1) {
          $('#cboxTitle').addClass('force-hide'); 
        }
      });

      $('a.fragment-images.colorbox-load', context).once('highwireFiguresMarkupProcessor', function() {
        $(this, context).each(function() {
          var $this = $(this);
          var figTitle = false;
          // This check will ensure for table fragment will not cause
          // any data attribute error.
          if ($this.is('[data-figure-caption]')) {
            figTitle = $this.data('figure-caption');
          }
          // Disable image preloading - this messes with our logging.
          cbsettings = $.extend(settings.colorbox, {'preloading': false, title: figTitle});

          $this.colorbox(cbsettings);
        });
      });
      
      //SUPPALLPLA-134: Hide cboxTitle fig pop-up if div.highwire-markup has no content
      $('.highwire-markup:empty').closest('#cboxTitle').addClass('force-hide');
    }
  };
})(jQuery);
