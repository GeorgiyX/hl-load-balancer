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

3. Клонируем репозиторий со скриптами:

```bash
git clone https://github.com/GeorgiyX/hl-load-balancer.git
```

3. Сборка подготовка контейнеров *pushgateway* и *flask*:

```bash
sudo docker compose build
sudo docker compose up
```

4. Запуск:

```bash
screen -dmS app_and_pushgateway docker compose up
screen -dmS cpu_monitor ./cpu_usage.sh backend-1
```



**Настройка хоста балансировщика**

1. Настройка prometheus:

```bash
wget https://github.com/prometheus/prometheus/releases/download/v2.35.0/prometheus-2.35.0.linux-amd64.tar.gz
tar -xvzf prometheus-2.35.0.linux-amd64.tar.gz
```

2. Запуск prometheus:

```bash
screen -dmS prometheus_screen prometheus-2.35.0.linux-amd64/prometheus --config.file=/home/hl-load-balancer/prometheus.yml
```

3. Запуск haproxy:

```bash
screen -dmS haproxy_screen /root/haproxy/haproxy -f /root/hl-load-balancer/haproxy.cfg
```

4. Настройка grafana:

```bash
sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common wget
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt-get update
sudo apt-get install grafana
```

5. Запуск grafana:

```bash
sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl status grafana-server
sudo systemctl enable grafana-server.service
```



**Полезные ссылки**

1. Сборка и настройка happroxy с модулем для прометея - [ссылка](https://www.haproxy.com/blog/haproxy-exposes-a-prometheus-metrics-endpoint/).
2. Использование graphana, prometheus, pushgateway для мониторинга CPU load - [ссылка](https://devconnected.com/monitoring-linux-processes-using-prometheus-and-grafana/).