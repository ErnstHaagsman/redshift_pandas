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
              state,
              count(likesports) as sports,
              count(liketheatre) as theater,
              count(likeconcerts) as concerts,
              count(likejazz) as jazz,
              count(likeclassical) as classical,
              count(likeopera) as opera,
              count(likerock) as rock,
              count(likevegas) as vegas,
              count(likebroadway) as broadway,
              count(likemusicals) as musicals
            from users
            group by state;""", conn)


corr = df.corr()

mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True

sns.heatmap(corr,
            mask=mask,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values,
            vmin=0.95,
            vmax=1)

plt.xticks(rotation=45)
plt.yticks(rotation=45)

plt.tight_layout()
plt.show()
