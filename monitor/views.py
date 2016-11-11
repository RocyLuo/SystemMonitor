import socket
from django.shortcuts import render
from .models import UserLog

host_name = socket.getfqdn(socket.gethostname())
host_ip = socket.gethostbyname(host_name)


def index(request):
    user_log_list = UserLog.objects.all()
    request.session['username'] = 'rocy'
    context = {
        'user_log_list': user_log_list,
        'session': request.session.session_key,
        'host_name': host_name,
        'host_ip': host_ip,
    }
    return render(request, 'monitor/index.html', context)