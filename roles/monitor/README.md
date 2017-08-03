# monitor

Provides InfluxDB 1.3.1 and Grafana 4.4.1.

## InfluxDB

Uses the CLI to anonymously create an admin user. Updates the configuration to require authentication. Uses the CLI as admin to create a database and users to store Telegraf metrics.

## Grafana

Uses API calls to create the datasource, a dashboard, and user accounts.
