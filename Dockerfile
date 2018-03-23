FROM ubuntu:16.04

WORKDIR /tmp/workspace

COPY . .

ENTRYPOINT ["/bin/bash"]
