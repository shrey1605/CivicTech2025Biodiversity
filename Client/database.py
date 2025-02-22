import streamlit as st
import json

@st.cache_data

def fetch_by_genus(file_name):
    #need function to fetch all instances by genus
    with open('data.json', 'r') as file:
        data = json.load(file_name)

    occurances = 0

    for i in data["genus"]:
        occurances += 1
        


    
    return (occurences, genuses)

def fetch_by_species(file_name, genus):
    #need function to fetch all instances by genus
    return (occurences, species)

