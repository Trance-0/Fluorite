docker run \
    -d \
    --restart=on-failure:5 \
    --pull=always \
    --name=sakurafrp \
    natfrp/frpc \
    -f <启动参数>