from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        kona = toml.loads(content)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(kona["tool"]["poetry"]["name"], kona["tool"]["poetry"]["description"], kona["tool"]["poetry"]["dependencies"], kona["tool"]["poetry"]["dev-dependencies"])
