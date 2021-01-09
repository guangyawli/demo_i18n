from django.http import JsonResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from demo_i18n import settings


@csrf_exempt
def set_language(request):
    """
    多语言切换
    """
    language = request.POST.get("language", "en")
    if language == "zh_hant":
        request.session[settings.LANGUAGE_SESSION_KEY] = 'zh-Hant'
    else:
        request.session[settings.LANGUAGE_SESSION_KEY] = 'en'

    return JsonResponse({'detail': 'success'}, status=200)


def home(request):
    send_content = {
        'Hello_msg': 'Hello World'
    }
    return render(request, 'index.html', send_content)

