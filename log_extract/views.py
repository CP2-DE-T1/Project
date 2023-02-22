from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
# Create your views here.
class LogExport(APIView):

    def get(self, request):
        get_log=open('logs/json_logger.log','rt')
        log_lines=get_log.readlines()
        data={'logs':[]}
        for log in log_lines:
            data['logs'].append(log)
        get_log.close()
        return Response(data)

