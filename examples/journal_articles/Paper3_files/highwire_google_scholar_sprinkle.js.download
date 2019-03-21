/**
 * @file
 * Highwire Google Scholar citation sprinkle links
 *
 * Copyright (c) HighWire Press, Inc
 * This software is open-source licensed under the GNU Public License Version 2
 * or later. The full license is available in the LICENSE.TXT file at the root
 * of this repository.
 */

(function ($) {
  Drupal.behaviors.highwire_google_scholar = { attach: function (context, settings) {
    if($('.cit-extra').length > 0) {
      $('.cit-list .ref-cit').once('google_scholar_link',function() {
        $(this).each(function() {

          // Pull the set of authors to submit as an array.
          var authorList = '';
          var c = 0;
          $(this).find('.cit-auth').each(function () {

            var given = $(this).find('.cit-name-given-names') !== 'undefined' ? $(this).find('.cit-name-given-names').html() : '';
            var surname = $(this).find('.cit-name-surname') !== 'undefined' ? $(this).find('.cit-name-surname').html() : '';
            if(given || surname) {
              authorList += '&author[' + c + ']=' + (given ? given : '') + (surname ? '+' + surname : '');
            } else if ($(this).hasClass('cit-collab')) {
              authorList += '&author[' + c + ']=' + $(this).text();
            }
            c++;
          });

          var articleTitle = $(this).find('.cit-article-title').length > 0 ? $(this).find('.cit-article-title').text() : false;

          var articlePub = $(this).find('.cit-pub-date').length > 0 ? $(this).find('.cit-pub-date').html() : false;

          var gs_link_suffix = ''
          // We need all three values to submit a lookup.
          if (articleTitle !== false
            && articlePub !== false
            && authorList !== '') {
            // Regex used to strip inlne html tags from article title.
            var gs = {
              gsAuthor: authorList,
              gsTitle: articleTitle.replace(/< *img[^>]*src *= *["\']?([^"\']*)"\/>/gi, '').replace(/\ /g, '+'),
              publicationYear: articlePub
            };
            // Additional, non-required fields that are available in various
            // citation formats.
            extraFields = {
              journal: $(this).find('.cit-jnl-abbrev').length > 0 ? $(this).find('.cit-jnl-abbrev').html() : false,
              volume: $(this).find('.cit-vol').length > 0 ? $(this).find('.cit-vol').html() : false,
              issn: $(this).find('.cit-issn').length > 0 ? $(this).find('.cit-issn').html() : false,
              isbn: $(this).find('.cit-isbn').length > 0 ? $(this).find('.cit-isbn').html() : false,
              doi: $(this).find('.cit-doi').length > 0 ? $(this).find('.cit-doi').html() : false,
              pages: ($(this).find('.cit-fpage').length > 0 && $(this).find('.cit-lpage').length > 0)? $(this).find('.cit-fpage').html() + '-' +  $(this).find('.cit-lpage').html() : false
            };

            extraFieldString = '';
            $.each(extraFields, function (idx, val){
              if (val !== false) {
                extraFieldString += '&' + idx + '=' + val.replace(/\ /g, '+');
              }
            });
            gs_link_suffix = authorList + '&title=' + gs.gsTitle + '&publication_year=' + gs.publicationYear + extraFieldString;
          }
          else {
            var q_text = $(this).find('cite').clone().remove().end().text();
            if (q_text.length) {
              q_text = q_text.replace(/< *img[^>]*src *= *["\']?([^"\']*)"\/>/i, '');
              var q_split = q_text.split(' ');
              var q_temp = [];
              $.each(q_split, function (idx, val) {
                if (val !== '') {
                  q_temp.push(encodeURIComponent(val));
                }
              });
              q_text = q_temp.join('+');
              gs_link_suffix = '&q_txt=' + q_text;
            }
          }

          var gs_link = '<a href="/lookup/google-scholar?link_type=googlescholar&gs_type=article' + gs_link_suffix + '" target="_blank" class="cit-ref-sprinkles cit-ref-sprinkles-google-scholar cit-ref-sprinkles-google-scholar"><span>Google Scholar</span></a>';

          $(this, context).once('custom-js', function(){
            $(this).find('.cit-extra').append(gs_link);
          });
        });
      });
    }
  }}
})(jQuery);
