# Intelligent Log Monitoring System

## Overview
This project is a log monitoring and anomaly detection system built using Flask and DevOps practices.

## Features
- Upload log files
- Detect errors using keywords
- Identify anomalies based on error frequency
- Dashboard visualization
- Dockerized deployment
- CI/CD using GitHub Actions

## Tech Stack
- Python (Flask)
- Docker
- GitHub Actions

## How to Run

### Local
pip install -r requirements.txt  
python app.py  

### Docker
docker build -t log-monitor .  
docker run -p 5000:5000 log-monitor  

## Future Work
- ML-based anomaly detection
- Real-time log streaming