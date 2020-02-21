

from notifications.email import send_email_template

def sendSSOToken(user):
    print(user)


def sendVerificationEmail(user, token):
    try:
        domain = os.environ.get('DOMAIN')
    except:
        print('environ not set...')
        return False
    link = 'https://%s/landing/verifyEmail/%s/id/%s/token/%s' % (domain, user.email, user.id, token)
    return send_email_template(user.email, 'Verifiser din e-postadresse', 'verifyemail', context={'link':link, 'email':user.email})
