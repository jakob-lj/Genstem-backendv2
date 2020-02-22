
import requests
import json
import os

try:
	domain = os.environ.get('MAILGUN_DOMAIN_NAME')
except:
	domain = "mg.genstem.jakoblj.com"
fAdress = "Genstem Login <support@mg.genstem.jakoblj.com>"

def send_email(to, subject, body=""):
	if os.environ.get('MAILGUN_API_KEY'):
		return requests.post(
			"https://api.eu.mailgun.net/v3/"+ domain + "/messages",
			auth=("api", os.environ.get('MAILGUN_API_KEY')),
			data={
				"from": fAdress,
				"to": [to],
				"subject": subject,
				"text": body})
	else:
		print({'to':to, 'subject':subject, 'text':body})
		return True


def send_email_template(to, subject, template, context):
	if os.environ.get('MAILGUN_API_KEY'):
		args = json.dumps(context)
		return requests.post(
			"https://api.eu.mailgun.net/v3/" + domain + "/messages",
			auth=("api", os.environ.get('MAILGUN_API_KEY')),
			files=[("inline", open('assets/files/logo.png', 'rb'))],
			data={"from": fAdress,
				"to": to,
				"subject": subject,
				"template": template,
				"h:X-Mailgun-Variables": args})
	else:
		print('Suppost to send %s to %s' % (template, to))
		print('context')
		print(context)


def send_inline_image():
    # return requests.post(
    #     "https://api.eu.mailgun.net/v3/" + domain + "/messages",
    #     auth=("api", "key"),
    #     files=[("inline", open("assets/files/logo.png", 'rb'))],
    #     data={"from": fAdress,
    #           "to": "jakob@owe-it.com",
    #           "subject": "Inline image",
    #           "text": "Testing some Mailgun awesomness!",
    #           "html": '<html>Inline image here: <img src="cid:logo.png"></html>'})
	return False

def send_inline_image_in_template():
	# return requests.post(
	# 	"https://api.eu.mailgun.net/v3/" + domain + "/messages",
	# 	auth=("api", "key"),
	# 	files=[("inline", open('assets/files/logo.png', 'rb'))],
	# 	data={"from": fAdress,
	# 		"to": "Jakob Lund Johannessen <jakob98.lj@gmail.com>",
	# 		"subject": "Hello Jakob Lund Johannessen",
	# 		"template": "fortgottpassword",
	# 		"h:X-Mailgun-Variables": '{"link": "owe-it.com"}'})
	return False