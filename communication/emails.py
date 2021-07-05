# due to cyclic import

from django.conf import settings

from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
from sendgrid import SendGridAPIClient

SENDGRID_API_KEY="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"

def send_mail(to,subject,content):
    message = Mail(
        from_email='gmakara@bismart.co.ke',
        to_emails=to,
        subject=subject,
        html_content=content)
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
        # login unsent emails
