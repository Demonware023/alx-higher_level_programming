#!/usr/bin/python3
""" Write a class BaseGeometry (based on 5-base_geometry.py). """


class BaseGeometry():
    """ Creates a public instance method of area that raises an\n
        exception wiht the message area() is not implemented """
    def area(self):
        raise Exception("area() is not implemented")
