import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    parsed = urlparse(url)
    
    features.append(len(url))
    features.append(url.count('.'))
    features.append(1 if "https" in url else 0)
    features.append(1 if re.match(r'\d+\.\d+\.\d+\.\d+', url) else 0)
    features.append(1 if '@' in url else 0)
    features.append(1 if '-' in parsed.netloc else 0)
    features.append(len(parsed.netloc.split('.')) - 2)
    features.append(1 if "http" in parsed.netloc else 0)
    features.append(len(parsed.path))
    features.append(sum(c.isdigit() for c in url))
    features.append(len(re.findall(r'[^\w]', url)))

    suspicious_words = ['login', 'verify', 'bank', 'update', 'free']
    features.append(1 if any(word in url.lower() for word in suspicious_words) else 0)

    features.append(len(parsed.netloc))
    features.append(1 if any(x in url for x in ['bit.ly','tinyurl','goo.gl']) else 0)
    features.append(url.count('?'))

    return features