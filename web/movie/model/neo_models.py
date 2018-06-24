import sys
import os

from py2neo import Graph,Node,Relationship

class Neo4j():
    graph = None
    def __init__(self):
        print("create neo4j class ...")

    def connectDB(self):
        self.graph = Graph("http://127.0.0.1:7474", username="neo4j", password="123456")

    def getPersonInfoByTitle(self,value):
        db = self.graph
        answer = db.run('MATCH (p {name: "'+ value +'"}) RETURN p').data()
        return answer
    
    def getMovieInfoByTitle(self,value):
        db = self.graph
        answer = db.run('MATCH (m {title: "'+value+ '"}) RETURN m').data()
        return answer

    def getPersonRelationsByTitle(self,value):
        db = self.graph
        answer = db.run('MATCH (p:Person {name:"'+ value +'"})- [rel] -> (pm) RETURN p, Type(rel) as rel, pm').data()
        return answer

    def getMovieRelationsByTitle(self,value):
        db = self.graph
        answer = db.run('MATCH (m:Movie {title:"'+ value +'"})<- [rel] - (mp) RETURN m, Type(rel) as rel, mp').data()
        return answer

    def getPersonRecommendByTitle(self,value):
        db = self.graph
        answer = db.run('MATCH (bacon:Person {name:"'+value+'"})-[*1..2]-(prec) RETURN DISTINCT prec').data()
        return answer

    def getMovieRecommendByTitle(self,value):
        db = self.graph
        answer = db.run('MATCH (bacon:Movie {title:"'+value+'"})-[*1..2]-(mrec) RETURN DISTINCT mrec').data()
        return answer


"""

MATCH (p {name: "Tom Hanks"}) RETURN p

MATCH (p {title: "The Matrix"}) RETURN p

MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(tomHanksMovies) RETURN tom,tomHanksMovies


MATCH (cloudAtlas {title: "Cloud Atlas"})<-[:DIRECTED]-(directors) RETURN directors


MATCH (people:Person)-[relatedTo]-(:Movie {title: "Cloud Atlas"}) RETURN people, Type(relatedTo), relatedTo


MATCH p=shortestPath(
  (bacon:Person {name:"Kevin Bacon"})-[*]-(meg:Person {name:"Meg Ryan"})
)
RETURN p


MATCH (n1:Person {name:"Tom Hanks"})- [rel] -> (n2) RETURN n1, Type(rel),n2

MATCH (n1:Movie {title:"The Matrix"})<- [rel] - (n2) RETURN n1, Type(rel),n2

"""