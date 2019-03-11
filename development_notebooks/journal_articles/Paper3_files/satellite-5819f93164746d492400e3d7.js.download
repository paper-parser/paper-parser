_satellite.pushAsyncScript(function(event, target, $variables){
  if(typeof _satellite.readCookie('member id') === "undefined" && _satellite.getVar('membership ID').length > 0) {
  var expDate = new Date();
	expDate.setMonth(expDate.getMonth() + 12);
  
	document.cookie = "member id=" + _satellite.getVar('membership ID') + ";expires=" + expDate + ";domain=.sciencemag.org;path=/";  
}
});
