(function($) {
  Drupal.behaviors.panels_ajax_pane = {
    attach: function(context) {
      $('.panels-ajax-pane', context).once('panels-ajax-pane-once', function() {
        (function($container) {
          $.ajax({
            type: 'POST',
            data: Drupal.settings.panels_ajax_pane[$container.data('pid')], 
            url: Drupal.settings.basePath + 'panels_ajax_pane/render',
            cache: true,
            error: function(jqXHR, textStatus, errorThrown) {
              if (typeof console == "object") {
                console.error('Panels Ajax Pane Error: ' + errorThrown);
              }
            }
          }).done(function(data) {
            $title_span = $('span.panels-ajax-pane-title[data-pid=' + $container.data('pid') + ']');

            if (data['markup'] === false) {
              $container.closest('.pane-panels-ajax-pane-content').remove();
              $container.remove();
              $title_span.closest('.pane-title').remove();
              $title_span.parent().remove();
            }
            else {
              $container.append(data['markup']);
              $title_span.append(data['title']);
              $container.find('style').append('head'); // Move style elements to head
            }

            if (data['title'] === false) {
              $title_span.closest('.pane-title').remove();
              $title_span.parent().remove();
            }

            // Attach drupal behaviors
            Drupal.attachBehaviors($container);          
          });
        })($(this));
      });
    }
  }
})(jQuery);
