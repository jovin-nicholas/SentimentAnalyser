FROM python:3.6.6-alpine
COPY sa /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 -m textblob.download_corpora
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["sentiment_analysis.py"]