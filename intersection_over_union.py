import numpy as np

def area(coordinates):
    return (coordinates[1] - coordinates[0]) * (coordinates[3] - coordinates[2])

def intersection(coordinates_1, coordinates_2):
    intersection_x1 = max(coordinates_1[0], coordinates_2[0])
    intersection_y1 = max(coordinates_1[2], coordinates_2[2])
    intersection_x2 = min(coordinates_1[1], coordinates_2[1])
    intersection_y2 = min(coordinates_1[3], coordinates_2[3])

    return intersection_x1, intersection_x2, intersection_y1, intersection_y2

def compute_tomas(coordinates, scores, threshold=0.5):
    # coordinate[i] = [x1, x2, y1, y2]
    # scores[i] = float

    intersections_over_unions = np.zeros((len(coordinates), len(coordinates)))
    delete_boxes = np.zeros(len(coordinates))

    for index_1 in range(len(coordinates)):
        for index_2 in range(index_1 + 1, len(coordinates)):
            box_1 = coordinates[index_1]
            box_2 = coordinates[index_2]
            intersection_12 = intersection(box_1, box_2)

            area_1 = area(box_1)
            area_2 = area(box_2)
            area_intersection_12 = area(intersection_12)
            area_union_12 = area_1 + area_2 - area_intersection_12

            intersections_over_unions[index_1, index_2] = area_intersection_12 / area_union_12

    for index_1 in range(len(coordinates)):
        for index_2 in range(index_1 + 1, len(coordinates)):
            if intersections_over_unions[index_1][index_2] > threshold:
                if scores[index_1] > scores[index_2]:
                    delete_boxes[index_2] = 1
                else:
                    delete_boxes[index_1] = 1

    return np.where(delete_boxes == 0)[0]



coordinates = np.random.rand(100, 100)
scores = np.random.rand(100)

print(compute_tomas(coordinates, scores))
