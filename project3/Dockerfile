FROM python:alpine
COPY script.py /home
COPY IF.txt /home/data/IF.txt
COPY Limerick-1.txt /home/data/Limerick-1.txt

WORKDIR /home
CMD ["python", "script.py"]