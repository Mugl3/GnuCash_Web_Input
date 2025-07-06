#Todo - Autobuild using github actions a docker file with latest changes.
#Add ability to upload new account tree with GUI button
FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    gcc \
    musl-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY src/ .src/
COPY .streamlit/ .streamlit/

# RUN apk add --no-cache gcc musl-dev python3-dev
# RUN pip install pandas
RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]