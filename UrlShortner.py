import pyshorteners

def shorten_url(url):
    return pyshorteners.Shortener().tinyurl.short(url)

url = input("Enter the URL to shorten:")
print("Shortened URL:", shorten_url(url))