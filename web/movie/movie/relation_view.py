#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from toolkit.pre_load import neo_con
from django.http import JsonResponse
import os

import json

def search_entity(request):
	ctx = {"ssdd":"sdfsf"}
	#根据传入的实体名称搜索出关系
	if(request.GET):
		entity = request.GET['user_text']
		entity = "Tom Hanks"
		#连接数据库
		entityRelation = neo_con.matchItembyTitle(entity)
		# if len(entityRelation) == 0:
		# 	#若数据库中无法找到该实体，则返回数据库中无该实体
		# 	ctx= {'title' : '<h1>数据库中暂未添加该实体</h1>'}
		# 	return render(request,'entity.html',{'ctx':json.dumps(ctx,ensure_ascii=False)})
		# else:
			#返回查询结果
			#将查询结果按照"关系出现次数"的统计结果进行排序
			#entityRelation = sortDict(entityRelation)
		if(entityRelation):
		    return render(request,'entity.html',{'ctx':entityRelation})
		else:
		    return render(request,'entity.html',{'ctx':'hello'})

	return render(request,"entity.html",{'ctx':ctx})