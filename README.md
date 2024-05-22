# SentimentAnalyser

## Description
Developed a Sentiment Analyser using TextBlob to get polarity for the sentence input by the user

Created backend API using Python and used Spring Boot WebApp as a Bastion Host. 
Front-end website is created using React.js

## Pre-requisites
Java(JRE), Python(>3.1), npm, mvn

## Installation

Run Python WebAPI:
- navigate to sa-logic/sa
- python -m pip install -r requirements.txt
- python -m textblob.download_corpora
- python sentiment_analysis.py

Run Java Spring Boot Web App:
- navigate to sa-webapp
- mvn install
- navigate to sa-webapp/target
- java -jar sentiment-analysis-web-0.0.1-SNAPSHOT.jar --sa.logic.api.url=http://localhost:5000

Run React Web App:
- navigate to sa-frontend
- npm install
- npm start

## Screenshots

<img width="1468" alt="image" src="https://github.com/jovin-nicholas/SentimentAnalyser/assets/32580407/a888a7f8-235c-4d17-84cf-72705cf1b481">
