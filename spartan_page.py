from pathlib import Path
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from utils import hide_table_index, hide_dataframe_index
import os
from PIL import Image
from correlation_page import correlation_page
# from data_page import data_page
from TF_page import TF_page

page_style = """
        <style>
        #MainMenu {visibility: hidden;}  
        footer  {visibility: hidden;}  
        div.css-1vq4p4l.e1fqkh3o4{padding: 2rem 1rem 1.5rem;}
        div.block-container{padding-top:3rem;}
        </style>
        """

# st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
# st.write('<style>div.css-1vq4p4l.e1fqkh3o4{padding: 4rem 1rem 1.5rem;}</style>', unsafe_allow_html=True)

st.markdown(page_style, unsafe_allow_html=True)

path = "./data"
protein_names = pd.read_csv(Path(path)/"protein_names.csv", index_col=0).T
celltype_names = pd.read_csv(Path(path)/"celltype_names.csv", index_col=0).T
dataset_info = pd.read_csv(Path(path)/"dataset_info.csv", index_col=0)
celltypes = celltype_names.iloc[0,:].tolist()
cell_count = pd.read_csv(Path(path)/"cell_count.csv")
cell_count.index.name = None

# get the gene names of mRNA violin plot
path_mRNA = ("./data/mRNA_data/violinPlot")

gene_list = sorted([x.split(".")[0][11:] for x in os.listdir(path_mRNA)])
path_data = Path(f"./data/CLR1norm") 

def spartan_page(setting):

    choose_spartan = option_menu("", ["Data overview", "TF activity analysis", "Protein-TF correlations"],
                                icons=['clipboard-data',
                                        'lightning-charge', 'bar-chart-line'],
                                menu_icon="arrow-return-right", default_index=0, orientation="horizontal",
                                styles={
                "container": {"padding": "5!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "18px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#FD5816"},
            }
            )
        

    if choose_spartan == "Protein-TF correlations":
        
        correlation_page(path_data)

    elif choose_spartan == "TF activity analysis":
        
        TF_page(path_data)

    elif choose_spartan == "Data overview":

        
        spartan_data = pd.read_csv(path_data/"celltype_info.csv", index_col=0)

        spartan_data.dropna(inplace=True)
        
        st.dataframe(spartan_data.style.format(
            {'RNArate': '{:.2f}', 'number of genes': '{:.0f}', 'number of TFs': '{:.0f}', 'number of proteins': '{:.0f}' }), use_container_width=True)
   
    
    # st.session_state.main = mainTitle2idx[choose2]

