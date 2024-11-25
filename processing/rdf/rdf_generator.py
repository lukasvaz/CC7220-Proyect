# recomendacion  usar rdflib para generar el rdf     
import csv
import json
import ast
rdf_schema = """
@base <http://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://www.example.org/ontology#> .

ex:Profesor rdf:type rdfs:Class; rdf:subClassOf ex:Person.
ex:Cargo rdf:type rdfs:Class .
ex:Grado rdf:type rdfs:Class .
ex:Departamento rdf:type rdfs:Class .
ex:Curso rdf:type rdfs:Class .
ex:Universidad rdf:type rdfs:Class .
ex:Estudio rdf:type rdfs:Class .

#Propiedades
#profesor
ex:departamento rdf:type rdf:Property ;
    rdfs:domain ex:Profesor ;
    rdfs:range ex:Departamento .

ex:cargo rdf:type rdf:Property ;
    rdfs:domain ex:Profesor ;
    rdfs:range ex:Cargo .

ex:estudio rdf:type rdf:Property ;
    rdfs:domain ex:Profesor ;
    rdfs:range ex:Estudio .

#Estudio
ex:fecha rdf:type rdf:Property ;
    rdfs:domain ex:Estudio ;
    rdfs:range xsd:date .

ex:institucion rdf:type rdf:Property ;
    rdfs:domain ex:Estudio ;
    rdfs:range ex:Universidad .

ex:grado rdf:type rdf:Property ;
    rdfs:domain ex:Estudio ;
    rdfs:range ex:Grado .

#Curso
ex:departamento rdf:type rdf:Property ;
    rdfs:domain ex:Curso ;
    rdfs:range ex:Departamento .
ex:impartidoPor rdf:type rdf:Property ;
    rdfs:domain ex:Curso ;
    rdfs:range ex:Profesor .

ex:poseeRequisitos rdf:type rdf:Property ;
    rdfs:domain ex:Curso ;
    rdfs:range ex:Curso .
"""

with open("./rdf/rdf_generator.ttl", "w") as ttl_file:
    ttl_file.write(rdf_schema)
    with open("./cleaning/profesores_formateados.csv", "r") as professors_csv:
        professors = csv.DictReader(professors_csv)
        for professor in professors:
            if professor['Nombre']:ttl_file.write(f"ex:{professor['Nombre']} rdf:type ex:Profesor ;\n")
            if professor['Codigo']:ttl_file.write(f"    ex:departamento ex:{professor['Codigo']} ;\n")
            if professor['Grados']:
                for grado in ast.literal_eval(professor['Grados']): 
                    print(grado)
                    ttl_file.write(f'ex:estudio [\nrdf:type ex:Estudio ;\nex:fecha "{grado["fecha"]}"^^xsd:date ;\nex:institucion ex:{grado["Institucion"]} ;\nex:grado  ex:{grado["Grado"]}];\n')
            if professor['Cargo']:ttl_file.write(f"ex:cargo ex:{professor['Cargo']} .\n")
            
        professors_csv.close()

    with open("./cleaning/cursos_formateados.csv", "r") as courses_csv:
        courses = csv.DictReader(courses_csv)
        for course in courses:
            # print(course)
            if course['Codigo']:ttl_file.write(f"ex:{course['Codigo']} rdf:type ex:Curso ;\n")
            if course['Creditos']:ttl_file.write(f"    ex:creditos {course['Creditos']} ;\n")
            if course['Titulo']:ttl_file.write(f"    ex:titulo \"{course['Titulo']}\" ;\n")
            if course['Profesores']:
                for profesor in ast.literal_eval(course['Profesores'])[0].split(", "):
                    print(profesor)
                    ttl_file.write(f"    ex:impartidoPor ex:{profesor} ;\n")
            if course['Requisitos']:
                for requisito in ast.literal_eval(course['Requisitos']):
                    ttl_file.write(f"    ex:poseeRequisitos ex:{requisito} ;\n")
            if course['Departamento']:ttl_file.write(f"    ex:departamento ex:{course['Departamento']} .\n")
            ttl_file.write("\n")
        
        courses_csv.close()
# ex:CC5002 rdf:type ex:Curso ;
#     ex:titulo "Desarrollo de Aplicaciones Web" ;
#     ex:creditos 6 ;
#     ex:requisitos ex:CC1002 ;
#     ex:impartidoPor ex:Andres_Abeliuk ;
#     ex:departamento ex:DCC  .

