__author__ = 'Joe Linn'

import functools
import json
import httpretty
from pyflare import Pyflare


def mock_response(test):
    @functools.wraps(test)      # ensure that the test_* function names are retained so that tests are discovered by nose
    @httpretty.activate
    def wrapper(*args, **kw):
        name = test.__name__.replace('test_', '')
        httpretty.httpretty.register_uri(httpretty.httpretty.POST, Pyflare.CLOUDFLARE_URL,
                                         body=responses[name], content_type='application/json')
        return test(*args, **kw)
    return wrapper

responses = {
    'stats': json.dumps({"response": {"result": {"timeZero": 1333051372000,"timeEnd": 1335643372000,"count": 1,"has_more": False,"objs": [{"cachedServerTime": 1335816172000,"cachedExpryTime": 1335859372000,"trafficBreakdown": {"pageviews": {"regular": 2640,"threat": 27,"crawler": 4},"uniques": {"regular": 223,"threat": 16,"crawler": 4}},"bandwidthServed": {"cloudflare": 78278.706054688,"user": 58909.374023438},"requestsServed": {"cloudflare": 4173,"user": 3697},"pro_zone": False,"pageLoadTime": None,"currentServerTime": 1335824051000,"interval": 20,"zoneCDate": 1307574643000,"userSecuritySetting": "Medium","dev_mode": 0,"ipv46": 5,"ob": 0,"cache_lvl": "agg"}]}},"result": "success","msg": None}),
    'zone_load_multi': json.dumps({"request": {"act": "zone_load_multi","a": "zone_load_multi","email": "sample@example.com","tkn": "8afbe6dea02407989af4dd4c97bb6e25"},"response": {"zones": {"has_more": False,"count": 3,"objs": [{"zone_id": "42","user_id": "1","zone_name": "exampledomain1.com","display_name": "exampledomain1.com","zone_status": "V","zone_mode": "1","host_id": "415","zone_type": "P","host_pubname": "WebHost","host_website": "http://WEBSITEOFHOST.com","vtxt": None,"fqdns": None,"step": "4","zone_status_class": "statusactive","zone_status_desc": "CloudFlare powered, this website will be accelerated and protected (<a class=\"modallinkfaq muted\" href=\"#\" onClick=\"cloudFlare.faq('en_US', ['CompleteActive']);return False;\">info</a>)","ns_vanity_map": [ ],"orig_registrar": None,"orig_dnshost": None,"orig_ns_names": None,"props": {"dns_cname": 0,"dns_partner": 1,"dns_anon_partner": 0,"pro": 0,"expired_pro": 0,"pro_sub": 0,"ssl": 0,"expired_ssl": 0,"expired_rs_pro": 0,"reseller_pro": 0,"force_interal": 0,"ssl_needed": 0,"alexa_rank": 0},"confirm_code": {"zone_deactivate": "f91eb75acb516aa95dabf5fa2b7305ec","zone_dev_mode1": "84fae8e497487d5dea45a39f00054488"},"allow": ["analytics","threat_control","cf_apps","dns_editor","cf_settings","page_rules","zone_deactivate","zone_dev_mode1"]},{"zone_id": "43","user_id": "1","zone_name": "exampledomain2.net","display_name": "exampledomain2.net","zone_status": "V","zone_mode": "0","host_id": None,"zone_type": "F","host_pubname": None,"host_website": None,"vtxt": None,"fqdns": ["norm.ns.cloudflare.com","pat.ns.cloudflare.com"],"step": "4","zone_status_class": "statusdeactivated","zone_status_desc": "Deactivated: Web traffic to this website will no longer pass through the CloudFlare system. We will continue to resolve your DNS. However, you will not receive the benefits of CloudFlare. You may <a href=\"/mywebsites.html?act=zone_reactivate&z=exampledomain2.net\">reactivate</a> CloudFlare for this website at any time. (<a class=\"modallinkfaq muted\" href=\"javascript:void(0);\" onClick=\"cloudFlare.faq('en_US', ['DeactivateInProgress']);return False;\">help</a>)","ns_vanity_map": [ ],"orig_registrar": "A Registrar!","orig_dnshost": None,"orig_ns_names": "{NS1.OLDNAMESERVER.COM,NS2.OLDNAMESERVER.COM}","props": {"dns_cname": 0,"dns_partner": 0,"dns_anon_partner": 0,"pro": 0,"expired_pro": 0,"pro_sub": 0,"ssl": 0,"expired_ssl": 0,"expired_rs_pro": 0,"reseller_pro": 0,"force_interal": 0,"ssl_needed": 0,"alexa_rank": 0},"confirm_code": {"zone_delete": "79fece02a0b6db49ba25d78490142ba2"},"allow": ["zone_reactivate","analytics","zone_delete","dns_editor","cf_settings","page_rules"]},{"zone_id": "44","user_id": "1","zone_name": "exampledomain3.org","display_name": "exampledomain3.org","zone_status": "V","zone_mode": "1","host_id": "115","zone_type": "P","host_pubname": "Some Host!","host_website": "WEBSITEOFHOST.org","vtxt": None,"fqdns": None,"step": "4","zone_status_class": "statusactive","zone_status_desc": "CloudFlare powered, this website will be accelerated and protected (<a class=\"modallinkfaq muted\" href=\"#\" onClick=\"cloudFlare.faq('en_US', ['CompleteActive']);return False;\">info</a>)","ns_vanity_map": [ ],"orig_registrar": None,"orig_dnshost": None,"orig_ns_names": None,"props": {"dns_cname": 0,"dns_partner": 1,"dns_anon_partner": 0,"pro": 0,"expired_pro": 0,"pro_sub": 0,"ssl": 0,"expired_ssl": 0,"expired_rs_pro": 0,"reseller_pro": 0,"force_interal": 0,"ssl_needed": 0,"alexa_rank": 0},"confirm_code": {"zone_deactivate": "c85831462b7bf79d69ad82aba1fa02ce","zone_dev_mode1": "fc6cacf3b4ef5bbdb9c0099a9762ae94"},"allow": ["analytics","threat_control","cf_apps","dns_editor","cf_settings","page_rules","zone_deactivate","zone_dev_mode1"]}]}},"result": "success","msg": None}),
    'rec_load_all': json.dumps({"request": {"act": "rec_load_all","a": "rec_load_all","email": "sample@example.com","tkn": "8afbe6dea02407989af4dd4c97bb6e25","z": "example.com"},"response": {"recs": {"has_more": False,"count": 7,"objs": [{"rec_id": "16606009","rec_tag": "7f8e77bac02ba65d34e20c4b994a202c","zone_name": "example.com","name": "direct.example.com","display_name": "direct","type": "A","prio": None,"content": "[server IP]","display_content": "[server IP]","ttl": "1","ttl_ceil": 86400,"ssl_id": None,"ssl_status": None,"ssl_expires_on": None,"auto_ttl": 1,"service_mode": "0","props": {"proxiable": 1,"cloud_on": 0,"cf_open": 1,"ssl": 0,"expired_ssl": 0,"expiring_ssl": 0,"pending_ssl": 0}},{"rec_id": "16606003","rec_tag": "d5315634e9f5660d3670e62fa176e5de","zone_name": "example.com","name": "home.example.com","display_name": "home","type": "A","prio": None,"content": "[server IP]","display_content": "[server IP]","ttl": "1","ttl_ceil": 86400,"ssl_id": None,"ssl_status": None,"ssl_expires_on": None,"auto_ttl": 1,"service_mode": "0","props": {"proxiable": 1,"cloud_on": 0,"cf_open": 1,"ssl": 0,"expired_ssl": 0,"expiring_ssl": 0,"pending_ssl": 0}},{"rec_id": "16606000","rec_tag": "23b26c051884e94e18711742942760b1","zone_name": "example.com","name": "example.com","display_name": "example.com","type": "A","prio": None,"content": "[server IP]","display_content": "[server IP]","ttl": "1","ttl_ceil": 86400,"ssl_id": None,"ssl_status": None,"ssl_expires_on": None,"auto_ttl": 1,"service_mode": "1","props": {"proxiable": 1,"cloud_on": 1,"cf_open": 1,"ssl": 0,"expired_ssl": 0,"expiring_ssl": 0,"pending_ssl": 0}},{"rec_id": "18136402","rec_tag": "3bcef45cdf5b7638b13cfb89f1b6e716","zone_name": "example.com","name": "test.example.com","display_name": "test","type": "A","prio": None,"content": "[server IP]","display_content": "[server IP]","ttl": "1","ttl_ceil": 86400,"ssl_id": None,"ssl_status": None,"ssl_expires_on": None,"auto_ttl": 1,"service_mode": "0","props": {"proxiable": 1,"cloud_on": 0,"cf_open": 1,"ssl": 0,"expired_ssl": 0,"expiring_ssl": 0,"pending_ssl": 0}},{"rec_id": "16606018","rec_tag": "c0b453b2d94213a7930d342114cbda86","zone_name": "example.com","name": "www.example.com","display_name": "www","type": "CNAME","prio": None,"content": "example.com","display_content": "example.com","ttl": "1","ttl_ceil": 86400,"ssl_id": None,"ssl_status": None,"ssl_expires_on": None,"auto_ttl": 1,"service_mode": "0","props": {"proxiable": 1,"cloud_on": 0,"cf_open": 1,"ssl": 0,"expired_ssl": 0,"expiring_ssl": 0,"pending_ssl": 0}},{"rec_id": "17119732","rec_tag": "1faa40f85c78bccb69ee8116e84f3b40","zone_name": "example.com","name": "xnvii.example.com","display_name": "","type": "CNAME","prio": None,"content": "example.com","display_content": "example.com","ttl": "1","ttl_ceil": 86400,"ssl_id": None,"ssl_status": None,"ssl_expires_on": None,"auto_ttl": 1,"service_mode": "1","props": {"proxiable": 1,"cloud_on": 1,"cf_open": 1,"ssl": 0,"expired_ssl": 0,"expiring_ssl": 0,"pending_ssl": 0}},{"rec_id": "16606030","rec_tag": "2012b3a2e49978ef18ee13dd98e6b6f7","zone_name": "example.com","name": "yay.example.com","display_name": "yay","type": "CNAME","prio": None,"content": "domains.tumblr.com","display_content": "domains.tumblr.com","ttl": "1","ttl_ceil": 86400,"ssl_id": None,"ssl_status": None,"ssl_expires_on": None,"auto_ttl": 1,"service_mode": "0","props": {"proxiable": 1,"cloud_on": 0,"cf_open": 1,"ssl": 0,"expired_ssl": 0,"expiring_ssl": 0,"pending_ssl": 0}}]}},"result": "success","msg": None}),
    'zone_check': json.dumps({"response": {"zones": {"example1.com": 1,"example2.com": 2,"example3.com": 3}},"result": "success","msg": None}),
    'zone_ips': json.dumps({"response": {"ips": [{"ip": "[IP of Visitor]","classification": "regular","hits": 44,"latitude": 37.76969909668,"longitude": 122.39330291748,"zone_name": "example.com"},{"ip": "[IP of Visitor]","classification": "regular","hits": 21,"latitude": 37.396099090576,"longitude": 121.96170043945,"zone_name": "example.com"},{"ip": "[IP of Visitor]","classification": "regular","hits": 8,"latitude": 37.76969909668,"longitude": 122.39330291748,"zone_name": "example.com"},{"ip": "[IP of Visitor]","classification": "regular","hits": 4,"latitude": 38,"longitude": 97,"zone_name": "example.com"}]},"result": "success","msg": None}),
    'ip_lkup': json.dumps({"response": {"0.0.0.0": "BAD:0"},"result": "success","msg": None}),
    'zone_settings': json.dumps({"request": {"act": "zone_settings","tkn": "8afbe6dea02407989af4dd4c97bb6e25","a": "zone_settings","z": "example.com","email": "sample@example.com"},"response": {"result": {"objs": [{"userSecuritySetting": "Medium","dev_mode": 1345768790,"ipv46": 3,"ob": 1,"cache_lvl": "agg","outboundLinks": "disabled","async": "0","bic": "1","chl_ttl": "900","exp_ttl": "7200","fpurge_ts": "1345757991","hotlink": "1","img": "171","lazy": "1","minify": "0","outlink": "0","preload": "0","s404": "1","sec_lvl": "med","spdy": "1","ssl": "1","waf_profile": "high"}]}},"result": "success","msg": None}),
    'sec_lvl': json.dumps({u'msg': None, u'result': u'success'}),
    'cache_lvl': json.dumps({u'msg': None, u'result': u'success'}),
    'devmode': json.dumps({"response": {"expires_on": 1336697110,"zone": {"obj": {"zone_id": "42","user_id": "1","zone_name": "example.com","display_name": "example.com","zone_status": "V","zone_mode": "1","host_id": "415","zone_type": "P","host_pubname": "SomeHost","host_website": "http://www.SomeHost.com","vtxt": None,"fqdns": None,"step": "4","zone_status_class": "statusdevmode","zone_status_desc": "<strong>Development mode</strong> active: CloudFlare's accelerated cache is inactive on this site, so changes to cachable content (like images, CSS, or JavaScript) are visible immediately. Press shiftreload if your changes are not immediate. Development mode will automatically toggle off <strong>3 hours</strong> after initial setup.","ns_vanity_map": [ ],"orig_registrar": None,"orig_dnshost": None,"orig_ns_names": None,"props": {"dns_cname": 0,"dns_partner": 1,"dns_anon_partner": 0,"pro": 0,"expired_pro": 0,"pro_sub": 0,"ssl": 0,"expired_ssl": 0,"expired_rs_pro": 0,"reseller_pro": 0,"force_interal": 0,"ssl_needed": 0,"alexa_rank": 0},"confirm_code": {"zone_deactivate": "f91eb75acb516aa95dabf5fa2b7305ec"},"allow": ["analytics","threat_control","cf_apps","dns_editor","cf_settings","page_rules","zone_deactivate","zone_dev_mode0"]}}},"result": "success","msg": None}),
    'fpurge_ts': json.dumps({u'msg': None, u'attributes': {u'cooldown': 20}, u'response': {u'fpurge_ts': 1378840095}, u'result': u'success'}),
    'zone_file_purge': json.dumps({u'msg': None, u'request': {u'act': u'zone_file_purge'}, u'response': {u'url': u'https://site.com/image.jpg', u'vtxt_match': None}, u'result': u'success'}),
    'zone_grab': json.dumps({u'msg': None, u'result': u'success'}),
    'wl': json.dumps({u'msg': None, u'response': {u'result': {u'action': u'WL', u'ip': u'0.0.0.0'}}, u'result': u'success'}),
    'ban': json.dumps({u'msg': None, u'response': {u'result': {u'action': u'BAN', u'ip': u'0.0.0.0'}}, u'result': u'success'}),
    'nul': json.dumps({u'msg': None, u'response': {u'result': {u'action': u'NUL', u'ip': u'0.0.0.0'}}, u'result': u'success'}),
    'ipv46': json.dumps({u'msg': None, u'result': u'success'}),
    'async': json.dumps({u'msg': None, u'result': u'success'}),
    'minify': json.dumps({u'msg': None, u'result': u'success'}),
    'mirage2': json.dumps({u'msg': None, u'result': u'success'}),
    'rec_new': json.dumps({"request": {"act": "rec_new","a": "rec_new","tkn": "8afbe6dea02407989af4dd4c97bb6e25","email": "sample@example.com","type": "A","z": "example.com","name": "test","content": "96.126.126.36","ttl": "1","service_mode": "1"},"response": {"rec": {"obj": {"rec_id": "23734516","rec_tag": "b3db8b8ad50389eb4abae7522b22852f","zone_name": "example.com","name": "test.example.com","display_name": "test","type": "A","prio": None,"content": "96.126.126.36","display_content": "96.126.126.36","ttl": "1","ttl_ceil": 86400,"ssl_id": "12805","ssl_status": "V","ssl_expires_on": None,"auto_ttl": 1,"service_mode": "0","props": {"proxiable": 1,"cloud_on": 0,"cf_open": 1,"ssl": 1,"expired_ssl": 0,"expiring_ssl": 0,"pending_ssl": 0,"vanity_lock": 0}}}},"result": "success","msg": None}),
    'rec_edit': json.dumps({"request": {"act": "rec_edit","a": "rec_edit","tkn": "1296c62233d48a6cf0585b0c1dddc3512e4b2","id": "23734516","email": "sample@example.com","type": "A","z": "example.com","name": "sub","content": "96.126.126.36","ttl": "1","service_mode": "1"},"response": {"rec": {"obj": {"rec_id": "23734516","rec_tag": "b3db8b8ad50389eb4abae7522b22852f","zone_name": "example.com","name": "sub.example.com","display_name": "sub","type": "A","prio": None,"content": "96.126.126.36","display_content": "96.126.126.36","ttl": "1","ttl_ceil": 86400,"ssl_id": "12805","ssl_status": "V","ssl_expires_on": None,"auto_ttl": 1,"service_mode": "1","props": {"proxiable": 1,"cloud_on": 1,"cf_open": 0,"ssl": 1,"expired_ssl": 0,"expiring_ssl": 0,"pending_ssl": 0,"vanity_lock": 0}}}},"result": "success","msg": None}),
    'rec_delete': json.dumps({u'msg': None, u'result': u'success'}),
}