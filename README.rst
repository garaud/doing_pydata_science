
Doing Data Science in Python
############################

**Python** code samples and solutions based on examples and exercises in `Doing
Data Science`_ by `Rachel Schutt <http://columbiadatascience.com/>`_ and `Cathy
O'Neil <http://mathbabe.org/>`_

These code samples and solutions are splitted into different `IPython/Jupyter
notebooks`_.

Clone this repo and launch ``ipython notebook`` at the root directory of this
project. You can also launch the Bash script ``launch.sh`` which carries out the
same command with some specific ipython options.

You can also use the NBViewer_ website to read a notebook.

**Note**: This repo aims to practice myself in Data Science and to show that's
easy to do Data Science in Python.

.. _Doing Data Science: http://shop.oreilly.com/product/0636920028529.do
.. _NBViewer: http://nbviwer.ipython.org/

Data Samples
============

Data samples can be downloaded at the official *Doing Data Science* Github
project at https://github.com/oreillymedia/doing_data_science

For some exercises, I provide a Python script which downloads needed files.

Notebooks
=========

* `Chapter 2 - Exploratory Data Analysis <http://nbviewer.ipython.org/github/garaud/doing_pydata_science/blob/master/chapter2-eda.ipynb>`_

  Play with some (simulated) data about ads shown and clicks recorded on the NY
  Time home page.

  The file ``down_nyt.py`` downloads the 31 CSV files into the ``nyt-data``
  directory. Just do::

    python down_nyt.py

  and wait... it can be a quite long.


Requirements
============

* `IPython notebook`_
* pandas_
* requests_

.. _pandas: http://pandas.pydata.org/
.. _requests: http://docs.python-requests.org/en/latest/
.. _IPython Notebook: http://ipython.org/notebook.html
.. _IPython/Jupyter Notebooks: http://ipython.org/notebook.html
.. _IPython Notebooks: http://ipython.org/notebook.html
