#!/usr/bin/python3
"""Base class"""
import json
import csv
import turtle


class Base:
    """Base class for all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the instance with an id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries represented by json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                dict_list = cls.from_json_string(f.read())
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and saves to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width,
                                    obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes and loads from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="") as f:
                reader = csv.reader(f)
                if cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                    objs = [cls(**dict(zip(keys, map(int, row)))) for row in reader]
                elif cls.__name__ == "Square":
                    keys = ["id", "size", "x", "y"]
                    objs = [cls(**dict(zip(keys, map(int, row)))) for row in reader]
                return objs
        except FileNotFoundError:
            return []
        
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares
        using the Turtle graphics module."""
        turtle.setup(width=600, height=600)
        turtle.bgcolor("white")
        
        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            
            for i in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
                
        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            
            for i in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.done()
