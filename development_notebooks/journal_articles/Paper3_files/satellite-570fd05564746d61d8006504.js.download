_satellite.pushAsyncScript(function(event, target, $variables){
  var audioPlayers = document.querySelectorAll('audio');
for( var i = 0; i < audioPlayers.length; i++ ) {
  
  var evtDetail = {
    
  };
  
  audioPlayers[i].addEventListener( 'play', function() {
    if( isNaN( this.duration ) ) { // duration hasn't loaded yet. Wait for it.
      this.addEventListener( 'durationchange', function() {
        _satellite.notify( "Audio duration loaded." );
        evtDetail.src = this.src.match(/.*\/(.*?)$/)[1];
        evtDetail.duration = Math.floor(this.duration);
        evtDetail.offset = Math.floor(this.currentTime);
        _satellite.setVar('audioSource', evtDetail.src );
        _satellite.setVar('audioDuration', evtDetail.duration );
        _satellite.setVar('audioOffset', evtDetail.offset );
        _sdi.sendCustomEvent( 'analyticsAudioPlay', evtDetail );
      });
    } else {
      evtDetail.src = this.src.match(/.*\/(.*?)$/)[1];
      evtDetail.duration = Math.floor(this.duration);
      evtDetail.offset = Math.floor(this.currentTime);
      _satellite.setVar('audioSource', evtDetail.src );
      _satellite.setVar('audioDuration', evtDetail.duration )
      _satellite.setVar('audioOffset', evtDetail.offset );
      _sdi.sendCustomEvent('analyticsAudioPlay', evtDetail);
    }
  });
  
  audioPlayers[i].addEventListener( 'pause', function() {
    evtDetail.src = this.src.match(/.*\/(.*?)$/)[1];
    evtDetail.duration = Math.floor(this.duration);
    evtDetail.offset = Math.floor(this.currentTime);
    _satellite.setVar('audioSource', evtDetail.src );
    _satellite.setVar('audioDuration', evtDetail.duration )
    _satellite.setVar('audioOffset', evtDetail.offset );
    _sdi.sendCustomEvent('analyticsAudioPause', evtDetail);
  });
  
}
});
