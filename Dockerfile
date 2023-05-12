FROM python:3.10-alpine
WORKDIR /code
RUN mkdir /code/templates
COPY ./index.html /code/templates
COPY ./app.py /code
RUN pip install flask \
&& pip install flask_cors
ENV RUN=python
ENV FLASK=app.py
EXPOSE 5000
CMD ["RUN", "FLASK"]
