from django.shortcuts import render, redirect
import smtplib
from email.mime.text import MIMEText
from aniverse import emailp
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


def home(request):
    return render(request, 'aniverse/home.html')

def send_mail(request):
    if request.method == 'POST':
        sender = "appfk92@gmail.com"
        email_password = emailp.password
        email = request.POST.get('email', '')

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        
        try:
            with open("aniverse/new-email.html", 'r', encoding='utf-8') as file:
                template = file.read()
        except IOError as ex:
            return render(request, 'aniverse/home.html', {'error_message': ex})

        try:
            server.login(sender, email_password)
            msg = MIMEText(template, "html", 'utf-8')
            msg["FROM"] = sender
            msg["TO"] = email
            msg["Subject"] = "Курс по рисованию в стиле Аниме!"
            server.sendmail(sender, email, msg.as_string())

            print("The message was sent successfully")
        except Exception as _ex:
            print(f"{_ex}\nCheck your login or password please!")
        return redirect('home')