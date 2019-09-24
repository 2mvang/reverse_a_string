def get_domain(url):
    url_arr = url.split(".")
    tld = url_arr[2].split("/")[0]
    print(url_arr[1] + "." + tld)

get_domain("https://docs.google.com/document/d/156NEaYK6nabpgSdclz98xhZdCddypVcB0hBRbwNFYzw/edit)
