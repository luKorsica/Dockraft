FROM eclipse-temurin:21-jre

ARG JAR_FILE=server.jar

ENV MINECRAFT_VERSION=1.21.1 \
    SERVER_PORT=25565 \
    MEMORY_MIN=1G \
    MEMORY_MAX=2G \
    EULA=false

RUN groupadd -r minecraft && useradd -r -g minecraft minecraft

WORKDIR /minecraft
RUN mkdir -p /minecraft/world /minecraft/logs /minecraft/plugins /minecraft/config

COPY ${JAR_FILE} /minecraft/server.jar

RUN echo "eula=true" > eula.txt

RUN chown -R minecraft:minecraft /minecraft

EXPOSE $SERVER_PORT

USER minecraft

VOLUME ["/minecraft/world", "/minecraft/logs"]

CMD java -Xms$MEMORY_MIN -Xmx$MEMORY_MAX -jar server.jar nogui