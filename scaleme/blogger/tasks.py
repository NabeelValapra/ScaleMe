from settings.celery import app
# from django.core.mail import EmailMessage

@app.task
def email_hello():
    print 'Email sending.'
    for a in range(1,10):
        print 'Email :' + str(a)
    # email = EmailMessage('This is sample subject.', 'This is sample messages.', ['nabeelvalapra@gmail.com'])
    # email.send()
    print 'Email send.'
