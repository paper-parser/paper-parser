var shared_numbers = {}, shared_errors = {}, shared_collections = {}, shared_html = {}, shared_selection = {}, shared_strings = {}, shared_http = {}, shared_storage = {}, shared_location = {}, shared_state = {}, shared_requests = {}, shared_events = {}, shared_features = {}, shared_templates = {}, shared_messaging = {}, config_config = {}, shared_scroll = {}, iframe_host = {}, entry_point_launcher = {}, entry_point_entry_point = {};
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
//# sourceMappingURL=errors.js.map;
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
shared_features = function (exports, storage_1) {
  var Features = function () {
    function Features(events) {
      this.events = events;
    }
    Features.prototype.check = function (done) {
      if (!this.has('web-storage', function () {
          return storage_1.hasStorage();
        }))
        return;
      if (!this.has('web-messaging', function () {
          return window.postMessage;
        }))
        return;
      if (!this.has('selector-api', function () {
          return document.querySelectorAll;
        }))
        return;
      if (!this.has('Object.keys', function () {
          return Object.keys;
        }))
        return;
      if (!this.has('Array.prototype.map', function () {
          return Array.prototype.map;
        }))
        return;
      if (!this.has('Array.prototype.filter', function () {
          return Array.prototype.filter;
        }))
        return;
      done();
    };
    Features.prototype.has = function (name, test) {
      try {
        if (test())
          return true;
      } catch (e) {
      }
      this.missing(name);
      return false;
    };
    Features.prototype.missing = function (feature) {
      this.events.fire('client', 'missing', 'feature', { feature: feature });
    };
    return Features;
  }();
  exports.Features = Features;
  return exports;
}(shared_features, shared_storage);
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
//# sourceMappingURL=scroll.js.map;
var __extends = this && this.__extends || function (d, b) {
  for (var p in b)
    if (b.hasOwnProperty(p))
      d[p] = b[p];
  function __() {
    this.constructor = d;
  }
  d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
iframe_host = function (exports, scroll_1, messaging_1, http_1, errors_1, selection_1, location_1) {
  var Host = function (_super) {
    __extends(Host, _super);
    function Host(baseUrl, articleClientPath, jobClientPath, state) {
      var sourceOrigin = http_1.BaseUrl.origin(baseUrl);
      _super.call(this, window, sourceOrigin);
      errors_1.Debug.log('Host expecting to send and receive messages from ' + sourceOrigin);
      this.state = state;
      this.style = {
        width: '0',
        height: '0'
      };
      this.articleIframe = this.createIframe('' + baseUrl + articleClientPath + '?source=' + http_1.BaseUrl.origin(window.location.href), 'uptodate-client');
      this.appendArticleIframe();
      var messageSenderWindows = [this.articleIframe.contentWindow];
      var jobIframeLocation = selection_1.get('span[data-recommended=\'jobs\']');
      if (state.config.jobs && jobIframeLocation) {
        this.jobIframe = this.createIframe('' + baseUrl + jobClientPath + '?source=' + http_1.BaseUrl.origin(window.location.href), 'job-client');
        this.appendJobIframe(jobIframeLocation);
        this.jobIframe.style.marginTop = '28px';
        messageSenderWindows.push(this.jobIframe.contentWindow);
      }
      this.sender = new messaging_1.MessageSender(messageSenderWindows, sourceOrigin);
      new scroll_1.HostScrollListener(this.sender, this, this.state);
      new scroll_1.JobHostScrollListener(this.sender, this, this.state);
    }
    Host.prototype.state_request = function () {
      this.sender.send('state_response', this.state);
    };
    Host.prototype.job_state_request = function () {
      this.sender.send('job_state_response', this.state);
    };
    Host.prototype.inline_css_request = function () {
      if (this.linkToCss) {
        this.sender.send('inline_css_response', this.linkToCss.toString());
      }
    };
    Host.prototype.resize = function (style) {
      if (this.fullScreen) {
        this.style = style;
      } else {
        this.articleIframe.style.width = style.width;
        this.articleIframe.style.height = style.height;
      }
    };
    Host.prototype.jobResize = function (style) {
      this.jobIframe.style.width = style.width;
      this.jobIframe.style.height = style.height;
    };
    Host.prototype.inlineEvent = function (className) {
      if (this.state.config['inline_version']) {
        if (className == 'uptodate-no-content') {
          this.articleIframe.style.display = 'none';
        } else if (className == 'uptodate-display') {
          var recommendationsContainer = selection_1.get('.uptodate-recommendations-off', document);
          if (recommendationsContainer) {
            recommendationsContainer.classList.remove('uptodate-recommendations-off');
            recommendationsContainer.classList.add('uptodate-recommendations-on');
          }
        }
      }
    };
    Host.prototype.full_screen = function (value) {
      if (value && !this.state.config['inline_version']) {
        this.articleIframe.style.width = '100%';
        this.articleIframe.style.height = '100%';
      } else {
        this.articleIframe.style.width = this.style.width;
        this.articleIframe.style.height = this.style.height;
      }
      this.fullScreen = value && !(this.state.current_location.display_type === 'inline');
    };
    Host.prototype.createIframe = function (url, uid) {
      var iframe = document.createElement('iframe');
      iframe.style.width = '0';
      iframe.style.height = '0';
      iframe.style.bottom = '0';
      iframe.style.right = '0';
      iframe.style.zIndex = '100000';
      iframe.frameBorder = '0';
      iframe.scrolling = 'no';
      iframe.src = url;
      iframe.name = uid;
      iframe.id = uid;
      iframe.title = 'Personalised recommendations';
      iframe.setAttribute('allowtransparency', 'true');
      return iframe;
    };
    Host.prototype.appendArticleIframe = function () {
      var inlineElement = this.getInlineElement();
      if (inlineElement && this.state.config['inline_version']) {
        var href = inlineElement.getAttribute('href') == null ? inlineElement.getAttribute('data-href') : inlineElement.getAttribute('href');
        this.linkToCss = http_1.uri(href);
        var padding = parseInt(window.getComputedStyle(inlineElement.parentElement)['padding-left'].replace('px', ''));
        var parentInnerWidth = inlineElement.parentElement.offsetWidth - padding * 2 + 'px';
        this.articleIframe.style.width = parentInnerWidth;
        this.style.width = parentInnerWidth;
        inlineElement.parentElement.replaceChild(this.articleIframe, inlineElement);
      } else {
        this.articleIframe.style.position = 'fixed';
        document.body.appendChild(this.articleIframe);
      }
    };
    Host.prototype.appendJobIframe = function (jobElementLocation) {
      if (jobElementLocation) {
        jobElementLocation.parentElement.replaceChild(this.jobIframe, jobElementLocation);
        this.jobIframe.style.padding = '0';
        this.jobIframe.style.width = '100%';
      }
    };
    Host.prototype.getInlineElement = function () {
      return selection_1.get(location_1.CurrentLocation.inlineSelector, document);
    };
    return Host;
  }(messaging_1.MessageReceiver);
  exports.Host = Host;
  return exports;
}(iframe_host, shared_scroll, shared_messaging, shared_http, shared_errors, shared_selection, shared_location);
entry_point_launcher = function (exports, events_1, state_1, strings_1, errors_1, features_1, location_1, http_1, requests_1, config_1, collections_1, host_1, storage_1) {
  var Launcher = function () {
    function Launcher(state, done, events) {
      if (events === void 0) {
        events = new events_1.Events(state);
      }
      this.state = state;
      this.done = done;
      this.events = events;
      errors_1.Debug.enable(errors_1.Debug.isDebug(state.current_location.url));
      this.state.config = state.config;
      this.updateLocalStorage();
      this.trackCurrentPage();
      this.display();
    }
    Launcher.prototype.updateLocalStorage = function () {
      if (storage_1.hasStorage()) {
        var userId = this.state.config.user_id;
        errors_1.Debug.log('Storing user-id: ' + userId + ' in local storage');
        window.localStorage.setItem(storage_1.LOCALSTORAGE_KEY, userId);
      }
    };
    Launcher.prototype.trackCurrentPage = function () {
      if (location_1.CurrentLocation.trackTypes.indexOf(this.state.current_location.type) != -1) {
        this.events.fire('website', 'displays', this.state.current_location.type);
      }
    };
    Launcher.prototype.display = function () {
      var _this = this;
      if (strings_1.isEmpty(this.state.current_location.type)) {
        if (!(this.state.current_location.hostsite == 'nature' && this.state.current_location.display_type == 'inline')) {
          return;
        }
      }
      if (location_1.CurrentLocation.doNotDisplay.indexOf(this.state.current_location.type) != -1)
        return;
      if (strings_1.isEmpty(this.state.current_location.issn)) {
        if (!(this.state.current_location.type == 'homepage' && this.state.current_location.hostsite == 'recommended')) {
          return;
        }
      }
      if (this.state.current_location.type == 'journalHomepage' && this.state.config['experiment_srep_homepage'] != true) {
        return;
      }
      if (!this.state.config.show_recommendations) {
        return;
      }
      if (window.screen.availWidth < this.state.config.minimum_width && this.state.current_location.display_type != 'inline')
        return;
      this.state.config.minimised = this.autoMinimise();
      new features_1.Features(this.events).check(function () {
        try {
          _this.done(_this.state);
        } catch (e) {
          errors_1.Debug.log(e);
        }
      });
    };
    Launcher.prototype.autoMinimise = function () {
      return this.state.config['autominimise'] ? window.screen.availWidth < 1920 : this.state.config.minimised;
    };
    return Launcher;
  }();
  exports.Launcher = Launcher;
  function entryPoint(lambda, baseUrl) {
    try {
      var currentLocation_1 = new location_1.CurrentLocation();
      http_1.http(requests_1.Requests.config(baseUrl, currentLocation_1), function (response) {
        if (response.status != 200)
          return;
        var queryConfig = config_1.Config.extractConfig(http_1.queryObject(currentLocation_1.url));
        var config = collections_1.mergeObjects(response.entity.json(), queryConfig);
        currentLocation_1.checkForBrowserExtension(config['browser-extension-id'], function () {
          var s = state_1.state(config, currentLocation_1);
          if (s.config['experiment_srep_homepage'] == true && s.current_location.type != 'journalHomepage') {
            s.config['experiment_srep_homepage'] = false;
          }
          lambda(s, function (state) {
            return new Launcher(state, function (state) {
              new host_1.Host(config.host, 'generated/client.html', 'generated/job-client.html', state);
            });
          });
        });
      });
    } catch (e) {
      errors_1.UnhandledError.unhandled(e);
    }
  }
  exports.entryPoint = entryPoint;
  return exports;
}(entry_point_launcher, shared_events, shared_state, shared_strings, shared_errors, shared_features, shared_location, shared_http, shared_requests, config_config, shared_collections, iframe_host, shared_storage);
entry_point_entry_point = function (exports, launcher_1, http_1) {
  launcher_1.entryPoint(function (s, done) {
    done(s);
  }, http_1.BaseUrl.baseUrl('entry-point.js'));
  return exports;
}(entry_point_entry_point, entry_point_launcher, shared_http);
//# sourceMappingURL=entry-point.js.map
