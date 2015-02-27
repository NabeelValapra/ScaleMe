from settings.celery import app
from django.core.mail import send_mail

@app.task
def email_hello():
    # print 'Email sending.'
    # for a in range(1,10):
    #     print 'Email :' + str(a)
    try:
        send_mail('This is sample subject.', 'This is sample messages.', 'pymailone@gmail.com', ['nabeelvalapra@gmail.com'])
        print 'Email send.'
    except Exception, e:
        print 'Email sending failed.'
        print str(e)

