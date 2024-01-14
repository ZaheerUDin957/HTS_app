import streamlit as st
from ML.ML_cl import MLClassificationPage
from ML.ML_reg import MLRegressionPage
from DL.DL_cl import DLClassificationPage
from DL.DL_reg import DLRegressionPage
from Data_Analytics.Analytics import AnalyticsPage

class App:
    def __init__(self):
        self.pages = {
            'Data Analytics': AnalyticsPage,
            'ML Classification': MLClassificationPage,
            'ML Regression': MLRegressionPage,
            'DL Classification': DLClassificationPage,
            'DL Regression': DLRegressionPage
        }
        self.page_names = list(self.pages.keys())
        self.current_page_name = st.sidebar.radio("Select a page", self.page_names, 0)

    def run(self):
        page = self.pages[self.current_page_name]()
        page.run()

if __name__ == "__main__":
    app = App()
    app.run()
