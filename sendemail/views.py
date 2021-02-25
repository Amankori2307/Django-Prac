from django.shortcuts import render
from rest_framework import views 
from django.core.mail import send_mail, send_mass_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from django.conf import settings
    

def mailTemplate(name):
    html_message = '''
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Coding Specials - Welcome</title>
        <style>
            *{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Courier New', Courier, monospace;
            }
            header{
                width: 100%;
                display: flex;
                align-items: center;
                padding: 0px 15px 20px;

            }
            .logo{
                width: 50px;
                height: 50px;     
                border-radius: 32px;
                overflow: hidden;
                margin-right: 10px;
            }
            .logo img{
                object-fit: cover;
                width: 100%;
                height: 100%;
            }
            .message{
                margin-top: 10px;
            }
            .message p{
                padding:5px 15px;
            }

        </style>
    </head>
    <body>
        <header>
            <div class="logo">
                <img src="https://blogsmedia.lse.ac.uk/blogs.dir/9/files/2019/07/code.jpg" alt="logo">
            </div>
            <h2 class="brand-name">Coding Specials</h2>
        </header>
        <main>
            <section class="message">
                <p>Hi <b>Aman Kori</b>,</p>
                <p>Greetings from <b>Coding Specials</b>!</p>
                <p>We are glad see that you have subscribed to our <b>Golden</b> plan.</p>

            </section>
            </p>
        </main>
    </body>
    </html>
    '''
    return html_message

class SendEmail(views.APIView):
    
    def post(self, request):
        reqData = request.data

        html_message = mailTemplate("Aman Kori")
        message = reqData["message"]
        subject = reqData["subject"]
        recipient_list = reqData["recipient_list"]
        from_email = settings.EMAIL_HOST_USER 
        send_mail(message=message, recipient_list=recipient_list, from_email=from_email, subject=subject, html_message=html_message)

        return Response({
            "message": "Sent Successfully"
        }, status=status.HTTP_200_OK)