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
FROM mcr.microsoft.com/dotnet/sdk:7.0 as chroot

RUN /usr/sbin/useradd -u 1000 user

COPY currency_conversion.txt flag.txt MichaelBank.deps.json MichaelBank.dll MichaelBank.runtimeconfig.json michael_password.txt /home/user/

FROM gcr.io/kctf-docker/challenge@sha256:d884e54146b71baf91603d5b73e563eaffc5a42d494b1e32341a5f76363060fb

COPY --from=chroot / /chroot

COPY nsjail.cfg /home/user/

CMD kctf_setup && \
    kctf_drop_privs \
    socat \
      TCP-LISTEN:1337,reuseaddr,fork \
      EXEC:"kctf_pow nsjail --config /home/user/nsjail.cfg -- /usr/bin/env DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=false LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 /usr/bin/dotnet MichaelBank.dll"
