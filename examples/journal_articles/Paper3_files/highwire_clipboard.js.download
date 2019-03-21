(function ($) {  

  Drupal.behaviors.clipboardjs = {
    attach: function (context, settings) {

      // Initialize clipboard.js.
      Drupal.clipboard = new Clipboard('button.clipboardjs-button');

      

      // Process successful copy.
      Drupal.clipboard.on('success', function (e) {
        var alertStyle = $(e.trigger).data('clipboard-alert-style');
        var alertText = $(e.trigger).data('clipboard-alert-text');
        var target = e.trigger;

        // Display as alert.
        if (alertStyle === 'alert') {
          alert(alertText);
        }

        // Display as tooltip.
        else if (alertStyle === 'tooltip') {
          var $target = $(target);

          // Add title to target div.
          $target.prop('title', alertText);

          // Show tooltip.
          $target.tooltip({
            placement: 'bottom',
          }).click();

          $target.tooltip('open');

          // Destroy tooltip after delay.
          setTimeout(function () {
            $target.prop('title', '');
          }, 3000);
        }
      });

      // Process unsuccessful copy.
      Drupal.clipboard.on('error', function (e) {
        var alertStyle = $(e.trigger).data('clipboard-alert-style');
        var target = e.trigger;
        var $target = $(target);

        $target.prop('title', function (action) {
          var actionMsg = '';
          var actionKey = (action === 'cut' ? 'X' : 'C');

          if (/iPhone|iPad/i.test(navigator.userAgent)) {
            actionMsg = 'This device does not support HTML5 Clipboard Copying. Please copy manually.';
          }
          else if (/android/i.test(navigator.userAgent)) {
            actionMsg = 'Please copy manually.';
          }
          else {
            if (/Mac/i.test(navigator.userAgent)) {
              actionMsg = 'Press ⌘-' + actionKey + ' to ' + action;
            }
            else {
              actionMsg = 'Press Ctrl-' + actionKey + ' to ' + action;
            }
          }

          return actionMsg;
        }(e.action));

        // Show tooltip.
        $target.tooltip({
          placement: 'bottom',
        }).click();
 
        $target.tooltip('open');
        
        // Destroy tooltip after delay.
        setTimeout(function () {  
          $target.prop('title', '');
        }, 3000);
      });
    }
  };
}(jQuery));
