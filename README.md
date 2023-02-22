# Lighthouse_ds_challenge


# Introduction  

This project has the objective of analyzing a dataset containing information from urban traffic of the city of São Paulo in Brazil and walk through the process of build a machine learning model to predict the traffic slowness percentage.

The original dataset can be accessed via the link below  
https://archive.ics.uci.edu/ml/datasets/Behavior+of+the+urban+traffic+of+the+city+of+Sao+Paulo+in+Brazil

The processes contained in this document consist of:

- Exploratory Data Analysis
- Feature Engineering
- Modeling
- Deploy


# Instructions for use

## Project Report

There is a project report notebook on the _notebooks/Project_Report.ipynb_ path  and also a pdf version.

## Overview

This is your new Kedro project, which was generated using `Kedro 0.18.4`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.


## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, `catalog`, and `startup_error`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r src/requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```
