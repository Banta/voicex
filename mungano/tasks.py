from celery.decorators import task
from transport.voicex import VoiceXTransport
from transport import config
import time

@task(name='mungano.tasks.delayed_sms')
def delayed_sms(obj, phone_num, msg, delay):
	print "inside tasks"
	time.sleep(delay * 60)
	obj.sms(phone_num, msg)
