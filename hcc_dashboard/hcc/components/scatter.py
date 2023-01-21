from numpy import dot
from numpy.linalg import norm
import pandas as pd
import plotly.express as px

COLS_TO_DROP = [
    "PlateletCount",
    "CVS",
    "Hypertension",
    "Recurrence",
    "DaysToRecurrence",
]


def generate_cosine_sim(inputs):

    df = pd.read_csv("../data/training_data.csv").drop(COLS_TO_DROP, axis=1).T
    df_cos_sim = pd.DataFrame(columns=["patient_id", "cosine_sim"])

    for col in df.columns:
        cos_sim = dot(inputs, df[col]) / (norm(inputs) * norm(df[col]))
        df_temp = pd.DataFrame([col, cos_sim]).T
        df_temp.columns = ["patient_id", "cosine_sim"]
        df_cos_sim = pd.concat([df_cos_sim, df_temp])
    df_cos_sim.patient_id = df_cos_sim.patient_id.astype(int)
    df_cos_sim.cosine_sim = df_cos_sim.cosine_sim.astype(float)
    df_cos_sim = df_cos_sim.reset_index()
    df_cos_sim = df_cos_sim[df_cos_sim["cosine_sim"].astype(float) > 0.75]
    return df_cos_sim


def generate_scatter_plot(inputs):
    df_pats = pd.read_csv("../data/training_data.csv").drop(COLS_TO_DROP, axis=1).T
    df_cos_sim = generate_cosine_sim(inputs)

    fig = px.scatter(
        df_cos_sim,
        x="cosine_sim",
        y="index",
        # y="Approved Date",
        # color="DeID Doc",
        # size="No. of Px",
        # color_discrete_sequence=color_map,
    )

    fig = fig.update_yaxes(visible=False, showticklabels=False)
    fig.update_traces(hoverinfo="none", hovertemplate=None)
    fig.update_traces(
        marker=dict(size=12),
        # line=dict(width=2,
        # color='DarkSlateGrey')),
        # selector=dict(mode='markers')
    )
    return fig