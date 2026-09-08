# Spotpris Platform

A machine learning system that predicts Danish electricity spot prices,
running on a self-managed Kubernetes cluster.

This is a learning project, built between September 2026 and February 2027.
The goal is to understand how a system like this is built and operated —
not to ship a product.

## What it does

Electricity prices in Denmark change every hour. The price is set a day in
advance and published by Energinet, the national grid operator, through a
free public API.

The system:

1. Collects hourly spot prices for DK1 and DK2 and stores them
2. Trains a model on historical prices to predict the price one hour ahead
3. Serves that prediction over HTTP
4. Monitors itself — latency, throughput, and whether predictions are
   drifting away from reality

## Where it runs

The same system is deployed to three places:

| Environment | Purpose |
|---|---|
| k3d on a laptop | Development. Fast to create, fast to throw away |
| k3s on a Raspberry Pi 5 | Always on. Real operation over time |
| Azure (AKS) | Created and destroyed on demand with Terraform |

Running it in more than one place is deliberate. The interesting question is
not whether it works, but what breaks when it moves.

## Languages

Python for anything that involves learning from data — exploration, feature
engineering, model training.

Rust for anything that runs continuously or needs to be fast — data
collection, backtesting.

The inference server is written twice, once in each language, serving the
same model. The point is to measure the difference rather than assume it.

## Status

September 2026 — just started. Setting up the cluster.

See `PLAN.md` for the full six-month plan.

## Notes

Data source: [Energi Data Service](https://www.energidataservice.dk/)
(Energinet, free, no API key)

This is a solo learning project. Things will be wrong, and the commit
history is meant to show that.
