# Ambiente de execução de referência — Foremost-NG (T8/LEAS)
#
# Imagem Ubuntu limpa, escrita do zero. NÃO deriva do Dockerfile dos autores
# (foremost-ng-bb812a22/Dockerfile), que faz parte do artefato avaliado.
# O código do artefato NÃO é copiado nem compilado aqui: a compilação é passo
# do roteiro e será feita, gravada, dentro do contêiner.
#
# Justificativas de versão e de cada pacote: ambiente.md (mesma pasta).
#
# Construção (na pasta ambiente/):
#   docker build -t t8/foremost-ng-ref:noble-20250619-snap20250708 .

# Ubuntu 24.04 LTS, última tag datada anterior ao commit bb812a22 (08/07/2025).
FROM ubuntu:noble-20250619@sha256:440dcf6a5640b2ae5c77724e68787a906afb8ddee98bf86db94eea8528c2c076

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8

# Fixa o estado do arquivo apt no instante do commit fixado (snapshot.ubuntu.com).
ARG APT_SNAPSHOT=20250708T190020Z
RUN echo "APT::Snapshot \"${APT_SNAPSHOT}\";" > /etc/apt/apt.conf.d/50snapshot

# Bootstrap: a imagem base não traz certificados e o serviço de snapshot só
# atende por HTTPS. Somente este passo desliga a verificação TLS; a integridade
# dos índices e pacotes continua garantida pela assinatura GPG do apt.
RUN apt-get update -o Acquire::https::Verify-Peer=false \
 && apt-get install -y --no-install-recommends -o Acquire::https::Verify-Peer=false \
      ca-certificates=20240203 \
 && rm -rf /var/lib/apt/lists/*

# Dependências indicadas pelo README/artigo/Makefile do SHA fixado (ver ambiente.md).
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      gcc=4:13.2.0-7ubuntu1 \
      gcc-13=13.3.0-6ubuntu2~24.04 \
      make=4.3-4.1build2 \
      libssl-dev=3.0.13-0ubuntu3.5 \
      libcurl4-openssl-dev=8.5.0-2ubuntu10.6 \
      git=1:2.43.0-1ubuntu7.3 \
      sudo=1.9.15p5-3ubuntu5.24.04.1 \
      man-db=2.12.0-4build2 \
 && rm -rf /var/lib/apt/lists/*

# Instrumentação do registro (não é dependência do artefato):
# unzip para abrir pacote/artefato.zip; `script` (util-linux) já vem na base.
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      unzip=6.0-28ubuntu4.1 \
 && rm -rf /var/lib/apt/lists/*

# A imagem minimizada troca /usr/bin/man por um aviso; restaura o man real
# (mesmo procedimento do `unminimize`) para que `man foremost-ng` funcione.
RUN if [ -f /usr/bin/man.REAL ]; then \
      rm -f /usr/bin/man && dpkg-divert --quiet --remove --rename /usr/bin/man; \
    fi

# Usuário comum com sudo, porque README e artigo usam `sudo make install`.
RUN useradd -m -s /bin/bash revisor \
 && echo 'revisor ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/revisor \
 && chmod 0440 /etc/sudoers.d/revisor

USER revisor
WORKDIR /home/revisor
CMD ["/bin/bash"]
