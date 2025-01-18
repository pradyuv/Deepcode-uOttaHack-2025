import urllib.parse
import validators
import urllib
from urllib.parse import urlparse

def validate_url(url_to_val):
# Returns boolean
    return validators.url(url_to_val)

def parse_url(url_to_parse):
    #Returns 6 item named-tuple
    return urllib.parse(url_to_parse)

