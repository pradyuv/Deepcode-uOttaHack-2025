import utils
import requests

def ping_url(url_to_ping):
    if utils.validate_url(url_to_ping): # Validate URL syntactically 
        try:
            r = requests.head(url=url_to_ping, timeout=5)

            r.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            # HTTP errors (e.g., 404 Not Found, 500 Internal Server Error)
            print(f"HTTP error occurred: {http_err} - URL responded with status code {r.status_code}")
            return False
    
        except requests.exceptions.ConnectionError as conn_err:
            # network-related errors such as DNS failures, refused connections, etc.
            print(f"Connection error occurred: {conn_err}")
            return False
    
        except requests.exceptions.Timeout as timeout_err:
            # handles request timeouts
            print(f"Timeout error occurred: {timeout_err}")
            return False
            
        except requests.exceptions.RequestException as req_err:
            # Catches any other request-related exceptions
            print(f"An unexpected error occurred: {req_err}")
            print ("Try using GET method")

            try:
                r = requests.get(url=url_to_ping, timeout=5, stream=True )

            except requests.RequestException as e:
                print(f"GET request failed as well: {e}")

            else:
                print("URL is live (verified with GET)!")
    
    else:
        print("Live URL verified with HEAD")
        return True




