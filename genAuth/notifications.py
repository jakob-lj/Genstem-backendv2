
import os
from notifications.email import send_email_template

def sendSSOToken(user, code):
    code = str(code)
    code = code[:3] + ' ' + code[3:]
    return send_email_template(user.email, 'Engangskode', 'ssologin', context={'email':user.email, 'code':code})



def sendVerificationEmail(user, token):
    try:
        domain = os.environ.get('DOMAIN')
    except:
        print('environ not set...')
        return False
    link = 'https://%s/landing/verifyEmail/%s/id/%s/token/%s' % (domain, user.email, user.id, token)
    return send_email_template(user.email, 'Verifiser din e-postadresse', 'verifyemail', context={'link':link, 'email':user.email})
