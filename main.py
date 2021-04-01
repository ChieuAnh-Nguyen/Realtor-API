import requests


if __name__ == '__main__':


    url = "https://realtor.p.rapidapi.com/locations/auto-complete"

    querystring = {"input": "california"}

    headers = {
        'x-rapidapi-key': "1ca487dc23msh132a97fd2e1f268p15a399jsn87aff619022a",
        'x-rapidapi-host': "realtor.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    california_cities = response.json()
    for each in california_cities.items():
        print(each[0])
    my_string = california_cities['autocomplete'][0]['counties'][0]
    for each in my_string.items():
        print(each[1])
    print(my_string)