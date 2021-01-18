FROM python:3.8

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#exposing default port for streamlit EXPOSE 8501
EXPOSE 8000

RUN mkdir ~/.streamlit
RUN cp config.toml ~/.streamlit/config.toml
RUN cp credentials.toml ~/.streamlit/credentials.toml

ENTRYPOINT ["streamlit", "run"]

CMD ["app/app.py"]