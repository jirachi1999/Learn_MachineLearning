import os
import file_reader as fr
import json

train_path = os.path.join(os.getcwd(), "Data/10Topics/Ver1.1/Train_Full")


class DataLoader:
    def __init__(self, data_path):
        self.data_path = data_path

    def __get_file(self):
        files = {}
        for topic in os.listdir(self.data_path):
            title_path = os.path.join(self.data_path, topic)
            files[topic] = [os.path.join(title_path, file) for file in os.listdir(title_path)]
        return files

    def get_json(self):
        files = self.__get_file()
        data = []
        for topic in files:
            for file in files[topic]:
                content = fr.FileReader(file).content()
                data.append({
                    'category': topic,
                    'content': content
                })
        return data
