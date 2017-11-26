import folium as fl
import pandas as pd
import urllib
url = "http://whois.kisa.or.kr/openapi/whois.jsp?query=202.30.50.51&key=2017112121575473818443&answer=json"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if (rescode == 200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
