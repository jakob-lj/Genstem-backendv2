from genAuth.models import SSOCode
import datetime
from django.utils import timezone

def getCode(user):
    try:
        ssoCode = SSOCode.objects.get(user=user)
        twoDaysAgo = timezone.now() - datetime.timedelta(days=2)
        if ssoCode.date < twoDaysAgo:
            ssoCode.date = timezone.now()
            ssoCode.code = loginCode()
            ssoCode.save()
    except Exception as e:
        print(e)
        ssoCode = SSOCode.objects.create(user=user)
    return ssoCode.code