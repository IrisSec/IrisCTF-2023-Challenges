# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
FROM ubuntu:18.04 as chroot

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

FROM gcr.io/kctf-docker/challenge@sha256:d884e54146b71baf91603d5b73e563eaffc5a42d494b1e32341a5f76363060fb

COPY --from=chroot / /chroot

COPY nsjail.cfg /home/user/

CMD kctf_setup && \
    kctf_drop_privs \
    socat \
      TCP-LISTEN:1337,reuseaddr,fork \
      EXEC:"kctf_pow nsjail --config /home/user/nsjail.cfg -- /usr/bin/python3 /home/user/runner.py"
