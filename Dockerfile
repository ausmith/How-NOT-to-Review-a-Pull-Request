FROM ubuntu:18.04

WORKDIR /tmp/workspace

COPY . .

ENTRYPOINT ["/bin/bash"]
