var bodyTags = document.getElementsByTagName('body');
var body = bodyTags[0];
var trendmd_instances  = Drupal.settings.highwire.trendmd;

for (var id in trendmd_instances){
  if (trendmd_instances.hasOwnProperty(id)) {
    var s = document.createElement('script');
    s.type = 'text/javascript';
    s.src = "//js.trendmd.com/trendmd.min.js";
    s.defer = 'defer';
    s.setAttribute('data-trendmdconfig', trendmd_instances[id]);
    body.insertBefore(s, body.lastChild.nextSibling);
  }
}
