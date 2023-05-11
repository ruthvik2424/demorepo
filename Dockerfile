FROM docker.io/library/centos
WORKDIR /code
COPY ./app.py /code
RUN yum install -y python \
&& yum install -y pip \
&& pip install flask \
&& pip install flask_cors
EXPOSE 5000
CMD ["RUN", "FLASK"]
