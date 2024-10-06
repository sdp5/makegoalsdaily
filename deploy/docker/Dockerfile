# Dockerfile for make-goals-daily

FROM fedora
LABEL maintainer="suanand@fedoraproject.org"

RUN dnf -y update && dnf -y install make python3-pip git sqlite && dnf clean all

ENV PYTHONUNBUFFERED=1
RUN mkdir /workspace
WORKDIR /workspace
RUN git clone -b main https://github.com/sdp5/makegoalsdaily.git .
RUN make env

EXPOSE 8080

CMD ["/workspace/deploy/server.sh"]
