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

with open("/home/lukas/Escritorio/Proyecto-Watos/CC7220-Proyect/processing/rdf/rdf_generator.py", "w") as file:
    file.write(rdf_schema)