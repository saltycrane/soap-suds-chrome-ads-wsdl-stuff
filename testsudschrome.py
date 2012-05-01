import logging
import os
import os.path
import sys

from suds.client import Client
from suds.sax.element import Element


CHROME_URL = 'file://' + os.path.join(os.path.abspath(os.path.dirname(__file__)), '7a.wsdl')
CHROME_ACCOUNT_NUMBER = os.environ['CHROME_ACCOUNT_NUMBER']
CHROME_ACCOUNT_SECRET = os.environ['CHROME_ACCOUNT_SECRET']


formatter = logging.Formatter('[%(asctime)s] %(levelname)s (%(process)d) %(name)s:%(lineno)s %(message)s')
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(formatter)
logger = logging.getLogger('suds')
logger.setLevel(logging.INFO)
logger.addHandler(sh)


def get_version_info_failure():
    client = Client(CHROME_URL)

    account_info = client.factory.create('AccountInfo')
    account_info._number = CHROME_ACCOUNT_NUMBER
    account_info._secret = CHROME_ACCOUNT_SECRET
    account_info._country = 'US'
    account_info._language = 'en'

    version_info_request = client.factory.create('VersionInfoRequest')
    version_info_request.accountInfo = account_info
    print version_info_request

    result = client.service.getVersionInfo(version_info_request)
    print result
    # results:
    # (BaseRequest){
    #    accountInfo = 
    #       (AccountInfo){
    #          _number = "123456"
    #          _secret = "xxxxxxxxxxxxxxxx"
    #          _country = "US"
    #          _language = "en"
    #          _behalfOf = ""
    #       }
    #  }
    # [2012-04-30 18:12:29,101] ERROR (5914) suds.client:656 <?xml version="1.0" encoding="UTF-8"?>
    # <SOAP-ENV:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="urn:description7a.services.chrome.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    #    <SOAP-ENV:Header/>
    #    <ns0:Body>
    #       <ns1:VersionInfoRequest>
    #          <ns1:accountInfo>
    #             <ns1:accountInfo number="123456" secret="xxxxxxxxxxxxxxxx" country="US" language="en"/>
    #          </ns1:accountInfo>
    #       </ns1:VersionInfoRequest>
    #    </ns0:Body>
    # </SOAP-ENV:Envelope>
    # Traceback (most recent call last):
    #   File "testsudschrome.py", line 128, in <module>
    #     get_version_info_failure()
    #   File "testsudschrome.py", line 68, in get_version_info_failure
    #     result = client.service.getVersionInfo(version_info_request)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/client.py", line 542, in __call__
    #     return client.invoke(args, kwargs)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/client.py", line 602, in invoke
    #     result = self.send(soapenv)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/client.py", line 657, in send
    #     result = self.failed(binding, e)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/client.py", line 712, in failed
    #     r, p = binding.get_fault(reply)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/bindings/binding.py", line 265, in get_fault
    #     raise WebFault(p, faultroot)
    # suds.WebFault: Server raised fault: 'cvc-complex-type.4: Attribute 'number' must appear on element 'ns1:accountInfo'.'


def get_version_info_success():
    client = Client(CHROME_URL)

    account_info = client.factory.create('AccountInfo')
    account_info._number = CHROME_ACCOUNT_NUMBER
    account_info._secret = CHROME_ACCOUNT_SECRET
    account_info._country = 'US'
    account_info._language = 'en'

    result = client.service.getVersionInfo(account_info)
    print result
    # result:
    # (reply){
    #    responseStatus = 
    #       (ResponseStatus){
    #          _description = "Successful"
    #          _responseCode = "Successful"
    #       }
    #    data[] = 
    #       (data){
    #          _date = 2012-04-29 19:30:00
    #          _country = "US"
    #          _build = "43"
    #       },
    #       (data){
    #          _date = 2012-04-29 20:12:00
    #          _country = "CA"
    #          _build = "43"
    #       },
    #  }


def describe_vehicle_failure(vin):
    """This fails because an extra accountInfo element is added in the request xml
    """
    client = Client(CHROME_URL)

    account_info = client.factory.create('AccountInfo')
    account_info._number = CHROME_ACCOUNT_NUMBER
    account_info._secret = CHROME_ACCOUNT_SECRET
    account_info._country = 'US'
    account_info._language = 'en'

    vin_element = Element('vin', ns=('ns1', 'urn:description7a.services.chrome.com'))
    vin_element.setText(vin)

    vehicle_description_request = client.factory.create('VehicleDescriptionRequest')
    vehicle_description_request.accountInfo = account_info
    vehicle_description_request.switch.append(vin_element)
    print vehicle_description_request

    result = client.service.describeVehicle(vehicle_description_request)
    print result
    # results:
    # (VehicleDescriptionRequest){
    #    accountInfo = 
    #       (AccountInfo){
    #          _number = "123456"
    #          _secret = "xxxxxxxxxxxxxxxx"
    #          _country = "US"
    #          _language = "en"
    #          _behalfOf = ""
    #       }
    #    trimName = None
    #    manufacturerModelCode = None
    #    wheelBase = None
    #    OEMOptionCode[] = <empty>
    #    equipmentDescription[] = <empty>
    #    exteriorColorName = None
    #    interiorColorName = None
    #    nonFactoryEquipmentDescription[] = <empty>
    #    switch[] = 
    #       <ns1:vin xmlns:ns1="urn:description7a.services.chrome.com">KMHCN4AC7AU407141</ns1:vin>,
    #    vehicleProcessMode = 
    #       (SwitchAvailability){
    #          value = None
    #       }
    #    optionsProcessMode = 
    #       (SwitchAvailability){
    #          value = None
    #       }
    #    includeMediaGallery = 
    #       (SwitchChromeMediaGallery){
    #          value = None
    #       }
    #    includeTechnicalSpecificationTitleId[] = <empty>
    #  }
    # [2012-04-30 18:18:18,113] ERROR (12024) suds.client:656 <?xml version="1.0" encoding="UTF-8"?>
    # <SOAP-ENV:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="urn:description7a.services.chrome.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    #    <SOAP-ENV:Header/>
    #    <ns0:Body>
    #       <ns1:VehicleDescriptionRequest>
    #          <ns1:accountInfo xsi:type="ns1:VehicleDescriptionRequest">
    #             <ns1:accountInfo number="123456" secret="xxxxxxxxxxxxxxxx" country="US" language="en"/>
    #             <ns1:vin xmlns:ns1="urn:description7a.services.chrome.com">KMHCN4AC7AU407141</ns1:vin>
    #             <ns1:vehicleProcessMode/>
    #             <ns1:optionsProcessMode/>
    #             <ns1:includeMediaGallery/>
    #          </ns1:accountInfo>
    #       </ns1:VehicleDescriptionRequest>
    #    </ns0:Body>
    # </SOAP-ENV:Envelope>
    # Traceback (most recent call last):
    #   File "testsudschrome.py", line 161, in <module>
    #     describe_vehicle_failure(VIN)
    #   File "testsudschrome.py", line 127, in describe_vehicle_failure
    #     result = client.service.describeVehicle(vehicle_description_request)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/client.py", line 542, in __call__
    #     return client.invoke(args, kwargs)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/client.py", line 602, in invoke
    #     result = self.send(soapenv)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/client.py", line 657, in send
    #     result = self.failed(binding, e)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/client.py", line 712, in failed
    #     r, p = binding.get_fault(reply)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/bindings/binding.py", line 265, in get_fault
    #     raise WebFault(p, faultroot)
    # suds.WebFault: Server raised fault: 'cvc-elt.4.2: Cannot resolve 'ns1:VehicleDescriptionRequest' to a type definition for element 'ns1:accountInfo'.'


def describe_vehicle_failure2(vin):
    """This fails because there is a bug related when prettyxml is False
    https://fedorahosted.org/suds/ticket/432
    """
    client = Client(CHROME_URL)

    account_info = client.factory.create('AccountInfo')
    account_info._number = CHROME_ACCOUNT_NUMBER
    account_info._secret = CHROME_ACCOUNT_SECRET
    account_info._country = 'US'
    account_info._language = 'en'

    vin_element = Element('vin', ns=('ns1', 'urn:description7a.services.chrome.com'))
    vin_element.setText(vin)

    result = client.service.describeVehicle(account_info, vin_element)
    print result
    # results:
    # [2012-04-30 18:20:38,971] ERROR (14590) suds.client:656 <?xml version="1.0" encoding="UTF-8"?>
    # <SOAP-ENV:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="urn:description7a.services.chrome.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    #    <SOAP-ENV:Header/>
    #    <ns0:Body>
    #       <ns1:VehicleDescriptionRequest>
    #          <ns1:accountInfo number="123456" secret="xxxxxxxxxxxxxxxx" country="US" language="en"/>
    #          <ns1:vin xmlns:ns1="urn:description7a.services.chrome.com">KMHCN4AC7AU407141</ns1:vin>
    #       </ns1:VehicleDescriptionRequest>
    #    </ns0:Body>
    # </SOAP-ENV:Envelope>
    # Traceback (most recent call last):
    #   File "testsudschrome.py", line 244, in <module>
    #     describe_vehicle_failure2(VIN)
    #   File "testsudschrome.py", line 208, in describe_vehicle_failure2
    #     result = client.service.describeVehicle(account_info, vin_element)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/client.py", line 542, in __call__
    #     return client.invoke(args, kwargs)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/client.py", line 602, in invoke
    #     result = self.send(soapenv)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/client.py", line 657, in send
    #     result = self.failed(binding, e)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/client.py", line 712, in failed
    #     r, p = binding.get_fault(reply)
    #   File "/tmp/soap-suds-chrome-ads-wsdl-stuff/venv/src/suds/suds/bindings/binding.py", line 265, in get_fault
    #     raise WebFault(p, faultroot)
    # suds.WebFault: Server raised fault: 'cvc-complex-type.2.4.a: Invalid content was found starting with element 'vin'. One of '{"urn:description7a.services.chrome.com":modelYear, "urn:description7a.services.chrome.com":vin, "urn:description7a.services.chrome.com":styleId}' is expected.'


def describe_vehicle_failure3(vin):
    """This fails becuase attributes on the root of the response element, such
    as bestMakeName, are not available
    """
    # NOTE: prettyxml must be set to True in order to add `vin_element` below
    # https://fedorahosted.org/suds/ticket/432
    client = Client(CHROME_URL, prettyxml=True)

    account_info = client.factory.create('AccountInfo')
    account_info._number = CHROME_ACCOUNT_NUMBER
    account_info._secret = CHROME_ACCOUNT_SECRET
    account_info._country = 'US'
    account_info._language = 'en'

    vin_element = Element('vin', ns=('ns1', 'urn:description7a.services.chrome.com'))
    vin_element.setText(vin)

    result = client.service.describeVehicle(account_info, vin_element)
    print str(result)[:1000]
    print result._bestMakeName
    # results:
    # (reply){
    #    responseStatus = 
    #       (ResponseStatus){
    #          _description = "Successful"
    #          _responseCode = "Successful"
    #       }
    #    vinDescription = 
    #       (vinDescription){
    #          _division = "Hyundai"
    #          _modelName = "Accent"
    #          _bodyType = "Sedan 4 Dr."
    #          _vin = "KMHCN4AC7AU407141"
    #          _modelYear = 2010
    #          _styleName = "4dr Sdn GLS"
    #          WorldManufacturerIdentifier = "South Korea Hyundai - Passenger Cars (Mpv & Rv) Buses & Trucks (Including Vans) "
    #          marketClass[] = 
    #             (marketClass){
    #                value = "4-door Compact Passenger Car"
    #                _id = 43
    #             },
    #       }
    #    style[] = 
    #       (Style){
    #          _trim = "GLS"
    #          _fleetOnly = False
    #          _drivetrain = "Front Wheel Drive"
    #          _nameWoTrim = "4dr Sdn Man"
    #          _modelFleet = False
    #          _altModelName = "Accent"
    #          _passDoors = 4
    #          _altBodyType = "4dr Car"
    #          _modelYear = 2010
    #          _mfrModelCode = "15433"

    # Traceback (most recent call last):
    #   File "testsudschrome.py", line 265, in <module>
    #     describe_vehicle_success(VIN)
    #   File "testsudschrome.py", line 255, in describe_vehicle_success
    #     print result._bestMakeName
    # AttributeError: reply instance has no attribute '_bestMakeName'


def describe_vehicle_success_with_never_unwrap_output_patch(vin):
    """This uses a patched version of suds which never tries to unwrap the output message
    """
    # NOTE: prettyxml must be set to True in order to add `vin_element` below
    # https://fedorahosted.org/suds/ticket/432
    client = Client(CHROME_URL, prettyxml=True, never_unwrap_output=True)

    account_info = client.factory.create('AccountInfo')
    account_info._number = CHROME_ACCOUNT_NUMBER
    account_info._secret = CHROME_ACCOUNT_SECRET
    account_info._country = 'US'
    account_info._language = 'en'

    vin_element = Element('vin', ns=('ns1', 'urn:description7a.services.chrome.com'))
    vin_element.setText(vin)

    result = client.service.describeVehicle(account_info, vin_element)
    print str(result)[:1000]
    print result._bestMakeName
    # results:
    # (VehicleDescription){
    #    _bestStyleName = "4dr Sdn GLS"
    #    _language = "en"
    #    _country = "US"
    #    _bestTrimName = "GLS"
    #    _modelYear = 2010
    #    _bestMakeName = "Hyundai"
    #    _bestModelName = "Accent"
    #    responseStatus = 
    #       (ResponseStatus){
    #          _description = "Successful"
    #          _responseCode = "Successful"
    #       }
    #    vinDescription = 
    #       (vinDescription){
    #          _division = "Hyundai"
    #          _modelName = "Accent"
    #          _bodyType = "Sedan 4 Dr."
    #          _vin = "KMHCN4AC7AU407141"
    #          _modelYear = 2010
    #          _styleName = "4dr Sdn GLS"
    #          WorldManufacturerIdentifier = "South Korea Hyundai - Passenger Cars (Mpv & Rv) Buses & Trucks (Including Vans) "
    #          marketClass[] = 
    #             (marketClass){
    #                value = "4-door Compact Passenger Car"
    #                _id = 43
    #             },
    #       }
    #    style[] = 
    #       (Style){
    #          _trim = "GLS"
    #          _fleetOnly = False
    #          _drivetrain = "Front Wheel Drive"
    #          _nameWoTrim = "4dr Sdn M
    # Hyundai


if __name__ == '__main__':
    VIN = 'KMHCN4AC7AU407141'

    get_version_info_failure()
    get_version_info_success()
    describe_vehicle_failure(VIN)
    describe_vehicle_failure2(VIN)
    describe_vehicle_failure3(VIN)
    describe_vehicle_success_with_never_unwrap_output_patch(VIN)
