#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_cars(owner, **cars):
    print(f"Owner name: {owner}")
    for car, name in cars.items():
        print(f"{car }: {name}")


if __name__ == "__main__":
    print_cars(
        "Dmitriy",
        cars=["ГАЗ-3102", "Jaguar XF", "Toyota Camry"]
    )
