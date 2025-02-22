import streamlit as st
import json

@st.cache_data

def fetch_by_genus(file_name):
    #need function to fetch all instances by genus
    with open(file_name, 'r') as file:
        data = json.load(file)

    genuses = []

    for i in data["genuses"]:
        occurences = i["occurencesTotalGenus"]
        name = i["name"]
        genuses.append(name)
    
    return (occurences, genuses)

def fetch_by_species(file_name, genus):
    #need function to fetch all instances by genus
    with open(file_name, 'r') as file:
        data = json.load(file)

    species = []

    for i in data[genus]["subgenea"]:
        occurences = i["occurences"]
        name = i["name"]
        species.append(name)
    
    return (occurences, species)

def fetch_plant(file_name, genus, species):
    with open(file_name, 'r') as file:
        data = json.load(file)

    for i in data[genus][species]:
        name = i["name"]
        #image = i["image"]
        description = i["description"]
        
    return name, description #image, 


       


