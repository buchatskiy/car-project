# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import MyForm
from models import Brand, Model


def cart(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        args['form'] = MyForm(request.POST)
        if request.POST['brand']:
            brand_id = int(request.POST['brand'])
        else:
            brand_id = 1
        selected_models = Model.objects.filter(brands=Brand.objects.get(id=brand_id))
        args['form'].fields['model'].queryset = selected_models
        if args['form'].is_valid():
            args['thanks'] = True
            args['model'] = Model.objects.get(pk=request.POST['model'])
            args['brand'] = Brand.objects.get(pk=request.POST['brand'])
            args['distance'] = request.POST['run']
            return render_to_response('base.html', args)
        return render_to_response('base.html', args)
    else:
        selected_models = Model.objects.filter(brands=Brand.objects.get(id=1))
        args['form'] = MyForm(initial={'brand': 1})
        args['form'].fields['model'].queryset = selected_models
        return render_to_response('base.html', args)