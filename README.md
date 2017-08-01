Analyzing Data in Redshift with Pandas
======================================

This is a sample project for a blog post at:
https://blog.jetbrains.com/pycharm/2017/08/analyzing-data-in-amazon-redshift-with-pandas

To run the code, copy `config.py.example` to `config.py` and complete the connection 
string to the appropriate value for your AWS Redshift cluster.

Dependencies:
-------------

- Seaborn
- Pandas
- SQLAlchemy
- SQLAlchemy-redshift
- Psycopg2

As these dependencies are hard to install on many platforms, I recommend using Anaconda. 
The SQLAlchemy-redshift package is available from the `conda-forge` channel.

For additional details, 
[see the blog post](https://blog.jetbrains.com/pycharm/2017/08/analyzing-data-in-amazon-redshift-with-pandas)