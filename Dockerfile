FROM python:3.10-alpine
WORKDIR /code
COPY ./app.py /code
RUN pip install flask \
&& pip install flask_cors
EXPOSE 5000
CMD ["RUN", "FLASK"]
