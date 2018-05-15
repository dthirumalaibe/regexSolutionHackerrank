# https://www.hackerrank.com/challenges/ip-address-validation/problem
import re

for x in range(int(input())):
    string = input()
    z = bool(re.search('^([01]\d?\d?|2[0-6]?[0-5]?|[0-9]{2}|[0-9])\.([01]\d?\d?|2[0-6]?[0-5]?|[0-9]{2}|[0-9])\.([01]\d?\d?|2[0-6]?[0-5]?|[0-9]{2}|[0-9])\.([01]\d?\d?|2[0-6]?[0-5]?|[0-9]{2}|[0-9])$',string))
    if z:
        print('IPv4')
    else:
        z = bool(re.search(
            '^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$',
            string))
        if z:
            print('IPv6')
        else:
            print('Neither')