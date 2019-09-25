# FROM continuumio/miniconda3

# Take the base-image
FROM pytorch/pytorch:0.4.1-cuda9-cudnn7-devel

# Prepare miniconda
RUN apt-get update && apt-get install -y curl

# Install miniconda to /miniconda
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
RUN bash Miniconda-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda

# Create environment
ADD environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml

# Activate environment
RUN echo "source activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH
# Activate environment in detach mode


# Install some dependencies
RUN apt-get install -y libsm6 libxext6 libxrender-dev

# Add files
ADD src /StructSeg
WORKDIR /StructSeg