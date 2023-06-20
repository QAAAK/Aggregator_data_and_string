def normalize_url(site):
    if site[0:8] == 'https://':
        return site
    elif site[0:7] == 'http://':
        return site.replace('http://','https://',2)
    else:
        return 'https://' + site