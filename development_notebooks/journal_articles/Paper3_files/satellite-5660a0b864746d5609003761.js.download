_satellite.pushAsyncScript(function(event, target, $variables){
  insertChunk("https://subscriptions.sciencemag.org/dtm/form-subscribe-capture_081418.html", "#aaas-util-foot-1");

var sub = "science";

var subdomain = document.location.hostname.match(/([a-zA-Z+]+)\./)[1];

if(subdomain === "advances" || subdomain === "stke" || subdomain === "stm" || subdomain === "immunology" || subdomain === "robotics") {
	sub = subdomain;
}

if(document.location.pathname === "/journals/robotics") {
	sub = "robotics";
}

// GDPR Version - Validation code is in the Insertchunk JS bucket. Added there due to timing issues. Controlled if third param added to insertChunk
insertChunk("https://subscriptions.sciencemag.org/dtm/footer-newsletter-form/form-" + sub + "_081518.html", "#aaas-util-foot-2", 'true');
});
