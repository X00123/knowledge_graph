#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from toolkit.pre_load import neo_con
from django.http import JsonResponse
import os

import json

def recommend_entity(request):
	if(request.GET):
		
		entity = request.GET['user_text']
		entityRelation1 = neo_con.getPersonRecommendByTitle(entity)
		entityRelation2 = neo_con.getMovieRecommendByTitle(entity)

		entityRelation = entityRelation1 + entityRelation2
		
		if (len(entityRelation) > 0):
			ctx= {'code' : 0,  'title':entity, 'result' : json.dumps(entityRelation,ensure_ascii=False) }
			return render(request,'recommend.html',{'ctx':ctx})
	
		else: 
			ctx= {'code' : 400, 'title':entity, 'result' : '<h1>数据库中暂未添加该实体'+ entity +'</h1>' }
			return render(request,'recommend.html',{'ctx':ctx})


	return render(request,"recommend.html",{})