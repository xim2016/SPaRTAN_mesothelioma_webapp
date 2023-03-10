from pathlib import Path
import streamlit as st

from os import listdir
from os.path import isfile, join


page_style = """
        <style>
        #MainMenu {visibility: hidden;}  
        footer  {visibility: hidden;}  
        div.css-1vq4p4l.e1fqkh3o4{padding: 2rem 1rem 1.5rem;}
        div.block-container{padding-top:3rem;}
        </style>
        """

st.markdown(page_style, unsafe_allow_html=True)

path_ADT = "./data/Nanostring_data/dotPlot"

filenames = [f for f in listdir(path_ADT) if isfile(join(path_ADT, f))]
genepaths = [x.split("_")[2] + "_"+ x.split("_")[3].split(".")[0] for x in filenames]
genenames = [ x.split("_")[3].split(".")[0] for x in filenames]

gene2path = dict(zip(genenames, genepaths))


def nanostring_page():
    st.markdown("### Nanostring gene information", True)        
    c1, c2 = st.columns([7,2])
    gene_selected = c1.selectbox(
        'Genes',
        sorted(genenames),
        0
    )

    imgfile = str(Path(path_ADT) / f"Dotplot_Nanostring_{gene2path[gene_selected]}.png"
                    )

    st.image(imgfile)