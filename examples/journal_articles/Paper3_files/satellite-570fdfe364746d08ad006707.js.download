if( typeof _sdi == "undefined" ) _sdi = {};

/**
 * Creates and dispatches an event trigger
 * @param {String} evt - The name of the event
 */
_sdi.sendCustomEvent = function(evt, evtDetail){

  var params = {
  	detail: evtDetail,
  	bubbles: true,
    cancelable: true
  };

  if(window.CustomEvent && document.body.dispatchEvent) {
    var event = new CustomEvent(evt, params);
    document.body.dispatchEvent(event);
  } else if(document.createEvent && document.body.dispatchEvent){
    var event = document.createEvent('Event',params);
    event.initEvent(evt, true, true); //can bubble, and is cancellable
    document.body.dispatchEvent(event);
  }

  return event;
}
