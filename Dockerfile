FROM python:3.10-alpine
WORKDIR /code
RUN mkdir /code/templates
COPY ./index.html /code/templates
COPY ./app.py /code
RUN pip install flask \
&& pip install flask_cors
EXPOSE 5000
CMD ["python", "app.py"]
