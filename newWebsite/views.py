from django.shortcuts import render
from newWebsite.models import  *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
from datetime import datetime
import numpy as np
import os
import pickle
import pandas as pd
import networkx as nx
# Create your views here.

sid = SentimentIntensityAnalyzer()

def string_toDatetime(string):
    return datetime.strptime(string, "%Y-%m-%d")

def index(request):
    return render(request,'index.html')

def search_users(request):
	q = request.GET['search2']
	print (q)
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	users = pd.read_csv(os.path.join(BASE_DIR,'newWebsite','users.csv'))
	id_login = {}
	for i in range(len(users)):
		data = np.array(users.iloc[i])
		id_login[data[0]] = data[1]

	for m,n in id_login.items():
		if n==q:
			person = m
	person = list(id_login.keys())[list(id_login.values()).index(q)]
	# similarity in interests 

	edges = pd.read_csv(os.path.join(BASE_DIR,'newWebsite','user_language_network_edge.csv'))
	nodes = pd.read_csv(os.path.join(BASE_DIR,'newWebsite','user_language_network_node.csv'))
	languages = {}
	query_res = []

	N = {}
	for i in range(len(edges)):
		data = np.array(edges.iloc[i])
		N[data[1]] = N.get(data[1],0)+data[2]
		if data[0]==person:
			query_res.append(data[1])

	score_res = {}
	pre = 58
	score = 0
	for i in range(len(edges)):
		data = np.array(edges.iloc[i])	
		if data[0]==person: continue;
		
		if data[0]!=pre:
			score_res[pre] = score
			score = 0
			pre = data[0]

		if data[1] in query_res:
			languages[(data[0],data[1])] = languages.get((data[0],data[1]),0)+data[2]
			score += float(data[2])/N[data[1]]
	
	# similarity in status
	edges = pd.read_csv(os.path.join(BASE_DIR,'newWebsite','follower_network_edge.csv'))
	nodes = pd.read_csv(os.path.join(BASE_DIR,'newWebsite','follower_network_node.csv'))
	
	# G = nx.Graph()
	# for i in range(len(edges)):
	# 	data = np.array(edges.iloc[i])
	# 	G.add_edge(data[0],data[1])
	
	# pagerank = nx.pagerank(G,alpha=0.85)
	with open(os.path.join(BASE_DIR,'newWebsite','rank.pkl'),'rb') as f:
		pagerank = pickle.load(f)

	candidates = []
	scores = []
	for i,j in score_res.items():
		try:
			candidates.append(id_login[i])
			k = abs(pagerank[person]-pagerank[i])/max((pagerank[person],pagerank[i]))
			scores.append(round(j*k,5))
		except KeyError:continue;


	scores = np.array(scores)
	candidates = np.array(candidates)
	indexes = np.argsort(scores)[::-1]
	candidates = candidates[indexes]
	scores = scores[indexes]
	c = []
	for i in range(len(candidates)):
		if i > 10:
			break
		dic = {}
		dic['name'] = candidates[i]
		dic['score'] = scores[i]
		c.append(dic)

	context = dict()
	context.__setitem__('headers', ['candidates','scores'])
	context.__setitem__('rows', c)

	return render(request,'index.html',context)





