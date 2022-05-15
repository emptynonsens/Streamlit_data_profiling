import  pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import streamlit as st

st.set_page_config(layout="wide")
c = st.container()

def print_data(dataSource):
    data = pd.read_csv(dataSource)
    st.dataframe(data)

    profilerTypeList = ['Minimal', 'Full']
    profilerTyp = st.selectbox('REPORT TYPE', profilerTypeList, 0)

    if profilerTyp == profilerTypeList[0]:
        report = ProfileReport(data, minimal=True)
    elif profilerTyp == profilerTypeList[1]:
        report = ProfileReport(data)

    st_profile_report(report)

with c:
    availible_datasets = ['Your own dataset (or choose some other)','attention','diamonds', 'penguins', 'planets', 'titanic', 'flights', 'geyser', 'car_crashes', 'brain_networks']

    dataset = st.selectbox('Datasets', availible_datasets, 0)

    if dataset == availible_datasets[0]:

        data = st.file_uploader("Choose your own file")
        if data == None:
            st.write('Waiting for dataset')
        else:
            print_data(data)

        #print_data(data)
    else:
        st.write('Dataset from https://github.com/mwaskom/seaborn-data', unsafe_allow_html=True)
        link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/%s.csv' % (dataset)
        print_data(link)
