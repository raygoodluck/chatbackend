import openai
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
import json
import re
from . import dataaccess


def getApiKey():
    apikey = dataaccess.getSetting("openai_api_key")
    return apikey


openai.api_key = getApiKey()


defaultOpenAIOption = {
    "engine": "text-davinci-003",
    "max_tokens": 1000,
    "n": 1,
    "stop": None,
    "temperature": 0.5,
}


def is_number(string):
    pattern = re.compile(r"^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$")
    return bool(pattern.match(string))


def is_int(string):
    pattern = re.compile(r"^[-+]?[0-9]*$")
    return bool(pattern.match(string))


def processNumber(dict):
    result = {}
    for k, v in dict.items():
        if v == "None":
            result[k] = None
        elif is_int(v):
            result[k] = int(v)
        elif is_number(v):
            result[k] = float(v)
        else:
            result[k] = v
    return result


def getOpenAIOption():
    aiOption = dataaccess.getDictItems("openai_api_option")
    print(aiOption)
    option = {}
    option.update(defaultOpenAIOption)
    optionFromDb = processNumber(aiOption)
    option.update(optionFromDb)
    return option


def generate_text(prompt):
    option = getOpenAIOption()
    option.update({"prompt": prompt})
    print(option)
    response = openai.Completion.create(**option)
    if response and len(response.choices) > 0:
        return response.choices[0].text


def getAnswer(request):
    result = {}
    if request.method == "POST":
        print(request.body)
        request_data = json.loads(request.body)
        for item in request_data:
            print(item, request_data.get(item))
        question = request_data.get("question")

        answer = generate_text(question)
        # print(answer)

        result["is_successed"] = "1"
        result["msg"] = answer.strip()
        # return redirect(data["JenkinsJob"].url)
    else:
        result["is_successed"] = "0"
        result["msg"] = "This is an error!"
        return HttpResponseBadRequest()

    return JsonResponse(result)
