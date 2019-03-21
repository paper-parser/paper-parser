(function($) {
  // Check jQuery version for 1.6 or higher
  if ($().jquery.split(".")[0] == "1" && parseInt($().jquery.split(".")[1]) < 6) {
    if (typeof console == "object") {
      console.error('Panels Ajax Tab Error: jQuery 1.6 or higher required.');
    }
  }

  window.onpopstate = function(e) {
    if(e.state != null){
      $('a[data-panel-name="'+e.state.tab+'"]').panels_ajax_tabs_trigger();
    }
  };

  Drupal.behaviors.panels_ajax_tabs = {
    attach: function(context) {
      $('.panels-ajax-tab-tab', context).once('panels-ajax-tabs-once', function() {
        // We need to push the state when the page first loads, so we know what the first tab is
        if ($(this).parent().hasClass('active') && $(this).data('url-enabled') == 1) {
          if (typeof window.history.pushState != 'undefined') {
            window.history.replaceState({'tab':$(this).data('panel-name')}, $(this).html(), window.location.href);
          }
        }

        $(this).click(function(e) {
          e.preventDefault();

          // Push the history
          if (typeof window.history.pushState != 'undefined' && $(this).data('url-enabled') == 1) {
            var href = $(this).attr('href') ? $(this).attr('href') : location.pathname;
            window.history.pushState({'tab':$(this).data('panel-name')}, $(this).html(), href);
          }

          if (!$(this).parent().hasClass('active')) {
            $(this).panels_ajax_tabs_trigger();
          }

        })
        .css('cursor', 'pointer');
      });

      // Trigger a click event on the first tab to load it
      $('.pane-panels-ajax-tab-tabs', context).once('panels-ajax-tabs-once', function() {
        var tabs = $('.panels-ajax-tab-tab:not(.panels-ajax-tabs-first-loaded)', this);
        var firstTab = tabs.first();
        var target_id = firstTab.data('target-id');
        var preloaded = $('#panels-ajax-tab-container-' + target_id).data('panels-ajax-tab-preloaded');
        var currentTab;

        if (preloaded === '') {
          currentTab = firstTab;
          firstTab.trigger('click');
        }
        else {
          currentTab = tabs.filter('*[data-panel-name="' + preloaded + '"]');
        }

        currentTab.addClass('panels-ajax-tabs-first-loaded');
        currentTab.parent().addClass('active');
      });
    }
  }
})(jQuery);


/**
 * Panels-ajax-tabs-trigger is a jquery plugin that can be triggered.
 * A callback, to be called after content has been loaded, can optionally be passed
 */
(function($){
  $.fn.extend({
    panels_ajax_tabs_trigger: function(callback) {
      return this.each(function() {
        var $tab = $(this);
        var container = $tab.parents('.panels-ajax-tab:first');

        // If it's already in the process of loading, don't do anything
        if ($(container).data('loading') === true) {
          return true;
        }
        $(container).data('loading', true);

        var target_id = $tab.data('target-id');
        var panel_name = $tab.data('panel-name');
        var entity_context = $tab.data('entity-context');
        var url_enabled = $tab.data('url-enabled');
        var trigger = $tab.data('trigger');

        // Create a few jQuery.Event events for a panel being loaded so that other code may hook into it
        var eventData = {
          tab: this,
          tabObject: $tab,
          containerId: '#panels-ajax-tab-container-' + target_id,
          callback: callback,
          cache: false,
        }
        var preLoadEvent     = $.Event("panelsAjaxTabsPreLoad", eventData);      // We are about to do an ajax request. Will have data.cache = true if cache was used.
        var preBehaviorEvent = $.Event("panelsAjaxTabsPreBehavior", eventData);  // Content is loaded but behaviors have not fired. Not triggered when using cache.
        var loadedEvent      = $.Event("panelsAjaxTabsLoaded", eventData);       // Everything is done. Will have data.cache = true if cache was used.

        // If we have it cached we don't need to do AJAX
        if ($('#panels-ajax-tab-container-' + target_id).children('.panels-ajax-tab-wrap-' + panel_name).length) {
          preLoadEvent.cached = true;
          $(document).trigger(preLoadEvent, preLoadEvent.data);

          $('#panels-ajax-tab-container-' + target_id).children().hide();
          $('#panels-ajax-tab-container-' + target_id).children('.panels-ajax-tab-wrap-' + panel_name).show();

          $(container).data('loading', false);

          // Trigger optional callback
          if (callback) {
            callback.call(this, $tab);
          }

          // Trigger jQuery Event
          loadedEvent.cached = true;
          $(document).trigger(loadedEvent);
        }
        else {
          // Do AJAX request.
          $.ajax({
            url: Drupal.settings.basePath + 'panels_ajax_tab/' + panel_name + '/' + entity_context + '/' + url_enabled + '?panels_ajax_tab_trigger=' + trigger + '&panels_ajax_tab_tab=' + panel_name,
            datatype: 'html',
            headers: {"X-Request-Path": document.location.pathname},
            cache: false,
            beforeSend: function(xhr) {
              // Trigger jQuery Event
              $(document).trigger(preLoadEvent);

              // Hide content and show the spinning loading wheel
              $('#panels-ajax-tab-container-' + target_id).children().hide();
              $('#panels-ajax-tab-container-' + target_id).children('.panels-ajax-tab-loading').show();
            },
            error: function(jqXHR, textStatus, errorThrown) {
              if (typeof console == "object") {
                console.error('Panels Ajax Tab Error: ' + errorThrown);
              }
              $(container).data('loading', false);
            }
          }).done(function(data) {
            $('#panels-ajax-tab-container-' + target_id).children('.panels-ajax-tab-loading').hide();
            $('#panels-ajax-tab-container-' + target_id).append('<div class="panels-ajax-tab-wrap-' + panel_name +'">' + data['markup'] + '</div>')

            // Trigger jQuery Event
            $(document).trigger(preBehaviorEvent, preBehaviorEvent.data);

            // Attach drupal behaviors
            Drupal.attachBehaviors($('#panels-ajax-tab-container-' + target_id + ' .panels-ajax-tab-wrap-' + panel_name)[0]);
            $(container).data('loading', false);

            // Trigger optional callback
            if (callback) {
              callback.call(this, $tab);
            }
            // Trigger jQuery Event
            $(document).trigger(loadedEvent);
          })
        }
        $tab.parent().siblings().removeClass('active');
        $tab.parent().addClass('active');
      });
    }
  });
})(jQuery);
