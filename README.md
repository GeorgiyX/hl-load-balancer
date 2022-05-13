**Настройка хоста backend**

1. Установка docker:

```bash
sudo apt-get update
sudo apt install -y ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

2. Запуск скрипта сбора метрики cpu_usage:

``` 
./cpu_usage.sh host-1
```

3. Клонируем репозиторий со скриптами:

```bash
git clone git@github.com:GeorgiyX/hl-load-balancer.git
```

3. Запуск контейнеров с *pushgateway* и *flask*:

```bash
sudo docker compose build
sudo docker compose up
```



**Настройка хоста балансировщика**

```bash
docker run -p 9090:9090 -v prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```