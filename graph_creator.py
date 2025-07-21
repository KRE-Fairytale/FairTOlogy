import pandas as pd
import rdflib
from rdflib import URIRef, Literal, Namespace, RDF, RDFS, OWL, Graph, XSD
import pprint

# Define namespaces
FTO = Namespace("http://www.semanticweb.org/nazanin/ontologies/2025/Fairtology_L1#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
XML = Namespace("http://www.w3.org/XML/1998/namespace")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")

# Define graph
g = Graph()

# Bind the namespaces
g.bind("fto", FTO)
g.bind("rdfs", RDFS)
g.bind("rdf", RDF)
g.bind("owl", OWL)
g.bind("xml", XML)
g.bind("xsd", XSD)

# Define object properties
g.add((FTO.hasCharacterType, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasEndingType, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasMoralTheme, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasCharacterType, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasNarrativeStructure, RDF.type, OWL.ObjectProperty))
g.add((FTO.ReceivedBy, RDF.type, OWL.ObjectProperty))

# Specify the type of properties (namespaces)
g.add((FTO.hasValue, RDF.type, OWL.DatatypeProperty))

# Read the datasets
base_df = pd.read_csv("data/Fairytale_Adaptations_Dataset_FinalUpdated.csv")
char_df = pd.read_csv("data/characters_full.csv")
plt_df = pd.read_csv("data/plot.csv")
full_df = base_df.merge(char_df, how= 'outer', on='ID').merge(plt_df, how='outer', on='ID')

# Define classes
g.add((FTO['Audience'], RDF.type, OWL.Class))
g.add((FTO['CharacterArchetype'], RDF.type, OWL.Class))
g.add((FTO['Helper'], RDF.type, OWL.Class))
g.add((FTO['Hero'], RDF.type, OWL.Class))
g.add((FTO['Trickster'], RDF.type, OWL.Class))
g.add((FTO['Villain'], RDF.type, OWL.Class))
g.add((FTO['EndingType'], RDF.type, OWL.Class))
g.add((FTO['BittersweetEnding'], RDF.type, OWL.Class))
g.add((FTO['HappilyEverAfter'], RDF.type, OWL.Class))
g.add((FTO['TragicEnding'], RDF.type, OWL.Class))
g.add((FTO['Fairytale'], RDF.type, OWL.Class))
g.add((FTO['Character'], RDF.type, OWL.Class))
g.add((FTO['Plot'], RDF.type, OWL.Class))
g.add((FTO['LiteraryMode'], RDF.type, OWL.Class))
g.add((FTO['IronicMode'], RDF.type, OWL.Class))
g.add((FTO['MythicMode'], RDF.type, OWL.Class))
g.add((FTO['RomanticMode'], RDF.type, OWL.Class))
g.add((FTO['TragicMode'], RDF.type, OWL.Class))
g.add((FTO['MoralTheme'], RDF.type, OWL.Class))
g.add((FTO['NarrativeUnit'], RDF.type, OWL.Class))
g.add((FTO['RecurringNarrativeStructure'], RDF.type, OWL.Class))
g.add((FTO['Departure'], RDF.type, OWL.Class))
g.add((FTO['MagicalAid'], RDF.type, OWL.Class))
g.add((FTO['ReturnAndReward'], RDF.type, OWL.Class))
g.add((FTO['TestOrTrial'], RDF.type, OWL.Class))
g.add((FTO['Transformation'], RDF.type, OWL.Class))

# Define subclasses
g.add((FTO['Helper'], RDFS.subClassOf, FTO.CharacterArchetype))
g.add((FTO['Hero'], RDFS.subClassOf, FTO.CharacterArchetype))
g.add((FTO['Trickster'], RDFS.subClassOf, FTO.CharacterArchetype))
g.add((FTO['Villain'], RDFS.subClassOf, FTO.CharacterArchetype))

g.add((FTO['BittersweetEnding'], RDFS.subClassOf, FTO.EndingType))
g.add((FTO['HappilyEverAfter'], RDFS.subClassOf, FTO.EndingType))
g.add((FTO['TragicEnding'], RDFS.subClassOf, FTO.EndingType))

g.add((FTO['Character'], RDFS.subClassOf, FTO.Fairytale))
g.add((FTO['Plot'], RDFS.subClassOf, FTO.Fairytale))

g.add((FTO['IronicMode'], RDFS.subClassOf, FTO.LiteraryMode))
g.add((FTO['MythicMode'], RDFS.subClassOf, FTO.LiteraryMode))
g.add((FTO['RomanticMode'], RDFS.subClassOf, FTO.LiteraryMode))
g.add((FTO['TragicMode'], RDFS.subClassOf, FTO.LiteraryMode))

g.add((FTO['Departure'], RDFS.subClassOf, FTO.RecurringNarrativeStructure))
g.add((FTO['MagicalAid'], RDFS.subClassOf, FTO.RecurringNarrativeStructure))
g.add((FTO['ReturnAndReward'], RDFS.subClassOf, FTO.RecurringNarrativeStructure))
g.add((FTO['TestOrTrial'], RDFS.subClassOf, FTO.RecurringNarrativeStructure))
g.add((FTO['Transformation'], RDFS.subClassOf, FTO.RecurringNarrativeStructure))

g.add((FTO.RecurringNarrativeStructure, OWL.sameAs, FTO.NarrativeUnit))

# Iterate over the rows
for index, row in full_df.iterrrows():
    if pd.notna(row):
        fairytale_uri = URIRef(FTO[row['Fairytale'].strip().lower().replace(" ","_")])
        g.add((fairytale_uri, RDF.type, FTO.Fairytale))
        






