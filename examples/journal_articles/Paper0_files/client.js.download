var shared_errors = {}, shared_strings = {}, shared_http = {}, shared_requests = {}, shared_numbers = {}, shared_collections = {}, shared_html = {}, shared_selection = {}, recommendation_recommendation = {}, text_text = {}, shared_storage = {}, shared_location = {}, shared_state = {}, shared_events = {}, shared_messaging = {}, shared_component = {}, shared_templates = {}, shared_forms = {}, email_this_email_this = {}, recommendation_journey_recommendation_journey = {}, minimised_minimised = {}, email_journey_email = {}, shared_scroll = {}, shared_functions = {}, pre_rec_email_journey_pre_rec_email = {}, pre_rec_plugin_journey_pre_rec_plugin = {}, shared_cookies = {}, popup_popup = {}, inline_inline = {}, config_config = {}, application_application = {}, iframe_client = {};
var __extends = this && this.__extends || function (d, b) {
  for (var p in b)
    if (b.hasOwnProperty(p))
      d[p] = b[p];
  function __() {
    this.constructor = d;
  }
  d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
shared_errors = function (exports) {
  var UnhandledError = function () {
    function UnhandledError() {
    }
    UnhandledError.unhandled = function (e) {
      Debug.log(e);
    };
    UnhandledError.capture = function (fun) {
      return function () {
        try {
          fun();
        } catch (e) {
          UnhandledError.unhandled(e);
        }
      };
    };
    return UnhandledError;
  }();
  exports.UnhandledError = UnhandledError;
  var NoSuchElement = function (_super) {
    __extends(NoSuchElement, _super);
    function NoSuchElement() {
      _super.apply(this, arguments);
    }
    return NoSuchElement;
  }(Error);
  exports.NoSuchElement = NoSuchElement;
  var Debug = function () {
    function Debug() {
    }
    Debug.log = function (message) {
      var optionalParams = [];
      for (var _i = 1; _i < arguments.length; _i++) {
        optionalParams[_i - 1] = arguments[_i];
      }
      if (Debug.enabled) {
        console.log(message, optionalParams);
      }
    };
    Debug.enable = function (value) {
      Debug.enabled = value;
    };
    Debug.isDebug = function (url) {
      return url.indexOf('uptodate-debug=true') != -1;
    };
    Debug.enabled = false;
    return Debug;
  }();
  exports.Debug = Debug;
  return exports;
}(shared_errors);
shared_strings = function (exports) {
  function isEmpty(value) {
    if (value == null)
      return true;
    return value == '';
  }
  exports.isEmpty = isEmpty;
  function coerce(value) {
    if (typeof value == 'undefined' || value == 'undefined')
      return null;
    try {
      return JSON.parse(value);
    } catch (e) {
      return value;
    }
  }
  exports.coerce = coerce;
  function startsWith(start, whole) {
    return whole.indexOf(start) == 0;
  }
  exports.startsWith = startsWith;
  function endsWith(end, whole) {
    return whole.indexOf(end) == whole.length - end.length;
  }
  exports.endsWith = endsWith;
  return exports;
}(shared_strings);
shared_http = function (exports, errors_1, strings_1) {
  var Entity = function () {
    function Entity(content) {
      this.content = content;
    }
    Entity.prototype.xml = function () {
      return new DOMParser().parseFromString(this.content, 'application/xml');
    };
    Entity.prototype.text = function () {
      return this.content;
    };
    Entity.prototype.json = function () {
      return JSON.parse(this.content);
    };
    Entity.prototype.html = function () {
      return new DOMParser().parseFromString(this.content, 'text/html');
    };
    return Entity;
  }();
  exports.Entity = Entity;
  exports.fireAndForget = function (ignore) {
  };
  var previousRequest = {};
  function http(request, responseHandler) {
    if (responseHandler === void 0) {
      responseHandler = exports.fireAndForget;
    }
    if (JSON.stringify(request) == JSON.stringify(previousRequest)) {
      errors_1.Debug.log('duplicate request', request, previousRequest);
      return function () {
      };
    }
    previousRequest = request;
    var handler = new XMLHttpRequest();
    handler.open(request.method, request.url, true);
    handler.withCredentials = true;
    var headers = request.headers || {};
    Object.keys(headers).forEach(function (name) {
      handler.setRequestHeader(name, headers[name]);
    });
    handler.addEventListener('readystatechange', errors_1.UnhandledError.capture(function () {
      if (handler.readyState == 4) {
        var headers_1 = handler.getAllResponseHeaders().split('\n').reduce(function (a, header) {
          var pair = header.split(': ');
          a[pair[0]] = pair[1];
          return a;
        }, {});
        responseHandler({
          status: handler.status,
          headers: headers_1,
          entity: new Entity(handler.responseText)
        });
      }
    }));
    handler.send(request.entity);
    return function () {
      handler.abort();
    };
  }
  exports.http = http;
  function uri(value) {
    var a = document.createElement('a');
    a.href = value;
    return {
      scheme: a.protocol ? a.protocol.replace(/(:$)/, '') : '',
      host: a.hostname,
      authority: a.host,
      path: a.pathname.indexOf('/') === 0 ? a.pathname : '/' + a.pathname,
      query: a.search ? a.search.replace(/(^\?)/, '') : '',
      fragment: a.hash ? a.hash.replace(/(^#)/, '') : '',
      toString: function () {
        var builder = [];
        if (this.scheme != '') {
          builder.push(this.scheme);
          builder.push(':');
        }
        if (this.authority != '') {
          builder.push('//');
          builder.push(this.authority);
        }
        builder.push(this.path);
        if (this.query != '') {
          builder.push('?');
          builder.push(this.query);
        }
        if (this.fragment != '') {
          builder.push('#');
          builder.push(this.fragment);
        }
        return builder.join('');
      }
    };
  }
  exports.uri = uri;
  function queryObject(href) {
    if (href === void 0) {
      href = document.location.href;
    }
    var query = uri(href).query;
    if (query == '')
      return {};
    return query.split('&').map(function (pair) {
      return pair.split('=');
    }).reduce(function (a, v) {
      var name = v[0];
      var newValue = strings_1.coerce(v[1]);
      var oldValue = a[name];
      if (typeof oldValue == 'undefined') {
        a[name] = newValue;
      } else if (typeof oldValue == 'object') {
        oldValue.push(newValue);
      } else {
        a[name] = [
          oldValue,
          newValue
        ];
      }
      return a;
    }, {});
  }
  exports.queryObject = queryObject;
  function toQueryString(obj) {
    var result = [];
    Object.keys(obj).forEach(function (key) {
      var values = obj[key];
      if (values == null) {
        result.push(encodeURIComponent(key));
      } else if (typeof values == 'object') {
        values.forEach(function (value) {
          result.push(encodeURIComponent(key) + '=' + encodeURIComponent(value));
        });
      } else {
        result.push(encodeURIComponent(key) + '=' + encodeURIComponent(values));
      }
    });
    return result.join('&');
  }
  exports.toQueryString = toQueryString;
  var BaseUrl = function () {
    function BaseUrl() {
    }
    BaseUrl.baseUrl = function (name) {
      var extractor = {
        regex: new RegExp('(https?://[^/]+/[^/]+/).*' + name),
        process: function (value) {
          return value.match(extractor.regex)[1];
        }
      };
      try {
        throw new Error();
      } catch (e) {
        try {
          return extractor.process(e.stack);
        } catch (e) {
          return extractor.process(document.querySelector('script[src$="' + name + '"]').src);
        }
      }
    };
    BaseUrl.origin = function (url) {
      var a = document.createElement('a');
      a.href = url;
      return a.protocol + '//' + a.host;
    };
    return BaseUrl;
  }();
  exports.BaseUrl = BaseUrl;
  return exports;
}(shared_http, shared_errors, shared_strings);
shared_requests = function (exports) {
  var Requests = function () {
    function Requests() {
    }
    Requests.config = function (hostname, location) {
      return {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'text/plain'
        },
        url: hostname + 'user/config',
        entity: JSON.stringify(location)
      };
    };
    Requests.postEvent = function (data) {
      return {
        method: 'POST',
        url: data.config.host + 'events/' + encodeURIComponent(data['event']['subject']) + '_' + encodeURIComponent(data['event']['action']) + '_' + encodeURIComponent(data['event']['object']),
        headers: { 'Content-Type': 'text/plain' },
        entity: JSON.stringify(data)
      };
    };
    Requests.get = function (url) {
      return {
        method: 'GET',
        url: url
      };
    };
    Requests.recommendations = function (state) {
      return {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'text/plain'
        },
        url: state.config.host + 'recommendations',
        entity: JSON.stringify(state)
      };
    };
    Requests.jobRecommendations = function (state) {
      //FIXME hack for now to only display max of 3 job recs
      state.config.number_of_recommendations = 3;
      return {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'text/plain'
        },
        url: state.config.host + 'recommendations/jobs',
        entity: JSON.stringify(state)
      };
    };
    return Requests;
  }();
  exports.Requests = Requests;
  return exports;
}(shared_requests);
shared_numbers = function (exports) {
  function randomInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  exports.randomInteger = randomInteger;
  return exports;
}(shared_numbers);
//# sourceMappingURL=numbers.js.map;
var __extends = this && this.__extends || function (d, b) {
  for (var p in b)
    if (b.hasOwnProperty(p))
      d[p] = b[p];
  function __() {
    this.constructor = d;
  }
  d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
shared_collections = function (exports, numbers_1, errors_1) {
  function shuffle(array) {
    for (var i = array.length - 1; i > 0; i--) {
      var j = numbers_1.randomInteger(0, i);
      var temp = array[i];
      array[i] = array[j];
      array[j] = temp;
    }
    return array;
  }
  exports.shuffle = shuffle;
  var List = function (_super) {
    __extends(List, _super);
    function List() {
      _super.apply(this, arguments);
    }
    List.prototype.each = function (fun) {
      for (var i = 0; i < this.length; ++i) {
        fun(this[i], i);
      }
      return this;
    };
    List.prototype.map = function (fun) {
      var array = new List();
      this.each(function (item, i) {
        array.push(fun(item, i));
      });
      return array;
    };
    List.prototype.flatMap = function (fun, array) {
      if (array === void 0) {
        array = new List();
      }
      this.each(function (item, i) {
        var elements = fun(item, i);
        Array.prototype.push.apply(array, elements);
      });
      return array;
    };
    List.prototype.filter = function (predicate) {
      var array = new List();
      this.each(function (item, i) {
        if (predicate(item))
          array.push(item);
      });
      return array;
    };
    List.prototype.find = function (predicate) {
      return this.filter(predicate).head();
    };
    List.prototype.as = function (s) {
      var list = this;
      return list.filter(function (t) {
        return t instanceof s;
      });
    };
    List.prototype.head = function () {
      // if(this.isEmpty()) throw new NoSuchElement();
      return this[0];
    };
    List.prototype.last = function () {
      if (this.isEmpty())
        throw new errors_1.NoSuchElement();
      return this[this.length - 1];
    };
    List.prototype.isEmpty = function () {
      return this.length == 0;
    };
    List.prototype.groupBy = function (key) {
      return this.reduce(function (accumulator, instance) {
        var value = key instanceof Function ? key(instance) : instance[key];
        (accumulator[value] = accumulator[value] || new List()).push(instance);
        return accumulator;
      }, {});
    };
    return List;
  }(Array);
  exports.List = List;
  function list(nodes) {
    var array = new List();
    if (!nodes)
      return array;
    for (var i = 0; i < nodes.length; ++i) {
      array.push(nodes[i]);
    }
    return array;
  }
  exports.list = list;
  function mergeObjects() {
    var objects = [];
    for (var _i = 0; _i < arguments.length; _i++) {
      objects[_i - 0] = arguments[_i];
    }
    var result = {};
    var _loop_1 = function (i) {
      var obj = objects[i];
      if (obj == null)
        return 'continue';
      Object.keys(obj).forEach(function (key) {
        result[key] = obj[key];
      });
    };
    for (var i = 0; i < objects.length; i++) {
      _loop_1(i);
    }
    return result;
  }
  exports.mergeObjects = mergeObjects;
  return exports;
}(shared_collections, shared_numbers, shared_errors);
shared_html = function (exports, collections_1, selection_1) {
  var Elements = function () {
    function Elements() {
    }
    Elements.path = function (element) {
      var result = new collections_1.List();
      while (element) {
        result.push(element);
        element = element.parentElement;
      }
      return result;
    };
    Elements.matches = function (element, selector) {
      element.matches = element.matches || element.msMatchesSelector || function (s) {
        return false;
      };
      return element.matches(selector);
    };
    Elements.calculateBoxShadow = function (element) {
      try {
        var shadow = Elements.path(element).map(function (p) {
          return window.getComputedStyle(p).boxShadow;
        }).find(function (shadow) {
          return shadow != 'none';
        });
        return parseInt(shadow.split('px ')[2]);
      } catch (ignore) {
        return 0;
      }
    };
    return Elements;
  }();
  exports.Elements = Elements;
  function appendHtml(parent, html) {
    var children = parseHtml(html);
    for (var i = 0; i < children.length; i++) {
      var child = children[i];
      parent.appendChild(child);
    }
    return parent;
  }
  exports.appendHtml = appendHtml;
  function isHTML(x) {
    return x.outerHTML !== undefined;
  }
  exports.isHTML = isHTML;
  function parseHtml(html) {
    var temp = document.createElement('div');
    temp.innerHTML = isHTML(html) ? html.outerHTML : html;
    return temp.childNodes;
  }
  exports.parseHtml = parseHtml;
  function insertHtml(node, html) {
    var parent = node.parentNode;
    var children = parseHtml(html);
    for (var i = 0; i < children.length; i++) {
      var child = children[i];
      parent.insertBefore(child, node);
    }
    return node;
  }
  exports.insertHtml = insertHtml;
  function attributes() {
    var attributes = [];
    for (var _i = 0; _i < arguments.length; _i++) {
      attributes[_i - 0] = arguments[_i];
    }
    return function (element) {
      for (var i = 0; i < attributes.length; i++) {
        var attr = attributes[i];
        Object.keys(attr).forEach(function (name) {
          var value = attr[name];
          var type = typeof value;
          switch (type) {
          case 'function':
            element.setAttribute(name, value(element.getAttribute(name)));
            break;
          case 'boolean':
            value ? element.setAttribute(name, '') : element.removeAttribute(name);
            break;
          case 'object':
            element.setAttribute(name, JSON.stringify(value));
            break;
          default:
            element.setAttribute(name, value);
          }
        });
      }
      return element;
    };
  }
  exports.attributes = attributes;
  function on(element, name, fun, capture) {
    if (typeof name == 'string')
      name = [name];
    for (var i = 0; i < name.length; i++) {
      var n = name[i];
      element.addEventListener(n, function (e) {
        var result = fun(e);
        if (!result) {
          e.preventDefault();
          e.stopPropagation();
        }
      }, capture);
    }
  }
  exports.on = on;
  function root() {
    return document.compatMode == 'BackCompat' ? document.body : document.documentElement;
  }
  exports.root = root;
  function hasVerticalScrollBar(element) {
    if (element === void 0) {
      element = root();
    }
    return element.scrollHeight > element.clientHeight;
  }
  exports.hasVerticalScrollBar = hasVerticalScrollBar;
  function hasHorizontalScrollBar(element) {
    if (element === void 0) {
      element = root();
    }
    return element.scrollWidth > element.clientWidth;
  }
  exports.hasHorizontalScrollBar = hasHorizontalScrollBar;
  function dataListObject(element) {
    return selection_1.select('dt', element).reduce(function (result, term) {
      result[term.textContent.trim()] = term.nextElementSibling.textContent.trim();
      return result;
    }, {});
  }
  exports.dataListObject = dataListObject;
  return exports;
}(shared_html, shared_collections, shared_selection);
//# sourceMappingURL=html.js.map;
var __extends = this && this.__extends || function (d, b) {
  for (var p in b)
    if (b.hasOwnProperty(p))
      d[p] = b[p];
  function __() {
    this.constructor = d;
  }
  d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
shared_selection = function (exports, collections_1, html_1) {
  var Select = function (_super) {
    __extends(Select, _super);
    function Select() {
      _super.apply(this, arguments);
    }
    Select.prototype.on = function (name, fun, capture) {
      return this.each(function (element) {
        html_1.on(element, name, function (event) {
          return fun(element, event);
        }, capture);
      });
    };
    Select.prototype.attr = function (name, value) {
      if (value == null)
        return this.map(function (element) {
          return element.getAttribute(name);
        });
      return this.each(function (element) {
        element.setAttribute(name, value);
      });
    };
    Select.prototype.removeAttr = function (name) {
      return this.each(function (element) {
        element.removeAttribute(name);
      });
    };
    Select.prototype.prop = function (name, value) {
      if (value == null)
        return this.map(function (element) {
          return element[name];
        });
      return this.each(function (element) {
        element[name] = value;
      });
    };
    Select.prototype.text = function (value) {
      if (value == null)
        return this.map(function (element) {
          return element.textContent;
        });
      return this.each(function (element) {
        element.textContent = value;
      });
    };
    Select.prototype.html = function (value) {
      if (value == null)
        return this.map(function (element) {
          return element.innerHTML;
        });
      return this.each(function (element) {
        element.innerHTML = value;
      });
    };
    Select.prototype.css = function (name, value) {
      if (value == null)
        return this.map(function (element) {
          return window.getComputedStyle(element).getPropertyValue(name);
        });
      return this.each(function (element) {
        element.style[name] = value;
      });
    };
    Select.prototype.append = function (html) {
      this.map(function (element) {
        return html_1.appendHtml(element, html);
      });
      return this;
    };
    Select.prototype.appendTo = function (parent) {
      return this.each(function (element) {
        parent.appendChild(element);
      });
    };
    Select.prototype.insert = function (html) {
      this.map(function (element) {
        return html_1.insertHtml(element, html);
      });
      return this;
    };
    Select.prototype.remove = function (predicate) {
      if (predicate === void 0) {
        predicate = function (ignore) {
          return true;
        };
      }
      return this.each(function (element) {
        if (predicate)
          element.parentNode.removeChild(element);
      });
    };
    Select.prototype.children = function () {
      return this.flatMap(function (element) {
        return collections_1.list(element.childNodes);
      }, new Select());
    };
    Select.prototype.detach = function () {
      var fragment = document.createDocumentFragment();
      this.each(function (element) {
        fragment.appendChild(element);
      });
      return fragment;
    };
    Select.prototype.clone = function () {
      var fragment = document.createDocumentFragment();
      this.each(function (element) {
        fragment.appendChild(element.cloneNode(true));
      });
      return fragment;
    };
    Select.prototype.show = function () {
      return this.each(function (element) {
        element.style.display = '';
      });
    };
    Select.prototype.hide = function () {
      return this.each(function (element) {
        element.style.display = 'none';
      });
    };
    Select.prototype.addClass = function (name) {
      return this.each(function (element) {
        element.classList.add(name);
      });
    };
    Select.prototype.removeClass = function (name) {
      return this.each(function (element) {
        element.classList.remove(name);
      });
    };
    return Select;
  }(collections_1.List);
  exports.Select = Select;
  function select(selector, element) {
    if (element === void 0) {
      element = document;
    }
    var selection = new Select();
    if (typeof selector !== 'string') {
      selection.push(selector);
      return selection;
    }
    function _select(array, e) {
      var nodes = e.querySelectorAll(selector);
      for (var i = 0; i < nodes.length; ++i) {
        array.push(nodes[i]);
      }
      return array;
    }
    if (element instanceof Select) {
      for (var i = 0; i < element.length; i++) {
        var e = element[i];
        _select(selection, e);
      }
      return selection;
    }
    return _select(selection, element);
  }
  exports.select = select;
  function get(selector, parent) {
    if (parent === void 0) {
      parent = document;
    }
    return parent.querySelector(selector);
  }
  exports.get = get;
  return exports;
}(shared_selection, shared_collections, shared_html);
recommendation_recommendation = function (exports, selection_1) {
  var RecommendationRenderer = function () {
    function RecommendationRenderer(parent) {
      // Nature + BMC + Springer Link/Open, generated from http://api.crossref.org/members?filter=prefix:10.1007 + http://api.crossref.org/members?filter=prefix:10.1038
      this.publishers = [
        '10.3858',
        '10.1013',
        '10.1038',
        '10.1057',
        '10.1245',
        '10.1251',
        '10.1114',
        '10.26778',
        '10.26777',
        '10.3758',
        '10.1186',
        '10.1140',
        '10.7603',
        '10.1361',
        '10.1379',
        '10.1381',
        '10.1385',
        '10.2165',
        '10.1007',
        '10.1065',
        '10.1023',
        '10.4333',
        '10.5822',
        '10.5819',
        '10.1617',
        '10.5052',
        '10.4056'
      ];
      this.element = selection_1.get('.recommendation', parent);
    }
    RecommendationRenderer.prototype.render = function (recommendation) {
      var link = selection_1.get('.link', this.element);
      link.href = recommendation.link;
      link.title = this.capitalizeWhenUpperCase(recommendation.title, link, recommendation);
      var title = selection_1.get('.title', this.element);
      title.innerHTML = recommendation.title;
      var author = selection_1.get('.author', this.element);
      var newAuthors = [];
      for (var i = 0; i < recommendation.authors.length; i++) {
        author.textContent = this.capitalizeWhenUpperCase(recommendation.authors[i], author, recommendation);
        newAuthors.push(author.outerHTML);
      }
      selection_1.get('.authors', this.element).innerHTML = newAuthors.join('');
      var journalElement = selection_1.get('.journal', this.element);
      journalElement.textContent = this.capitalizeWhenUpperCase(recommendation.journal, journalElement, recommendation);
      var year = selection_1.get('.year', this.element);
      year.textContent = '';
      if (recommendation.pubdate) {
        var pubYear = new Date(recommendation.pubdate).getFullYear();
        if (isNaN(pubYear) == false && pubYear != 1970) {
          year.textContent = String(pubYear);
        }
      }
    };
    RecommendationRenderer.prototype.capitalizeWhenUpperCase = function (text, parent, recommendation) {
      if (text == null) {
        return '';
      }
      // Don't mess with our Journals (i.e British Dental Journal - BDJ) as we should publish the meta data correctly
      if (this.publishers.indexOf(recommendation.doi.split('/')[0])) {
        return text;
      }
      if (text.toUpperCase() != text) {
        return text;
      }
      parent.classList.add('capitalise');
      return text.toLowerCase();
    };
    return RecommendationRenderer;
  }();
  exports.RecommendationRenderer = RecommendationRenderer;
  var JobRecommendationRenderer = function () {
    function JobRecommendationRenderer(parent) {
      this.element = selection_1.get('.recommendation', parent);
    }
    JobRecommendationRenderer.prototype.render = function (recommendation) {
      var link = selection_1.get('.link', this.element);
      link.href = recommendation.redirectUrl;
      link.title = recommendation.title;
      selection_1.get('.job-title', this.element).innerHTML = recommendation.title;
      selection_1.get('.company', this.element).innerHTML = recommendation.company;
    };
    return JobRecommendationRenderer;
  }();
  exports.JobRecommendationRenderer = JobRecommendationRenderer;
  return exports;
}(recommendation_recommendation, shared_selection);
text_text = function (exports, strings_1, collections_1, selection_1) {
  var Regex = function () {
    function Regex() {
    }
    Regex.each = function (str, regex, matched, nonMatchedRaw) {
      var nonMatched = function (value) {
        return !strings_1.isEmpty(value) && nonMatchedRaw ? nonMatchedRaw(value) : null;
      };
      var position = 0;
      var match;
      while ((match = regex.exec(str)) != null) {
        nonMatched(str.substring(position, match.index));
        matched(match);
        position = regex.lastIndex;
      }
      nonMatched(str.substring(position));
    };
    Regex.replace = function (str, regex, matchedRaw, nonMatchedRaw) {
      var result = [];
      var nonMatched = function (value) {
        return !strings_1.isEmpty(value) && nonMatchedRaw ? result.push(nonMatchedRaw(value)) : null;
      };
      var matched = function (value) {
        return result.push(matchedRaw(value));
      };
      Regex.each(str, regex, matched, nonMatched);
      return result.join('');
    };
    return Regex;
  }();
  exports.Regex = Regex;
  var StructuredText = function () {
    function StructuredText(word, overflowed, lineStart, lineEnd, ellipsisClass) {
      if (word === void 0) {
        word = 'word';
      }
      if (overflowed === void 0) {
        overflowed = 'overflowed';
      }
      if (lineStart === void 0) {
        lineStart = 'line-start';
      }
      if (lineEnd === void 0) {
        lineEnd = 'line-end';
      }
      if (ellipsisClass === void 0) {
        ellipsisClass = 'ellipsis';
      }
      this.word = word;
      this.overflowed = overflowed;
      this.lineStart = lineStart;
      this.lineEnd = lineEnd;
      this.ellipsisClass = ellipsisClass;
    }
    StructuredText.prototype.words = function (parent) {
      var _this = this;
      collections_1.list(parent.childNodes).forEach(function (child) {
        if (child instanceof Element && child.tagName.toLocaleLowerCase() == 'span' && child.classList.contains(_this.word)) {
          return;
        }
        if (child instanceof Text) {
          var result_1 = document.createDocumentFragment();
          Regex.each(child.wholeText, /\s+/g, function (spaces) {
            result_1.appendChild(document.createTextNode(spaces[0]));
          }, function (word) {
            var span = document.createElement('span');
            span.classList.add(_this.word);
            span.appendChild(document.createTextNode(word));
            result_1.appendChild(span);
          });
          parent.replaceChild(result_1, child);
        } else {
          _this.words(child);
        }
      });
    };
    StructuredText.prototype.overflow = function (parent) {
      var _this = this;
      var matched = false;
      this.allWords(parent).each(function (element) {
        if (overflowed(parent, element))
          matched = true;
        if (matched)
          element.classList.add(_this.overflowed);
        else
          element.classList.remove(_this.overflowed);
      });
    };
    StructuredText.prototype.allWords = function (parent) {
      return selection_1.select('.' + this.word, parent).as(HTMLElement);
    };
    StructuredText.prototype.visibleWords = function (parent) {
      return selection_1.select('.' + this.word + ':not(.' + this.overflowed + ')', parent).as(HTMLElement);
    };
    StructuredText.prototype.lastWord = function (parent) {
      return this.visibleWords(parent).last();
    };
    StructuredText.prototype.lines = function (parent) {
      var _this = this;
      var lines = this.visibleWords(parent).groupBy(function (element) {
        return element.offsetTop;
      });
      Object.keys(lines).map(function (line) {
        return lines[line];
      }).forEach(function (elements) {
        elements.each(function (e) {
          return e.classList.remove(_this.lineStart, _this.lineEnd);
        });
        elements.head().classList.add(_this.lineStart);
        elements.last().classList.add(_this.lineEnd);
      });
    };
    StructuredText.prototype.ellipsis = function (parent) {
      var _this = this;
      selection_1.select(this.ellipsisClass).each(function (e) {
        e.classList.remove(_this.ellipsisClass);
        e.textContent = e.getAttribute('original-text');
      });
      var last = this.lastWord(parent);
      if (this.allWords(parent).last() == last)
        return;
      var original = last.getAttribute('original-text') || last.textContent;
      last.setAttribute('original-text', original);
      last.classList.add(this.ellipsisClass);
      for (var i = original.length; i > 0; i--) {
        last.textContent = original.substr(0, i) + '\u2026';
        if (!overflowed(parent, last))
          break;
      }
    };
    StructuredText.prototype.squeeze = function (parent, newElement) {
      var last = this.lastWord(parent);
      last.parentElement.insertBefore(newElement, last.nextElementSibling);
      if (overflowed(parent, newElement)) {
        last.classList.add(this.overflowed);
        this.squeeze(parent, newElement);
      }
    };
    StructuredText.prototype.process = function (container, squeezeElement) {
      this.words(container);
      this.overflow(container);
      if (squeezeElement)
        this.squeeze(container, squeezeElement);
      this.ellipsis(container);
      this.lines(container);
    };
    return StructuredText;
  }();
  exports.StructuredText = StructuredText;
  function overflowed(parent, child) {
    return offsetBottom(child) > offsetBottom(parent);
  }
  exports.overflowed = overflowed;
  function offsetBottom(element) {
    return element.offsetHeight + element.offsetTop;
  }
  exports.offsetBottom = offsetBottom;
  return exports;
}(text_text, shared_strings, shared_collections, shared_selection);
shared_storage = function (exports, strings_1) {
  exports.LOCALSTORAGE_KEY = 'uptodate-user-id';
  function hasStorage() {
    try {
      var key = 'uptodate-test';
      var expected = 'works';
      window.localStorage.setItem(key, expected);
      var actual = window.localStorage.getItem(key);
      window.localStorage.removeItem(key);
      return expected === actual;
    } catch (e) {
      return false;
    }
  }
  exports.hasStorage = hasStorage;
  function storageObject(storage) {
    if (storage === void 0) {
      storage = window.localStorage;
    }
    var result = {};
    for (var i = 0; i < storage.length; i++) {
      var key = storage.key(i);
      result[key] = strings_1.coerce(storage.getItem(key));
    }
    return result;
  }
  exports.storageObject = storageObject;
  function copyIntoStorage(source, storage, prefix) {
    Object.keys(source).forEach(function (key) {
      if (strings_1.startsWith(prefix, key)) {
        var value = source[key];
        if (value == null || typeof value == 'undefined') {
          storage.removeItem(key);
        } else {
          storage.setItem(key, value);
        }
      }
    });
  }
  exports.copyIntoStorage = copyIntoStorage;
  return exports;
}(shared_storage, shared_strings);
shared_location = function (exports, selection_1, http_1, html_1, storage_1) {
  var CurrentLocation = function () {
    function CurrentLocation(type, display_type, design_type, doi, issn, url, hostsite, meta_data, session_ids, browser_extension_loaded) {
      if (type === void 0) {
        type = CurrentLocation.extractType();
      }
      if (display_type === void 0) {
        display_type = CurrentLocation.extractDisplayType();
      }
      if (design_type === void 0) {
        design_type = CurrentLocation.extractDesignType();
      }
      if (doi === void 0) {
        doi = CurrentLocation.extractDoi();
      }
      if (issn === void 0) {
        issn = CurrentLocation.extractIssn();
      }
      if (url === void 0) {
        url = window.location.href;
      }
      if (hostsite === void 0) {
        hostsite = CurrentLocation.extractHostsite(url);
      }
      if (meta_data === void 0) {
        meta_data = CurrentLocation.extractMetaData(type);
      }
      if (session_ids === void 0) {
        session_ids = CurrentLocation.extractSessionIds();
      }
      if (browser_extension_loaded === void 0) {
        browser_extension_loaded = false;
      }
      this.type = type;
      this.display_type = display_type;
      this.design_type = design_type;
      this.doi = doi;
      this.issn = issn;
      this.url = url;
      this.hostsite = hostsite;
      this.meta_data = meta_data;
      this.session_ids = session_ids;
      this.browser_extension_loaded = browser_extension_loaded;
      this.dois = doi ? [doi] : [];
    }
    CurrentLocation.prototype.checkForBrowserExtension = function (extensionId, callback) {
      if ('chrome' in window && extensionId) {
        var that_1 = this;
        window.chrome.runtime.sendMessage(extensionId, { type: 'browserExtensionInstalledRequest' }, function (val) {
          that_1.browser_extension_loaded = !!val;
          callback();
        });
      } else {
        callback();
      }
    };
    CurrentLocation.extractSessionIds = function () {
      var ids = [];
      if (storage_1.hasStorage()) {
        var item = window.localStorage.getItem(storage_1.LOCALSTORAGE_KEY);
        if (item != null)
          ids.push(item);
      }
      return ids;
    };
    CurrentLocation.extractHostsite = function (url) {
      var parsedUri = http_1.uri(url);
      var hostname;
      var hostsiteQueryParam = http_1.queryObject(url)['uptodate-hostsite'];
      if (hostsiteQueryParam) {
        hostname = hostsiteQueryParam;
      } else {
        hostname = parsedUri.authority;
      }
      // unfortunately, order matters here atm
      if (hostname.indexOf('recommendations.springernature.com') != -1 || hostname.indexOf('recommended.springernature.com') != -1)
        return 'recommended';
      if (hostname.indexOf('nature.com') != -1)
        return 'nature';
      if (hostname.indexOf('springer.com') != -1)
        return 'springer';
      if (hostname.indexOf('biomedcentral.com') != -1)
        return 'biomedcentral';
      if (hostname.indexOf('springeropen.com') != -1)
        return 'springeropen';
      if (hostname.indexOf('localhost') != -1)
        return 'localhost';
      return 'unknown';
    };
    CurrentLocation.prototype.toQuery = function () {
      return encodeURIComponent(this.json());
    };
    CurrentLocation.prototype.json = function () {
      return JSON.stringify(this);
    };
    CurrentLocation.extractDisplayType = function () {
      if (selection_1.get(CurrentLocation.inlineSelector, document)) {
        return 'inline';
      } else {
        return 'popup';
      }
    };
    CurrentLocation.extractDesignType = function () {
      if (selection_1.get('link[href*=mosaic], meta[name=\'WT.template\'][content=mosaic]', document)) {
        return 'mosaic';
      } else {
        return 'unknown';
      }
    };
    CurrentLocation.extractType = function () {
      var doi = CurrentLocation.extractDoi();
      if (doi)
        return 'article';
      var value = selection_1.select('meta[name=\'citation_article_type\'], meta[name=\'WT.cg_s\'], meta[name=\'dc.type\']').attr('content').head();
      if (value) {
        var page = value.toLowerCase();
        if (page == 'latest research')
          page = 'research';
        if (page == 'jobs')
          page = 'job';
        if (CurrentLocation.allowedTypes.indexOf(page) != -1)
          return page;
      }
      // Fallback to Title for Issue Page!
      if (document.title.indexOf('Table of contents') == 0)
        return 'issue';
      if (selection_1.select('meta[name=\'WT.cg_n\']').attr('content').head() == 'Natureevents')
        return 'event';
      if (selection_1.select('meta[name=\'WT.page_categorisation\']').attr('content').head() == 'Home')
        return 'journalHomepage';
      return null;
    };
    CurrentLocation.extractMetaData = function (type) {
      switch (type) {
      case 'job':
        return {
          'job': {
            id: selection_1.select('meta[name=\'DCSext.job_id\']').attr('content').head(),
            title: selection_1.select('meta[name=\'description\']').attr('content').head(),
            location: selection_1.select('meta[name=\'Job Location\']').attr('content').head(),
            employer: selection_1.select('meta[name=\'Job Employer\']').attr('content').head(),
            employer_id: selection_1.select('meta[name=\'DCSext.employer_id\']').attr('content').head(),
            type: selection_1.select('meta[name=\'Job Type\']').attr('content').head(),
            qualifications: selection_1.select('meta[name=\'Job Qualifications\']').attr('content').head()
          }
        };
      case 'event':
        var data = html_1.dataListObject(selection_1.get('dl[class="event-details"]'));
        return {
          'event': {
            id: selection_1.select('meta[name=\'DCSext.event_id\']').attr('content').head(),
            title: document.title.trim(),
            organization: data['Organization:'],
            type: data['Type:'],
            venue: data['Venue:'],
            location: data['Location:'],
            website: data['Website:'],
            area: data['Area'],
            specialty: data['Specialty'],
            subject: data['Subject']
          }
        };
      }
      return {};
    };
    CurrentLocation.extractDoi = function () {
      var doi = selection_1.select('meta[name=\'citation_doi\'], meta[name=\'dc.identifier\'], meta[name=\'DC.identifier\'], meta[name=\'prism.doi\'], meta[name=\'dc.Identifier\'], meta[property=\'citation_doi\']').attr('content');
      if (doi.isEmpty()) {
        doi = selection_1.select('a[ref=\'aid_type=doi\']').text();
      }
      if (doi.isEmpty()) {
        doi = selection_1.select('meta[name=\'citation_arxiv_id\']').attr('content').map(function (arxiv_id) {
          return 'arxiv:' + arxiv_id;
        });
      }
      return doi.map(function (instance) {
        if (!instance) {
          return null;
        }
        var match = instance.match(CurrentLocation.doiRegex);
        return match != null ? match[1] : null;
      }).filter(function (instance) {
        return instance != null;
      }).head();
    };
    CurrentLocation.extractIssn = function () {
      var meta = selection_1.select('meta[name=\'citation_issn\'], meta[name=\'prism.issn\'], meta[name=\'prism.eIssn\']').attr('content').head();
      if (meta)
        return meta.toUpperCase();
      var rawIssn = selection_1.select('.issn, .eissn').text().head();
      var text = rawIssn ? rawIssn.match(this.issnRegex) : null;
      return text ? text[0].toUpperCase() : null;
    };
    CurrentLocation.inlineSelector = 'div[data-rel=\'uptodate-inline\'], link[rel=\'uptodate-inline\']';
    CurrentLocation.allowedTypes = [
      'article',
      'research',
      'issue',
      'homepage',
      'job',
      'event'
    ];
    CurrentLocation.trackTypes = [
      'article',
      'job',
      'event'
    ];
    CurrentLocation.doNotDisplay = [
      'job',
      'event'
    ];
    CurrentLocation.doiRegex = /.*(10\.\d{4,9}\/[-._;()\/:A-Z0-9]+).*/i;
    CurrentLocation.issnRegex = /\d{4}\-\d{3}[\dxX]/i;
    return CurrentLocation;
  }();
  exports.CurrentLocation = CurrentLocation;
  return exports;
}(shared_location, shared_selection, shared_http, shared_html, shared_storage);
shared_state = function (exports, selection_1, strings_1, location_1, events_1, html_1, collections_1) {
  function state(config, current_location, screen) {
    if (current_location === void 0) {
      current_location = new location_1.CurrentLocation();
    }
    if (screen === void 0) {
      screen = window.screen;
    }
    return Converter.toUnderscore({
      config: config,
      current_location: current_location,
      screen: screen
    });
  }
  exports.state = state;
  var StateChange = function () {
    function StateChange(root, events) {
      if (events === void 0) {
        events = new events_1.ConsoleEventHandler();
      }
      this.root = root;
      this.events = events;
      this.capture();
      this.setInitialState();
    }
    StateChange.prototype.capture = function () {
      var _this = this;
      html_1.on(this.root, 'change', function (e) {
        var input = e.target;
        if (html_1.Elements.matches(input, '.state[name][value]'))
          _this.setState(input);
        if (html_1.Elements.matches(input, '[data-event-subject][data-event-action][data-event-object]'))
          _this.trackEvent(input);
        return true;
      }, true);
      html_1.on(this.root, [
        'click',
        'contextmenu'
      ], function (e) {
        var element = events_1.Events.path(e).find(function (e) {
          return html_1.Elements.matches(e, ':not(.state)[data-event-object]');
        });
        if (element)
          _this.trackEvent(element);
        return true;
      }, true);
    };
    StateChange.prototype.setState = function (input) {
      var groupLeader = selection_1.get('input[name=' + input.name + ']', this.root);
      var oldValue = groupLeader.getAttribute('state-new') || '';
      var newValue = input.value;
      if (oldValue != newValue) {
        groupLeader.setAttribute('state-old', oldValue);
        groupLeader.setAttribute('state-new', newValue);
      }
    };
    StateChange.prototype.trackEvent = function (element) {
      var data = this.dataAttributes(element);
      this.events.fire(encodeURIComponent(element.getAttribute('data-event-subject')), encodeURIComponent(element.getAttribute('data-event-action')), encodeURIComponent(element.getAttribute('data-event-object')), data);
    };
    StateChange.prototype.dataAttributes = function (input, data) {
      var _this = this;
      if (data === void 0) {
        data = {};
      }
      return collections_1.list(input.attributes).filter(function (a) {
        return strings_1.startsWith('data-', a.name);
      }).filter(function (a) {
        return !strings_1.startsWith('data-event', a.name);
      }).reduce(function (accumulator, attr) {
        accumulator[encodeURIComponent(attr.name.replace('data-', ''))] = _this.getAttributeValue(attr);
        return accumulator;
      }, data);
    };
    StateChange.prototype.getAttributeValue = function (attr) {
      try {
        return JSON.parse(attr.value);
      } catch (e) {
        return attr.value;
      }
    };
    StateChange.prototype.setInitialState = function () {
      var _this = this;
      selection_1.select('.state[name][value]:not([state-new]):checked', this.root).as(HTMLInputElement).each(function (state) {
        var groupLeader = selection_1.get('input[name=' + state.name + ']', _this.root);
        groupLeader.setAttribute('state-new', groupLeader.defaultValue);
      });
    };
    return StateChange;
  }();
  exports.StateChange = StateChange;
  function isArray(value) {
    return value != null && value.constructor == Array;
  }
  exports.isArray = isArray;
  function isObject(value) {
    return value != null && typeof value == 'object';
  }
  exports.isObject = isObject;
  var Converter = function () {
    function Converter() {
    }
    Converter.toUnderscore = function (obj) {
      return this.map(obj, function (key) {
        return key.replace(/-/g, '_');
      });
    };
    Converter.toHyphen = function (obj) {
      return this.map(obj, function (key) {
        return key.replace(/_/g, '-');
      });
    };
    Converter.map = function (obj, fun) {
      var _this = this;
      if (isArray(obj)) {
        var array = obj;
        return array.reduce(function (result, v) {
          result.push(_this.map(v, fun));
          return result;
        }, []);
      }
      if (isObject(obj)) {
        var result = {};
        for (var key in obj) {
          var v = obj[key];
          if (v == null || typeof v == 'function')
            continue;
          result[fun(key)] = this.map(v, fun);
        }
        return result;
      }
      return obj;
    };
    return Converter;
  }();
  exports.Converter = Converter;
  return exports;
}(shared_state, shared_selection, shared_strings, shared_location, shared_events, shared_html, shared_collections);
shared_events = function (exports, state_1, requests_1, http_1, collections_1, html_1) {
  var ConsoleEventHandler = function () {
    function ConsoleEventHandler() {
    }
    ConsoleEventHandler.prototype.fire = function (subject, action, object, data) {
      if (console.log)
        console.log('Event: ' + subject + ' ' + action + ' ' + object + ' -> ' + JSON.stringify(data));
    };
    return ConsoleEventHandler;
  }();
  exports.ConsoleEventHandler = ConsoleEventHandler;
  var Events = function () {
    function Events(state) {
      this.state = state;
    }
    Events.prototype.fire = function (subject, action, object, data) {
      http_1.http(requests_1.Requests.postEvent(state_1.Converter.toUnderscore(collections_1.mergeObjects(this.state, {
        event: {
          'subject': subject,
          'action': action,
          'object': object,
          'data': data,
          'client_time': this.toIsoStringWithOffset(new Date())
        }
      }))));
    };
    Events.prototype.toIsoStringWithOffset = function (date) {
      var tzo = -date.getTimezoneOffset(), dif = tzo >= 0 ? '+' : '-', pad = function (num) {
          var norm = Math.abs(Math.floor(num));
          return (norm < 10 ? '0' : '') + norm;
        };
      return date.getFullYear() + '-' + pad(date.getMonth() + 1) + '-' + pad(date.getDate()) + 'T' + pad(date.getHours()) + ':' + pad(date.getMinutes()) + ':' + pad(date.getSeconds()) + dif + pad(tzo / 60) + ':' + pad(tzo % 60);
    };
    Events.create = function (name, data) {
      if (data === void 0) {
        data = {
          bubbles: true,
          cancelable: true,
          detail: null
        };
      }
      if (data.detail) {
        try {
          return new CustomEvent(name, data);
        } catch (e) {
          var event_1 = document.createEvent('CustomEvent');
          event_1.initCustomEvent(name, data.bubbles, data.cancelable, data.detail);
          return event_1;
        }
      } else {
        try {
          return new Event(name, data);
        } catch (e) {
          var event_2 = document.createEvent('Event');
          event_2.initEvent(name, data.bubbles, data.cancelable);
          return event_2;
        }
      }
    };
    Events.path = function (e) {
      return html_1.Elements.path(e.target);
    };
    return Events;
  }();
  exports.Events = Events;
  return exports;
}(shared_events, shared_state, shared_requests, shared_http, shared_collections, shared_html);
shared_messaging = function (exports, events_1, http_1, errors_1, html_1) {
  var MessageDispatcher = function () {
    function MessageDispatcher() {
    }
    MessageDispatcher.fireResize = function (root, value, eventNameOverride) {
      var eventName = eventNameOverride || 'resize';
      var style;
      if (value instanceof HTMLElement) {
        var boxShadowBuffer = html_1.Elements.calculateBoxShadow(value);
        style = {
          width: value.offsetWidth + boxShadowBuffer + 'px',
          height: value.offsetHeight + boxShadowBuffer + 'px'
        };
      } else {
        style = value;
      }
      MessageDispatcher.dispatch(root, {
        name: eventName,
        body: style
      });
    };
    MessageDispatcher.dispatch = function (root, message) {
      root.dispatchEvent(events_1.Events.create('client_message', {
        bubbles: true,
        cancelable: true,
        detail: message
      }));
    };
    return MessageDispatcher;
  }();
  exports.MessageDispatcher = MessageDispatcher;
  var MessageReceiver = function () {
    function MessageReceiver(window, expectedOrigin) {
      var _this = this;
      this.window = window;
      this.expectedOrigin = expectedOrigin;
      window.addEventListener('message', function (event) {
        var actualHost = http_1.uri(event.origin).host;
        var expectedHost = http_1.uri(expectedOrigin).host;
        if (actualHost != expectedHost) {
          errors_1.Debug.log('Origin host did not match expected: expectedHost:' + expectedHost + ' actualHost:' + actualHost);
          return;
        }
        var data = event.data;
        errors_1.Debug.log(window.name + ' received message from ' + expectedOrigin + ' : ' + data.name + ' -> ' + JSON.stringify(data.body));
        var slot = _this[data.name];
        if (!slot) {
          errors_1.Debug.log('No slot called ' + data.name + ' found');
          return;
        }
        try {
          slot.call(_this, data.body);
        } catch (e) {
          errors_1.UnhandledError.unhandled(e);
        }
      }, true);
    }
    return MessageReceiver;
  }();
  exports.MessageReceiver = MessageReceiver;
  var MessageSender = function () {
    function MessageSender(windows, destinationOrigin) {
      this.windows = windows;
      this.destinationOrigin = destinationOrigin;
    }
    MessageSender.prototype.send = function (name, body) {
      var _this = this;
      this.windows.forEach(function (w) {
        w.postMessage({
          name: name,
          body: body
        }, _this.destinationOrigin);
      });
    };
    return MessageSender;
  }();
  exports.MessageSender = MessageSender;
  return exports;
}(shared_messaging, shared_events, shared_http, shared_errors, shared_html);
shared_component = function (exports, events_1, selection_1, messaging_1, html_1) {
  var Component = function () {
    function Component(selector, parent) {
      this.root = selection_1.get(selector, parent);
    }
    Component.prototype.fireResize = function (value) {
      var style;
      if (value instanceof HTMLElement) {
        var boxShadowBuffer = html_1.Elements.calculateBoxShadow(value);
        style = {
          width: value.offsetWidth + boxShadowBuffer + 'px',
          height: value.offsetHeight + boxShadowBuffer + 'px'
        };
      } else {
        style = value;
      }
      messaging_1.MessageDispatcher.dispatch(this.root, {
        name: 'resize',
        body: style
      });
    };
    Component.prototype.fireInlineEvent = function (className) {
      messaging_1.MessageDispatcher.dispatch(this.root, {
        name: 'inlineEvent',
        body: className
      });
    };
    Component.prototype.reset = function (fire, animate) {
      if (fire === void 0) {
        fire = true;
      }
      if (animate === void 0) {
        animate = true;
      }
      this.animate(animate);
      selection_1.select('.state', this.root).as(HTMLInputElement).each(function (input) {
        if (input.checked != input.defaultChecked) {
          input.checked = input.defaultChecked;
          if (fire)
            input.dispatchEvent(events_1.Events.create('change'));
        }
      });
      this.animate(true);
    };
    Component.prototype.animate = function (animate) {
      if (animate) {
        this.root.classList.remove('disable-animate');
      } else {
        this.root.classList.add('disable-animate');
      }
    };
    Component.prototype.stateInput = function (name, state) {
      return selection_1.get('input[name="' + name + '"][value="' + state + '"],input[name="' + name + '"][value="\\"' + state + '\\""]', this.root);
    };
    Component.prototype.hasState = function (name, state) {
      return this.stateInput(name, state).checked;
    };
    Component.prototype.set = function (name, state, fire) {
      if (fire === void 0) {
        fire = true;
      }
      var previousValue = this.get(name);
      var input = this.stateInput(name, state);
      input.checked = true;
      if (fire)
        input.dispatchEvent(events_1.Events.create('change'));
      return previousValue;
    };
    Component.prototype.fire = function (name) {
      var input = selection_1.get('input[name="' + name + '"]:checked', this.root);
      input.dispatchEvent(events_1.Events.create('change'));
    };
    Component.prototype.get = function (name) {
      var input = selection_1.get('input[name="' + name + '"]:checked', this.root);
      return input ? input.value : input;
    };
    return Component;
  }();
  exports.Component = Component;
  return exports;
}(shared_component, shared_events, shared_selection, shared_messaging, shared_html);
shared_templates = function (exports, selection_1) {
  var Templates = function () {
    function Templates() {
    }
    Templates.clone = function (template) {
      this.polyfill(template);
      return template.ownerDocument.importNode(template.content, true);
    };
    Templates.polyfill = function (template) {
      if (!template.content) {
        template.content = selection_1.select(template).children().detach();
      }
    };
    Templates.polyfillTemplates = function (root) {
      var _this = this;
      selection_1.select('template', root).each(function (template) {
        return _this.polyfill(template);
      });
    };
    return Templates;
  }();
  exports.Templates = Templates;
  return exports;
}(shared_templates, shared_selection);
shared_forms = function (exports, selection_1) {
  function request(form) {
    var inputs = selection_1.select('input[name], textarea[name], select[name]', form);
    var message = inputs.filter(function (input) {
      return !((input.type == 'radio' || input.type == 'checkbox') && !input.checked);
    }).map(function (input) {
      return encodeURIComponent(input.name) + '=' + encodeURIComponent(input.value);
    }).join('&');
    var method = (form.getAttribute('method') || 'GET').toUpperCase();
    var uri = form.getAttribute('action');
    var headers = {};
    var entity = '';
    if (method == 'GET') {
      uri = uri + '?' + message;
    }
    if (method == 'POST') {
      headers['Content-Type'] = 'application/x-www-form-urlencoded';
      entity = message;
    }
    return {
      method: method,
      url: uri,
      headers: headers,
      entity: entity
    };
  }
  exports.request = request;
  return exports;
}(shared_forms, shared_selection);
//# sourceMappingURL=forms.js.map;
var __extends = this && this.__extends || function (d, b) {
  for (var p in b)
    if (b.hasOwnProperty(p))
      d[p] = b[p];
  function __() {
    this.constructor = d;
  }
  d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
email_this_email_this = function (exports, component_1, selection_1, html_1, errors_1, http_1, forms_1) {
  var EmailThis = function (_super) {
    __extends(EmailThis, _super);
    function EmailThis(parent, state) {
      _super.call(this, '.email-this', parent);
      this.state = state;
    }
    EmailThis.prototype.attachToForm = function () {
      var _this = this;
      var form = selection_1.get('form.card-send', this.root);
      html_1.on(form, 'submit', function () {
        form.action = _this.state.config.host + 'send-article';
        var state = selection_1.get('input[name=state]', form);
        state.value = JSON.stringify(_this.state);
        _this.sending();
        errors_1.Debug.log('attempting to subscribe');
        http_1.http(forms_1.request(form), function (response) {
          if (response.status >= 299) {
            errors_1.Debug.log('failed to send');
            _this.error();
          } else {
            errors_1.Debug.log('succeeded in sending');
            _this.sent();
          }
        });
        return false;
      });
    };
    EmailThis.prototype.reset = function (fire, animate) {
      if (fire === void 0) {
        fire = true;
      }
      if (animate === void 0) {
        animate = true;
      }
      var form = selection_1.get('form.card-send', this.root);
      form.reset();
      return _super.prototype.reset.call(this, fire, animate);
    };
    EmailThis.prototype.send = function () {
      this.set('send-state', 'initial');
    };
    EmailThis.prototype.sending = function () {
      this.set('send-state', 'sending');
    };
    EmailThis.prototype.error = function () {
      this.set('send-state', 'error');
    };
    EmailThis.prototype.sent = function () {
      this.set('send-state', 'sent');
    };
    return EmailThis;
  }(component_1.Component);
  exports.EmailThis = EmailThis;
  return exports;
}(email_this_email_this, shared_component, shared_selection, shared_html, shared_errors, shared_http, shared_forms);
//# sourceMappingURL=email-this.js.map;
var __extends = this && this.__extends || function (d, b) {
  for (var p in b)
    if (b.hasOwnProperty(p))
      d[p] = b[p];
  function __() {
    this.constructor = d;
  }
  d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
recommendation_journey_recommendation_journey = function (exports, recommendation_1, text_1, component_1, selection_1, templates_1, html_1, email_this_1) {
  var RecommendationJourney = function (_super) {
    __extends(RecommendationJourney, _super);
    function RecommendationJourney(parent, state) {
      _super.call(this, '.recommendation-journey', parent);
      this.state = state;
      this.emailThis = new email_this_1.EmailThis(this.root, this.state);
    }
    RecommendationJourney.prototype.render = function (recommendations) {
      var _this = this;
      var parent = selection_1.get('.recommendations', this.root);
      var template = selection_1.get('template', parent);
      if (recommendations.length > 0) {
        this.state.popup_info = { position: 'recommendation-1' };
      }
      recommendations.forEach(function (recommendation, index) {
        var position = index + 1;
        // human readable
        var instance = templates_1.Templates.clone(template);
        var suffix = '-' + position;
        new recommendation_1.RecommendationRenderer(instance).render(recommendation);
        var eventAttributes = {
          'data-recommendation-doi': recommendation.doi,
          'data-recommendation-dois': [recommendation.doi],
          'data-recommendation-issn': recommendation.issn,
          'data-recommendation-position': String(position),
          'data-total-recommendations': String(recommendations.length),
          'data-randomised-recommendation': String(recommendation.randomised),
          'data-recommendation-link': recommendation.raw_link
        };
        var title = selection_1.get('.title', instance);
        var st = new text_1.StructuredText();
        st.process(title);
        selection_1.select('.next', instance).on('click', function (e) {
          var position = Number(e.getAttribute('data-recommendation-position'));
          _this.state.popup_info.position = 'recommendation-' + (position + 1);
          return true;
        });
        selection_1.select('.previous', instance).on('click', function (e) {
          var position = Number(e.getAttribute('data-recommendation-position'));
          _this.state.popup_info.position = 'recommendation-' + (position - 1);
          return true;
        });
        selection_1.select('input[name=recommendation-position]', instance).on('change', function () {
          st.process(title);
        }).map(html_1.attributes(eventAttributes, {
          value: String(position),
          id: function (value) {
            return value + suffix;
          },
          checked: position == 1
        }));
        var debug = selection_1.get('label[for=uptodate-recommendation-position].debug', instance);
        debug.htmlFor += suffix;
        selection_1.select('.text', debug).text(String(position));
        selection_1.get('.current-recommendation', instance).textContent = String(position);
        selection_1.get('.total-recommendations', instance).textContent = String(recommendations.length);
        selection_1.select('label[for=uptodate-recommendation-position].next', instance).map(html_1.attributes(eventAttributes, {
          'for': function (value) {
            return value + '-' + (position == recommendations.length ? 1 : position + 1);
          }
        }));
        if (index > 0) {
          selection_1.select('label[for=uptodate-recommendation-position].previous', instance).map(html_1.attributes(eventAttributes, {
            'for': function (value) {
              return value + '-' + (position - 1);
            }
          }));
        }
        parent.appendChild(instance);
      });
      this.emailThis.attachToForm();
    };
    RecommendationJourney.prototype.display = function (fire) {
      this.position(this.position(), fire);
    };
    RecommendationJourney.prototype.position = function (value, fire) {
      if (value) {
        return Number(this.set('recommendation-position', String(value), fire));
      }
      return Number(this.get('recommendation-position'));
    };
    return RecommendationJourney;
  }(component_1.Component);
  exports.RecommendationJourney = RecommendationJourney;
  return exports;
}(recommendation_journey_recommendation_journey, recommendation_recommendation, text_text, shared_component, shared_selection, shared_templates, shared_html, email_this_email_this);
minimised_minimised = function (exports, selection_1, events_1) {
  var Minimised = function () {
    function Minimised(parent) {
      this.parent = parent;
      this.element = selection_1.get('.minimised', parent);
    }
    Minimised.prototype.initial = function (fire) {
      if (fire === void 0) {
        fire = true;
      }
      this.check('minimised-state', 'initial', fire);
    };
    Minimised.prototype.notification = function (fire) {
      if (fire === void 0) {
        fire = true;
      }
      this.check('minimised-state', 'notification', fire);
    };
    Minimised.prototype.check = function (name, state, fire) {
      if (fire === void 0) {
        fire = true;
      }
      var input = selection_1.get('input[name=' + name + '][value=' + state + ']', this.element);
      input.checked = true;
      if (fire)
        input.dispatchEvent(events_1.Events.create('change'));
    };
    return Minimised;
  }();
  exports.Minimised = Minimised;
  return exports;
}(minimised_minimised, shared_selection, shared_events);
//# sourceMappingURL=minimised.js.map;
var __extends = this && this.__extends || function (d, b) {
  for (var p in b)
    if (b.hasOwnProperty(p))
      d[p] = b[p];
  function __() {
    this.constructor = d;
  }
  d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
email_journey_email = function (exports, http_1, forms_1, component_1, selection_1, html_1, errors_1) {
  var EmailJourney = function (_super) {
    __extends(EmailJourney, _super);
    function EmailJourney(parent, state) {
      _super.call(this, '.email', parent);
      this.state = state;
      this.elementName = 'email-journey';
      this.attachToForm();
    }
    EmailJourney.prototype.attachToForm = function () {
      var _this = this;
      var form = selection_1.get('.card-subscribe', this.root);
      html_1.on(form, 'submit', function () {
        form.action = _this.state.config.host + 'subscribe';
        var state = selection_1.get('input[name=state]', form);
        state.value = JSON.stringify(_this.state);
        _this.subscribing();
        errors_1.Debug.log('attempting to subscribe');
        http_1.http(forms_1.request(form), function (response) {
          if (response.status >= 299) {
            errors_1.Debug.log('failed to subscribe');
            _this.error();
          } else {
            errors_1.Debug.log('succeeded in subscribing');
            _this.subscribed();
          }
        });
        return false;
      });
    };
    EmailJourney.prototype.signup = function () {
      this.state.popup_info.position = 'email-signup';
      this.set(this.elementName, 'signup');
    };
    EmailJourney.prototype.subscribe = function () {
      this.state.popup_info.position = 'email-subscribe';
      this.set(this.elementName, 'subscribe');
      this.set('subscribe-state', 'initial');
    };
    EmailJourney.prototype.subscribing = function () {
      this.state.popup_info.position = 'email-subscribing';
      this.set('subscribe-state', 'subscribing');
    };
    EmailJourney.prototype.error = function () {
      this.state.popup_info.position = 'email-error';
      this.set('subscribe-state', 'error');
    };
    EmailJourney.prototype.subscribed = function () {
      this.state.popup_info.position = 'email-subscribed';
      this.set(this.elementName, 'subscribed');
    };
    return EmailJourney;
  }(component_1.Component);
  exports.EmailJourney = EmailJourney;
  return exports;
}(email_journey_email, shared_http, shared_forms, shared_component, shared_selection, shared_html, shared_errors);
shared_scroll = function (exports, html_1, selection_1) {
  var WindowScrollCondition = function () {
    function WindowScrollCondition(config) {
      this.config = config;
    }
    WindowScrollCondition.prototype.required = function () {
      return html_1.hasVerticalScrollBar() && !this.hasScrolledEnough();
    };
    WindowScrollCondition.prototype.hasScrolledEnough = function () {
      return window.pageYOffset > this.config.minimum_scroll_height;
    };
    WindowScrollCondition.prototype.await = function (done) {
      var _this = this;
      var scrollHandler = function () {
        if (_this.hasScrolledEnough()) {
          window.removeEventListener('scroll', scrollHandler);
          done();
        }
      };
      window.addEventListener('scroll', scrollHandler);
    };
    return WindowScrollCondition;
  }();
  exports.WindowScrollCondition = WindowScrollCondition;
  var ClientScrollListener = function () {
    function ClientScrollListener(sender, receiver, state) {
      var _this = this;
      this.sender = sender;
      this.receiver = receiver;
      this.state = state;
      this.receiver['scroll_info'] = function (value) {
        return _this.scroll_info(value);
      };
      this.receiver['scroll_bars_response'] = function (value) {
        return _this.scroll_bars_response(value);
      };
      this.sender.send('scroll_bars_request');
    }
    ClientScrollListener.prototype.scroll_bars_response = function (value) {
      this.scrollBars = value;
    };
    ClientScrollListener.prototype.scroll_info = function (value) {
      this.scrollInfo = value;
      if (this.done && this.hasScrolledEnough()) {
        var done = this.done;
        this.done = null;
        this.sender.send('scroll_info_stop');
        done();
      }
    };
    ClientScrollListener.prototype.required = function () {
      return this.scrollBars && this.scrollBars.vertical && !this.hasScrolledEnough();
    };
    ClientScrollListener.prototype.getScrolledPosOffset = function (elementTop, elementBottom) {
      var percentage = this.state.config['experiment_popup_scroll_position'] ? 0.75 : 1;
      var elementHeight = elementBottom - elementTop;
      var scrolledPosOffset = elementHeight * (1 - percentage);
      return scrolledPosOffset;
    };
    ClientScrollListener.prototype.hasScrolledEnough = function () {
      if (this.scrollInfo && this.scrollInfo.targetClientRect) {
        if (this.scrollInfo.targetClientRect.top === 0 && this.scrollInfo.targetClientRect.bottom === 0) {
          return false;
        }
        var elementTop = this.scrollInfo.targetClientRect.top;
        var elementBottom = this.scrollInfo.targetClientRect.bottom;
        if (this.state.current_location.display_type === 'inline') {
          //figure out a way for this to work mid way through the recommendations
          return elementBottom > 0 && elementTop < this.scrollInfo.windowHeight;
        } else {
          var scrolledPosOffset = this.getScrolledPosOffset(elementTop, elementBottom);
          return elementBottom < 0 || elementBottom - scrolledPosOffset < this.scrollInfo.windowHeight;
        }
      }
      return this.scrollInfo && this.scrollInfo.y > this.state.config.minimum_scroll_height;
    };
    ClientScrollListener.prototype.await = function (done) {
      this.done = done;
      this.sender.send('scroll_info_start');
    };
    return ClientScrollListener;
  }();
  exports.ClientScrollListener = ClientScrollListener;
  var JobClientScrollListener = function () {
    function JobClientScrollListener(sender, receiver, state) {
      var _this = this;
      this.sender = sender;
      this.receiver = receiver;
      this.state = state;
      this.receiver['jobs_scroll_info'] = function (value) {
        return _this.scroll_info(value);
      };
      this.receiver['jobs_scroll_bars_response'] = function (value) {
        return _this.scroll_bars_response(value);
      };
      this.sender.send('jobs_scroll_bars_request');
    }
    JobClientScrollListener.prototype.scroll_bars_response = function (value) {
      this.scrollBars = value;
    };
    JobClientScrollListener.prototype.scroll_info = function (value) {
      this.scrollInfo = value;
      if (this.done && this.hasScrolledEnough()) {
        var done = this.done;
        done();
        this.done = null;
        this.sender.send('jobs_scroll_info_stop');
      }
    };
    JobClientScrollListener.prototype.required = function () {
      return !this.hasScrolledEnough();
    };
    JobClientScrollListener.prototype.hasScrolledEnough = function () {
      if (this.scrollInfo && this.scrollInfo.targetClientRect) {
        if (this.scrollInfo.targetClientRect.top === 0 && this.scrollInfo.targetClientRect.bottom === 0) {
          return false;
        }
        var elementTop = this.scrollInfo.targetClientRect.top;
        var elementBottom = this.scrollInfo.targetClientRect.bottom;
        return elementBottom > 0 && elementTop < this.scrollInfo.windowHeight;
      }
      return this.scrollInfo && this.scrollInfo.y > this.state.config.minimum_scroll_height;
    };
    JobClientScrollListener.prototype.await = function (done) {
      this.done = done;
      this.sender.send('jobs_scroll_info_start');
    };
    return JobClientScrollListener;
  }();
  exports.JobClientScrollListener = JobClientScrollListener;
  var HostScrollListener = function () {
    function HostScrollListener(sender, receiver, state) {
      var _this = this;
      this.sender = sender;
      this.receiver = receiver;
      this.state = state;
      this.receiver['scroll_info_start'] = function () {
        return _this.start();
      };
      this.receiver['scroll_info_stop'] = function () {
        return _this.stop();
      };
      this.receiver['scroll_bars_request'] = function () {
        return _this.scroll_bars_request();
      };
    }
    HostScrollListener.prototype.scroll_bars_request = function () {
      this.sender.send('scroll_bars_response', {
        vertical: html_1.hasVerticalScrollBar(),
        horizontal: html_1.hasHorizontalScrollBar()
      });
    };
    HostScrollListener.prototype.start = function () {
      var _this = this;
      this.handler = window.setInterval(function () {
        function getAbstractElement() {
          var natureArticleSelector1 = 'div#abstract';
          var natureArticleSelector2 = 'section[aria-labelledby=\'abstract\'], section[aria-labelledby=\'Abs1\']';
          var bmcSpringerOpenSelector = 'section.Abstract';
          return selection_1.get(natureArticleSelector1 + ', ' + natureArticleSelector2 + ', ' + bmcSpringerOpenSelector);
        }
        function addAdditionalBodyInfo(bodyInfo, elm) {
          var boundingClientRect = elm.getBoundingClientRect();
          bodyInfo.windowHeight = window.innerHeight;
          bodyInfo.targetClientRect = {
            top: boundingClientRect.top,
            bottom: boundingClientRect.bottom
          };
          return bodyInfo;
        }
        var bodyInfo = {
          x: window.pageXOffset,
          y: window.pageYOffset
        };
        var uptodateClient = null;
        var abstractElement = null;
        if (_this.state.current_location.display_type === 'inline' && (uptodateClient = selection_1.get('#uptodate-client'))) {
          bodyInfo = addAdditionalBodyInfo(bodyInfo, uptodateClient);
        } else if (abstractElement = getAbstractElement()) {
          bodyInfo = addAdditionalBodyInfo(bodyInfo, abstractElement);
        }
        _this.sender.send('scroll_info', bodyInfo);
      }, 250);
    };
    HostScrollListener.prototype.stop = function () {
      window.clearInterval(this.handler);
    };
    return HostScrollListener;
  }();
  exports.HostScrollListener = HostScrollListener;
  var JobHostScrollListener = function () {
    function JobHostScrollListener(sender, receiver, state) {
      var _this = this;
      this.sender = sender;
      this.receiver = receiver;
      this.state = state;
      this.receiver['jobs_scroll_info_start'] = function () {
        return _this.start();
      };
      this.receiver['jobs_scroll_info_stop'] = function () {
        return _this.stop();
      };
      this.receiver['jobs_scroll_bars_request'] = function () {
        return _this.scroll_bars_request();
      };
    }
    JobHostScrollListener.prototype.scroll_bars_request = function () {
      this.sender.send('jobs_scroll_bars_response', {
        vertical: html_1.hasVerticalScrollBar(),
        horizontal: html_1.hasHorizontalScrollBar()
      });
    };
    JobHostScrollListener.prototype.start = function () {
      var _this = this;
      this.handler = window.setInterval(function () {
        var jobClient = selection_1.get('#job-client');
        if (jobClient) {
          var boundingClientRect = jobClient.getBoundingClientRect();
          var bodyInfo = {
            x: window.pageXOffset,
            y: window.pageYOffset,
            windowHeight: window.innerHeight,
            targetClientRect: {
              top: boundingClientRect.top,
              bottom: boundingClientRect.bottom
            }
          };
          _this.sender.send('jobs_scroll_info', bodyInfo);
        }
      }, 250);
    };
    JobHostScrollListener.prototype.stop = function () {
      window.clearInterval(this.handler);
    };
    return JobHostScrollListener;
  }();
  exports.JobHostScrollListener = JobHostScrollListener;
  return exports;
}(shared_scroll, shared_html, shared_selection);
shared_functions = function (exports, errors_1) {
  function delay(amount, fun) {
    return setTimeout(errors_1.UnhandledError.capture(fun), amount);
  }
  exports.delay = delay;
  function idle(timeout, fun) {
    var id = -1;
    return function () {
      if (id != -1)
        clearTimeout(id);
      id = setTimeout(errors_1.UnhandledError.capture(fun), timeout);
    };
  }
  exports.idle = idle;
  return exports;
}(shared_functions, shared_errors);
//# sourceMappingURL=functions.js.map;
var __extends = this && this.__extends || function (d, b) {
  for (var p in b)
    if (b.hasOwnProperty(p))
      d[p] = b[p];
  function __() {
    this.constructor = d;
  }
  d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
pre_rec_email_journey_pre_rec_email = function (exports, component_1, html_1, selection_1, errors_1, http_1, forms_1) {
  var PreRecEmail = function (_super) {
    __extends(PreRecEmail, _super);
    function PreRecEmail(parent, state) {
      _super.call(this, '.pre-rec-email', parent);
      this.state = state;
      this.elementName = 'pre-rec-email-journey';
      this.attachToForm();
    }
    PreRecEmail.prototype.attachToForm = function () {
      var _this = this;
      var form = selection_1.get('.card-subscribe', this.root);
      html_1.on(form, 'submit', function () {
        form.action = _this.state.config.host + 'subscribe';
        var state = selection_1.get('input[name=state]', form);
        state.value = JSON.stringify(_this.state);
        _this.subscribing();
        errors_1.Debug.log('attempting to subscribe');
        http_1.http(forms_1.request(form), function (response) {
          if (response.status >= 299) {
            errors_1.Debug.log('failed to subscribe');
            _this.error();
          } else {
            errors_1.Debug.log('succeeded in subscribing');
            _this.subscribed();
          }
        });
        return false;
      });
    };
    PreRecEmail.prototype.signup = function () {
      this.state.popup_info.position = 'email-pre-rec';
      this.set(this.elementName, 'email-signup');
    };
    PreRecEmail.prototype.subscribe = function () {
      this.state.popup_info.position = 'email-pre-rec-subscribe';
      this.set(this.elementName, 'subscribe');
      this.set('subscribe-state', 'initial');
    };
    PreRecEmail.prototype.subscribing = function () {
      this.state.popup_info.position = 'email-pre-rec-subscribing';
      this.set('subscribe-state', 'subscribing');
    };
    PreRecEmail.prototype.error = function () {
      this.state.popup_info.position = 'email-pre-rec-error';
      this.set('subscribe-state', 'error');
    };
    PreRecEmail.prototype.subscribed = function () {
      this.state.popup_info.position = 'email-pre-rec-subscribed';
      this.set(this.elementName, 'subscribed');
    };
    return PreRecEmail;
  }(component_1.Component);
  exports.PreRecEmail = PreRecEmail;
  return exports;
}(pre_rec_email_journey_pre_rec_email, shared_component, shared_html, shared_selection, shared_errors, shared_http, shared_forms);
//# sourceMappingURL=pre-rec-email.js.map;
var __extends = this && this.__extends || function (d, b) {
  for (var p in b)
    if (b.hasOwnProperty(p))
      d[p] = b[p];
  function __() {
    this.constructor = d;
  }
  d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
pre_rec_plugin_journey_pre_rec_plugin = function (exports, component_1) {
  var PreRecPlugin = function (_super) {
    __extends(PreRecPlugin, _super);
    function PreRecPlugin(parent, state) {
      _super.call(this, '.pre-rec-plugin', parent);
      this.state = state;
      this.elementName = 'pre-rec-plugin-journey';
    }
    PreRecPlugin.prototype.show = function () {
      this.state.popup_info.position = 'plugin-pre-rec';
      this.set(this.elementName, 'plugin');
    };
    return PreRecPlugin;
  }(component_1.Component);
  exports.PreRecPlugin = PreRecPlugin;
  return exports;
}(pre_rec_plugin_journey_pre_rec_plugin, shared_component);
shared_cookies = function (exports) {
  /*
   Original from https://github.com/madmurphy/cookies.js
  
   Converted to vanilla typescript
   */
  var Cookies = function () {
    function Cookies() {
    }
    Cookies.getItem = function (key) {
      if (!key) {
        return null;
      }
      return decodeURIComponent(document.cookie.replace(new RegExp('(?:(?:^|.*;)\\s*' + encodeURIComponent(key).replace(/[\-.+*]/g, '\\$&') + '\\s*\\=\\s*([^;]*).*$)|^.*$'), '$1')) || null;
    };
    Cookies.setItem = function (key, value, end, path, domain, secure) {
      if (!key || /^(?:expires|max-age|path|domain|secure)$/i.test(key)) {
        return false;
      }
      var sExpires = '';
      if (end) {
        switch (end.constructor) {
        case Number:
          sExpires = end === Infinity ? '; expires=Fri, 31 Dec 9999 23:59:59 GMT' : '; max-age=' + end;
          break;
        case String:
          sExpires = '; expires=' + end;
          break;
        case Date:
          sExpires = '; expires=' + end.toUTCString();
          break;
        }
      }
      document.cookie = encodeURIComponent(key) + '=' + encodeURIComponent(value) + sExpires + (domain ? '; domain=' + domain : '') + (path ? '; path=' + path : '') + (secure ? '; secure' : '');
      return true;
    };
    Cookies.removeItem = function (key, path, domain) {
      if (!this.hasItem(key)) {
        return false;
      }
      var encoded = encodeURIComponent(key) + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT' + (domain ? '; domain=' + domain : '') + (path ? '; path=' + path : '');
      document.cookie = encoded;
      return true;
    };
    Cookies.hasItem = function (key) {
      if (!key) {
        return false;
      }
      return new RegExp('(?:^|;\\s*)' + encodeURIComponent(key).replace(/[\-.+*]/g, '\\$&') + '\\s*\\=').test(document.cookie);
    };
    Cookies.keys = function () {
      var aKeys = document.cookie.replace(/((?:^|\s*;)[^=]+)(?=;|$)|^\s*|\s*(?:=[^;]*)?(?:\1|$)/g, '').split(/\s*(?:=[^;]*)?;\s*/);
      for (var nLen = aKeys.length, nIdx = 0; nIdx < nLen; nIdx++) {
        aKeys[nIdx] = decodeURIComponent(aKeys[nIdx]);
      }
      return aKeys;
    };
    return Cookies;
  }();
  exports.Cookies = Cookies;
  return exports;
}(shared_cookies);
//# sourceMappingURL=cookies.js.map;
var __extends = this && this.__extends || function (d, b) {
  for (var p in b)
    if (b.hasOwnProperty(p))
      d[p] = b[p];
  function __() {
    this.constructor = d;
  }
  d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
popup_popup = function (exports, recommendation_journey_1, minimised_1, email_1, scroll_1, functions_1, selection_1, component_1, errors_1, pre_rec_email_1, pre_rec_plugin_1, cookies_1) {
  var Popup = function (_super) {
    __extends(Popup, _super);
    function Popup(parent, state, config, scroll) {
      if (scroll === void 0) {
        scroll = new scroll_1.WindowScrollCondition(state.config);
      }
      _super.call(this, '.popup', parent);
      this.state = state;
      this.config = config;
      this.scroll = scroll;
      this.numberOfRecommendations = 0;
      this.checks = {
        email: {
          check: function () {
            return !this.state.config.user_registered && !this.state.config['email-journey-closed'];
          },
          display: this.displayEmailPreRecJourney
        },
        plugin: {
          check: function () {
            return !this.state.current_location.browser_extension_loaded && !this.state.config['plugin-journey-closed'];
          },
          display: this.displayPluginPreRecJourney
        },
        recommendations: {
          check: function () {
            return true;
          },
          display: this.openRecommendationJourney
        }
      };
      this.minimised = new minimised_1.Minimised(this.root);
      this.recommendationJourney = new recommendation_journey_1.RecommendationJourney(this.root, state);
      this.emailJourney = new email_1.EmailJourney(this.root, state);
      this.preRecEmail = new pre_rec_email_1.PreRecEmail(this.root, state);
      this.preRecPlugin = new pre_rec_plugin_1.PreRecPlugin(this.root, state);
    }
    Popup.prototype.render = function (recommendations) {
      this.numberOfRecommendations = recommendations.length;
      this.recommendationJourney.render(recommendations);
      this.insertOnwardJourney();
      this.handleClose();
      this.handleEmailThis();
    };
    Popup.prototype.insertOnwardJourney = function () {
      var _this = this;
      selection_1.select('.recommendations .next', this.root).on('click', function (e) {
        var label = e;
        var recommendationPosition = Number(label.getAttribute('data-recommendation-position'));
        var onwardPosition = Math.min(_this.numberOfRecommendations, _this.state.config.onward_journey_position);
        if (onwardPosition == recommendationPosition && !_this.state.config.user_registered) {
          selection_1.get('.onward', _this.root).className = selection_1.get('.onward', _this.root).className.replace('disable-animate', '');
          _this.displayEmailJourney();
          return false;
        }
        return true;
      });
      if (!this.state.config.user_registered) {
        this.incrementTotal();
      }
    };
    Popup.prototype.incrementTotal = function () {
      selection_1.select('.total-recommendations', this.root).map(function (span) {
        return span.textContent = String(Number(span.textContent) + 1);
      });
    };
    Popup.prototype.display = function () {
      var _this = this;
      if (this.scroll.required()) {
        return this.scroll.await(function () {
          return _this.display();
        });
      }
      if (this.numberOfRecommendations == 0)
        return;
      if (this.state.config.minimised || cookies_1.Cookies.getItem('uptodate-minimised') == 'true') {
        this.fireResize({
          width: '100px',
          height: '100px'
        });
        this.minimise();
        this.minimised.notification();
      } else {
        this.open();
      }
    };
    Popup.prototype.handlerJourneys = function () {
      if (this.hasState('journey', 'pre-rec')) {
        if (this.hasState('pre-rec', 'email-journey'))
          this.config.persist('email-journey-closed', 'true');
        if (this.hasState('pre-rec', 'plugin-journey'))
          this.config.persist('plugin-journey-closed', 'true');
      }
    };
    Popup.prototype.handleClose = function () {
      var _this = this;
      selection_1.select('.cancel, .no-thanks, .done', this.root).on('click', function () {
        _this.handlerJourneys();
        _this.openRecommendationJourney();
        functions_1.delay(1000, function () {
          _this.emailJourney.reset(false, false);
        });
        // TEMP FIX
        return false;
      });
      selection_1.select('.maximise', this.root).on('click', function () {
        _this.config.data.minimised = false;
        _this.config.persist('minimised', 'false');
        cookies_1.Cookies.setItem('uptodate-minimised', 'false');
        _this.minimised.initial();
        _this.open();
        return false;
      });
      selection_1.select('.close[for=uptodate-popup-minimised]', this.root).on('click', function () {
        if (_this.hasState('journey', 'recommendation') && _this.hasState('recommendation-position', '1')) {
          _this.config.data.minimised = true;
          _this.config.persist('minimised', 'true');
          cookies_1.Cookies.setItem('uptodate-minimised', 'true');
        }
        _this.handlerJourneys();
        if (_this.hasState('journey', 'pre-rec')) {
          _this.openRecommendationJourney();
          return false;
        } else {
          _this.minimise();
          return true;
        }
      });
      selection_1.select('.minimised, .journeys', this.root).on([
        'transitionend',
        'webkitTransitionEnd'
      ], function (element, event) {
        if (event.propertyName == 'visibility') {
          errors_1.Debug.log(event);
          var popupState = selection_1.get('input[name=popup]:checked', _this.root);
          errors_1.Debug.log(popupState.value);
          switch (popupState.value) {
          case 'minimised':
            var minimisedState = selection_1.get('input[name=minimised-state]:checked', _this.root);
            if (minimisedState.value != 'notification') {
              _this.fireResize({
                width: '80px',
                height: '80px'
              });
            }
            break;
          case 'closed':
            _this.fireResize({
              width: '0',
              height: '0'
            });
            break;
          }
        }
      });
      selection_1.select('.minimised', this.root).on([
        'animationend',
        'webkitAnimationEnd'
      ], function (element, event) {
        if (event.animationName == 'uptodate-sonar') {
          errors_1.Debug.log(event);
          _this.fireResize({
            width: '80px',
            height: '80px'
          });
        }
      });
    };
    Popup.prototype.open = function () {
      var _this = this;
      var journeys = this.state.config['journey_order']['value'] || ['recommendations'];
      var journey = journeys.filter(function (j) {
        return _this.checks[j].check.call(_this);
      })[0];
      this.checks[journey].display.call(this);
      this.set('popup', 'open');
    };
    Popup.prototype.openRecommendationJourney = function () {
      if (!this.hasState('journey', 'recommendation')) {
        this.displayRecommendationsJourney();
        this.recommendationJourney.position(1);
      } else {
        this.recommendationJourney.display();
      }
      this.fireResize(selection_1.get('.recommendation-journey', this.root));
    };
    Popup.prototype.showEmailPreRec = function () {
      return this.state.config['experiment_email_position'] && !this.state.config.user_registered && !this.state.config['closed-pre-rec-email'];
    };
    Popup.prototype.close = function () {
      this.set('popup', 'close');
    };
    Popup.prototype.minimise = function () {
      this.set('popup', 'minimised');
    };
    Popup.prototype.displayRecommendationsJourney = function () {
      this.set('journey', 'recommendation');
    };
    Popup.prototype.displayEmailJourney = function () {
      this.set('onward', 'email-journey');
      this.emailJourney.signup();
      this.fireResize(selection_1.get('.onward', this.root));
      this.set('journey', 'onward');
    };
    Popup.prototype.displayEmailPreRecJourney = function () {
      this.preRecEmail.signup();
      this.set('pre-rec', 'email-journey');
      this.fireResize(selection_1.get('.pre-rec', this.root));
      this.set('journey', 'pre-rec');
    };
    Popup.prototype.displayPluginPreRecJourney = function () {
      this.preRecPlugin.show();
      this.set('pre-rec', 'plugin-journey');
      this.fireResize(selection_1.get('.pre-rec', this.root));
      this.set('journey', 'pre-rec');
    };
    Popup.prototype.displaySafariJourney = function () {
      this.fireResize(selection_1.get('.safari', this.root));
      this.set('journey', 'safari');
    };
    Popup.prototype.handleEmailThis = function () {
      var _this = this;
      selection_1.select('.email-this-input', this.root).on('change', function () {
        var recommendationJourney = selection_1.get('.recommendation-journey', _this.root);
        _this.fireResize(recommendationJourney);
        functions_1.delay(500, function () {
          _this.recommendationJourney.emailThis.reset(false, false);
        });
        return true;
      });
      selection_1.select('.email-this-signup', this.root).on('click', function () {
        var sendEmail = selection_1.get('#uptodate-send-email', _this.root);
        var subscribeEmail = selection_1.get('#uptodate-subscribe-email', _this.root);
        subscribeEmail.value = sendEmail.value;
        _this.set('onward', 'email-journey');
        _this.emailJourney.signup();
        functions_1.delay(1000, function () {
          _this.recommendationJourney.emailThis.reset(false, false);
          selection_1.get('#uptodate-email-this', _this.root)['checked'] = false;
        });
        _this.fireResize(selection_1.get('.onward', _this.root));
        _this.set('journey', 'onward');
        return true;
      });
    };
    return Popup;
  }(component_1.Component);
  exports.Popup = Popup;
  return exports;
}(popup_popup, recommendation_journey_recommendation_journey, minimised_minimised, email_journey_email, shared_scroll, shared_functions, shared_selection, shared_component, shared_errors, pre_rec_email_journey_pre_rec_email, pre_rec_plugin_journey_pre_rec_plugin, shared_cookies);
//# sourceMappingURL=popup.js.map;
var __extends = this && this.__extends || function (d, b) {
  for (var p in b)
    if (b.hasOwnProperty(p))
      d[p] = b[p];
  function __() {
    this.constructor = d;
  }
  d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
inline_inline = function (exports, recommendation_1, selection_1, component_1, text_1, templates_1, events_1) {
  var Inline = function (_super) {
    __extends(Inline, _super);
    function Inline(parent, state, scroll) {
      _super.call(this, '.inline', parent);
      this.state = state;
      this.scroll = scroll;
      this.events = new events_1.Events(state);
    }
    Inline.prototype.render = function (recommendations) {
      this.recommendations = recommendations;
      var parent = selection_1.get('.recommendations', this.root);
      var template = selection_1.get('template', parent);
      recommendations.forEach(function (recommendation) {
        var instance = templates_1.Templates.clone(template);
        new recommendation_1.RecommendationRenderer(instance).render(recommendation);
        var title = selection_1.get('.title', instance);
        var st = new text_1.StructuredText();
        st.process(title);
        parent.appendChild(instance);
      });
    };
    Inline.prototype.display = function () {
      if (this.recommendations.length == 0) {
        this.fireInlineEvent('uptodate-no-content');
        this.events.fire('inline', 'displays', 'no-recommendation');
        return;
      }
      this.fireInlineEvent('uptodate-display');
      this.open();
      this.displayEvent();
    };
    Inline.prototype.displayEvent = function () {
      var _this = this;
      if (this.scroll.required()) {
        return this.scroll.await(function () {
          return _this.displayEvent();
        });
      }
      var eventData = {
        'recommendation-dois': this.recommendations.map(function (r) {
          return r.doi;
        }),
        'total-recommendations': this.recommendations.length,
        'randomised-recommendation': false
      };
      this.events.fire('inline', 'displays', 'recommendation', eventData);
    };
    Inline.prototype.open = function () {
      this.fireResize({
        width: '100%',
        height: this.root.offsetHeight + 'px'
      });
    };
    return Inline;
  }(component_1.Component);
  exports.Inline = Inline;
  return exports;
}(inline_inline, recommendation_recommendation, shared_selection, shared_component, text_text, shared_templates, shared_events);
config_config = function (exports, storage_1, strings_1, selection_1, templates_1, messaging_1, http_1, errors_1, collections_1) {
  var Config = function () {
    function Config(state, parent) {
      var _this = this;
      this.parent = parent;
      this.storage = window.localStorage;
      this.parent['config'] = this;
      storage_1.copyIntoStorage(http_1.queryObject(state.current_location.url), this.storage, Config.prefix);
      this.data = this.migrate(collections_1.mergeObjects(state.config, Config.extractConfig(storage_1.storageObject(this.storage))));
      this.render();
      selection_1.select('#' + this.id('debug')).on('change', function (element) {
        _this.debug(element.checked);
      });
      this.persist('debug', null);
      this.debug(errors_1.Debug.isDebug(state.current_location.url));
    }
    Config.extractConfig = function (obj) {
      var _this = this;
      return Object.keys(obj).reduce(function (a, key) {
        if (strings_1.startsWith(_this.prefix, key)) {
          var noConfig = key.substr(Config.prefix.length);
          a[noConfig] = obj[key];
        }
        return a;
      }, {});
    };
    Config.prototype.json = function () {
      return JSON.stringify(this.data);
    };
    Config.prototype.render = function () {
      var _this = this;
      Object.keys(this.data).forEach(function (name) {
        _this.createProperty(name, _this.data[name]);
      });
    };
    Config.prototype.createProperty = function (name, value) {
      var id = this.id(name);
      var type = typeof value;
      var input = selection_1.get('#' + id, this.parent);
      if (input) {
        type == 'boolean' ? input.checked = value : input.value = JSON.stringify(value);
      } else {
        var template = selection_1.get('template.config', this.parent);
        var instance = templates_1.Templates.clone(template);
        input = selection_1.get('input', instance);
        if (type == 'boolean') {
          input.setAttribute('type', 'checkbox');
        } else if (type == 'number') {
          input.setAttribute('type', 'number');
        } else {
          input.setAttribute('type', 'text');
        }
        input.setAttribute('id', id);
        input.classList.add(name.replace(/_/g, '-'));
        if (type == 'boolean') {
          value ? input.setAttribute('checked', '') : input.removeAttribute('checked');
        } else {
          input.setAttribute('value', JSON.stringify(value));
        }
        var label = selection_1.get('label', instance);
        label.setAttribute('for', id);
        var text = selection_1.get('.text', label);
        text.textContent = name.replace(/_/g, ' ');
        this.parent.insertBefore(instance, template.nextSibling);
      }
      Object.defineProperty(this.data, name, {
        enumerable: true,
        get: function () {
          return type == 'boolean' ? input.checked : strings_1.coerce(input.value);
        },
        set: function (newValue) {
          return type == 'boolean' ? input.checked = newValue : input.value = JSON.stringify(newValue);
        }
      });
    };
    Config.prototype.id = function (name) {
      return Config.prefix + name.replace(/_/g, '-');
    };
    Config.prototype.debug = function (value) {
      errors_1.Debug.enable(value);
      this.full_screen(value);
      if (value) {
        this.parent.classList.add('debug');
      } else {
        this.parent.classList.remove('debug');
      }
    };
    Config.prototype.full_screen = function (value) {
      messaging_1.MessageDispatcher.dispatch(this.parent, {
        name: 'full_screen',
        body: value
      });
    };
    Config.prototype.persist = function (name, value) {
      var key = Config.prefix + name;
      if (value == null) {
        this.storage.removeItem(key);
      } else {
        this.storage.setItem(key, value);
      }
    };
    Config.prototype.isPersisted = function (name) {
      var key = Config.prefix + name;
      return this.storage.getItem(key) !== null;
    };
    Config.prototype.migrate = function (minimalConfig) {
      this.migrateProperty(minimalConfig, 'closed-pre-rec-email', 'email-journey-closed');
      return minimalConfig;
    };
    Config.prototype.migrateProperty = function (minimalConfig, oldKey, newKey) {
      var value = minimalConfig[oldKey];
      if (typeof value != 'undefined') {
        minimalConfig[newKey] = value;
        if (this.isPersisted(oldKey)) {
          this.persist(oldKey, null);
          this.persist(newKey, value);
        }
      }
    };
    Config.prefix = 'uptodate-';
    return Config;
  }();
  exports.Config = Config;
  return exports;
}(config_config, shared_storage, shared_strings, shared_selection, shared_templates, shared_messaging, shared_http, shared_errors, shared_collections);
application_application = function (exports, http_1, requests_1, popup_1, inline_1, config_1, scroll_1, state_1, events_1, selection_1, templates_1, errors_1, cookies_1, strings_1) {
  var Application = function () {
    function Application(state, recommendations, events, scroll) {
      var _this = this;
      if (recommendations === void 0) {
        recommendations = null;
      }
      if (events === void 0) {
        events = new events_1.Events(state);
      }
      if (scroll === void 0) {
        scroll = new scroll_1.WindowScrollCondition(state.config);
      }
      this.state = state;
      this.recommendations = recommendations;
      this.events = events;
      this.scroll = scroll;
      try {
        this.setup();
      } catch (e) {
        this.handle(e);
      }
      errors_1.UnhandledError.unhandled = function (e) {
        return _this.handle(e);
      };
    }
    Application.prototype.handle = function (e) {
      if (this.state.config.debug)
        throw e;
      this.events.fire('client', 'throws', 'error', {
        name: e.name,
        message: e.message,
        stack: e.stack ? e.stack : ''
      });
    };
    Application.prototype.setup = function () {
      var _this = this;
      this.cleanupCookie();
      var uptodateElement = selection_1.get('#uptodate', document);
      if (!uptodateElement)
        return this.loadAssets(function () {
          return _this.setup();
        });
      var applicationElement = selection_1.get('.application', uptodateElement);
      applicationElement['application'] = this;
      this.config = new config_1.Config(this.state, applicationElement);
      this.state.config = this.config.data;
      // TEMP FIX
      if (this.state.config['inline_version'] && this.state.current_location.display_type == 'inline') {
        this.displayComponent = new inline_1.Inline(applicationElement, this.state, this.scroll);
      } else {
        this.state.current_location.display_type = 'popup';
        this.state.config['inline_version'] = false;
        this.displayComponent = new popup_1.Popup(applicationElement, this.state, this.config, this.scroll);
      }
      new state_1.StateChange(applicationElement, this.events);
      this.display();
    };
    Application.prototype.cleanupCookie = function () {
      var host = window.location.hostname;
      errors_1.Debug.log('COOKIE host: ' + host);
      if (host == 'recommendations.springernature.com') {
        errors_1.Debug.log('COOKIE deleting cookie: ' + host);
        cookies_1.Cookies.removeItem('nature_impact_pd', '/', 'recommendations.springernature.com');
      }
      var domain = 'springernature.com';
      if (strings_1.endsWith(domain, host)) {
        errors_1.Debug.log('COOKIE setting new cookie for domain: ' + domain);
        cookies_1.Cookies.setItem('nature_impact_pd', this.state.config.user_id, Infinity, '/', domain);
      }
    };
    Application.prototype.loadAssets = function (done) {
      http_1.http(requests_1.Requests.get(this.state.config.host + Application.assets), function (response) {
        if (response.status != 200)
          return;
        var template = response.entity.html();
        var uptodateElement = selection_1.get('#uptodate', template);
        templates_1.Templates.polyfillTemplates(uptodateElement);
        document.body.appendChild(uptodateElement);
        done();
      });
    };
    Application.prototype.display = function () {
      var _this = this;
      if (this.recommendations == null)
        return this.loadRecommendations(function () {
          return _this.display();
        });
      this.displayComponent.render(this.recommendations);
      this.displayComponent.display();
    };
    Application.prototype.loadRecommendations = function (done) {
      var _this = this;
      if (this.state.config['inline_version']) {
        switch (this.state.current_location.hostsite) {
        case 'recommended':
          this.state.config.number_of_recommendations = 2;
          break;
        case 'springer':
          this.state.config.number_of_recommendations = 3;
          break;
        case 'nature':
          if (this.state.config['experiment_srep_homepage'] === true) {
            this.state.config.number_of_recommendations = 1000;
            this.state.config.minimum_confidence = 10;
          }
          break;
        }
      }
      if (this.state.config.user_registered && this.state.current_location.display_type === 'popup') {
        this.state.config.number_of_recommendations = 10;
      }
      http_1.http(requests_1.Requests.recommendations(this.state), function (response) {
        if (response.status != 200)
          return;
        _this.recommendations = response.entity.json();
        if (_this.state.config['experiment_srep_homepage'] === true) {
          _this.recommendations = _this.recommendations.filter(function (rec) {
            return rec.issn === '2045-2322';
          }).slice(0, 6);
        }
        if (_this.recommendations.length < 3) {
          _this.recommendations = [];
        }
        done();
      });
    };
    Application.assets = 'application/application.html';
    return Application;
  }();
  exports.Application = Application;
  return exports;
}(application_application, shared_http, shared_requests, popup_popup, inline_inline, config_config, shared_scroll, shared_state, shared_events, shared_selection, shared_templates, shared_errors, shared_cookies, shared_strings);
//# sourceMappingURL=application.js.map;
var __extends = this && this.__extends || function (d, b) {
  for (var p in b)
    if (b.hasOwnProperty(p))
      d[p] = b[p];
  function __() {
    this.constructor = d;
  }
  d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
iframe_client = function (exports, application_1, http_1, scroll_1, errors_1, messaging_1, selection_1, events_1) {
  var Client = function (_super) {
    __extends(Client, _super);
    function Client() {
      var _this = this;
      var baseUrl = http_1.BaseUrl.baseUrl('client.js');
      var sourceOrigin = http_1.BaseUrl.origin(http_1.queryObject()['source']);
      errors_1.Debug.log('ARTICLE Client expecting to send and receive messages from ' + sourceOrigin);
      _super.call(this, window, sourceOrigin);
      this.sender = new messaging_1.MessageSender([window.parent], sourceOrigin);
      this.baseUrl = baseUrl;
      this.sender.send('state_request');
      this.sender.send('inline_css_request');
      selection_1.select(document.body).on('client_message', function (element, e) {
        var message = e.detail;
        _this.sender.send(message.name, message.body);
      }, true);
    }
    Client.prototype.state_response = function (state) {
      new application_1.Application(state, null, new events_1.Events(state), new scroll_1.ClientScrollListener(this.sender, this, state));
    };
    Client.prototype.inline_css_response = function (href) {
      var linkElement = document.createElement('link');
      linkElement.rel = 'stylesheet';
      linkElement.href = href;
      window.document.head.appendChild(linkElement);
      window.addEventListener('resize', function (event) {
        errors_1.Debug.log('resize event from iframe');
        var application = selection_1.get('.application', document);
        messaging_1.MessageDispatcher.fireResize(application, {
          height: application.offsetHeight + 'px',
          width: '100%'
        });
        return true;
      });
    };
    return Client;
  }(messaging_1.MessageReceiver);
  try {
    new Client();
  } catch (e) {
    errors_1.UnhandledError.unhandled(e);
  }
  return exports;
}(iframe_client, application_application, shared_http, shared_scroll, shared_errors, shared_messaging, shared_selection, shared_events);
//# sourceMappingURL=client.js.map
