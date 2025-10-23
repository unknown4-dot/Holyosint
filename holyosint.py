import requests
import socket
import ipapi
from colorama import Fore
from colorama import Style


def holyinfo(url):

    idk = Fore.YELLOW + "[+]"

    ip = socket.gethostbyname(url)

    print(f"\n{idk} IP | " + Style.RESET_ALL +  f"{ip}")

    response = ipapi.location(ip)

    print(f"\n{idk} network | " + Style.RESET_ALL + f"{response.get('network')}")

    print(f"\n{idk} region | " + Style.RESET_ALL + f"{response.get('region')}")

    print(f"\n{idk} city | " + Style.RESET_ALL + f"{response.get('city')}")

    print(f"\n{idk} isp | " + Style.RESET_ALL + f"{response.get('type')}")

    print(f"\n{idk} country code | " + Style.RESET_ALL + f"{response.get('country_code')}")

    print(f"\n{idk} ASN | " + Style.RESET_ALL + f"{response.get('asn')}")

    print(f"\n{idk} is proxy | " + Style.RESET_ALL + f"{response.get('proxy')}")

    print(f"\n{idk} time zone | " + Style.RESET_ALL + f"{response.get('timezone')}")

    print(f"\n{idk} zip code | " + Style.RESET_ALL + f"{response.get('zip')}")

    print(f"\n{idk} hosting | " + Style.RESET_ALL + f"{response.get('hosting')}")

    print(f"\n{idk} region name | " + Style.RESET_ALL + f"{response.get('regionName')}")

    print(f"\n{idk} reverse | " + Style.RESET_ALL + f"{response.get('reverse')}")

    print(f"\n{idk} email | " + Style.RESET_ALL + f"{response.get('email')}")

    print(f"\n{idk} is tor | " + Style.RESET_ALL + f"{response.get('is_tor')}")

    print(f"\n{idk} is vpn | " + Style.RESET_ALL + f"{response.get('is_vpn')}")  # FIXED THIS LINE

    print(f"\n{idk} created | " + Style.RESET_ALL + f"{response.get('created')}")

    print(f"\n{idk} updated | " + Style.RESET_ALL + f"{response.get('updated')}")

    print(f"\n{idk} whois | " + Style.RESET_ALL + f"{response.get('whois')}")

    print(f"\n{idk} route | " + Style.RESET_ALL + f"{response.get('route')}")

    print(f"\n{idk} state | " + Style.RESET_ALL + f"{response.get('state')}")

    print(f"\n{idk} domain | " + Style.RESET_ALL + f"{response.get('domain')}")

    print(f"\n{idk} org | " + Style.RESET_ALL + f"{response.get('org')}")



    print(f"\n{idk} " + Style.RESET_ALL + "you can get the asn lookup info in this | https://asnlookup.com/asn/{response.get('asn')}")