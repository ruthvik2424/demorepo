FROM registry.access.redhat.com/ubi9:9.2-489
LABEL maintainer="Ruthvik Shinde ruthvikshinde553@gmail.com"
LABEL decription="This is a custom image which contain an ML Model running in Flask Api"
WORKDIR /code
COPY ./app.py /code 
COPY ./mode5.py /code 
COPY ./requirements.txt /code 
COPY ./stutter_detection_model.json /code 
COPY ./stutter_detection_modela.h5 /code 
RUN yum install -y python \
&& yum install -y pip \
&& pip install -r requirements.txt 
EXPOSE 5000
CMD ["python", "app.py"]
