from django.shortcuts import render
from apps.users.models import User
from apps.boards.models import Board
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
# from dateutil.relativedelta import relativedelta

# Create your views here.
#남녀 별 통계
#APIView 는 Class-based view(CBV)
class GenderStatistics(APIView):
    
    def get(self, request):
        male_total = User.objects.filter(gender='Male').count()
        female_total = User.objects.filter(gender='Female').count()
        user_gender_total = User.objects.count()
        return Response({'남자 회원 수': male_total, '여자 회원 수': female_total, '총 회원 수':user_gender_total})


#연령대 별 통계
class AgeStatistics(APIView):
    
    def get(self, request):
        age_statistics = {}
        year_now = datetime.now().year
        for i in range(1,11):
            #datetime은 month, date 필수로 입력해야함
            age_count = User.objects.filter(birth_date__range=[datetime(year_now-(i*10),1,1),datetime(year_now-(i-1)*10+1,1,1)]).count()
            if i == 1:
                age_statistics['10대 이하']=age_count
            else:
                age_statistics[f'{i-1}0대']=age_count
        return Response({'나이대 분포': age_statistics})


#이용시간 별 통계
# class LoginStatistics(APIView):
    
#     def get(self, request):
#         login_statistics={}
#         login_statistics['0~6']=User.objects.filter(last_login__hour__range=(0,7)).count()
#         login_statistics['7~12']=User.objects.filter(last_login__hour__range=(7,13)).count()
#         login_statistics['13~18']=User.objects.filter(last_login__hour__range=(13,19)).count()
#         login_statistics['19~24']=User.objects.filter(last_login__hour__range=(19,24)).count()
#         return Response({'로그인 시간 별 통계':login_statistics})


#게시판 남녀 통계
class BoardGenderStatistics(APIView):
    
    def get(self, request):
        male_board_total = Board.objects.filter(user__gender='Male').count()
        female_board_total = Board.objects.filter(user__gender='Female').count()
        return Response({'남자 작성 게시물 수': male_board_total, '여자 작성 게시물 수': female_board_total})


#게시판 나이대 통계
class BoardAgeStatistics(APIView):

    def get(self, request):
        age_statistics = {}
        year_now = datetime.now().year
        for i in range(1,11):
            
            age_count = Board.objects.select_related('user').filter(user__birth_date__range=[datetime(year_now-(i*10),1,1),datetime(year_now-(i-1)*10+1,1,1)]).count()
            if i == 1:
                age_statistics['10대 이하']=age_count
            else:
                age_statistics[f'{i-1}0대']=age_count
        return Response({'작성자 나이대 분포': age_statistics})