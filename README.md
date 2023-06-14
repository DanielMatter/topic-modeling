# Introduction to Topic Modeling
This Repository is meant to provide an accessible introduction to topic modeling with a focus on Python.


## What is Topic Modeling?
Topic modeling is a method for unsupervised learning of the latent topics that occur in a collection of documents. It is a form of dimensionality reduction, in which the number of dimensions is reduced from the vocabulary of the documents to the number of topics. Topic modeling is a powerful tool for the discovery of hidden semantic structures in a text body. It is used for a variety of tasks, including document clustering, information retrieval, and recommender systems.

## Structure of this Repository
This repository includes a general introduction to topic modeling, as well as chapters on each of the presented methods.
Each part is accompanied by a Jupyter Notebook, which contains the code used to generate the results presented in the chapter.

**Please read through the data section, before starting the course.**


## Installation
To follow along with the code in this repository, you will need to install Jupyter Notebooks on your machine.
The easiest way to do this is to install the [Anaconda Distribution](https://www.anaconda.com/distribution/), which includes Jupyter Notebooks as well as many other useful packages for data science.

Once you installed Juypter, you can clone this repository to your machine by running the following command in your terminal:
```bash
git clone https://github.com/DanielMatter/topic-modeling.git
```

This repository depends on an array of packages, which are listed in ```requirements.txt```.
To install these packages, run the following command in your terminal:
```bash
pip install -r requirements.txt
```
If you are using Anaconda, you can also create a new environment with the required packages by running the following command in your terminal:
```bash
conda create --name topic-modeling --file requirements.txt
```

You will also need to install the ```en_core_web_sm``` model for spaCy, which can be done by running the following command in your terminal:
```bash
python3 -m spacy download en_core_web_sm
```


## Data
The quality of data is probably the single most important factor for the success of a topic modeling project. As data is only sparsely available and of poor quality, it is essential to understand the type and limitation of data at hand. To this end, each algorithm will be performed on two datasets with different characteristics.
The first dataset (News Articles)[https://huggingface.co/datasets/valurank/News_Articles_Categorization] contains 3,722 news articles from 8 different categories. The second dataset (News Headers)[https://huggingface.co/datasets/ag_news] contains 120,000 news headlines from 4 different categories.

Both datasets are available through Huggingface and hence do not come packaged with this repository.
However, to reproduce a more general workflow, we include ```download_data.ipynb``` in the ```data``` folder, which can be used to download the data from Huggingface and save it to the ```data``` folder. _We ask you to execute this script before starting the course._
