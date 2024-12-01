from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import XSD
import pandas as pd
from urllib.parse import quote

# File paths
movies_csv_path = "/content/drive/MyDrive/knowledgeEngineering/movie.csv" 
inflation_csv_path = "/content/drive/MyDrive/knowledgeEngineering/global_inflation_data.csv"
earnings_csv_path = "/content/drive/MyDrive/knowledgeEngineering/movie_earning.csv"
rdf_output_path = "movies.ttl"  # Output RDF file with split genres

# Load datasets
movies_data = pd.read_csv(movies_csv_path)
inflation_data = pd.read_csv(inflation_csv_path)
earnings_data = pd.read_csv(earnings_csv_path)

# Define namespace
namespace = Namespace("http://example.org/movies/")

# Initialize RDF graph
rdf_graph = Graph()

# Function to mint URIs: Mint specific entity type and identifier:
def mint_uri(entity_type, identifier):
 
    if not identifier or pd.isnull(identifier):
        identifier = "unknown"
    identifier = quote(str(identifier).strip().replace(" ", "_"))
    return URIRef(namespace[f"{entity_type}.{identifier}"])

# Add movies data to RDF
for _, movie in movies_data.iterrows():
    movie_uri = mint_uri("Movie", movie["title"])
    rdf_graph.add((movie_uri, RDF.type, URIRef(namespace["Movie"])))
    for column in movies_data.columns:
        value = movie[column]
        if pd.notnull(value):
            if column == "genre":  # split the genere: 
                genres = str(value).split(", ")  
                for genre in genres:
                    rdf_graph.add((movie_uri, URIRef(namespace["genre"]), Literal(genre, datatype=XSD.string)))
            else:
                rdf_graph.add((movie_uri, URIRef(namespace + column), Literal(value, datatype=XSD.string)))

# Add inflation data to RDF
for index, row in inflation_data.iterrows():
    inflation_uri = mint_uri("Inflation", index)
    rdf_graph.add((inflation_uri, RDF.type, URIRef(namespace["Inflation"])))
    for col in inflation_data.columns:
        value = row[col]
        if pd.notnull(value):
            rdf_graph.add((inflation_uri, URIRef(namespace + col), Literal(value, datatype=XSD.string)))

# Add earnings data to RDF
for index, row in earnings_data.iterrows():
    movie_title = row.get("title", None)
    if movie_title:
        movie_uri = mint_uri("Movie", movie_title)
        rdf_graph.add((movie_uri, RDF.type, URIRef(namespace["Movie"])))
        for col in earnings_data.columns:
            value = row[col]
            if pd.notnull(value):
                rdf_graph.add((movie_uri, URIRef(namespace + col), Literal(value, datatype=XSD.string)))

# Save RDF graph to Turtle format
rdf_graph.serialize(destination=rdf_output_path, format="turtle")
print(f"File saved at: {rdf_output_path}")
