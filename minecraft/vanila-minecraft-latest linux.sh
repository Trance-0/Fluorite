docker run -d --name mc-server-snapshot -v minecraft-vanila-snapshot:/data -e VERSION=SNAPSHOT -e MEMORY=8G -p 25525:25525 -e EULA=TRUE itzg/minecraft-server:java21