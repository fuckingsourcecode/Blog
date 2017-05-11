#-*- coding: UTF-8 -*-  
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django import forms
import json
from django.contrib.auth.models import User
from .models import Message 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.
class CreateForm(forms.Form):
	"""docstring for CreateForm"""
	username = forms.CharField(label='用户名', widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), required=True)
	content = forms.CharField(label='内容', widget=forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': 3, 'style': 'width:98%;resize:none;'}),required=True)

@login_required
def create_message(request):
	error = []
	messages = Message.objects.filter(acceptor=User.objects.get(username=request.session.get('username'))) | Message.objects.filter(sender=User.objects.get(username=request.session.get('username')))
	messages = messages.order_by('-pub_date')
	num = (Message.objects.filter(pub_date__gte=json.loads(request.session.get('last_login')))).count()
	if request.method == 'POST':
		print request.POST
		form = CreateForm(request.POST)
		if form.is_valid():
			acceptor = form.cleaned_data['username']
			content = form.cleaned_data['content']
			try:
				user = User.objects.get(username=acceptor)
			
				print 'hello'
				message = Message.objects.create(
					sender=User.objects.get(username=User.objects.get(username=request.session.get('username'))), acceptor=User.objects.get(username=acceptor), content=content)
				message.save()
				return HttpResponseRedirect('/message')
			except User.DoesNotExist:
				error.append('用户不存在')
	else:
		form = CreateForm()
	return render(request, 'message/message.html', {'form': form, 'error':error, 'messages': messages, 'num': num})