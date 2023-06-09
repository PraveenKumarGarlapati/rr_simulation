# # app/Dockerfile

# FROM python:3.9-slim

# WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

# RUN git clone https://github.com/PraveenKumarGarlapati/rr_simulation.git .

# RUN pip3 install -r requirements.txt

# EXPOSE 8080

# HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

# ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0"]


FROM python:3.9

WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]

# CMD streamlit run --server.port 8080 --server.enableCORS false main.py