FROM continuumio/miniconda3

RUN conda install -y numpy scipy
RUN pip install requests Flask flask-restful

RUN mkdir /app
ADD . /app
WORKDIR /app

# Default port is 3333.  Change both code and this value!
EXPOSE 3333

CMD python app.py