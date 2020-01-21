# Dockerfile for make-goals-daily

# http://makegoalsdaily.com/

FROM fedora
MAINTAINER Sundeep Anand <web@sundeep.co.in>

RUN dnf -y update && dnf -y install make python3-pip git sqlite && dnf clean all

ENV PYTHONUNBUFFERED 1
RUN mkdir /workspace
WORKDIR /workspace
RUN git clone -b master https://github.com/sundeep-co-in/makegoalsdaily.git .
RUN make env && make migrate

EXPOSE 8080

CMD ["/workspace/launch.sh"]
