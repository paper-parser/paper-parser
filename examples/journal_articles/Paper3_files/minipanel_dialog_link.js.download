(function ($) {
  // Store our function as a property of Drupal.behaviors.
  Drupal.behaviors.minipanel_dialog_link = { attach: function (context, settings) {

    var getWidth = function() {
      var winWidth = $(window).width();
      if(winWidth >= Drupal.settings.highwire.modal_window_width) {
        return Drupal.settings.highwire.modal_window_width;
      } else {
        return "90%";
      }
    }
    
    $('.minipanel-dialog-link-trigger', context, settings).once('minipanel-dialog-link-trigger', function() {
      if($(this).attr('title') != '<blank>'){
        var title = $(this).attr('title');
      }
      else {
        var title = '';
      }
      var $mini = $(this).parent().parent().find('.minipanel-dialog-link-mini');
      $mini.dialog({"modal":true, "draggable":false, "title": title, "resizable":false, "autoOpen": false});
      $(this).click(function() {
        $mini.dialog({"width":getWidth()});
        $mini.dialog("open");
        return false;
      });
    });
  }};
}(jQuery));
