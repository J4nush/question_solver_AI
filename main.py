import json
import requests


def generate(text):
    print(text)
    token = "<YOUR-API-TOKEN-HERE>"
    model = "text-davinci-003"
    temperature = "0.8"
    max_tokens = "4000"

    data_send = '{"model": "'+model+'","prompt": "'+text.rstrip()+'" ,"temperature": '+temperature+', "max_tokens": '+max_tokens+', "n":1 , "stream": false}'
    data_send = json.loads(data_send)
    headers = {'Content-Type' : 'application/json; charset=utf-8', 'Authorization': 'Bearer '+token}
    try:
        response = requests.post('https://api.openai.com/v1/completions', json=data_send, headers=headers)
        data_get = response.json()
        return data_get["choices"][0]["text"]
    except:
        return "error"
    print("DONE")

def writeLine(question, answer):
    f = open('result.txt', 'a', encoding="utf-8")
    f.write(question)
    f.write(answer)
    f.write("\n")
    f.write("---------------------------------------------------------------")
    f.write("\n\n\n\n")
    f.close()


def openFile(filename):
    f = open(filename, 'r', encoding="utf-8")
    lines = f.readlines()
    for line in lines:
        answer = generate(line)
        writeLine(line, answer)
    print("ENDING")

if __name__ == '__main__':
    print("START")
    result = openFile("questions.txt")
#by J4nush
