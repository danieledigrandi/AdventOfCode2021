from day1 import get_mode


class Probe:

    def __init__(self):

        self.x_position = 0
        self.y_position = 0
        self.x_velocity = 0
        self.y_velocity = 0

    def launch(self, target_area_coordinates, original_area_coordinates):

        max_x = original_area_coordinates[0][0] if abs(original_area_coordinates[0][0]) > abs(original_area_coordinates[0][1]) else original_area_coordinates[0][1]
        max_y = original_area_coordinates[1][0] if abs(original_area_coordinates[1][0]) > abs(original_area_coordinates[1][1]) else original_area_coordinates[1][1]

        x_range = (0, max_x) if max_x > 0 else (max_x, 0)
        y_range = (-max_y, max_y) if max_y > 0 else (max_y, -max_y)

        velocities_to_test = generate_all_coordinates([x_range, y_range])

        all_paths = {}

        for velocity in velocities_to_test:

            self.x_velocity = velocity[0]
            self.y_velocity = velocity[1]
            current_path = [(self.x_position, self.y_position)]

            while (self.x_position, self.y_position) not in target_area_coordinates and self.x_position < max_x and self.y_position > max_y:

                self.x_position += self.x_velocity
                self.y_position += self.y_velocity

                if self.x_velocity > 0:
                    self.x_velocity -= 1
                elif self.x_velocity < 0:
                    self.x_velocity += 1

                self.y_velocity -= 1

                current_path.append((self.x_position, self.y_position))

            self.initialise()
            if current_path[-1] in target_area_coordinates:  # if the last point is in the area coordinates
                all_paths[(velocity[0], velocity[1])] = current_path

        return all_paths

    def initialise(self):

        self.x_position = 0
        self.y_position = 0
        self.x_velocity = 0
        self.y_velocity = 0


def open_file(path):

    with open(path, 'r') as f:
        input_ = f.readlines()[0].strip('target area: x= \n').split(', y=')

    data = []
    for i in input_:
        x, y = i.split('..')
        x = int(x)
        y = int(y)
        data.append((x, y))

    return data


def generate_all_coordinates(data):

    target_area_coordinates = []

    for y in range(data[1][0], data[1][1] + 1):
        for x in range(data[0][0], data[0][1] + 1):
            target_area_coordinates.append((x, y))

    return target_area_coordinates


def analyse(all_paths):

    max_y = 0
    for velocity, path in all_paths.items():
        for point in path:
            if point[1] > max_y:
                max_y = point[1]
                initial_velocity = velocity

    return initial_velocity, max_y


def main():
    path = './data/input_day_17.txt'
    data = open_file(path)

    target_area_coordinates = generate_all_coordinates(data)

    probe = Probe()
    all_paths = probe.launch(target_area_coordinates, data)

    mode = get_mode()

    if mode == 1:
        initial_velocity, max_y = analyse(all_paths)
        print(f"For initial velocity of {initial_velocity}, the max y is: {max_y}")

    if mode == 2:
        print("Distinct initial velocity values that cause the probe to be within the target area:", len(all_paths))


if __name__ == '__main__':
    main()
