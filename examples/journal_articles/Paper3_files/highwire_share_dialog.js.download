(function ($) {
  // Store our function as a property of Drupal.behaviors.
  Drupal.behaviors.highwire_shareitajax = { attach: function (context, settings) {
    
    var getWidth = function() {
      var winWidth = $(window).width();
      if(winWidth >= Drupal.settings.highwire.share_modal_width) {
        return Drupal.settings.highwire.share_modal_width;
      } else {
        return "90%";
      }
    }

    var modalTitle = Drupal.settings.highwire.share_modal_title; 
    var success = false;
    var id ='';
    var encodedUrl = '';
    $('.highwire_clipboard_link_ajax', context, settings).click(function(){
      id = $(this).attr('id');
      $(this).parent().find('.highwire_clipboard_form_ajax_'+id).dialog({"modal":true, "draggable":false, "width":getWidth(), "title":modalTitle, "resizable":false});
      $('.highwire_clipboard_form_ajax_'+id).dialog('open');      
      return false;
    });
  }};
}(jQuery));
