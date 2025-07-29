import numpy as np
import pandas as pd
import rdflib
from rdflib import URIRef, Literal, Namespace, RDF, RDFS, OWL, Graph, XSD
import re
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore

# Define namespaces
FTO = Namespace("http://www.semanticweb.org/nazanin/ontologies/2025/Fairtology#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
XML = Namespace("http://www.w3.org/XML/1998/namespace")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
PERSP = Namespace("http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#")
GC = Namespace("https://ontology.golemlab.org.eu/")

# Define graph
g = Graph()

# Bind the namespaces
g.bind("fto", FTO)
g.bind("rdfs", RDFS)
g.bind("rdf", RDF)
g.bind("owl", OWL)
g.bind("xml", XML)
g.bind("xsd", XSD)
g.bind("persp", PERSP)
g.bind("gc", GC)

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
g.add((FTO.creates, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasAudienceAttitude, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasCharacter, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasMedium, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasPlot, RDF.type, OWL.ObjectProperty))
g.add((FTO.recievedBy, RDF.type, OWL.ObjectProperty))
g.add((FTO.hasLiteraryMode, RDF.type, OWL.ObjectProperty))

# Specify Domains
g.add((FTO.hasCharacterType, RDFS.domain, FTO.Character))
g.add((FTO.hasAttribute, RDFS.domain, FTO.CharacterArchetype))
g.add((FTO.hasAdaptation, RDFS.domain, FTO.Fairytale))
g.add((FTO.receivedBy, RDFS.domain, FTO.Fairytale))
g.add((FTO.createdBy, RDFS.domain, FTO.Fairytale))
g.add((FTO.hasAudienceAtitude, RDFS.domain, FTO.Fairytale))
g.add((FTO.hasCharacter, RDFS.domain, FTO.Fairytale))
g.add((FTO.hasEndingType, RDFS.domain, FTO.Fairytale))
g.add((FTO.hasLiteraryMode, RDFS.domain, FTO.Fairytale))
g.add((FTO.hasMedium, RDFS.domain, FTO.Fairytale))
g.add((FTO.hasMoralTheme, RDFS.domain, FTO.Fairytale))
g.add((FTO.hasNarrativeStructure, RDFS.domain, FTO.Plot))
g.add((FTO.hasPlot, RDFS.domain, FTO.Fairytale))
g.add((FTO.hasPromotedAspect, RDFS.domain, FTO.Fairytale))
g.add((FTO.has, RDFS.domain, FTO.Fairytale))
g.add((FTO.has, RDFS.domain, FTO.Fairytale))

# Specify Ranges
g.add((FTO.hasCharacterType, RDFS.range, FTO.CharacterArchetype))
g.add((FTO.hasAttribute, RDFS.range, FTO.CharacterAttribute))
g.add((FTO.hasValue, RDFS.range, RDFS.Literal))
g.add((FTO.receivedBy, RDFS.range, FTO.Audience))
g.add((FTO.createdBy, RDFS.range, FTO.Creator))
g.add((FTO.hasAdaptation, RDFS.range, FTO.Medium))
g.add((FTO.hasAudienceAtitude, RDFS.range, FTO.PublicAttitude))
g.add((FTO.hasCharacter, RDFS.range, FTO.Character))
g.add((FTO.hasEndingType, RDFS.range, FTO.EndingType))
g.add((FTO.hasLiteraryMode, RDFS.range, FTO.LiteraryMode))
g.add((FTO.hasMedium, RDFS.range, FTO.Medium))
g.add((FTO.hasMoralTheme, RDFS.range, FTO.MoralTheme))
g.add((FTO.hasNarrativeStructure, RDFS.range, FTO.RecurringNarrativeStructure))
g.add((FTO.hasPlot, RDFS.range, FTO.Plot))
g.add((FTO.hasPromotedAspect, RDFS.range, FTO.ActivePromotion))
g.add((FTO.has, RDFS.range, FTO.PublicAttitude))
g.add((FTO.has, RDFS.range, FTO.PublicAttitude))

# Specify the type of properties (namespaces)
g.add((FTO.hasValue, RDF.type, OWL.DatatypeProperty))

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
g.add((PERSP['Attitude'], RDF.type, OWL.Class))
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
g.add((FTO['MixedReception'], RDF.type, OWL.Class))
g.add((FTO['PositiveReception'], RDF.type, OWL.Class))
g.add((FTO['NegativeReception'], RDF.type, OWL.Class))
g.add((FTO['InnerSelf'], RDF.type, OWL.Class))
g.add((FTO['OuterWorld'], RDF.type, OWL.Class))
g.add((FTO['Character'], RDF.type, OWL.Class))

# Define Labels
g.add((FTO['EmpowermentTheme'], RDFS.label, Literal('Empowerment Theme')))
g.add((FTO['IdentityAndInclusionTheme'], RDFS.label, Literal('Identity and Inclusion Theme')))
g.add((FTO['MoralAmbiguityTheme'], RDFS.label, Literal('Moral Ambiguity Theme')))
g.add((FTO['VirtueRewardedTheme'], RDFS.label, Literal('Virtue Rewarded Theme')))
g.add((FTO['Innocent'], RDFS.label, Literal('Innocent')))
g.add((FTO['Evil'], RDFS.label, Literal('Evil')))
g.add((FTO['Rebel'], RDFS.label, Literal('Rebel')))
g.add((FTO['Tragic'], RDFS.label, Literal('Tragic')))
g.add((FTO['MixedReception'], RDFS.label, Literal('Mixed Reception')))
g.add((FTO['PositiveReception'], RDFS.label, Literal('Positive Reception')))
g.add((FTO['NegativeReception'], RDFS.label, Literal('Negative Reception')))
g.add((FTO['Helper'], RDFS.label, Literal('Helper')))
g.add((FTO['Hero'], RDFS.label, Literal('Hero')))
g.add((FTO['Trickster'], RDFS.label, Literal('Trickster')))
g.add((FTO['Villain'], RDFS.label, Literal('Villain')))
g.add((FTO['BittersweetEnding'], RDFS.label, Literal('Bittersweet Ending')))
g.add((FTO['HappilyEverAfter'], RDFS.label, Literal('Happily Ever After')))
g.add((FTO['TragicEnding'], RDFS.label, Literal('Tragic Ending')))
g.add((FTO['IronicMode'], RDFS.label, Literal('Ironic Mode')))
g.add((FTO['MythicMode'], RDFS.label, Literal('Mythic Mode')))
g.add((FTO['RomanticMode'], RDFS.label, Literal('Romantic Mode')))
g.add((FTO['TragicMode'], RDFS.label, Literal('Tragic Mode')))
g.add((FTO['TricksterMode'], RDFS.label, Literal('Trickster Mode')))
g.add((FTO['InnerSelf'], RDFS.label, Literal('Inner Self')))
g.add((FTO['OuterWorld'], RDFS.label, Literal('Outer World')))

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
g.add((FTO['PublicAttitude'], RDFS.subClassOf, PERSP.Attitude))
g.add((FTO.Innocent, RDFS.subClassOf, FTO.CharacterAttribute))
g.add((FTO.Evil, RDFS.subClassOf, FTO.CharacterAttribute))
g.add((FTO.Rebel, RDFS.subClassOf, FTO.CharacterAttribute))
g.add((FTO.Tragic, RDFS.subClassOf, FTO.CharacterAttribute))
g.add((FTO.EmpowermentTheme, RDFS.subClassOf, FTO.MoralTheme))
g.add((FTO.IdentityAndInclusionTheme, RDFS.subClassOf, FTO.MoralTheme))
g.add((FTO.MoralAmbiguityTheme, RDFS.subClassOf, FTO.MoralTheme))
g.add((FTO.VirtueRewardedTheme, RDFS.subClassOf, FTO.MoralTheme))
g.add((FTO['LiteraryForm'], RDFS.subClassOf, FTO.Medium))
g.add((FTO['InnerSelf'], RDFS.subClassOf, FTO.ActivePromotion))
g.add((FTO['OuterWorld'], RDFS.subClassOf, FTO.ActivePromotion))

g.add((FTO.RecurringNarrativeStructure, OWL.sameAs, FTO.NarrativeUnit))

# Read the datasets
base_df = pd.read_csv("data/Fairytale_Adaptations_Dataset_FinalUpdated.csv")
char_df = pd.read_csv("data/characters_full.csv")
plt_df = pd.read_csv("data/NarrativeUnit.csv")
full_df = base_df.merge(char_df, how= 'outer', on='ID').merge(plt_df, how='outer', on='ID')

# Omit unwanted elements from the strings
def normalize_string(string):
    rep = {"'":"_", " ":"_", "(":"", ")":"", "/":"_", "’":"_", ",":"", ".":""}
    string.strip()
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], string)
    return text

# Iterate over the rows
for index, row in full_df.iterrows():

    # Create and Add Fairytale uri
    fairytale_uri = URIRef(FTO[str(row['ID'])+'_'+ normalize_string(row['Fairytale'])])
    if (fairytale_uri, RDF.type, FTO.Fairytale) not in g:
        g.add((fairytale_uri, RDF.type, FTO.Fairytale))
        g.add((fairytale_uri, RDFS.label, Literal(row['Fairytale'])))

    # Create and add creator uri
    creator_uri = URIRef(FTO[normalize_string(row['Creator'])])
    if (fairytale_uri, FTO.createdBy, creator_uri) not in g:
        g.add((fairytale_uri, FTO.createdBy, creator_uri))
        g.add((creator_uri, RDF.type, FTO.Creator))
        g.add((creator_uri, FTO.hasValue, Literal(row['Creator'])))

    # Add Plot
    plot_uri = URIRef(FTO[str(row['ID'])+'_'+'Plot'])
    if (fairytale_uri, RDF.hasPlot, plot_uri) not in g: # Check if the triple for plot already added to the graph
        g.add((fairytale_uri, FTO.hasPlot, plot_uri))
        g.add((plot_uri, RDF.type, FTO.Plot))
        g.add((plot_uri, FTO.hasValue, Literal(row['Plot'])))

    # Add EndingTypes
    value = str(row['EndingType']).strip()
    if value and value != 'nan':
        if value == 'BittersweetEnding' and (fairytale_uri, FTO.hasEndingType, FTO.BittersweetEnding) not in g:
            g.add((fairytale_uri, FTO.hasEndingType, FTO.BittersweetEnding))

        elif value == 'HappilyEverAfter' and (fairytale_uri, FTO.hasEndingType, FTO.HappilyEverAfter) not in g:
            g.add((fairytale_uri, FTO.hasEndingType, FTO.HappilyEverAfter))

        elif value == 'TragicEnding' and (fairytale_uri, FTO.hasEndingType, FTO.TragicEnding) not in g:
            g.add((fairytale_uri, FTO.hasEndingType, FTO.TragicEnding))

    # Add different LiteraryModes
    value = str(row['LiteraryMode']).strip()
    if value and value != 'nan':
        if value == 'IronicMode' and (fairytale_uri, FTO.hasLiteraryMode, FTO.IronicMode) not in g:
                g.add((fairytale_uri, FTO.hasLiteraryMode, FTO.IronicMode))

        elif value == 'MythicMode' and (fairytale_uri, FTO.hasLiteraryMode, FTO.MythicMode) not in g:
            g.add((fairytale_uri, FTO.hasLiteraryMode, FTO.MythicMode))

        elif value == 'RomanticMode' and (fairytale_uri, FTO.hasLiteraryMode, FTO.RomanticMode) not in g:
            g.add((fairytale_uri, FTO.hasLiteraryMode, FTO.RomanticMode))

        elif value == 'TragicMode' and (fairytale_uri, FTO.hasLiteraryMode, FTO.TragicMode) not in g:
            g.add((fairytale_uri, FTO.hasLiteraryMode, FTO.TragicMode))

        elif value == 'TricksterMode' and (fairytale_uri, FTO.hasLiteraryMode, FTO.TricksterMode) not in g:
            g.add((fairytale_uri, FTO.hasLiteraryMode, FTO.TricksterMode))

    # Add MoralThemes
    value = str(row['MoralTheme']).strip()
    if value and value != 'nan':
        if value == 'EmpowermentTheme' and (fairytale_uri, FTO.hasMoralTheme, FTO.EmpowermentTheme) not in g:
            g.add((fairytale_uri, FTO.hasMoralTheme, FTO.EmpowermentTheme))

        elif value == 'IdentityAndInclusionTheme' and (fairytale_uri, FTO.hasMoralTheme,
                                                       FTO.IdentityAndInclusionTheme) not in g:
            g.add((fairytale_uri, FTO.hasMoralTheme, FTO.IdentityAndInclusionTheme))

        elif value == 'MoralAmbiguityTheme' and (fairytale_uri, FTO.hasMoralTheme, FTO.MoralAmbiguityTheme) not in g:
            g.add((fairytale_uri, FTO.hasMoralTheme, FTO.MoralAmbiguityTheme))

        elif value == 'VirtueRewardedTheme' and (fairytale_uri, FTO.hasMoralTheme, FTO.VirtueRewardedTheme) not in g:
            g.add((fairytale_uri, FTO.hasMoralTheme, FTO.VirtueRewardedTheme))

    value = str(row['ActivePromotion']).strip()
    if value and value != 'nan':
        if value == 'InnerSelf' and (fairytale_uri, FTO.hasPromotedAspect, FTO.InnerSelf) not in g:
            g.add((fairytale_uri, FTO.hasPromotedAspect, FTO.InnerSelf))

        elif value == 'OuterWorld' and (fairytale_uri, FTO.hasPromotedAspect, FTO.OuterWorld) not in g:
            g.add((fairytale_uri, FTO.hasPromotedAspect, FTO.OuterWorld))

    # Add character
    character_uri = URIRef(FTO[normalize_string(str(row['ID']) + '_' + row['Character'])])
    g.add((character_uri, RDF.type, FTO.Character))
    g.add((fairytale_uri, FTO.hasCharacter, character_uri))
    g.add((character_uri, RDFS.label, Literal(row['Character'].strip())))

    char_arch = ''
    value = str(row['CharacterArchetype']).strip()
    if value and value != 'nan':
        if value == 'Hero':
            hero_uri = URIRef(FTO[str(row['ID']) + '_' + 'Hero'])
            g.add((hero_uri, RDF.type, FTO.Hero))
            g.add((character_uri, FTO.hasCharacterType, hero_uri))
            char_arch = hero_uri

        elif value == 'Helper':
            helper_uri = URIRef(FTO[str(row['ID']) + '_' + 'Helper'])
            g.add((helper_uri, RDF.type, FTO.Helper))
            g.add((character_uri, FTO.hasCharacterType, helper_uri))
            char_arch = helper_uri

        elif value == 'Villain':
            villain_uri = URIRef(FTO[str(row['ID']) + '_' + 'Villain'])
            g.add((villain_uri, RDF.type, FTO.Villain))
            g.add((character_uri, FTO.hasCharacterType, villain_uri))
            char_arch = villain_uri

        elif value == 'Trickster':
            trickster_uri = URIRef(FTO[str(row['ID']) + '_' + 'Trickster'])
            g.add((trickster_uri, RDF.type, FTO.Trickster))
            g.add((character_uri, FTO.hasCharacterType, trickster_uri))
            char_arch = trickster_uri

    value = str(row['CharacterAttribute']).strip()
    if value and value != 'nan':
        if value == 'Innocent':
            g.add((char_arch, FTO.hasAttribute, FTO.Innocent))

        elif value == 'Evil':
            g.add((char_arch, FTO.hasAttribute, FTO.Evil))

        elif value == 'Rebel':
            g.add((char_arch, FTO.hasAttribute, FTO.Rebel))

        elif value == 'Tragic':
            g.add((char_arch, FTO.hasAttribute, FTO.Tragic))

    value = str(row['PublicAttitude']).strip()
    if value and value != 'nan':
        if value == 'MixedReception' and (fairytale_uri, FTO.hasAudienceAttitude, FTO.MixedReception) not in g:
            g.add((fairytale_uri, FTO.hasAudienceAttitude, FTO.MixedReception))

        elif value == 'NegativeReception' and (fairytale_uri, FTO.hasAudienceAttitude, FTO.NegativeReception) not in g:
            g.add((fairytale_uri, FTO.hasAudienceAttitude, FTO.NegativeReception))

        elif value == 'PositiveReception' and (fairytale_uri, FTO.hasAudienceAttitude, FTO.PositiveReception) not in g:
            g.add((fairytale_uri, FTO.hasAudienceAttitude, FTO.PositiveReception))

    #Add medium
    value = str(row['Medium']).strip()
    if value and value != 'nan':
        if value == 'LiteraryForm' and (fairytale_uri, FTO.hasMedium, FTO.LiteraryForm) not in g:
            g.add((fairytale_uri, FTO.hasMedium, FTO.LiteraryForm))

        elif value == 'CinematicAdaptation' and (fairytale_uri, FTO.hasMedium, FTO.CinematicAdaptation) not in g:
            g.add((fairytale_uri, FTO.hasMedium, FTO.CinematicAdaptation))

    # Define RecurrentNarrativeStructure instances
    departure_uri = URIRef(FTO[str(row['ID']) + '_' + 'departure'])
    magicaid_uri = URIRef(FTO[str(row['ID']) + '_' + 'magicaid'])
    returnandreward_uri = URIRef(FTO[str(row['ID']) + '_' + 'returnandreward'])
    testortrial_uri = URIRef(FTO[str(row['ID']) + '_' + 'testortrial'])
    transformation_uri = URIRef(FTO[str(row['ID']) + '_' + 'transformation'])

    if (plot_uri, FTO.hasNarrativeStructure, departure_uri) not in g:
        g.add((plot_uri, FTO.hasNarrativeStructure, departure_uri))
        g.add((departure_uri, RDF.type, FTO.Departure))
        g.add((departure_uri, FTO.hasValue, Literal(row['Departure'])))

    if (plot_uri, FTO.hasNarrativeStructure, magicaid_uri) not in g:
        g.add((plot_uri, FTO.hasNarrativeStructure, magicaid_uri))
        g.add((magicaid_uri, RDF.type, FTO.MagicalAid))
        g.add((magicaid_uri, FTO.hasValue, Literal(row['MagicAid'])))

    if (plot_uri, FTO.hasNarrativeStructure, returnandreward_uri) not in g:
        g.add((plot_uri, FTO.hasNarrativeStructure, returnandreward_uri))
        g.add((returnandreward_uri, RDF.type, FTO.ReturnAndReward))
        g.add((departure_uri, FTO.hasValue, Literal(row['ReturnAndReward'])))

    if (plot_uri, FTO.hasNarrativeStructure, testortrial_uri) not in g:
        g.add((plot_uri, FTO.hasNarrativeStructure, testortrial_uri))
        g.add((testortrial_uri, RDF.type, FTO.TestOrTrial))
        g.add((testortrial_uri, FTO.hasValue, Literal(row['TestOrTrial'])))

    if (plot_uri, FTO.hasNarrativeStructure, transformation_uri) not in g:
        g.add((plot_uri, FTO.hasNarrativeStructure, transformation_uri))
        g.add((transformation_uri, RDF.type, FTO.Transformation))
        g.add((transformation_uri, FTO.hasValue, Literal(row['Transformation'])))

# Serialize the graph to a Turtle file
with open("fairytale_graph.ttl", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))

# Add to graph database (blazegraph)
store = SPARQLUpdateStore()
endpoint = "http://127.0.0.1:9999/blazegraph/sparql"
store.open((endpoint, endpoint))

for triple in g.triples((None, None, None)):
    # Check if the triple already exists
    query = f"ASK {{ {triple[0].n3()} {triple[1].n3()} {triple[2].n3()} }}"  # Construct the ASK query
    result = store.query(query)

    if not bool(result):  # If the triple doesn't exist, add it
        store.add(triple)

store.close()