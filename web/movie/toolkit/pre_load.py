# -*- coding: utf-8 -*-
import csv
import sys
import os

sys.path.append("..")

from model.neo_models import Neo4j 

neo_con = Neo4j()   #预加载neo4j
neo_con.get_db()
print('neo4j connected!')