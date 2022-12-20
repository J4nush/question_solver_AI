import json
import requests


def generate(text):
    token = "<YOUR-API-TOKEN-HERE>"

    data_send = '{"model":"text-davinci-003","prompt": "'+text.rstrip()+'" ,"temperature":0.8, "max_tokens": 4000, "n":1 , "stream": false}'
    data_send = json.loads(data_send)
    headers = {'Content-Type' : 'application/json; charset=utf-8', 'Authorization': 'Bearer '+token}
    try:
        response = requests.post('https://api.openai.com/v1/completions', json=data_send, headers=headers)
        data_get = response.json()
        print(response.text)
        # print(data_get["choices"][0]["text"])
        return data_get["choices"][0]["text"]
    except:
        return "error"


def writeLine(question, answer):
    f = open('result.txt', 'a', encoding="utf-8")
    f.write(question)
    f.write(answer)
    f.write("\n")
    f.write("---------------------------------------------------------------")
    f.write("\n\n\n\n")
    f.close()


def openFile(filename):
    arr = {}
    f = open(filename, 'r', encoding="utf-8")
    lines = f.readlines()
    for line in lines:
        # print(type(line))
        answer = generate(line)
        if(answer != "error"):
            writeLine(line, answer)
        else:
            writeLine(line, "ERROR")
        # arr[line] = answer

    return arr

if __name__ == '__main__':
    result = openFile("questions.txt")

#by J4nush
