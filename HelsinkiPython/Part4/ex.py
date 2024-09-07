def read_points():
    results = []

    try:
        # Open the file 'statistics.txt' in read mode
        with open("statistics.txt", "r") as file:
            for line in file:
                line = line.strip()  # Remove any leading/trailing whitespace
                try:
                    # Split the line into team name and statistics
                    team_name, stats = line.split(":")
                    # Split the statistics into wins, losses, and ties
                    wins, losses, ties = stats.split("-")

                    # Convert wins, losses, and ties to integers
                    wins = int(wins)
                    losses = int(losses)
                    ties = int(ties)

                    # Calculate points: 3 points for a win, 1 point for a tie
                    points = (wins * 3) + (ties * 1)

                    # Append the result as a tuple to the results list
                    results.append((team_name, points))
                
                except ValueError:
                    # Raise ValueError with the specific line causing the issue
                    raise ValueError(f"Invalid format in file: {line}")
                    
    except FileNotFoundError:
        print("The file statistics.txt was not found.")
        return None

    return results


# Example usage
if __name__ == "__main__":
    try:
        points = read_points()
        if points:
            for team, point in points:
                print(f"{team}: {point} points")
    except ValueError as e:
        print(e)
