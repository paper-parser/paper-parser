/**
 * @file
 * script.js
 */

(function($) {
  Drupal.behaviors.science = {
    attach: function(context, settings) {

      $('.datatable')
        .respondTable();
        
      $(".header__header img, .journal-preview img, .footer__header img").switchPng();
      
      $('.nav-interior .is-collapsible', context).click(function(){
        $(this).toggleClass('target-is-expanded target-is-collapsed');
        $(this).siblings('ul').slideToggle(400, 'swing', function(){ $(this).css('overflow','visible') });
        return false;
      });

      $('.search-toggler__trigger', context).click(function() {
        $('.search-form-mobile', context).toggleClass('is-hidden');
      });

      $('.contributor-list__toggler', context).click(function() {
        $(this).parents('.article__header').children('.article__expandable-area').toggleClass('expanded collapsed');
      })
      
      // using jQuery
/*
      $('audio.audio--podcast').mediaelementplayer({
        audioWidth: "100%",
        audioHeight: 80,
        features: ['playpause','progress', 'volume', 'current', 'tracks', 'duration', 'seeking', 'seekable', 'timerail']
      });
*/

      Drupal.behaviors.science.sticky(context, settings);
      Drupal.behaviors.science.fixFonts(context,settings);
      Drupal.behaviors.science.smoothScroll(context, settings);
      Drupal.behaviors.science.viewsLoadMore(context, settings);

      // Tweak Owl carousel settings/output.
      Drupal.behaviors.science.owlCarouselNodeHero(context, settings);
      //Drupal.behaviors.science.owlCarouselArticleGallery(context, settings);
    },
    smoothScroll: function(context, settings) {
      /* https://css-tricks.com/snippets/jquery/smooth-scrolling/ */
      $('a[href*=#]:not([href=#], [href^=#tab])', context).click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
          if (target.length) {
            var stickyHeader = $('.sticky-header');
            var scrollOffset = stickyHeader.length ? stickyHeader.outerHeight() : 0;
            target.addClass('is-scroll-target');
            $('html,body').animate({
              scrollTop: target.offset().top - scrollOffset
            }, 1000, function(){
              target.removeClass('is-scroll-target');
            });
            return false;
          }
        }
      });
    },
    sticky: function(context, settings) {
      
      if (window.matchMedia("(min-width: 1025px)").matches) {
        $('.social-sidebar', context).sticky({
          topSpacing: 0,
          getWidthFrom: '.tertiary'
        });
      }
      
      $('.nav-sidebar', context).sticky({
        topSpacing: 0,
        getWidthFrom: '.secondary'
      });

      $('.sticky-header', context).stickyHeader({
        triggerElement: '[role="main"]',
        hiddenClass: 'sticky-header-is-hidden',
        scrollOffset: -75
      });

    },
    viewsLoadMore: function(context, settings) {

      // To use this "load more" pager instead of the default Views output, do
      // this:
      //  * Add 'view-load-more' CSS class to the View display.
      //  * Add 'view-load-more-item' CSS class to the row output.
      //  * Use "More" link and set whatever label you want.
      //  * Set "Paged output, full pager".
      var $link_page = $('.view-load-more .pager li.pager-item a', context);
      var $link_more = $('.view-load-more .more-link a', context);
      if (!$link_page.length || !$link_more.length) {
        return;
      }

      // Set View wrapper selector string.
      var selector = '.' + $('.view-load-more', context)
        .attr('class')
        .split(' ')
        .join('.');

      // Collect all paged href values.
      var history = [];
      $link_page.each(function(ix, e) {
        history
          .push($(e).attr('href'));
      });

      // Remove default Views pager.
      var $pager = $(selector + ' .pager', context)
        .hide();

      // Bind click behavior to More button.
      $link_more
        .addClass('btn btn--block')
        .click(function(evt) {
          evt.preventDefault();

          var $self = $(this);
          var label = $self.html().trim();
          var page = history.shift();
          var $target = $(selector + ' .view-content > ul, ' + selector + ' .view-content > ol', context);
          if (!$target.length) {
            $target = $(selector + ' .view-content', context);
          }

          // AJAX in the next page of View items, store results to hidden pager
          // element, then append the View content.
          $self
            .html(Drupal.t('Loading...'));

          $pager
            .load(page + ' ' + selector + ' .view-content .view-load-more-item', null, function(response, status, xhr) {
              $self
                .html(label);
              $target
                .append($pager.html());
              $pager
                .empty();

              if (history.length == 0) {
                $link_more
                  .addClass('element-invisible');
              }
            });

        });

    },
    owlCarouselNodeHero: function(context, settings) {

      $('.carousel--nodes', context)
        .each(function(ix, e) {
          var $self = $(e);
          if ($self.length) {
            settings.owlcarousel[e.id].settings.baseClass = 'carousel carousel--nodes owl-carousel';
            settings.owlcarousel[e.id].settings.margin = 30;
            settings.owlcarousel[e.id].settings.dots = false;
            // Prev/Next navigation, v2.x
            settings.owlcarousel[e.id].settings.nav = true;
            settings.owlcarousel[e.id].settings.navContainerClass = 'carousel--nodes__nav';
            settings.owlcarousel[e.id].settings.navClass = [ 'carousel--nodes__prev', 'carousel--nodes__next' ];
            settings.owlcarousel[e.id].settings.dotClass = "carousel__dot";
            settings.owlcarousel[e.id].settings.dotsClass = "caorusel__dots";
            settings.owlcarousel[e.id].settings.navText = ['&laquo;<span class="element-invisible">Previous slide</span>', '&raquo;<span class="element-invisible">Next slide</span>'];
            // Prev/Next navigation, v1.3.x
            settings.owlcarousel[e.id].settings.navigation = true;
            // Rebind Owl lib.
            Drupal.behaviors.owlcarousel.attach(context, settings);
            // Prev/Next navigation, v1.3.x
            $('.owl-controls .owl-buttons', $self).addClass('carousel--nodes__nav').removeClass('owl-buttons');
            $('.owl-controls .owl-prev', $self).addClass('carousel--nodes__prev');
            $('.owl-controls .owl-next', $self).addClass('carousel--nodes__next');
            $('.owl-controls .owl-pagination', $self).addClass('owl-dots');
            $('.owl-controls .owl-page', $self).addClass('owl-dot');
            $('.owl-controls .owl-page span', $self).css('background', 'none').addClass('owl-dot');
          }
        });

        // Capture window resize event and override Owl's pagination again
        $(window).resize(function(){
          setTimeout(function(){
            $('.owl-controls .owl-page').addClass('owl-dot');
            $('.owl-controls .owl-page span').css('background', 'none');
          }, 250);
        });

    },
    owlCarouselArticleGallery: function(context, settings) {
      var carousel = '.gallery-carousel';
      setTimeout(function(){
        $(carousel).addClass('carousel carousel--media figure article__figure');
        $(carousel + ' .owl-controls .owl-buttons').addClass('carousel--media__nav').removeClass('owl-buttons');
        $(carousel + ' .owl-controls .owl-prev').addClass('carousel--media__prev');
        $(carousel + ' .owl-controls .owl-next').addClass('carousel--media__next');
        $(carousel + ' .owl-item').each(function(i){
          var caption = jQuery(this).find('img').attr('alt');
          $(this).prepend('<figure class="figure">');
          $(this).append('<figcaption><p class="caption">'+caption+'</p><p class="credit"></p></figcaption>');
        });
      }, 1);
    },
    fixFonts: function(context, settings) {
      var fontTimeOut = 2000;

      var fontRoboto = new FontFaceObserver("Roboto");
      
      var fontRobotoBold = new FontFaceObserver("Roboto", {
        "weight": "bold"
      });
      
      var fontRobotoItalic = new FontFaceObserver("Roboto", {
        "font-style": "italic"
      });
      
      var fontRobotoBoldItalic = new FontFaceObserver("Roboto", {
        "font-weight": "bold",
        "font-style": "italic"
      });
      
      var fontRobotoCond = new FontFaceObserver("Roboto");
      
      var fontRobotoCondBold = new FontFaceObserver("Roboto Condensed", {
        "weight": "bold"
      });
      
      var fontRobotoCondItalic = new FontFaceObserver("Roboto Condensed", {
        "font-weight": "italic"
      });
      
      var fontRobotoCondBoldItalic = new FontFaceObserver("Roboto Condensed", {
        "font-weight": "bold",
        "font-style": "italic"
      });
      
      Promise.all ([
        fontRoboto.load(null, fontTimeOut),
        fontRobotoBold.load(null, fontTimeOut),
        fontRobotoItalic.load(null, fontTimeOut),
        fontRobotoBoldItalic.load(null, fontTimeOut),
        fontRobotoCond.load(null, fontTimeOut),
        fontRobotoCondBold.load(null, fontTimeOut),
        fontRobotoCondItalic.load(null, fontTimeOut),
        fontRobotoCondBoldItalic.load(null, fontTimeOut)
      ]).then ( function () {
        document.documentElement.className += " fonts-loaded";
      });
    }
  };

})(jQuery);
