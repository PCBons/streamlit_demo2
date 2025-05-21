import streamlit as st
import pandas as pd
import geopandas as gpd

gokken = []
st.title('Welkom bij de snoeppot app')

@st.fragment
def doe_gok():

	with st.form(key = '1'):
		gok = st.number_input('Vul hier je gok in:')
		st.form_submit_button()
	gokken.append(gok)

	st.write(gokken[1:])
	st.write(f'Er hebben tot nu toe {len(gokken)-1} mensen meegedaan.')

doe_gok()
