import openai
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
import json
from chat.models import SiteSetting


def getApiKey():
    settingItems = SiteSetting.objects.filter(
        name="openai_api_key",
    )
    if len(settingItems) > 0:
        openai_api_key = settingItems[0].value
        return openai_api_key
    raise Exception("Not found openai_api_key")


openai.api_key = getApiKey()


def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )
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
