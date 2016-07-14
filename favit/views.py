# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from json import dumps
from json import loads

from .models import Favorite


@login_required
def add_or_remove(request):

    if not request.is_ajax():
        return HttpResponseNotAllowed('POST')

    user = request.user

    try:
        post_data = loads(request.body)
        app_model = post_data['target_model']
        obj_id = int(post_data['target_object_id'])
        #  app_model = request.POST['target_model']
        #  obj_id = int(request.POST['target_object_id'])
    except KeyError as keyError:
        return HttpResponseBadRequest("key error: " + str(keyError))
    except ValueError as valueError:
        return HttpResponseBadRequest("value error: " + str(valueError))

    fav = Favorite.objects.get_favorite(user, obj_id, model=app_model)

    if fav is None:
        Favorite.objects.create(user, obj_id, app_model)
        status = 'added'
    else:
        fav.delete()
        status = 'deleted'

    response = {
        'status': status,
        'fav_count': Favorite.objects.for_object(obj_id, app_model).count()
    }

    return HttpResponse(
        dumps(response, ensure_ascii=False),
        content_type='application/json'
    )


@login_required
def add(request):

    if not request.is_ajax():
        return HttpResponseNotAllowed('POST')

    user = request.user

    try:
        post_data = loads(request.body)
        app_model = post_data['target_model']
        obj_id = int(post_data['target_object_id'])
        #  app_model = request.POST['target_model']
        #  obj_id = int(request.POST['target_object_id'])
    except KeyError as keyError:
        return HttpResponseBadRequest("key error: " + str(keyError))
    except ValueError as valueError:
        return HttpResponseBadRequest("value error: " + str(valueError))

    fav = Favorite.objects.get_favorite(user, obj_id, model=app_model)

    if fav is None:
        Favorite.objects.create(user, obj_id, app_model)
        status = 'added'
    else:
        status = 'already added before'

    response = {
        'status': status,
        'fav_count': Favorite.objects.for_object(obj_id, app_model).count()
    }

    return HttpResponse(
        dumps(response, ensure_ascii=False),
        content_type='application/json'
    )


@login_required
def remove(request):

    if not request.is_ajax():
        return HttpResponseNotAllowed('POST')

    user = request.user

    try:
        post_data = loads(request.body)
        app_model = post_data['target_model']
        obj_id = int(post_data['target_object_id'])
        #  app_model = request.POST['target_model']
        #  obj_id = int(request.POST['target_object_id'])
    except KeyError as keyError:
        return HttpResponseBadRequest("key error: " + str(keyError))
    except ValueError as valueError:
        return HttpResponseBadRequest("value error: " + str(valueError))

    status = 'delete failed'
    try:
        Favorite.objects.get_favorite(user, obj_id, model=app_model).delete()
        status = 'deleted'
    except:
        return HttpResponseBadRequest(status)

    response = {
        'status': status,
    }

    return HttpResponse(
        dumps(response, ensure_ascii=False),
        content_type='application/json'
    )
