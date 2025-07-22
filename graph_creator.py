import pandas as pd
import rdflib
from rdflib import URIRef, Literal, Namespace, RDF, RDFS, OWL, Graph, XSD
import pprint
import numpy as np

# Define namespaces
FTO = Namespace("http://www.semanticweb.org/nazanin/ontologies/2025/Fairtology_L1#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
XML = Namespace("http://www.w3.org/XML/1998/namespace")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
PERS = Namespace("http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#")

# Define graph
g = Graph()

# Bind the namespaces
g.bind("fto", FTO)
g.bind("rdfs", RDFS)
g.bind("rdf", RDF)
g.bind("owl", OWL)
g.bind("xml", XML)
g.bind("xsd", XSD)
g.bin("pers", PERS)

# Define object properties
g.add((FTO.hasCharacterType, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasEndingType, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasMoralTheme, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasAttribute, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasNarrativeStructure, RDF.type, OWL.ObjectProperty))
g.add((FTO.ReceivedBy, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasPromotedAspect, RDF.type, OWL.ObjectProperty))
g.add((FTO.createdBy, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasAdaptation, RDF.type, OWL.ObjectProperty))


# I defined these properties
g.add((FTO.hasPlot, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasMedium, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasLiteraryMode, RDF.type, OWL.ObjectProperty))

# Specify Domains
g.add((FTO.hasCharacterType, RDFS.domain, FTO.Character))
g.add((FTO.hasAttribute, RDFS.domain, FTO.CharacterArchetype))
g.add((FTO.hasAdaptation, RDFS.domain, FTO.LiteraryForm))

# Specify Ranges
g.add((FTO.hasCharacterType, RDFS.range, FTO.CharacterArchetype))
g.add((FTO.hasAttribute, RDFS.range, FTO.CharacterAttribute))



# Specify the type of properties (namespaces)
g.add((FTO.hasValue, RDF.type, OWL.DatatypeProperty))

# Read the datasets
base_df = pd.read_csv("data/Fairytale_Adaptations_Dataset_FinalUpdated.csv")
char_df = pd.read_csv("data/characters_full.csv")
plt_df = pd.read_csv("data/plot.csv")
full_df = base_df.merge(char_df, how= 'outer', on='ID').merge(plt_df, how='outer', on='ID')

# Define classes
g.add((FTO['Creator'], RDF.type, OWL.Class))
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
g.add((FTO['TricksterMode'], RDF.type, OWL.Class))

g.add((FTO['MoralTheme'], RDF.type, OWL.Class))
g.add((FTO['NarrativeUnit'], RDF.type, OWL.Class))
g.add((FTO['RecurringNarrativeStructure'], RDF.type, OWL.Class))
g.add((FTO['Departure'], RDF.type, OWL.Class))
g.add((FTO['MagicalAid'], RDF.type, OWL.Class))
g.add((FTO['ReturnAndReward'], RDF.type, OWL.Class))
g.add((FTO['TestOrTrial'], RDF.type, OWL.Class))
g.add((FTO['Transformation'], RDF.type, OWL.Class))
g.add((FTO['ActivePromotion'], RDF.type, OWL.Class))
g.add((FTO['PublicAttitude'], RDF.type, OWL.Class))
g.add((PERS['Attitude'], RDF.type, OWL.Class))
g.add((FTO['Character'], RDF.type, OWL.Class))
g.add((FTO['Innocent'], RDF.type, OWL.Class))
g.add((FTO['Evil'], RDF.type, OWL.Class))
g.add((FTO['Rebel'], RDF.type, OWL.Class))
g.add((FTO['Tragic'], RDF.type, OWL.Class))
g.add((FTO['EmpowermentTheme'], RDF.type, OWL.Class))
g.add((FTO['IdentityAndInclusionTheme'], RDF.type, OWL.Class))
g.add((FTO['MoralAmbiguityTheme'], RDF.type, OWL.Class))
g.add((FTO['VirtueRewardedTheme'], RDF.type, OWL.Class))
g.add((FTO['Medium'], RDF.type, OWL.Class))
g.add((FTO['LiteraryForm'], RDF.type, OWL.Class))
g.add((FTO['CinematicAdaptation'], RDF.type, OWL.Class))

# Define subclasses
g.add((FTO['Helper'], RDFS.subClassOf, FTO.CharacterArchetype))
g.add((FTO['Hero'], RDFS.subClassOf, FTO.CharacterArchetype))
g.add((FTO['Trickster'], RDFS.subClassOf, FTO.CharacterArchetype))
g.add((FTO['Villain'], RDFS.subClassOf, FTO.CharacterArchetype))

g.add((FTO['BittersweetEnding'], RDFS.subClassOf, FTO.EndingType))
g.add((FTO['HappilyEverAfter'], RDFS.subClassOf, FTO.EndingType))
g.add((FTO['TragicEnding'], RDFS.subClassOf, FTO.EndingType))

g.add((FTO['IronicMode'], RDFS.subClassOf, FTO.LiteraryMode))
g.add((FTO['MythicMode'], RDFS.subClassOf, FTO.LiteraryMode))
g.add((FTO['RomanticMode'], RDFS.subClassOf, FTO.LiteraryMode))
g.add((FTO['TragicMode'], RDFS.subClassOf, FTO.LiteraryMode))
g.add((FTO['Trickster'], RDFS.subClassOf, FTO.LiteraryMode))

g.add((FTO['Departure'], RDFS.subClassOf, FTO.RecurringNarrativeStructure))
g.add((FTO['MagicalAid'], RDFS.subClassOf, FTO.RecurringNarrativeStructure))
g.add((FTO['ReturnAndReward'], RDFS.subClassOf, FTO.RecurringNarrativeStructure))
g.add((FTO['TestOrTrial'], RDFS.subClassOf, FTO.RecurringNarrativeStructure))
g.add((FTO['Transformation'], RDFS.subClassOf, FTO.RecurringNarrativeStructure))

g.add((FTO['PublicAttitude']. RDFS.subClassof, PERS.Attitude))

g.add((FTO.Innocent, RDFS.subClassOf, FTO.CharacterAttribute))
g.add((FTO.Evil, RDFS.subClassOf, FTO.CharacterAttribute))
g.add((FTO.Rebel, RDFS.subClassOf, FTO.CharacterAttribute))
g.add((FTO.Tragic, RDFS.subClassOf, FTO.CharacterAttribute))

g.add((FTO.EmpowermentTheme, RDFS.subClassOf, FTO.MoralTheme))
g.add((FTO.IdentityAndInclusionTheme, RDFS.subClassOf, FTO.MoralTheme))
g.add((FTO.MoralAmbiguityTheme, RDFS.subClassOf, FTO.MoralTheme))
g.add((FTO.VirtueRewardedTheme, RDFS.subClassOf, FTO.MoralTheme))

g.add((FTO['LiteraryForm'], RDFS.subClassOf, FTO.Medium))
g.add((FTO['CinematicAdaptation'], RDF.type, OWL.Class))

g.add((FTO.RecurringNarrativeStructure, OWL.sameAs, FTO.NarrativeUnit))

# Iterate over the rows
for index, row in full_df.iterrows():
    if pd.notna(row):
        # Create and Add Fairy tale uri
        fairytale_uri = URIRef(FTO[row['ID']+'_'+row['Fairytale'].strip().lower().replace(" ","_")])
        g.add((fairytale_uri, RDF.type, FTO.Fairytale))
        g.add((fairytale_uri, FTO.hasValue, Literal(row['Fairytale'])))

        # Create and add creator uri
        creator_uri = URIRef(FTO[row['Creator'].strip().lower().replace(" ", "_")])
        g.add((creator_uri, RDF.type, FTO.Creator))
        g.add((fairytale_uri, FTO.createdBy, creator_uri))
        g.add((creator_uri, FTO.hasValue, Literal(row['Creator'])))

        # Add Plot
        plot_uri = URIRef(FTO[row['ID']+'_'+'Plot'])
        g.add((plot_uri, RDF.type, FTO.Plot))
        g.add((fairytale_uri, RDF.hasPlot, plot_uri))
        g.add((plot_uri, FTO.hasValue, Literal(row['Plot'])))

        # Add EndingTypes
        if row['EndingType'] != '' or row['EndingType'] != np.nan:
            if row['EndingType'].strip() == 'BitterSweetEnding':
                g.add((fairytale_uri, FTO.hasEndingType, FTO.BittersweetEnding))

            elif row['EndingType'].strip() == 'HappilyEverAfter':
                g.add((fairytale_uri, FTO.hasEndingType, FTO.HappilyEverAfter))

            elif row['EndingType'].strip() == 'TragicEnding':
                g.add((fairytale_uri, FTO.hasEndingType, FTO.TragicEnding))

        # Add different LiteraryModes
        if row['LiteraryMode'] != '' or row['LiteraryMode'] != np.nan:
            if row['LiteraryMode'].strip() == 'IronicMode':
                g.add((fairytale_uri, FTO.hasLiteraryMode, FTO.IronicMode))

            elif row['LiteraryMode'].strip() == 'MythicMode':
                g.add((fairytale_uri, FTO.hasLiteraryMode, FTO.MythicMode))

            elif row['LiteraryMode'].strip() == 'RomanticMode':
                g.add((fairytale_uri, FTO.hasLiteraryMode, FTO.RomanticMode))

            elif row['LiteraryMode'].strip() == 'TragicMode':
                g.add((fairytale_uri, FTO.hasLiteraryMode, FTO.TragicMode))

            elif row['LiteraryMode'].strip() == 'TricksterMode':
                g.add((fairytale_uri, FTO.hasLiteraryMode, FTO.TricksterMode))

        # Add MoralThemes
        if row['MoralTheme'] != '' or row['MoralTheme'] != np.nan:
            if row['MoralTheme'].strip() == 'EmpowermentTheme':
                g.add((fairytale_uri, FTO.hasMoralTheme, FTO.EmpowermentTheme))

            elif row['MoralTheme'].strip() == 'IdentityAndInclusionTheme':
                g.add((fairytale_uri, FTO.hasMoralTheme, FTO.IdentityAndInclusionTheme))

            elif row['MoralTheme'].strip() == 'MoralAmbiguityTheme':
                g.add((fairytale_uri, FTO.hasMoralTheme, FTO.MoralAmbiguityTheme))

            elif row['MoralTheme'].strip() == 'VirtueRewardedTheme':
                g.add((fairytale_uri, FTO.hasMoralTheme, FTO.VirtueRewardedTheme))

        activepromotion_uri = URIRef(FTO[row['ActivePromotion'].strip()])
        g.add((activepromotion_uri, RDF.type, FTO.ActivePromotion))
        g.add((fairytale_uri, FTO.hasActivePromotion, activepromotion_uri))

        # Add character
        character_uri = URIRef(FTO[row['Character'].strip()])
        g.add((character_uri, RDF.type, FTO.Chracter))
        g.add(fairytale_uri, FTO.hasCharacter, character_uri)
        g.add((character_uri, FTO.hasValue, Literal(row['Character'].strip())))

        char_arch = ''
        if row['CharacterArchetype'] != "" or row['CharacterArchetype'] != np.nan:
            if row['CharacterArchetype'].strip() == 'Hero':
                g.add((character_uri, FTO.hasCharacterType, FTO.Hero))
                char_arch = FTO.Hero

            elif row['CharacterArchetype'].strip() == 'Helper':
                g.add((character_uri, FTO.hasCharacterType, FTO.Helper))
                char_arch = FTO.Helper

            elif row['CharacterArchetype'].strip() == 'Villain':
                g.add((character_uri, FTO.hasCharacterType, FTO.Villain))
                char_arch = FTO.Villain

            elif row['CharacterArchetype'].stirp() == 'Trickster':
                g.add((character_uri, FTO.hasCharacterType, FTO.Trickster))
                char_arch = FTO.Trickster

        if row['CharacterAttribute'] != "" or row['CharacterAttribute'] != np.nan:
            if row['CharacterAttribute'].strip() == 'Innocent':
                g.add((char_arch, FTO.hasAttribute, FTO.Innocent))

            elif row['CharacterAttribute'].strip() == 'Evil':
                g.add((char_arch, FTO.hasAttribute, FTO.Evil))

            elif row['CharacterAttribute'].strip() == 'Rebel':
                g.add((char_arch, FTO.hasAttribute, FTO.Rebel))

            elif row['CharacterAttribute'].strip() == 'Tragic':
                g.add((char_arch, FTO.hasAttribute, FTO.Tragic))

        # Define RecurrentNarrativeStructure instances
        departure_uri = URIRef(FTO[row['ID']+'_'+'departure'])
        magicalaid_uri = URIRef(FTO[row['ID'] + '_' + 'magicalaid'])
        returnandreward_uri = URIRef(FTO[row['ID'] + '_' + 'returnandreward'])
        testortrial_uri = URIRef(FTO[row['ID'] + '_' + 'testortrial'])
        transformation_uri = URIRef(FTO[row['ID'] + '_' + 'transformation'])

        g.add((fairytale_uri, FTO.hasNarrativeStructure, departure_uri))
        g.add((departure_uri, RDF.type, FTO.Departure))
        g.add((departure_uri, FTO.hasValue, Literal(row['Departure'])))

        g.add((fairytale_uri, FTO.hasNarrativeStructure, magicalaid_uri))
        g.add((magicalaid_uri, RDF.type, FTO.MagicalAid))
        g.add((magicalaid_uri, FTO.hasValue, Literal(row['MagicalAid'])))

        g.add((fairytale_uri, FTO.hasNarrativeStructure, returnandreward_uri))
        g.add((returnandreward_uri, RDF.type, FTO.ReturnAndReward))
        g.add((departure_uri, FTO.hasValue, Literal(row['ReturnAndReward'])))

        g.add((fairytale_uri, FTO.hasNarrativeStructure, testortrial_uri))
        g.add((testortrial_uri, RDF.type, FTO.TestOrTrial))
        g.add((testortrial_uri, FTO.hasValue, Literal(row['TestOrTrial'])))

        g.add((fairytale_uri, FTO.hasNarrativeStructure, transformation_uri))
        g.add((transformation_uri, RDF.type, FTO.Transformation))
        g.add((transformation_uri, FTO.hasValue, Literal(row['Transformation'])))











