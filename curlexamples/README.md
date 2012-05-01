
weather
-------
<https://docs.google.com/present/view?id=dfr68gz6_200dhctmwg4>

command:

    curl -H "Content-Type: text/xml; charset=utf-8" -H "SOAPAction:http://www.webserviceX.NET/GetWeather" -d@weather.xml http://www.webservicex.net/globalweather.asmx | xmltool.py

output:

    <?xml version="1.0" ?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <soap:Body>
        <GetWeatherResponse xmlns="http://www.webserviceX.NET">
          <GetWeatherResult>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-16&quot;?&gt;
    &lt;CurrentWeather&gt;
      &lt;Location&gt;Milano / Linate, Italy (LIML) 45-26N 009-17E 103M&lt;/Location&gt;
      &lt;Time&gt;Apr 30, 2012 - 07:50 PM EDT / 2012.04.30 2350 UTC&lt;/Time&gt;
      &lt;Wind&gt; from the ESE (110 degrees) at 6 MPH (5 KT):0&lt;/Wind&gt;
      &lt;Visibility&gt; 4 mile(s):0&lt;/Visibility&gt;
      &lt;SkyConditions&gt; mostly cloudy&lt;/SkyConditions&gt;
      &lt;Temperature&gt; 59 F (15 C)&lt;/Temperature&gt;
      &lt;DewPoint&gt; 57 F (14 C)&lt;/DewPoint&gt;
      &lt;RelativeHumidity&gt; 93%&lt;/RelativeHumidity&gt;
      &lt;Pressure&gt; 29.97 in. Hg (1015 hPa)&lt;/Pressure&gt;
      &lt;Status&gt;Success&lt;/Status&gt;
    &lt;/CurrentWeather&gt;</GetWeatherResult>
        </GetWeatherResponse>
      </soap:Body>
    </soap:Envelope>

version info 
------------
command:

    curl -H "Content-Type: text/xml; charset=utf-8" -d@version-info.xml http://services.chromedata.com:80/Description/7a | xmltool.py

output:

    <?xml version="1.0" ?>
    <S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
      <S:Body>
        <VersionInfo xmlns="urn:description7a.services.chrome.com">
          <responseStatus description="Successful" responseCode="Successful"/>
          <data build="43" country="US" date="2012-04-29T19:30:00-07:00"/>
          <data build="43" country="CA" date="2012-04-29T20:12:00-07:00"/>
        </VersionInfo>
      </S:Body>
    </S:Envelope>

vehicle description
-------------------

command:

    curl -H "Content-Type: text/xml; charset=utf-8" -d@vehicle-description.xml http://services.chromedata.com:80/Description/7a | xmltool.py

output:

    <?xml version="1.0" ?>
    <S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
      <S:Body>
        <VehicleDescription bestMakeName="Hyundai" bestModelName="Accent" bestStyleName="4dr Sdn GLS" bestTrimName="GLS" country="US" language="en" modelYear="2010" xmlns="urn:description7a.services.chrome.com">
          <responseStatus description="Successful" responseCode="Successful"/>
          <vinDescription bodyType="Sedan 4 Dr." division="Hyundai" modelName="Accent" modelYear="2010" styleName="4dr Sdn GLS" vin="KMHCN4AC7AU407141">
            <WorldManufacturerIdentifier>South Korea Hyundai - Passenger Cars (Mpv &amp; Rv) Buses &amp; Trucks (Including Vans) </WorldManufacturerIdentifier>
            <marketClass id="43">4-door Compact Passenger Car</marketClass>
          </vinDescription>
          <!-- output deleted -->
        </VehicleDescription>
      </S:Body>
    </S:Envelope>
