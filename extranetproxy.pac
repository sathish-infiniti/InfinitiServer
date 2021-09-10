function FindProxyForURL(url, host)
{
// variable strings to return
var proxy_yes = "PROXY extranetproxy.int.abnamro.com:8080";
var proxy_no = "DIRECT";
if (shExpMatch(url, "https://3rdpartyaccess-pw.int.abnamro.com*")) { return proxy_yes; }
if (shExpMatch(url, "https://3rdpartyaccess-sc.int.abnamro.com*")) { return proxy_yes; }
if (shExpMatch(url, "https://3rdpartyaccess-rsa.int.abnamro.com*")) { return proxy_yes; }
if (shExpMatch(url, "https://3rdpartyaccess-pw-qa.int.abnamro.com*")) { return proxy_yes; }
if (shExpMatch(url, "https://3rdpartyaccess-sc-qa.int.abnamro.com*")) { return proxy_yes; }
if (shExpMatch(url, "https://3rdpartyaccess-rsa-qa.int.abnamro.com*")) { return proxy_yes; }
return "DIRECT";
}
