FROM ubuntu:18.04

RUN /usr/sbin/useradd -u 1000 user

# Build based on nsjail provided dockerfile
RUN apt-get -y update && apt-get install -y \
    autoconf \
    bison \
    flex \
    gcc \
    g++ \
    git \
    libprotobuf-dev \
    libnl-route-3-dev \
    libtool \
    make \
    pkg-config \
    protobuf-compiler

RUN git clone https://github.com/google/nsjail/

# Latest as of making this challenge
RUN cd nsjail && git checkout 3.3

RUN cd nsjail && make && mv ./nsjail /bin && mv configs/bash-with-fake-geteuid.cfg /nsjail.cfg && cd .. && rm -rf nsjail
RUN sed -i 's/"\/bin\/bash"/"\/solve"/' /nsjail.cfg
RUN echo "\nmount {\n\tsrc: \"/tmp/solve\"\n\tdst: \"/solve\"\n\tis_bind: true\n}\n" | tee -a /nsjail.cfg

RUN apt-get install -y socat python3

COPY flag /
COPY runner.py /home/user/

# To compile
CMD ["bash"]

# To test
# CMD ["python3", "/home/user/runner.py"]

# Ensure you run the docker with --privileged
