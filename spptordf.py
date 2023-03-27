import csv
from rdflib import Graph


authormap={"L. Kröger":{},"M. Foucher":{}}
projectmap={"SPP-Im Netzwerk fluvialer Häfen":"https://gepris.dfg.de/gepris/projekt/198801704","Binnenhäfen/Inland harbours":"https://gepris.dfg.de/gepris/projekt/219647198"}
countries={"Turkey":"http://www.wikidata.org/entity/Q43","Armenia":"http://www.wikidata.org/entity/Q399","Austria":"http://www.wikidata.org/entity/Q40","Bosnia and Herzegovina":"http://www.wikidata.org/entity/Q225","Britain, England":"http://www.wikidata.org/entity/Q21","Britain, Northern Ireland":"http://www.wikidata.org/entity/Q26","Britain, Scotland":"http://www.wikidata.org/entity/Q22","Britain, Wales":"http://www.wikidata.org/entity/Q25","Bulgaria":"http://www.wikidata.org/entity/Q219","Croatia":"http://www.wikidata.org/entity/Q224","Czech Republic":"http://www.wikidata.org/entity/Q213","Denmark":"http://www.wikidata.org/entity/Q35","Estonia":"http://www.wikidata.org/entity/Q191","Finland":"http://www.wikidata.org/entity/Q33","France":"http://www.wikidata.org/entity/Q142","Greece":"http://www.wikidata.org/entity/Q41","Hungary":"http://www.wikidata.org/entity/Q28","Italy":"http://www.wikidata.org/entity/Q38","Latvia":"http://www.wikidata.org/entity/Q211","Lithuania":"http://www.wikidata.org/entity/Q37","Netherlands":"http://www.wikidata.org/entity/Q55","Norway":"http://www.wikidata.org/entity/Q20","Poland":"http://www.wikidata.org/entity/Q36","Portugal":"http://www.wikidata.org/entity/Q45","Romania":"http://www.wikidata.org/entity/Q218","Serbia":"http://www.wikidata.org/entity/Q403","Russia":"http://www.wikidata.org/entity/Q159","Slovenia":"http://www.wikidata.org/entity/Q215","Spain":"http://www.wikidata.org/entity/Q29","Ireland":"http://www.wikidata.org/entity/Q27","Sweden":"http://www.wikidata.org/entity/Q34","Belgium":"http://www.wikidata.org/entity/Q31","Germany":"http://www.wikidata.org/entity/Q183","Ukraine":"http://www.wikidata.org/entity/Q212","Switzerland":"http://www.wikidata.org/entity/Q39"}
bodyofwater={"Ems":"http://www.wikidata.org/entity/Q1648","Lough Owel":"http://www.wikidata.org/entity/Q2702889","River Quoile":"http://www.wikidata.org/entity/Q3332405","Lac de Chalain":"http://www.wikidata.org/entity/Q1799622","Saône":"http://www.wikidata.org/entity/Q187834","Kilbirnie Loch":"http://www.wikidata.org/entity/Q6406556","Loch Arthur":"http://www.wikidata.org/entity/Q24657046","River Tay":"http://www.wikidata.org/entity/Q19719", "Mosel":"http://www.wikidata.org/entity/Q1667","Lago Trasimeno":"http://www.wikidata.org/entity/Q188487","Bacchiglione":"http://www.wikidata.org/entity/Q1242186","Jezioro Mausz":"http://www.wikidata.org/entity/Q4745402","Jezioro Lednickie":"http://www.wikidata.org/entity/Q6512708","Wolchow":"http://www.wikidata.org/entity/Q15243","Loch Kinord":"http://www.wikidata.org/entity/Q6664930", "Loch Laggan":"http://www.wikidata.org/entity/Q6664933", "Neckar":"http://www.wikidata.org/entity/Q1673", "Chiemsee":"http://www.wikidata.org/entity/Q4138", "Charente":"http://www.wikidata.org/entity/Q123362", "Lippe":"http://www.wikidata.org/entity/Q153945", "Starnberger See":"http://www.wikidata.org/entity/Q131615", "Steinhuder Meer":"http://www.wikidata.org/entity/Q165782", "River Moy":"http://www.wikidata.org/entity/Q1149711", "Lago di Bientina":"http://www.wikidata.org/entity/Q3825910", "Lago di Monate":"http://www.wikidata.org/entity/Q2259119", "Mersey":"http://www.wikidata.org/entity/Q19724","Lough Oughter":"http://www.wikidata.org/entity/Q3756406", "Ziese":"http://www.wikidata.org/entity/Q199218", "Lough Derravaragh":"http://www.wikidata.org/entity/Q1586768", "Zugersee":"http://www.wikidata.org/entity/Q14436", "Ägerisee":"http://www.wikidata.org/entity/Q14507", "Federsee":"http://www.wikidata.org/entity/Q248234", "Haine":"http://www.wikidata.org/entity/Q1569447", "Vorskla":"http://www.wikidata.org/entity/Q844041","River Foyle":"http://www.wikidata.org/entity/Q958530", "River Trent":"http://www.wikidata.org/entity/Q19714", "Seine":"http://www.wikidata.org/entity/Q1471","Brivet":"http://www.wikidata.org/entity/Q178081", "River Clyde":"http://www.wikidata.org/entity/Q19721", "River Thames":"http://www.wikidata.org/entity/Q19686", "Ljubljanica":"http://www.wikidata.org/entity/Q339990","Mlosina":"http://www.wikidata.org/entity/Q11142243", "Amstel":"http://www.wikidata.org/entity/Q185405", "Elblag":"http://www.wikidata.org/entity/Q32750600", "North Sea":"http://www.wikidata.org/entity/Q1693", "Ijssel":"http://www.wikidata.org/entity/Q217818", "Dnjepr":"http://www.wikidata.org/entity/Q40855","Elbe":"http://www.wikidata.org/entity/Q1644", "Styr":"http://www.wikidata.org/entity/Q1136609", "Strupino":"http://www.wikidata.org/entity/Q9347030", "Warta":"http://www.wikidata.org/entity/Q201823", "Omulew":"http://www.wikidata.org/entity/Q2023557","Oder":"http://www.wikidata.org/entity/Q552", "Arve":"http://www.wikidata.org/entity/Q633819", "Lake Constance":"http://www.wikidata.org/entity/Q4127", "Bieler See":"http://www.wikidata.org/entity/Q14429", "Lough Neagh":"http://www.wikidata.org/entity/Q206942", "Lough Gara":"http://www.wikidata.org/entity/Q6686123", "Desna":"http://www.wikidata.org/entity/Q202796", "Oka":"http://www.wikidata.org/entity/Q172089", "Main":"http://www.wikidata.org/entity/Q1670", "Lough Allen":"http://www.wikidata.org/entity/Q1366974", "Lough Cullin":"http://www.wikidata.org/entity/Q3776431", "Waal":"http://www.wikidata.org/entity/Q216171", "Baltic Sea":"http://www.wikidata.org/entity/Q545", "Loch Doon":"http://www.wikidata.org/entity/Q1547670", "Lough Ennell":"http://www.wikidata.org/entity/Q2639357","Loire":"http://www.wikidata.org/entity/Q1469","Lough Gara":"http://www.wikidata.org/entity/Q6686123", "Breedogue River":"http://www.wikidata.org/entity/Q32535533","Loch Glashan":"http://www.wikidata.org/entity/Q3776179", "Lough Beg":"http://www.wikidata.org/entity/Q24196547", "Lough Rea":"http://www.wikidata.org/entity/Q24196547", "Weser":"http://www.wikidata.org/entity/Q1650","Spree":"http://www.wikidata.org/entity/Q1684","Mediterranean Sea":"http://www.wikidata.org/entity/Q4918","Brenta":"http://www.wikidata.org/entity/Q214551","Nidelva":"http://www.wikidata.org/entity/Q499668","Oude Rijn":"http://www.wikidata.org/entity/Q1345836", "Adda":"http://www.wikidata.org/entity/Q63109","Arno":"http://www.wikidata.org/entity/Q115457","Lago di Fimon":"http://www.wikidata.org/entity/Q3825951","Ijsselmeer":"http://www.wikidata.org/entity/Q4121", "Rotte":"http://www.wikidata.org/entity/Q674294","Maas":"http://www.wikidata.org/entity/Q41986", "Rhine":"http://www.wikidata.org/entity/Q584", "Vecht":"http://www.wikidata.org/entity/Q168904","Weichsel":"http://www.wikidata.org/entity/Q548","Derwitzer See":"http://www.wikidata.org/entity/Q317486", "Genfer See":"http://www.wikidata.org/entity/Q6403","Murtensee":"http://www.wikidata.org/entity/Q14448","Danube":"http://www.wikidata.org/entity/Q1653","Don":"http://www.wikidata.org/entity/Q1229"}


ns="http://data.archaeology.link/data/spphaefen/"
nsont="http://www.spp-haefen.de/ont#"
triples=set()
triples.add("<http://www.opengis.net/ont/geosparql#Feature> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.opengis.net/ont/geosparql#SpatialObject> .\n")
triples.add("<http://www.opengis.net/ont/geosparql#Geometry> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.opengis.net/ont/geosparql#SpatialObject> .\n")
triples.add("<http://www.opengis.net/ont/geosparql#hasGeometry> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#ObjectProperty> .\n")
triples.add("<http://www.opengis.net/ont/geosparql#asWKT> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#DatatypeProperty> .\n")
triples.add("<http://www.opengis.net/ont/sf#Point> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.opengis.net/ont/geosparql#Geometry> .\n")
triples.add("<"+str(nsont)+"Harbour> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.opengis.net/ont/geosparql#Feature> .\n")
triples.add("<http://www.wikidata.org/prop/direct/P206> <http://www.w3.org/2000/01/rdf-schema#label> \"located in or next to body of water\"@en .\n")
triples.add("<http://www.wikidata.org/prop/direct/P17> <http://www.w3.org/2000/01/rdf-schema#label> \"country\"@en .\n")
with open('source/HarbourDataRepository_001_Kroeger_2018.csv', newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        cururi=ns+row["ID_place"]
        #print(cururi)
        triples.add("<"+str(cururi)+"> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <"+str(nsont)+"Harbour> .\n")
        triples.add("<"+str(cururi)+"> <http://www.opengis.net/ont/geosparql#hasGeometry> <"+str(cururi)+"_geom> .\n")
        triples.add("<"+str(cururi)+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Name_mod"]).replace("\"","'")+"\"@en .\n")
        if row["Hydro_name_mod"] in bodyofwater:
            triples.add("<"+str(cururi)+"> <http://www.wikidata.org/prop/direct/P206> <"+bodyofwater[str(row["Hydro_name_mod"])]+"> .\n <"+bodyofwater[str(row["Hydro_name_mod"])]+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Hydro_name_mod"])+"\"@en .\n")
        else:
            triples.add("<"+str(cururi)+"> <http://www.wikidata.org/prop/direct/P206> \""+str(row["Hydro_name_mod"]).replace("\"","'")+"\"^^<http://www.w3.org/2001/XMLSchema#string> .\n")
            if str(row["Hydro_name_mod"])!="Unknown":
                print(str(row["Hydro_name_mod"]))
        triples.add("<"+str(cururi)+"> <"+str(nsont)+"locationSecure> \""+str(row["Locat_secure"]).replace("\"","'")+"\"^^<http://www.w3.org/2001/XMLSchema#string> .\n")
        if row["Project"] in projectmap:
           triples.add("<"+str(cururi)+"> <http://purl.org/cerif/frapo/isOutputOf> <"+projectmap[str(row["Project"])]+"> .\n <"+projectmap[str(row["Project"])]+"> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.org/cerif/frapo/Project> .\n <"+projectmap[str(row["Project"])]+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Project"])+"\"@en .\n")
        else:
           triples.add("<"+str(cururi)+"> <http://purl.org/cerif/frapo/isOutputOf> \""+str(row["Project"])+"\"^^<http://www.w3.org/2001/XMLSchema#string> .\n")
        if row["Country"] in countries:
            triples.add("<"+str(cururi)+"> <http://www.wikidata.org/prop/direct/P17> <"+countries[str(row["Country"])]+"> .\n <"+countries[str(row["Country"])]+"> <http://www.w3.org/2000/01/rdf-schema#label> \""+str(row["Country"])+"\"@en .\n")
        else:
            triples.add("<"+str(cururi)+"> <http://www.wikidata.org/prop/direct/P17> \""+str(row["Country"])+"\"^^<http://www.w3.org/2001/XMLSchema#string> .\n")
        if "Date_min" in row and row["Date_min"].strip()!="":
            triples.add("<"+str(cururi)+"> <"+str(nsont)+"date_min> \""+str(row["Date_min"])+"\"^^<http://www.w3.org/2001/XMLSchema#string> .\n")
        if "Date_max" in row and row["Date_max"].strip()!="":
            triples.add("<"+str(cururi)+"> <"+str(nsont)+"date_max> \""+str(row["Date_max"])+"\"^^<http://www.w3.org/2001/XMLSchema#string> .\n")
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
