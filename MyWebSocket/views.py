from django.shortcuts import render
from channels.layers import get_channel_layer
from rest_framework.views import APIView
from rest_framework.response import Response
from asgiref.sync import async_to_sync
# from
import json
# Create your views here.


class SendNotification(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data.get("message"))
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(data.get("to"), {
            'type': 'chat.message', 'msg': data.get("message")
        })
        return Response({})
