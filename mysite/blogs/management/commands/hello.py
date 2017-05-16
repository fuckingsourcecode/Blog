# -*- coding: utf-8 -*-
# @Author: fuckingsourcecode
# @Date:   2017-05-12 13:31:41
# @Last Modified by:   fuckingsourcecode
# @Last Modified time: 2017-05-12 13:40:11
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
	"""docstring for Command"""
	def handle(self, *args, **options):
		print "hello world"
		self.stdout.write(self.style.SUCCESS('Successfully print'))
