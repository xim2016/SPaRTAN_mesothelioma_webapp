
import streamlit as st

from  streamlit_option_menu import option_menu

from data_page import data_page
from spartan_page import spartan_page


# page_style = """
#         <style>
#         #MainMenu {visibility: hidden;}  
#         footer  {visibility: hidden;}  
#         div.css-1vq4p4l.e1fqkh3o4{padding: 2rem 1rem 1.5rem;}
#         div.block-container{padding-top:3rem;}
#         </style>
#         """

# # st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
# # st.write('<style>div.css-1vq4p4l.e1fqkh3o4{padding: 4rem 1rem 1.5rem;}</style>', unsafe_allow_html=True)

# st.markdown(page_style, unsafe_allow_html=True)


def main_page(setting):

    with st.sidebar:

        choose2 = option_menu(setting, ["CITE-seq overview", "SPaRTAN analysis"],
                            icons=['clipboard-data',
                                    'lightning-charge'],
                            menu_icon="arrow-return-right", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "18px"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "orange"},
        }
        )
        

    if choose2 == "SPaRTAN analysis":
        
        spartan_page(choose2)

    elif choose2 == "CITE-seq overview":
        
        data_page(choose2)
   
    
    
    