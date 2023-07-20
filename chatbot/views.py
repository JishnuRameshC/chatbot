from django.shortcuts import render
from django.http import JsonResponse
import openai
# Create your views here.
openai_api_key = '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'

# openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 150,
        n =1,
        stop = None,
        temperature = 0.7
    )
    print (response)
    
    answer = response.choices[0].message.content.strip()
    return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({"message":message, "response":response})
    return render(request,'chatbot.html')