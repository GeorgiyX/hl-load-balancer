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
screen -dmS prometheus_screen prometheus-2.35.0.linux-amd64/prometheus --config.file=/root/hl-load-balancer/prometheus.yml
```

3. Запуск haproxy:

```bash
screen -dmS haproxy_screen /root/haproxy/haproxy -f /root/hl-load-balancer/haproxy.cfg -db
```

4. Настройка grafana:

```bash
sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common wget
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt-get update
sudo apt-get install grafana
sudo systemctl daemon-reload
sudo systemctl enable grafana-server.service
```

5. Запуск grafana:

```bash
sudo systemctl start grafana-server
```



**Результаты тестирования**

* C 3:16:00 по 3:17:15 backend-1 перезагружался.  Запросы были распределены между backend-2 backend-3

<img src="/mnt/files/Programming/Python/l4-balancer/.img/cpu_per_backed.png" alt="cpu_per_backed" style="zoom:50%;" />

<img src="/mnt/files/Programming/Python/l4-balancer/.img/rps_per_back.png" alt="rps_per_back" style="zoom:50%;" />

<img src="/mnt/files/Programming/Python/l4-balancer/.img/total_rps.png" alt="total_rps" style="zoom:50%;" />