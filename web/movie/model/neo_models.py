# -*- coding: utf-8 -*-
import sys
import os
from json import dumps

from neo4j.v1 import GraphDatabase, basic_auth

class Neo4j():
    graph = None

    def get_db(self):
        driver = GraphDatabase.driver('bolt://localhost:7687/',auth=basic_auth("neo4j", "123456"))
        self.graph = driver.session()
    
    def serialize_movie(self, movie):
        return {
            'id': movie['id'],
            'title': movie['title'],
            'summary': movie['summary'],
            'released': movie['released'],
            'duration': movie['duration'],
            'rated': movie['rated'],
            'tagline': movie['tagline']
        }

    def serialize_cast(self, cast):
        return {
            'name': cast[0],
            'job': cast[1],
            'role': cast[2]
        }

    def get_search(self, q):
        results = self.graph.run("MATCH (movie:Movie) "
                 "WHERE movie.title =~ {title} "
                 "RETURN movie", {"title": "(?i).*" + q + ".*"}
        )
        return dumps([self.serialize_movie(record['movie']) for record in results])


