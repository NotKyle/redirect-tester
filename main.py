import requests

def main():
    text_file = open('urls.txt', 'r')

    lines = text_file.read().split('\n')

    bad_responses = []

    for line in lines:
        url = "https://www.clearwaterinternational.com/"+line

        # response = requests.get(url, allow_redirects=False)
        response = requests.get(url, allow_redirects=False)

        print("Received response %s for url %s" % (response.status_code, url))

        if response.status_code != 301:
            bad_responses.append([response.status_code, url])

    print("Found the following bad responses:")

    for k,v in bad_responses:
        print("Received bad response %s for url %s" % (k, v))

    num_bad = (len(bad_responses) / len(lines) * 100)
    print("Out of %s URLs, there were %s error(s) [%s]" % (len(lines), len(bad_responses), (str(round(num_bad, 2)) + "%")))

    return


main()