from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def get_category(self, category_id):
        return next(filter(lambda x: x.id == category_id, self.categories))

    def get_topic(self, topic_id):
        return next(filter(lambda x: x.id == topic_id, self.topics))

    def get_document(self, document_id):
        return next(filter(lambda x: x.id == document_id, self.documents))

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        self.get_category(category_id).edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        self.get_topic(topic_id).edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self.get_document(document_id).edit(new_file_name)

    def delete_category(self, category_id) -> None:
        self.categories.remove(self.get_category(category_id))

    def delete_topic(self, topic_id) -> None:
        self.topics.remove(self.get_topic(topic_id))

    def delete_document(self, document_id) -> None:
        self.documents.remove(self.get_document(document_id))

    def __repr__(self):
        return '\n'.join([str(document) for document in self.documents])
