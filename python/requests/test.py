import requests


def run():
    url = 'https://image-background-removal4.p.rapidapi.com/remove'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-RapidAPI-Key': '<YOUR_API_KEY>',
        'X-RapidAPI-Host': 'image-background-removal4.p.rapidapi.com',
    }
    input_file = 'test.jpg'
    resp = requests.post(url, headers=headers, data=open(input_file, 'rb'))
    output_file = 'result.png'
    if resp.ok:
        with open(output_file, 'wb') as f:
            f.write(resp.content)
    else:
        print('Something went wrong:', resp.status_code)


if __name__ == '__main__':
    run()