/**
 * Highwire OpenURL
 *
 * Copyright (c) HighWire Press, Inc
 * This software is open-source licensed under the GNU Public License Version 2
 * or later. The full license is available in the LICENSE.TXT file at the root
 * of this repository.
 */

(function ($) {
  Drupal.behaviors.highwire_openurl = { attach: function (context, settings) {
    if ($('.cit-ref-sprinkles-open-url').length > 0) {
      // Get the insitutional OpenURL branding data
      var id = '';
      if ("apath" in Drupal.settings.highwire) {
        id = '?apath=' + encodeURIComponent(Drupal.settings.highwire.apath);
      }
      $.getJSON(

        Drupal.settings.basePath + 'highwire/openurl_branding' + id,
        function(data){
          if(data){
            // Add to Drupal.settings in case we have another use for it
            Drupal.settings.highwireOpenurl = data;

            // Not all journals have OpenURL implementations
            if (data.base_url === null) {
              $('.cit-ref-sprinkles-open-url').hide();
            }
            else {
              // Update each link to show institutional branding
              $('.cit-ref-sprinkles-open-url').each(function(){
                var $link = $(this);
                $link.once('insertImage', function(){
                  var branding = Drupal.settings.highwireOpenurl;
                  var href = $link.attr('href');
                  var placeholder = '';
                  var queryKey = '';

                  // Check if this is content from old markup server.
                  if (href.indexOf('{openurl}') != -1) {
                    // Set placeholder accordingly.
                    placeholder = '{openurl}';
                    // The href from the old markup server is encoded twice, so decode twice.
                    href = decodeURIComponent(href);
                    try {
                      href = decodeURIComponent(href);   
                    } catch(e) {
                      // debug if needed 
                    }
                  }
                  // Check if this is content from the new markup server.
                  // @see JIRA ticket: GP-86
                  else if (href.indexOf('urn:openurl:') != -1) {
                    // Set placeholdet text and query key accordingly.
                    placeholder = 'urn:openurl:';
                    queryKey = '?';
                  }
                  // Update openURL link with new href and text.
                  href = href.replace('?query=','?');
                  href = href.replace(placeholder, Drupal.settings.basePath + 'highwire/openurl' + queryKey);
                  var openurl_link = href + '&redirect_url=' + branding.base_url;
                  $link.attr('href', openurl_link.replace(/\+/g,  " "));
                  $link.text(branding.link_text);
                  if(branding.image){
                    $link.prepend('<img src="' + branding.image + '"/>');
                  }
                });
              });
            }
          }
        }
      );
    }
  }}
})(jQuery);
