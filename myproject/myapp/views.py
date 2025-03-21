from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os
import datetime
import subprocess

def htop_view(request):
    full_name = "pragati"
    username = os.getenv("USER") or os.getenv("pragatirajput07")
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = subprocess.getoutput('top -bn1')

    response = f"""
    Name: {full_name}<br>
    Username: {username}<br>
    Server Time (IST): {server_time}<br><br>
    TOP output:<br>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response, content_type="text/html")
