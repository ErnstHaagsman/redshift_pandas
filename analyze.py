import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import create_engine
from config import connstr

engine = create_engine(connstr)

with engine.connect() as conn, conn.begin():
    df = pd.read_sql("""
            select
              likesports as sports,
              liketheatre as theater,
              likeconcerts as concerts,
              likejazz as jazz,
              likeclassical as classical,
              likeopera as opera,
              likerock as rock,
              likevegas as vegas,
              likebroadway as broadway,
              likemusicals as musicals
            from users;""", conn)

# Map dataframe to have 1 for 'True', 0 for null, and -1 for False
def bool_to_numeric(x):
    if x:
        return 1
    elif x is None:
        return 0
    else:
        return -1

df = df.applymap(bool_to_numeric)

# Calculate correlations
corr = df.corr()

mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True

sns.heatmap(corr,
            mask=mask,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)

plt.xticks(rotation=45)
plt.yticks(rotation=45)

plt.tight_layout()
plt.show()
