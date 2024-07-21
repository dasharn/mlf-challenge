import json
from collections import deque, defaultdict
from typing import Dict, List, Tuple


class C3PO:
    """
    A class to represent the Millennium Falcon's navigation system.

    Attributes:
        mf_data (dict): Data loaded from the Millennium Falcon JSON file.
        autonomy (int): The autonomy of the Millennium Falcon in days.
        routes (list): A list of routes available for travel.
        graph (defaultdict): A graph representation of routes for navigation.

    Methods:
        __init__(self, millenniumFalconJsonFilePath): Initializes the C3PO object with data from the Millennium Falcon JSON file.
        _load_json(self, file_path): Loads JSON data from a file.
        _build_graph(self): Builds a graph from the routes data.
    """

    def __init__(self, millenniumFalconJsonFilePath: str) -> None:
        """
        Initializes the C3PO object with data from the Millennium Falcon JSON file.

        Parameters:
            millenniumFalconJsonFilePath (str): The file path to the Millennium Falcon JSON data file.
        """
        self.mf_data = self._load_json(millenniumFalconJsonFilePath)
        self.autonomy = self.mf_data['autonomy']
        self.routes = self.mf_data['routes']
        self.graph = self._build_graph()
    
    def _load_json(self, file_path: str) -> Dict:
        """
        Loads JSON data from a file.

        Parameters:
            file_path (str): The file path to the JSON data file.

        Returns:
            dict: The JSON data loaded from the file.

        Raises:
            ValueError: If the file is not found or the JSON format is invalid.
        """
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise ValueError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {file_path}")

    def _build_graph(self) -> Dict[str, List[Tuple[str, int]]]:
        """
        Builds a graph from the routes data.

        The graph is represented as a defaultdict of lists, where each key is a planet (origin),
        and the value is a list of tuples (destination, travelTime) representing the routes from that planet.

        Returns:
            defaultdict: The graph representing the routes.
        """
        graph = defaultdict(list)
        for route in self.routes:
            origin, destination, travel_time = route['origin'], route['destination'], route['travelTime']
            graph[origin].append((destination, travel_time))
            graph[destination].append((origin, travel_time))
        return graph
    
    def giveMeTheOdds(self, empireJsonFilePath: str) -> float:
        """
        Calculates the maximum probability of successfully reaching the destination before the countdown ends.

        This method implements a breadth-first search (BFS) algorithm to explore all possible routes from the start
        planet to the destination, considering the autonomy of the Millennium Falcon, the presence of bounty hunters,
        and the countdown until the mission fails. It updates the probability of success based on the presence of
        bounty hunters on each planet visited.

        Parameters:
            empireJsonFilePath (str): The file path to the JSON file containing the empire's data, including the countdown,
                                    bounty hunters' locations, and their schedules.

        Returns:
            float: The maximum probability of successfully reaching the destination before the countdown ends.
        """
        # Load empire data from the provided JSON file path
        empire_data = self._load_json(empireJsonFilePath)
        # Extract the countdown and bounty hunters information from the empire data
        countdown = empire_data['countdown']
        bounty_hunters = self._parse_bounty_hunters(empire_data['bounty_hunters'])
        
        # Set the starting planet and the destination
        start = 'Tatooine'
        destination = 'Endor'
        
        # Initialize the BFS queue with the starting position, day 0, full autonomy, and initial probability of success as 1.0
        queue = deque([(start, 0, self.autonomy, 1.0)])

        # Use a nested defaultdict to keep track of visited states with their corresponding probability of success
        # The use of defaultdict with lambda functions allows for dynamic and on-demand creation of nested dictionaries and default values. This means that you don't need to initialize the structure for all possible keys ahead of time. Instead, any attempt to access a non-existent key will automatically initialize it with the specified default structure or value. This is highly efficient for sparse data where only a subset of all possible key combinations will actually be used.

        #Purpose of Each Level:
        #First Level (Outermost): Represents the current planet or location in the traversal. This allows the algorithm to keep track of different locations separately.
        #Second Level: Represents the day in the traversal. This is crucial for algorithms that need to consider the progression of time or steps, as it allows tracking the state of each location at different times.
        #Third Level (Innermost): Represents the autonomy level or any other metric that might change as the traversal progresses. This level allows tracking finer-grained state information that could affect the outcome or decision-making process.
        #Value (Float): The final value represent the probability of success
        visited = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
        
        # Initialize the maximum probability of success to 0.0
        max_prob_success = 0.0
        
        # Start BFS loop
        while queue:
            # Dequeue the next state to explore
            current_planet, current_day, remaining_autonomy, prob_success = queue.popleft()
            
            # Skip this state if the current day exceeds the countdown
            if current_day > countdown:
                continue
            
            # If the current planet is the destination, update the maximum probability of success
            if current_planet == destination:
                max_prob_success = max(max_prob_success, prob_success)
                continue
            
            # Explore all neighboring planets
            for neighbor, travel_time in self.graph[current_planet]:
                next_day = current_day + travel_time
                
                # Skip this neighbor if reaching it would exceed the countdown
                if next_day > countdown:
                    continue
                
                # Calculate the probability of success for reaching this neighbor
                next_prob_success = self._calculate_prob_success(prob_success, bounty_hunters[neighbor], next_day)
                
                # Check if the remaining autonomy is sufficient for the travel
                if remaining_autonomy >= travel_time:
                    next_autonomy = remaining_autonomy - travel_time
                    # Update the visited dictionary and enqueue the state if this path offers a better probability of success
                    if next_prob_success > visited[neighbor][next_day][next_autonomy]:
                        visited[neighbor][next_day][next_autonomy] = next_prob_success
                        queue.append((neighbor, next_day, next_autonomy, next_prob_success))
                else:
                    # Handle refueling if the remaining autonomy is not sufficient for the travel
                    self._handle_refueling(queue, visited, current_planet, current_day, countdown, prob_success, bounty_hunters)
        
        # Return the maximum probability of success after exploring all possible paths
        return max_prob_success
    
    def _parse_bounty_hunters(self, bounty_hunter_data: List[Dict[str, str | int]]) -> Dict[str, List[int]]:
        """
        Parses bounty hunter data to organize it by planet.

        Parameters:
            bounty_hunter_data (list of dict): A list of dictionaries where each dictionary contains
                                                'planet' and 'day' keys representing the planet the
                                                bounty hunter will be on and the day they will be there.

        Returns:
            defaultdict(list): A dictionary with planets as keys and lists of days as values, representing
                                the days bounty hunters will be present on each planet.
        """

        bounty_hunters = defaultdict(list)
        for bh in bounty_hunter_data:
            bounty_hunters[bh['planet']].append(bh['day'])
        return bounty_hunters
    
    def _calculate_prob_success(self, prob_success, bounty_days, current_day):
        """
        Calculates the probability of success for a given day, adjusting for the presence of bounty hunters.

        Parameters:
            prob_success (float): The current probability of success.
            bounty_days (list): A list of days when bounty hunters are present on a planet.
            current_day (int): The current day of travel.

        Returns:
            float: The adjusted probability of success after considering the presence of bounty hunters.
        """
        if current_day in bounty_days:
            return prob_success * 0.9  # 10% chance of being captured
        return prob_success
    
    def _handle_refueling(self, queue: deque, visited: Dict, current_planet: int, current_day: int, countdown: int, prob_success: float, bounty_hunters: Dict[str, List[int]]):
        """
        Handles the refueling process, updating the queue and visited records for days spent refueling.

        Parameters:
            queue (deque): The queue of planets to visit, along with the current day, remaining autonomy, and probability of success.
            visited (dict): A record of visited planets, days, and the remaining autonomy with the highest probability of success.
            current_planet (str): The current planet where the Millennium Falcon is located.
            current_day (int): The current day of the journey.
            countdown (int): The total number of days before the mission fails.
            prob_success (float): The current probability of success.
            bounty_hunters (defaultdict(list)): A dictionary with planets as keys and lists of days as values, representing
                                                the days bounty hunters will be present on each planet.

        Updates the queue with new states considering the days spent refueling and adjusts the probability of success
        accordingly. It also updates the visited dictionary with these new states.
        """
        # Increment the current day to simulate the next day for refueling
        refuel_day = current_day + 1
        
        # Loop through the days until the countdown ends
        while refuel_day <= countdown:
            # Calculate the probability of success for the next day, considering bounty hunters and refueling
            next_prob_success = self._calculate_prob_success(prob_success, bounty_hunters[current_planet], refuel_day)
            # If the calculated probability is not better than what's already recorded for this day and planet, stop the loop
            if next_prob_success <= visited[current_planet][refuel_day][self.autonomy]:
                break

            # Update the visited dictionary with the new, higher probability of success for this day and planet
            visited[current_planet][refuel_day][self.autonomy] = next_prob_success
            # Add the current state to the queue for further exploration
            queue.append((current_planet, refuel_day, self.autonomy, next_prob_success))
            # Move to the next day for potential refueling
            refuel_day += 1

