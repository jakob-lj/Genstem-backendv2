from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from genAuth.models import User, UserVerificationToken
from genAuth.notifications import sendSSOToken, sendVerificationEmail
from security.errorHandling import verbosedFeedback
import datetime

# Create your views here.
class SSOLogin(APIView):

    def get(self, request):
        return Response(200)

    def post(self, request):
        try:
            email = request.data['email'] 
            user = User.objects.get(email=email) # user exists
        except KeyError as e:
            return Response({'ok':False, 'err':'MISSING_EMAIL', 'verbosed':verbosedFeedback(e)}, status=400)

        except ObjectDoesNotExist: # user does not exist   
            return Response({'ok':False, 'err':'NOT_A_USER'}, status=400)
        except:
            print('none')
            return Response()
        # if no exceptions

        
        sendSSOToken(user)
        return Response({'ok':True}, status=200)
    
class CreateUser(APIView):
    def post(self, request):
        try:
            name = request.data['name']
            email = request.data['email']
            User.objects.get(email=email) # test to see if user exists
            return Response({'ok':False, 'err':'USER_ALREADY_EXISTS'}, status=400)
        except KeyError as e:
            return Response({'ok':False, 'err':'MISSING_INFO', 'verbose':verbosedFeedback(e)}, status=400)
        except ObjectDoesNotExist: # create new user here
            user = User.objects.create(name=name, email=email)
            sendSSOToken(user)
            try:
                tokenObj = UserVerificationToken.objects.get(user=user)
            except ObjectDoesNotExist:
                tokenObj = UserVerificationToken.objects.create(user=user)
            token = tokenObj.token
            sendVerificationEmail(user, token)
            return Response({'ok':True}, status=200)


class VerifyUser(APIView):

    def get(self, request):
        return Response(status=200)

    def put(self, request):
        try:
            token = request.data['token']
            email = request.data['email']
            id = request.data['id']
            user = User.objects.get(email=email, id=id)
        except KeyError as e:
            return Response({'ok':False, 'err':'MISSING_INFO', 'verbosed':verbosedFeedback(e)}, status=400)
        except ObjectDoesNotExist:
            return Response({'ok':False, 'err':'USER_NOT_FOUND'}, status=400)
        try:
            today = datetime.date.today()
            twoDaysAgo = today - datetime.timedelta(days=2)
            uvf = UserVerificationToken.objects.get(user = user, token=token, date__gte=twoDaysAgo)
            uvf.delete()
        except Exception as e:
            print(e)
            return Response({'ok':False, 'err':'TOKEN_EXPIRED', 'verbosed':'token is either expired or does not exist'}, status=400)
        
        user.verified = True
        user.dummy = False
        user.save()
        return Response({'ok':True}, status=200)