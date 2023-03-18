import csv


authormap={"L. Kröger":{},"M. Foucher":{}}
projectmap={"SPP-Im Netzwerk fluvialer Häfen":"https://gepris.dfg.de/gepris/projekt/198801704","Binnenhäfen/Inland harbours":"https://gepris.dfg.de/gepris/projekt/219647198"}
countries={"Turkey":"http://www.wikidata.org/entity/Q43","Armenia":"http://www.wikidata.org/entity/Q399","Austria":"http://www.wikidata.org/entity/Q40","Bosnia and Herzegovina":"http://www.wikidata.org/entity/Q225","Britain, England":"http://www.wikidata.org/entity/Q21","Britain, Northern Ireland":"http://www.wikidata.org/entity/Q26","Britain, Scotland":"http://www.wikidata.org/entity/Q22","Britain, Wales":"http://www.wikidata.org/entity/Q25","Bulgaria":"http://www.wikidata.org/entity/Q219","Croatia":"http://www.wikidata.org/entity/Q224","Czech Republic":"http://www.wikidata.org/entity/Q213","Denmark":"http://www.wikidata.org/entity/Q35","Estonia":"http://www.wikidata.org/entity/Q191","Finland":"http://www.wikidata.org/entity/Q33","France":"http://www.wikidata.org/entity/Q142","Greece":"http://www.wikidata.org/entity/Q41","Hungary":"http://www.wikidata.org/entity/Q28","Italy":"http://www.wikidata.org/entity/Q38","Latvia":"http://www.wikidata.org/entity/Q211","Lithuania":"http://www.wikidata.org/entity/Q37","Netherlands":"http://www.wikidata.org/entity/Q55","Norway":"http://www.wikidata.org/entity/Q20","Poland":"http://www.wikidata.org/entity/Q36","Portugal":"http://www.wikidata.org/entity/Q45","Romania":"http://www.wikidata.org/entity/Q218","Serbia":"http://www.wikidata.org/entity/Q403","Russia":"http://www.wikidata.org/entity/Q159","Slovenia":"http://www.wikidata.org/entity/Q215","Spain":"http://www.wikidata.org/entity/Q29","Ireland":"http://www.wikidata.org/entity/Q27","Sweden":"http://www.wikidata.org/entity/Q34","Belgium":"http://www.wikidata.org/entity/Q31","Germany":"http://www.wikidata.org/entity/Q183","Ukraine":"http://www.wikidata.org/entity/Q212","Switzerland":"http://www.wikidata.org/entity/Q39"}

ns="http://www.spp-haefen.de/data/"
nsont="http://www.spp-haefen.de/ont#"
triples=set()
triples.add("<http://www.opengis.net/ont/geosparql#Feature> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.opengis.net/ont/geosparql#SpatialObject> .\n")
triples.add("<http://www.opengis.net/ont/geosparql#Geometry> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.opengis.net/ont/geosparql#SpatialObject> .\n")
triples.add("<http://www.opengis.net/ont/geosparql#hasGeometry> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#ObjectProperty> .\n")
triples.add("<http://www.opengis.net/ont/geosparql#asWKT> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#DatatypeProperty> .\n")
triples.add("<http://www.opengis.net/ont/sf#Point> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.opengis.net/ont/geosparql#Geometry> .\n")
triples.add("<"+str(nsont)+"Harbour> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.opengis.net/ont/geosparql#Feature> .\n")
with open('source/HarbourDataRepository_001_Kroeger_2018.csv', newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        cururi=ns+row["ID_place"]
        #print(cururi)
        triples.add("<"+str(cururi)+"> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <"+str(nsont)+"Harbour> .\n")
        triples.add("<"+str(cururi)+"> <http://www.opengis.net/ont/geosparql#hasGeometry> <"+str(cururi)+"_geom> .\n")
        triples.add("<"+str(cururi)+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Name_mod"]).replace("\"","'")+"\"@en .\n")
        if row["Project"] in projectmap:
            triples.add("<"+str(cururi)+"> <http://purl.org/cerif/frapo/isOutputOf> <"+projectmap[str(row["Project"])]+"> .\n <"+projectmap[str(row["Project"])]+"> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.org/cerif/frapo/Project> .\n <"+projectmap[str(row["Project"])]+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Project"])+"\"@en .\n")
        else:
           triples.add("<"+str(cururi)+"> <http://purl.org/cerif/frapo/isOutputOf> \""+str(row["Project"])+"\"^^<http://www.w3.org/2001/XMLSchema#string> .\n")
           print(str(row["Project"]))
        if row["Country"] in countries:
            triples.add("<"+str(cururi)+"> <"+str(nsont)+"country> <"+countries[str(row["Country"])]+"> .\n <"+countries[str(row["Country"])]+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Country"])+"\"@en .\n")
        else:
            triples.add("<"+str(cururi)+"> <"+str(nsont)+"country> \""+str(row["Country"])+"\"^^<http://www.w3.org/2001/XMLSchema#string> .\n")
        if "Date_min" in row and row["Date_min"].strip()!="":
            triples.add("<"+str(cururi)+"> <"+str(nsont)+"date_min> \""+str(row["Date_min"])+"\"^^<http://www.w3.org/2001/XMLSchema#gYear> .\n")
        if "Date_max" in row and row["Date_max"].strip()!="":
            triples.add("<"+str(cururi)+"> <"+str(nsont)+"date_max> \""+str(row["Date_max"])+"\"^^<http://www.w3.org/2001/XMLSchema#gYear> .\n")
        if "Locat_precision" in row and row["Locat_precision"].strip()!="":
            triples.add("<"+str(cururi)+"> <"+str(nsont)+"precision> <"+str(nsont)+str(row["Locat_precision"])+"> .\n")
        triples.add("<"+str(cururi)+"_geom> <http://www.opengis.net/ont/geosparql#asWKT> \"POINT("+row["Longitude"]+" "+row["Latitude"]+")\"^^<http://www.opengis.net/ont/geosparql#wktLiteral> .\n")
        triples.add("<"+str(cururi)+"_geom> <http://www.w3.org/2000/01/rdf-schema#label> \"\"\""+str(row["Name_mod"]).replace("\"","'")+" Geometry\"\"\"@en .\n")
        triples.add("<"+str(cururi)+"_geom> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.opengis.net/ont/sf#Point> .\n")
        if "Comments" in row and row["Comments"]!="":
            triples.add("<"+str(cururi)+"> <http://www.w3.org/2000/01/rdf-schema#comment> \"\"\""+row["Comments"].replace("\"","'")+"\"\"\"@en .\n")
        if "Ref_mod" in row and row["Ref_mod"]!="":
            refs= row["Ref_mod"].split(";")
            triples.add("<"+str(cururi)+"> <http://www.w3.org/2004/02/skos/core#note> \"\"\""+row["Ref_mod"]+"\"\"\" .\n")

with open("spp_result.ttl","w",encoding="utf-8") as resfile:
    resfile.write("".join(triples))
    resfile.close()
