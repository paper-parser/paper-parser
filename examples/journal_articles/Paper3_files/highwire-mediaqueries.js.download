/**
 * This function returns the current matching Breakpoint layout using
 * enquire.js. Falls back to legacy Drupal.omega.getCurrentLayout();
 *
 * An example where this is used is the onActivate method for clueTip popups.
 */
 
Drupal.highwireResponsive = Drupal.highwireResponsive || {};
 
(function($) {

  var baseLayout = 'mobile';
  var current = baseLayout;
  var previous = baseLayout;
  var order = [];
  var index = 0;
  var breakpointsReady = false;

  /**
   * Fired when breakpoint matches
   */
  var breakpointMatch = function(key){
    previous = current || baseLayout;
    current = key;
    triggerTransition();
  }

  /**
   * Fired when breakpoint unmatches
   */
  var breakpointUnmatch = function(key){
    previous = key;
    var i = order.indexOf(key);
    current = order[i-1] || baseLayout;
    triggerTransition();
  }

  /**
   * Return the current layout for the page, based on Breakpoint media queries.
   * Fall back to legacy Drupal.omega.getCurrentLayout().
   *
   * @param bool distinctMobileLayouts
   *  If false, will group all the mobile layouts into a single "mobile" layout.
   *  Defaults to false.
   *
   * @return
   *  A string matching the current breakpoint layout name based on viewport size.
   *
   * @see Drupal.highwireResponsive.getMobileLayouts
   */
  Drupal.highwireResponsive.getCurrentLayout = function (distinctMobileLayouts) {
    if (typeof distinctMobileLayouts == 'undefined') {
      distinctMobileLayouts = false;
    }
    if (breakpointsReady) {
      if (!distinctMobileLayouts && Drupal.highwireResponsive.isCurrentLayoutMobile(current)) {
        return baseLayout;
      }
      else {
        return current;
      }
    }
    else if (typeof Drupal.omega != 'undefined') {
      return Drupal.omega.getCurrentLayout(); // See omega-mediaqueries.js in the Omega theme
    }
  };
  
  /**
   * Return previous layout state
   * Fall back to legacy Drupal.omega.getPreviousLayout().
   *
   * @param bool distinctMobileLayouts
   *  If false, will group all the mobile layouts into a single "mobile" layout.
   *  Defaults to false.
   *  
   * @return
   *  A string matching the previous breakpoint layout name based on viewport size.
   *
   * @see Drupal.highwireResponsive.getMobileLayouts
   */
  Drupal.highwireResponsive.getPreviousLayout = function (distinctMobileLayouts) {
    if (typeof distinctMobileLayouts == 'undefined') {
      distinctMobileLayouts = false;
    }
    if (breakpointsReady) { 
      if (!distinctMobileLayouts && Drupal.highwireResponsive.isCurrentLayoutMobile(previous)) {
        return baseLayout;
      }
      else {
        return previous;
      }
    }
    else if (typeof Drupal.omega != 'undefined') {
      return Drupal.omega.getPreviousLayout(); // See omega-mediaqueries.js in the Omega theme
    }
  };

  /**
   * Determine whether the layout is part of the mobile layout group.
   *
   * @param string layout
   *  The layout to check.
   *
   * @return
   *  True if the layout is part of the mobile group, otherwise false.
   *
   * @see Drupal.highwireResponsive.getMobileLayouts
   */
  Drupal.highwireResponsive.isCurrentLayoutMobile = function (layout) {
    layout = layout || baseLayout;
    var mobileLayouts = Drupal.highwireResponsive.getMobileLayouts();
    if (mobileLayouts.indexOf(layout) != -1) {
      return true;
    }
    else {
      return false;
    }
  }

  /**
   * Get the layouts that should be grouped together as "mobile".
   *
   * @return
   *  An array of layout keys.
   */
  Drupal.highwireResponsive.getMobileLayouts = function () {
    return [
      'mobile',
      'zero',
      'xsmall'
    ];
  };
  
 /**
  *  This adds responsive body classes, i.e. hw-responsive-layout-narrow 
  *  This also adds a global trigger event which fires on the transition, similar to Omega's resize.responsivelayout event.
  *
  *  // Example
  *  $('body').bind('highwireResponsiveLayoutTransition', function(e, d) {
  *    if(d.from != d.to) {
  *      // Do something when transitioning between any mediaquery state
  *    }
  *  });
  */
  var triggerTransition = function() {
    $('body').removeClass('hw-responsive-layout-' + previous).addClass('hw-responsive-layout-' + current); 
    $.event.trigger('highwireResponsiveLayoutTransition', {from: previous, to: current});
  }

  Drupal.behaviors.highwireResponsiveMediaQueries = {
    attach: function (context, settings) {
      if (typeof Drupal.settings.highwireResponsive != 'undefined' &&  Drupal.settings.highwireResponsive.enquire_enabled === 1 && Drupal.settings.highwireResponsive.breakpoints_configured === 1) {
        if (typeof Drupal.settings.highwireResponsive.breakpoints != 'undefined') {
          breakpointsReady = true;
        }
      }
      /**
       * Setup and register enquire.js callbacks based on breakpoints
       * If Breakpoints are configured but no match is made, this will often return 'mobile'.
       * This is done to support mobile-first design - in practice you shouldn't be
       * defining a "mobile" media query as it should be assumed to be the default.
       */
      if (breakpointsReady) {
        // Breakpoints should be defined in order of smallest to largest
        var breakpoints = Drupal.settings.highwireResponsive.breakpoints;
        $.each(breakpoints, function( key, value ) {
          order[index] = key;
          index++;
          enquire.register(value, {
            match : function() {
              breakpointMatch(key);
            },
            unmatch : function() {
              breakpointUnmatch(key);
            }
          });

        });
        // Trigger transition on initial page load
        $(window, context).bind('load', function(){
          triggerTransition();
        });
      }
    }
  };

})(jQuery); 
