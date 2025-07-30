import plotly
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import plotly.express as pt
import os 
from dotenv import load_dotenv
import supabase 
load_dotenv()
from supabase import create_client, Client


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

#This is for the main page
st.markdown("<h1 style='text-align: center; font-size: 28px;'>Shelby County PH IDEAS Dashboard</h1>", unsafe_allow_html=True)


#This is for the Sidebar Menu 
st.sidebar.markdown("<h1 style='font-size: 36px;'>Menu</h1>", unsafe_allow_html=True)
page = st.sidebar.radio("Navigation", [
    "Home", 
    "Dashboard",  
    "About",  
    "FAQ", 
])

#This is for the pages of the Menu

#This is for the Homepage
if page == "Home":
    st.text("PH-IDEAS brings together a multidisciplinary team with a wide range of expertise in public health research, practice, health informatics and data analysts, policymakers and evaluation experts along with co-participation of the community-based organizations.")
    st.markdown("<h2 style='text-align: center;'>PH-Ideas Metrics</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 28px;'>-For Shelby County, TN-</p>", unsafe_allow_html=True)

#Bar Charts for Homepage
#Linked to Care Within 1 Month of diagnosis Bar Chart
    st.markdown("<h6 style='text-align: ;left;'>Linked to Care Within 1 Month of Diagnosis</h6>", unsafe_allow_html=True)
    
    data = supabase.table("prep_num").select("*").execute().data
    chart_data = pd.DataFrame(data)

    years = chart_data["year"]
    prep_num = chart_data["prep_num"]

    fig = go.Figure(data=go.Bar(x=years, y=prep_num, marker_color="Turquoise"))
    st.plotly_chart(fig)

#Virally suppressed among persons living with diagnosed HIV (PLWDH) Bar Chart
    st.markdown("<h6 style='text-align: center;'>Virally suppressed among persons living with diagnosed HIV (PLWDH)</h6>", unsafe_allow_html=True)
    
    data = supabase.table("vls_plwdh_perc").select("*").execute().data
    chart_data = pd.DataFrame(data)

    years = chart_data["year"]
    vls_plwdh_perc = chart_data["vls_plwdh_perc"]

    fig = go.Figure(data=go.Bar(x=years, y=vls_plwdh_perc, marker_color="Turquoise"))
    st.plotly_chart(fig)

#Concurrent HIV/AIDS diagnoses Bar Chart
    st.markdown("<h6 style='text-align: right;'>Concurrent HIV/AIDS diagnoses</h6>", unsafe_allow_html=True)
    
    data = supabase.table("aids_12m_num").select("*").execute().data
    chart_data = pd.DataFrame(data)

    years = chart_data["year"]
    aids_12m_num = chart_data["aids_12m_num"]

    fig = go.Figure(data=go.Bar(x=years, y=aids_12m_num, marker_color="Purple"))
    st.plotly_chart(fig)
    
elif page == "Dashboard":
    st.markdown("<h1 style='text-align: center;'>Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 28px;'>-For Shelby County, TN-</p>", unsafe_allow_html=True)

#Prep Users Line Chart
    data = supabase.table("prep_num").select("*").execute().data
    chart_data = pd.DataFrame(data)
    st.line_chart(chart_data,x="year" , y="prep_num")

    years = chart_data["year"]
    prep_num = chart_data["prep_num"]

#New HIV diagnoses Number Line Chart
    data = supabase.table("hivdx_num").select("*").execute().data
    chart_data = pd.DataFrame(data)
    st.line_chart(chart_data,x="year" , y="hivdx_num")

    years = chart_data["year"]
    hivdx_num = chart_data["hivdx_num"]

#New HIV diagnoses Rate Line Chart
    data = supabase.table("hivdx_rate").select("*").execute().data
    chart_data = pd.DataFrame(data)
    st.line_chart(chart_data,x="year" , y="hivdx_rate")

    years = chart_data["year"]
    hivdx_rate = chart_data["hivdx_rate"]

#Linked to Care With 1 Month of Diagnosis
    data = supabase.table("link_1m_perc").select("*").execute().data
    chart_data = pd.DataFrame(data)
    st.line_chart(chart_data,x="year" , y="link_1m_perc")

    years = chart_data["year"]
    link_1m_perc = chart_data["link_1m_perc"]

#Virally suppressed among persons living with diagnosed HIV (PLWDH) Line Chart
    data = supabase.table("vls_plwdh_perc").select("*").execute().data
    chart_data = pd.DataFrame(data)
    st.line_chart(chart_data,x="year" , y="vls_plwdh_perc")

    years = chart_data["year"]
    vls_plwdh_perc = chart_data["vls_plwdh_perc"]

#Persons living with diagnosed HIV (PLWDH) Line Chart
    data = supabase.table("plwdh_num").select("*").execute().data
    chart_data = pd.DataFrame(data)
    st.line_chart(chart_data,x="year" , y="plwdh_num")

    years = chart_data["year"]
    plwdh_num = chart_data["plwdh_num"]

#Persons living with diagnosed HIV (PLWDH) Line Chart
    data = supabase.table("plwdh_rate").select("*").execute().data
    chart_data = pd.DataFrame(data)
    st.line_chart(chart_data,x="year" , y="plwdh_rate")

    years = chart_data["year"]
    plwdh_rate = chart_data["plwdh_rate"]


elif page == "About":
    st.text("Bring together a multidisciplinary team with a wide range of expertise in public health research, practice, health informatics and data analysts, policymakers and evaluation experts along with co-participation of the community-based organizations.")
    
#Vision & Mission

#Vision
    st.markdown("<h2 style='text-align: center;'>Our Vision</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 28px;'>To empower, develop, and equip a resilient, diverse, and dynamic public health workforce capable of addressing current and emerging health challenges, fostering health equity, and safeguarding the well-being of communities.</p>", unsafe_allow_html=True)

#Mission   
    st.markdown("<h2 style='text-align: center;'>Our Mission</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Advance public health through a trained and dedicated workforce with the essential knowledge and skills to respond to current and emerging public health needs.</h2>", unsafe_allow_html=True)
    
 
elif page == "FAQ":
    st.header("Frequently Asked Questions")

#What is HIV and how does it spread?
    with st.expander("1. What is HIV and how does it spread?"):
        st.write(""" Human Immunodeficiency Virus is a virus that affects your immune system. It spreads through contact with certain body fluids, like blood and sexual fluids.
        Click the link below for more information from the World Health Organization (WHO):
        https://www.who.int/news-room/fact-sheets/detail/hiv-aids""")

#What are the signs of HIV?
    with st.expander("What are the signs of HIV?"):
        st.write("""Early signs can feel like the flu, such as fever, tiredness, and sore throat. Later on, people may lose weight or have swollen lymph nodes.
        Click the link below for more information from the Central of Disease Control and Prevention (CDC):
        https://www.cdc.gov/hiv/about/""")

#How do I get tested for HIV?
    with st.expander("How can I get tested for HIV?"):
        st.write("""You can get tested at health clinics, hospitals, or use home test kits.
        Click the link below for more information from the Shelby County Health Department for understanding PrEP/PEP and HIV Testing:
        https://www.shelbytnhealth.com/657/Free-HIV-Testing""")

#What's the difference between HIV and AIDS?
    with st.expander("What's the difference between HIV and AIDS?"):
        st.write("""HIV is the virus, and AIDS (Acquired Immunodeficiency Syndrome) is the late stage of HIV when the immune system is very weak.
        HIV.gov provides definition for both HIV and AIDS allowing readers to understand the difference and how both are acquired. 
        Click the link below to learn more information HIV.gov:
        https://www.hiv.gov/hiv-basics/overview/about-hiv-and-aids/what-are-hiv-and-aids""")


