from math import ceil


class PhotoAlbum:
    PAGE_CAPACITY = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PAGE_CAPACITY))

    def add_photo(self, label: str):
        for idx in range(len(self.photos)):
            if len(self.photos[idx]) < PhotoAlbum.PAGE_CAPACITY:
                self.photos[idx].append(label)
                return f"{label} photo added successfully on page {idx + 1} slot {len(self.photos[idx])}"

        return "No more free slots"

    def display(self):
        result = ["-----------"]
        for row in self.photos:
            if row:
                line = ["[]" for _ in range(len(row))]
                result.append(f"{' '.join(line)}\n-----------")
            else:
                result.append("\n-----------")

        return '\n'.join(result)
