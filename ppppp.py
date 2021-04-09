import requests
import time #拖慢速度

URL="https://www.majortests.com/word-lists/word-list-0{}.html"

def generate_urls(url, start_page, end_page):
    urls = []
    for page in range (start_page, end_page):
        urls.append(url.format(page))
    return urls



def get_resource(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ApplWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
    return requests.get(url, headers=headers)


if __name__ == "__main__":
    urlx = generate_urls(URL, 1, 10)
    for url in urlx:
        file = url.split("/")[-1]
        print("catching: ", file, " web data...")
        r = get_resource(url)
        if r.status_code == requests.codes.ok:
            print(r.text)
            print("--------------\n\n")
        else:
            print("HTTP request error!!")
        
        print("sleep 5 second")
        time.sleep(5)