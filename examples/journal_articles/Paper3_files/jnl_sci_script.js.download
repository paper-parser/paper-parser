(function ($) {
  Drupal.behaviors.jnl_sci_styles = {
    attach: function(context, settings) {
      $("ul.toc-section:contains('Content Does Not Exist in Drupal')").hide();
      $(".pane-science-home-page-archive-tab .issue-archive-date-browser ul.years li a").each(function(index) {
         var a_href = $(this).attr('href');
         $(this).attr('href', '/content/by/year' + a_href);
      });
    }
  }
})(jQuery);
