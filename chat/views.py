from django.shortcuts import render
import openai

openai.api_key = "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"


# Create your views here.
def index(request):
    data = {"head": "myapp"}

    if request.method == "POST":
        question = request.POST["question"]
        data["question"] = question
        print(question)
        result = generate_text(question)
        data["answer"] = result
        return render(request, "index.html", {"data": data})
    else:
        return render(request, "index.html", {"data": data})


def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text
