if(typeof Ajax == "undefined"){
  var Ajax = {};
}

/*����XMLHttpRequest����*/
Ajax.createXMLHttpRequest = function(){
  var _xmlHttpRequest;
  if(window.ActiveXObject){
    try{
      _xmlHttpRequest = new ActiveXObject("Msxml3.XMLHTTP");
    }catch (e){
      try{
        _xmlHttpRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e){
        try {
          _xmlHttpRequest = new ActiveXObject("Microsoft.XMLHTTP");
        }catch(e){
        }
      }
    }
  }else if(window.XMLHttpRequest){
    _xmlHttpRequest = new XMLHttpRequest();
    if(_xmlHttpRequest.overrideMimeType)
      _xmlHttpRequest.overrideMimeType('text/xml');
  }
  return _xmlHttpRequest;
}

/*��������, url:�����ַ; callback:����������Ӧ�Ļص�����; content: �������; method:����ʽ(post,get����,Ĭ��Ϊpost)*/
Ajax.sendRequest = function(url, callback, content, method){
  var _xmlHttpRequest = this.createXMLHttpRequest();
  if(!_xmlHttpRequest){
    alert("��������汾��֧��XMLHttpRequest����,����ʹ��֧��XMLHttpRequest�����������鿴��ҳ!");
    return false;
  }

  _xmlHttpRequest.onreadystatechange = function(){
    if(_xmlHttpRequest.readyState == 4 && _xmlHttpRequest.status == 200){
      var _reXML = _xmlHttpRequest.responseXML;
      if(_reXML != null && _reXML.xml != null && _reXML.xml != "")
        callback(_reXML.xml);
      else
        callback(_xmlHttpRequest.responseText);
    }
  };

  if(method != "get")
    method = "post";
  if(method.toLowerCase() == "get"){
    _xmlHttpRequest.open("get", url, true);
  }else{
    _xmlHttpRequest.open("post", url, true);
    _xmlHttpRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  }
  _xmlHttpRequest.send(content);
}

/*��Ajax�ύForm��,form:����; callback:����������Ӧ�Ļص�����*/
Ajax.commitForm = function(form, callback){
  var url = form.action;
  var method = form.method;
  var content = "";
  for (var i=0;i<form.elements.length;i++){
    var e = form.elements[i];
    if(e.type=="checkbox" || e.type=="radio"){
      if(e.checked)
        content += e.name + "=" + e.value + "&";
    }else
      content += e.name + "=" + e.value + "&";
  }

  this.sendRequest(url, callback, content, method);
}
