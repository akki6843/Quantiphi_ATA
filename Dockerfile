# Use an official Ubuntu base image
FROM ubuntu:20.04

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget bzip2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

# Update PATH environment variable
ENV PATH /opt/conda/bin:$PATH

# Copy the quantiphi.yaml file to the working directory
COPY quantiphi.yaml /app/

# Set the working directory
WORKDIR /app

# Create the conda environment from the quantiphi.yaml file
RUN conda env create -f quantiphi.yaml

# Activate the conda environment
RUN echo "source activate $(head -n 1 quantiphi.yaml | cut -d' ' -f2)" > ~/.bashrc

# Update PATH to include the conda environment
ENV PATH /opt/conda/envs/$(head -n 1 quantiphi.yaml | cut -d' ' -f2)/bin:$PATH

# Copy the src folder to the working directory
COPY src /app/src

# Change the working directory to src
WORKDIR /app
RUN chmod +x /app/src
RUN pip install streamlit
EXPOSE 8501

# Run the Streamlit application
ENTRYPOINT ["python", "-m", "streamlit", "run", "./textbook_Q_n_A.py", "--server.port=8501"]
