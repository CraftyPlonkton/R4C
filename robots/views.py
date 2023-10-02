import json
from http import HTTPStatus
from json import JSONDecodeError

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .forms import RobotCreateForm


@csrf_exempt
@require_http_methods(['POST'])
def robot_create(request):
    """Создание экземпляра модели робот на основе полученного JSON запроса."""
    try:
        json_data = json.loads(request.body.decode())
    except JSONDecodeError as error:
        return JsonResponse({'Invalid JSON data': error.msg},
                            status=HTTPStatus.BAD_REQUEST)
    form = RobotCreateForm(json_data)
    if form.is_valid():
        form.save()
        return JsonResponse(form.cleaned_data, status=HTTPStatus.CREATED)
    return JsonResponse(form.errors, status=HTTPStatus.BAD_REQUEST)
