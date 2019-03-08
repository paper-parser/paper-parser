var insertChunk = function(source, target, runValidation) {

  var chunkData      = target + " data chunk",
      chunkTime      = target + " deposit time",
      request        = new XMLHttpRequest(),
      targetElement  = document.querySelector(target);
  
  request.open('GET', source, true);

  request.onload = function() {
    if (request.status >= 200 && request.status < 400 && targetElement) {

      var responseChunk = request.responseText,
          storedTime    = localStorage.getItem(chunkTime),
          storedChunk   = localStorage.getItem(chunkData),
          timeNow       = (new Date()).getTime(),
          oneDayAgo     = timeNow - (1000 * 60 * 60 * 24);

      if ( storedTime  === null || storedChunk === null || oneDayAgo > storedTime || (typeof runValidation !== 'undefined' && runValidation === 'true' && typeof localStorage.newsFooterV0815 === 'undefined') ) {

        localStorage.setItem(chunkData, responseChunk);
        localStorage.setItem(chunkTime, timeNow);
        localStorage.setItem('newsFooterV0815', 1);

        targetElement.insertAdjacentHTML("afterbegin", responseChunk);
      } else {
        targetElement.insertAdjacentHTML("afterbegin", storedChunk);
      }
			
      // Validation for newsletter footer
      if (typeof runValidation !== 'undefined' && runValidation === 'true'){
      	/* TF - Code to validate footer newsletter sign up form */
        // Global vars
        var firstPartyConsentId = 'newsletter-footer-consent-first-party';
        var thirdPartyConsentId = 'newsletter-footer-consent-third-party';
        var editorialConsentId = 'newsletter-footer-consent-editorial';
        var firstPartyConsent = document.getElementById(firstPartyConsentId);
        var thirdPartyConsent = document.getElementById(thirdPartyConsentId);
        var editorialConsent = document.getElementById(editorialConsentId);
        var countryList = document.getElementById('newsletter-footer-country');
        var emailInput = document.getElementById('newsletter-footer-email');
        var submitBtn = document.getElementById('newsletter-footer-submit');
        var checkboxes = document.getElementById("newsletter-footer-checkboxes").querySelectorAll("input[type='checkbox']");
        var firstPartyConsentOrigin = document.getElementById('newsletter-footer-consent-first-party-origin');
        var thirdPartyConsentOrigin = document.getElementById('newsletter-footer-consent-third-party-origin');
        //var additionalNews = document.getElementsByClassName('newsletter-footer-additional-newsletters');
        var formOrigin = "NL_Signup_Footer";

        // Function to set date/time for hidden fields for email consent
        function setConsentTime(id, timestamp){
          var hiddenFieldId = id + "-timestamp";
          var hiddenField = document.getElementById(hiddenFieldId);
          hiddenField.value = timestamp;
        }

        // Function to add leading zeros where needed in date/time
        function addLeadingZero(num){
          var ret = num.toString();
          ret = ret.length == 1 ? '0' + ret : ret;
          return ret;
        }

        // Function to get current date in UTC
        function getDate(){
          var currTime = new Date().getTime();

          var now = new Date(currTime);

          var hour = addLeadingZero((now.getUTCHours()).toString());
          var min = addLeadingZero(now.getUTCMinutes().toString());
          var sec = addLeadingZero(now.getUTCSeconds().toString());
          var month = addLeadingZero((now.getUTCMonth() + 1).toString());
          var day = addLeadingZero(now.getUTCDate().toString());

          var date = now.getUTCFullYear().toString() + '-' + month + '-' + day + ' ' + hour + ':' + min + ':' + sec;

          return date;
        }

        // Check if country has been selected
        function checkCountrySelection(){
          if (countryList.value.length){
            return true;
            } else {
            return false;
            }
        }

        // Validate email address input
        function validateEmail(email) {
            var re = /[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+\.*/;
            return re.test(String(email).toLowerCase());
        }

        // Validate requires fields -- Email address and Country. Enable/disable submit button accordingly
        function validateReqFields(){
          var selected = document.getElementById("newsletter-footer-checkboxes").querySelectorAll("input[type='checkbox']:checked").length;
          if (!checkCountrySelection() || !validateEmail(emailInput.value) || !selected){
            submitBtn.setAttribute("disabled", true);
            } else {
              submitBtn.removeAttribute("disabled");
              // Set timestamp for editorial consent 
            setConsentTime(editorialConsentId, getDate());
            }
        }

        // Run validateReqFields on email field keypress
        emailInput.addEventListener('keyup', function(){
          validateReqFields();
        })

        // Run validateReqFields on country select box change
        countryList.addEventListener('change', function(){
          validateReqFields();
        });

        // Click listeners to force check if 3rd party box is checked. If so, also adds consent for 1st party and additional newsletters
        thirdPartyConsent.addEventListener('click', function(){
          if (thirdPartyConsent.checked) {
            firstPartyConsent.value = true;

            // Set timestamp for consent-timestamp hidden fields
            setConsentTime(firstPartyConsentId, getDate());
            setConsentTime(thirdPartyConsentId, getDate());

            // Set origin in consent origin fields
            firstPartyConsentOrigin.value = formOrigin;
            thirdPartyConsentOrigin.value = formOrigin;

            /*for (var i = 0; i < additionalNews.length; i++){
              additionalNews[i].value = true;
            }*/

            } else {
              //clear fields and disable (disabling prevents them from being included with form payload completely)
              firstPartyConsent.value = ''
              firstPartyConsentOrigin.value = '';
            thirdPartyConsentOrigin.value = '';
            document.getElementById(firstPartyConsentId + "-timestamp").value = '';
            document.getElementById(thirdPartyConsentId + "-timestamp").value = '';
            /*for (var i = 0; i < additionalNews.length; i++){
              additionalNews[i].value = '';
            }*/
            }
        });

        // Add event listener to run validateReqFields on checkbox change
        for (var i = 0; i < checkboxes.length; i++) {
          checkboxes[i].addEventListener("change", function() {
            validateReqFields();
          });
        }

        // Disable button on page load since no selections will have been made
        validateReqFields();
      }
      
    } else {
      // We reached the server but couldn't find the source file or the target element is missing
      // Consider reporting errors via DTM
    }
  };

  request.onerror = function() {
    // There was a connection error while attempting to reach the server to fetch the source
  }
    request.send();
};
