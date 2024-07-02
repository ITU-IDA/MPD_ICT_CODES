# Documentation for Setting Up a Conda Environment with PySpark

This guide provides step-by-step instructions on setting up a Conda environment specifically for working with PySpark. PySpark requires a Java environment, so this setup includes installing Java alongside PySpark and other useful Python data science packages.

## Step 1: Install Conda Environment

Create a new Conda environment named `spark` and activate it. This environment will use Python 3.8. To do so, run the following commands in your terminal:

```bash
conda create --name spark python=3.8
conda activate spark
```

## Step 2: Install Java and Notebook Support

For PySpark to work, it requires Java. Additionally, to support Jupyter notebooks within this environment, we will install relevant packages. Execute the following commands:

```bash
conda install -c anaconda openjdk
conda install nb_conda_kernels
conda install anaconda::ipykernel
python -m ipykernel install --user --name spark
```

After installation, please reload any open web pages (e.g., Jupyter Notebook/Lab) to ensure that the new ipykernel is available in the UI.

## Step 3: Install Package Dependencies

To make the most of this environment, the following data analysis and visualization packages will be installed: PySpark, Pandas, NumPy, SciPy, tqdm, GeoPandas, Matplotlib, PyArrow, Folium, and Seaborn. These packages provide a comprehensive toolkit for data processing and visualization in Python.

Run the following commands to install these packages:

```bash
conda install -c conda-forge pyspark
pip install -q pandas numpy scipy tqdm geopandas matplotlib pyarrow folium seaborn
```

## Step 4: Test PySpark Installation

To ensure that PySpark has been correctly installed and configured, you can test it by checking the version of the Spark shell. This can be done by running the following command:

```bash
spark-shell --version
```

If installed correctly, this command will output the version of Spark alongside some additional environment information. This confirms that your Conda environment is set up and ready for PySpark development.

---

Remember, every time you wish to work with PySpark, you will need to activate the `spark` Conda environment using the `conda activate spark` command. This environment segregates your PySpark setup, ensuring it doesn't interfere with other Python projects or environments.


