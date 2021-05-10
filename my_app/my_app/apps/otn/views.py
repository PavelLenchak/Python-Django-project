import os
import time
from django.shortcuts import render
from django.http import HttpResponseRedirect
from docxtpl import DocxTemplate


def fill_words_template(request):
    path = os.path.dirname(__file__)
    word_templates_dir = '{}{}word templates'.format(path,os.sep)

    today = '{}{}saves{}{}'.format(path,os.sep,os.sep,time.strftime('%d_%m_%Y'))
    if not os.path.exists(today):
        os.mkdir(today)

    context = {}
    for key, value in dict(request.POST).items():
        context[key] = ''.join(value)
    print(context)

    template_name = '{}.docx'.format(context['template_name'])
    file_name = '{}.docx'.format(context['file_name'])

    doc = DocxTemplate(word_templates_dir + os.sep + template_name)
    doc.render(context)
    doc.save(today + os.sep + file_name)


def index(request):
    return render(request, 'otn/index.html')


def otn_letter_tube(request):
    if request.method == 'POST':
        fill_words_template(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'otn/otn_letter_tube.html')


def otn_letter_apparatus(request):
    if request.method == 'POST':
        fill_words_template(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'otn/otn_letter_apparatus.html')
