#!/usr/bin/env python3

import os
from os.path import expanduser
from pathlib import Path
import subprocess


class Project:
    def __init__(self, path):
        self.path = Path(expanduser(path))
        if Path(path).joinpath("build.gradle").exists():
            self.builder = 'gradle'
        if Path(path).joinpath("pom.xml").exists():
            self.builder = 'mvn'
        if Path(path).joinpath("Makefile").exists():
            self.builder = 'make'

    def build(self):
        os.chdir(str(self.path))
        if self.builder == 'gradle':
            subprocess.run(["gradle", "clean", "build"])
        if self.builder == 'mvn':
            subprocess.run(["mvn", "clean", "install"])
        if self.builder == 'make':
            subprocess.run(["make"])

    def get_artefacts(self):
        rootPath = str(self.path)
        buildPath = None
        if self.builder = 'gradle':
            buildPath = Path(rootPath).joinpath("build").joinpath("libs")
        if self.builder = 'mvn':
            buildPath = Path(rootPath).joinpath("target")
        if self.builder = 'mvn':
            buildPath = Path(rootPath)
        # todo file extension hardcode
        return buildPath.glob("*.jar")
            
            
def get_projects_list():
    projects = []
    projects.append(Project("/home/stcarolas/Coding/NetBeansProjects/customeref"))
    return projects

projects = get_projects_list()

def build_projects():
    for project in projects:
        project.build()

if __name__ == '__main__':
    build_projects()
    
