from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from plusdefapp.models import HelloWorld, chatgptcbot

import openai
from .models import ChatGptcode
from django.contrib.auth.decorators import login_required
# Create your views here.
openai.api_key = "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"
# Create your views here.


def cgcode(request):
    # check if user is authenticated
    if request.user.is_authenticated:
        if request.method == 'POST':
            # get user input from the form
            user_input = request.POST.get('userInput')
            # clean input from any white spaces
            clean_user_input = str(user_input).strip()
            # send request with user's prompt
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "I want you to act as an IT Architect. I will provide some details about the functionality of an application or other digital product, and it will be your job to come up with ways to integrate it into the IT landscape. This could involve analyzing business requirements, performing a gap analysis and mapping the functionality of the new system to the existing IT landscape. Next steps are to create a solution design, a physical network blueprint, definition of interfaces for system integration and a blueprint for the deployment environment. Please reply to my request in Korean"
                    },
                    {
                        "role": "user",
                        "content": clean_user_input
                    },
                ],
                temperature=0,
                max_tokens=3000,
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0
            )
            # get response
            bot_response = response['choices'][0]["message"]["content"]

            obj, created = ChatGptcode.objects.get_or_create(
                user=request.user,
                messageInputs=clean_user_input,
                bot_responsees=bot_response.strip(),
            )
            return redirect(request.META['HTTP_REFERER'])
        else:
            # retrieve all messages belong to logged in user
            get_history = ChatGptcode.objects.filter(user=request.user)
            context = {'get_history': get_history}
            return render(request, 'chatgptcodeapp/chatgptcode.html', context)
    else:
        return render(request, 'accountapp/login.html')


@login_required
def DeleteHistory(request):
    ChatGptcodeobjs = ChatGptcode.objects.filter(user = request.user)
    ChatGptcodeobjs.delete()
    return redirect(request.META['HTTP_REFERER'])