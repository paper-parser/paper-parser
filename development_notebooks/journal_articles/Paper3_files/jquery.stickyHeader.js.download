(function($) {

  $.fn.stickyHeader = function( options ) {

    var settings = $.extend({
      triggerElement  : '.contentbody',
      hiddenClass     : 'is-hidden',
      scrollOffset    : null,
      scrollInterval  : 250
    }, options);

    var $this = $(this);

    return this.each( function() {

      var scrolled = false;

      function sciScrollEvents() {
        scrolled = true;
      }

      $this.addClass(settings.hiddenClass);

      window.onscroll = sciScrollEvents;

      setInterval(function() {

        var contentTop = $(settings.triggerElement).offset().top - settings.scrollOffset - $(document).scrollTop();

        if (scrolled && contentTop < 0) {
          scrolled = false;

          $this.removeClass(settings.hiddenClass);
      }

      else if (scrolled && contentTop >= 0) {
        $this.addClass(settings.hiddenClass);
      }
    }, settings.scrollInterval);

    });

  };

}(jQuery));
