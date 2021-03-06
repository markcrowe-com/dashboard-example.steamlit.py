from pandas import read_csv, DataFrame, to_datetime
from matplotlib import pyplot
import streamlit

filepath: str = "./assets/cso-tsa04-cattle-beef-exports-eda-output.csv"


def show_explore_page():
    exports_dataframe: DataFrame = read_csv(filepath)
    exports_dataframe = exports_dataframe.set_index('Year')
    exports_dataframe.index = to_datetime(exports_dataframe.index, format='%Y')

    streamlit.header("Exports")

    streamlit.subheader("Data")
    streamlit.dataframe(exports_dataframe)

    streamlit.subheader("Stats")
    streamlit.dataframe(exports_dataframe.describe())

    streamlit.subheader("Graph")
    streamlit.line_chart(exports_dataframe, use_container_width=True)

    streamlit.subheader("Histogram")
    figure, axis = pyplot.subplots()
    axis.hist(exports_dataframe, bins=20)
    streamlit.pyplot(figure)
