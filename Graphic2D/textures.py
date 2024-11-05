import os
import json

import pygame

from PIL import Image
from utils import type_checking


class Textures:
    """The application's texture handler"""
    TEXTURES = []

    @staticmethod
    def __textures_division(path: str, textures: dict) -> list:
        """Separates the texture according to the specified parameters"""
        textures_ = []
        for name, divide_parameters in textures["textures"].items():
            try:
                image = Image.open(path).crop(divide_parameters)
                textures_.append({
                    "name": name,
                    "image": pygame.image.fromstring(image.tobytes(), image.size, image.mode).convert()
                })
            except ValueError:
                continue
            except KeyError:
                continue
        return textures_
    
    @classmethod
    def set_textures(cls) -> None:
        """Loading all textures"""
        path = ".\\resources"

        try:
            for filename in os.listdir(f"{path}\\init"):
                file_path = os.path.join(f"{path}\\init", filename)

                if os.path.isfile(file_path) and filename.endswith(".json"):
                    with open(file_path, "r", encoding="utf-8-sig") as file:
                        try:
                            content = json.load(file)
                            cls.TEXTURES.append({
                                "id": content["id"],
                                "textures": cls.__textures_division(f"{path}\\assets\\{content['path']}", content)
                            })
                        except KeyError:
                            continue
        except FileNotFoundError:
            cls.TEXTURES = None
    
    @classmethod
    def get_images(cls, id: str) -> list:
        """Returns textures by the specified id"""
        type_checking(id, str, "Invalid id type!")

        images = []
        for textures in cls.TEXTURES:
            if textures["id"] == id:
                for image in textures["textures"]:
                    images.append(image["image"])
        return images
