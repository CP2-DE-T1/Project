from django.shortcuts import render
from apps.users.models import User
from apps.boards.models import Board
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

# Create your views here.
#남녀 별 통계
#APIView 는 Class-based view(CBV)
class GenderStatistics(APIView):
    
    def get(self, request):
        male_total = User.objects.filter(gender='Male').count()
        female_total = User.objects.filter(gender='Female').count()
        return Response({'남자 회원 수': male_total, '여자 회원 수': female_total})

#연령대 별 통계
class AgeStatistics(APIView):

    age_statistics = {}
    def get(self, request):
        year_now = datetime.now().today()
        for i in range(1,11):
            age_count = User.objects.filter(birth_date__year__range=(year_now-i*10,year_now+1-(i-1)*10)).count()
            if i == 1:
                age_statistics['10대 이하']=age_count
            else:
                age_statistics[f'{i-1}대']=age_count
        return Response({'나이대 분포': age_statistics})


#이용시간 별 통계
class LoginStatistics(APIView):
    login_statistics = {}
    def get(self, request):
        login_statistics['0~6']=User.objects.filter(updated_at__time__range=(0,7))
        login_statistics['7~12']=User.objects.filter(updated_at__time__range=(7,13))
        login_statistics['13~18']=User.objects.filter(updated_at__time__range=(13,19))
        login_statistics['19~24']=User.objects.filter(updated_at__time__range=(19,24))
        return Response({'로그인 시간 별 통계':login_statistics})