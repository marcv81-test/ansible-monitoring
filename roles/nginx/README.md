# nginx

Provides Nginx 1.12.1 and Certbot 0.10.2.

Configures Nginx to proxy the following services if available.
- InfluxDB at https://influxdb.hostname/
- Grafana at https://grafana.hostname/

Bootstraps Nginx with a fake TLS certificate. Then requests real certificates from Let's Encrypt and reload.
