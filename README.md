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

To use the C3PO Navigation System, you can
A - create an instance of the `C3PO` class with the path to the `millennium-falcon.json` file. Then, call the `giveMeTheOdds` method with the path to the `empire.json` file to calculate the success probability.

B - execute `python app.py` in terminal and select the `millennium-falcon.json` and `empire.json` you want to use from the UI

### Example

```python

c3po = C3PO('examples/example1/millennium-falcon.json')
odds = c3po.giveMeTheOdds('examples/example1/empire.json')
print(f"The probability of success is: {odds:.2f}")
```

or run this command in ther terminal
```python

python app.py
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

## Extensions

### User Experience

**1. Intuitive Interface:**

To make sure clients really get how to use the software and find it useful, I’d design the UI with some key features:

- **Easy File Uploads:** Users would upload their Millennium Falcon and Empire JSON files through simple "Select File" buttons. I’d make sure the software checks the files for issues like wrong formats or missing data and tells users right away if there’s a problem.

- **Clear Instructions and Feedback:** The app would give clear instructions and instant feedback. After uploading files, users would see progress updates and confirmation messages, so they know exactly what’s happening and what to do next.

- **Visualizations:** To enhance user understanding, I would incorporate visualizations that display routes and travel times on an interactive map. This feature would provide users with a clear, graphical representation of their data, making it easier to grasp the navigation paths and travel durations at a glance

- **Results Presentation:** Results would be shown in a dedicated section, making it easy for users to see the maximum probability of success. I’d make sure the information is straightforward and easy to interpret.

**2. User Testing and Iteration:**

In real life, I’d make sure the app is tested with real users to get their feedback. Based on what they say, I’d tweak and improve the design to make sure it works well for everyone.

**3. Documentation and Training:**

To help users understand and use the software, I’d provide:

- **User Guides:** Detailed guides with step-by-step instructions and screenshots to help users get started and solve any problems they might have.

- **Training Sessions:** Optional training sessions for key users to walk them through the software’s features and how to use them effectively.

### Ease of Deployment and Operation

**1. Easy Deployment:**

**Packaging and Distribution:**

- **Standalone Executable:** I’d package the software as a standalone executable or installer. This way, users wouldn’t have to worry about installing additional dependencies or setting up environments manually.

- **Automated Setup:** An automated setup process would be included, probably through an installer or setup wizard. This would ensure that everything is installed and configured correctly, making the deployment process smoother and reducing the chances of errors. I have recently discovered my self from doing an internship that setting up the software for the first time can often be an ardous process.
