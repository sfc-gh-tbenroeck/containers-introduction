# https://docs.snowflake.com/en/developer-guide/snowpark/python/setup
# https://github.com/snowflakecorp/frostbytes/blob/312d1cdee023bf8690ad18eed1d6ff7ba0345e5b/Tasty%20Bytes/30%20-%20vignettes/Workload%20Deep%20Dive/Data%20Science/Snowpark%20101/README.md


# Use a base image with Miniconda (Python 3.10) installed
FROM continuumio/miniconda3:4.10.3

# Create a new conda environment with Python 3.10 and install necessary packages
RUN conda create --name snowpark_env python=3.10 --override-channels -c https://repo.anaconda.com/pkgs/snowflake -y && \
    echo "conda activate snowpark_env" >> ~/.bashrc

# Use the new environment to install packages
SHELL ["conda", "run", "-n", "snowpark_env", "/bin/bash", "-c"]

# Install necessary packages using conda and pip
RUN conda install -c https://repo.anaconda.com/pkgs/snowflake numpy pandas scikit-learn joblib cachetools pyarrow=8.0.0 snowflake-snowpark-python ipykernel -y && \
    pip install --no-cache-dir matplotlib plotly notebook


# Create a folder named 'examples'
RUN mkdir -p /example

# Copy files into the 'examples' folder
COPY  notebooks/default.ipynb /example/default.ipynb
COPY notebooks/snowpark_auth.json.template /example/snowpark_auth.json

# Set the working directory
WORKDIR /notebooks

# The default command to run when starting the container
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]
