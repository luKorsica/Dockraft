FROM eclipse-temurin:21-jre

ARG MINECRAFT_VERSION=1.21.8
ARG PAPER_BUILD=30

ENV SERVER_PORT=25565 \
    MEMORY_MIN=1G \
    MEMORY_MAX=2G \
    RCON_PASSWORD=minecraft123

# Créer l'utilisateur minecraft
RUN groupadd -r minecraft && useradd -r -g minecraft minecraft

# Installer mcrcon
RUN apt-get update && \
    apt-get install -y --no-install-recommends wget ca-certificates && \
    cd /tmp && \
    wget -q https://github.com/Tiiffi/mcrcon/releases/download/v0.7.2/mcrcon-0.7.2-linux-x86-64.tar.gz && \
    tar -xzf mcrcon-0.7.2-linux-x86-64.tar.gz && \
    mv mcrcon /usr/local/bin/ && \
    chmod +x /usr/local/bin/mcrcon && \
    rm -rf /tmp/* && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /minecraft

RUN mkdir -p /minecraft/world /minecraft/logs /minecraft/plugins /minecraft/config

# Télécharger le JAR du serveur
RUN wget -q https://api.papermc.io/v2/projects/paper/versions/${MINECRAFT_VERSION}/builds/${PAPER_BUILD}/downloads/paper-${MINECRAFT_VERSION}-${PAPER_BUILD}.jar -O /minecraft/server.jar

RUN echo "eula=true" > eula.txt

# Créer un server.properties de base avec RCON activé
RUN echo "enable-rcon=true" > server.properties && \
    echo "rcon.port=25575" >> server.properties && \
    echo "rcon.password=${RCON_PASSWORD}" >> server.properties && \
    echo "server-port=${SERVER_PORT}" >> server.properties

RUN chown -R minecraft:minecraft /minecraft

EXPOSE $SERVER_PORT 25575

USER minecraft

VOLUME ["/minecraft/world", "/minecraft/logs"]

CMD java -Xms$MEMORY_MIN -Xmx$MEMORY_MAX -jar server.jar nogui