FROM python:3.10

ENV HOME /app
WORKDIR $HOME

COPY requirements.txt .
RUN python3 -m pip install --no-cache -r requirements.txt
#RUN python -m pip install --upgrade pip
#RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
