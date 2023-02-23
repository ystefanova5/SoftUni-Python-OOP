from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for item in self.albums:
            if item == album:
                return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for item in self.albums:
            if item.name == album_name:
                if item.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(item)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += album.details() + "\n"
        return result
