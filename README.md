# C3PO Navigation System for the Millennium Falcon

## Overview

The C3PO Navigation System is designed to help the Millennium Falcon navigate through various star systems while avoiding bounty hunters and ensuring timely arrival at the destination. This system takes into account the Falcon's autonomy (maximum travel days without refueling) and calculates the best route to maximize the probability of a successful mission.

## Features

- **Route Planning:** Uses a breadth-first search algorithm to explore all possible routes from the starting planet to the destination.
- **Bounty Hunter Avoidance:** Adjusts the probability of success based on the presence of bounty hunters on various planets.
- **Refueling Management:** Considers the need for refueling and incorporates it into the route planning process.
- **JSON Configuration:** Loads route and bounty hunter data from JSON files for easy configuration and extension.

## Project Structure

```
.

├── examples
│   ├── example1
│   │   ├── millennium-falcon.json
│   │   ├── empire.json
│   ├── example2
│   │   ├── millennium-falcon.json
│   │   ├── empire.json
│   ├── example3
│   │   ├── millennium-falcon.json
│   │   ├── empire.json
│   ├── example4
│       ├── millennium-falcon.json
│       ├── empire.json
└── test_examples
    ├── millennium-falcon.json
    ├── invalid_mlf.json
├── cp30_tests.py
├── cp30.py
├── README.md
```

## Getting Started

### Prerequisites

- Python 3.6 or higher
- `unittest` library (part of the Python standard library)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-repo/c3po-navigation.git
    ```

2. Ensure you have the required JSON files in the `examples` and `test_examples` directories.

### Running the Tests

Use the following command to run the unit tests:

```sh
python -m unittest c3po_tests.py -v
```

## Usage

To use the C3PO Navigation System, create an instance of the `C3PO` class with the path to the `millennium-falcon.json` file. Then, call the `giveMeTheOdds` method with the path to the `empire.json` file to calculate the success probability.

### Example

```python
from cp30 import C3PO

c3po = C3PO('examples/example1/millennium-falcon.json')
odds = c3po.giveMeTheOdds('examples/example1/empire.json')
print(f"The probability of success is: {odds:.2f}")
```

## JSON File Structure

### millennium-falcon.json

```json
{
    "autonomy": 6,
    "routes": [
        {
            "origin": "Tatooine",
            "destination": "Dagobah",
            "travelTime": 6
        },
        ...
    ]
}
```

### empire.json

```json
{
    "countdown": 7,
    "bounty_hunters": [
        {
            "planet": "Tatooine",
            "day": 4
        },
        ...
    ]
}
```
