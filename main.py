#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

* File Name : main.py

* Purpose : Contain the base class for plugin manager

* Creation Date : 06-06-2016

* Copyright (c) 2016 Mandeep Singh <mandeeps708@gmail.com>

"""

from __future__ import print_function
import requests, bs4
from github import Github
# import ipdb


class Plugin():
    "Information about plugin."
    # def __init__(self, name, author, plugin_type, description, baseurl, infourl):
    def __init__(self, name, baseurl):
        "returns plugin info"
        self.name = name
        # self.author = author
        # self.plugin_type = plugin_type
        # self.description = description
        self.baseurl = baseurl
        # self.infourl = infourl

class Fetch():
    "The base fetch class"

    def __init__(self):
        print("Object created")
        self.Plugins = []

    def getPluginsList(self):
        print("Plugins list")

    def getInfo(self):
        print("Plugin Info")

    def isInstalled(self):
        print("If installed or not")

    def install(self):
        print("Installing")
        
    def isUpToDate(self):
        print("Check for latest version")


class FetchFromGitHub(Fetch):
    "class to get workbenches from GitHub"

    def __init__(self):
        print("git workbenches")
        # For storing instances of Plugin() class.
        instances = []

    def getpluginsList(self):
        g = Github("3595cd09a660854ff274f828ca15cdbc86865d14")

        github_username = "FreeCAD"

        # Name of the repository residing at github_username account.
        repository = "FreeCAD-addons"

        # Repository instance.
        repo = g.get_user(github_username).get_repo(repository)
        print("Fetching repository details...")

        # To store count of number of submodules.
        count = 0
        
        instances = []

        # Iterations to fetch submodule entries and their info.
        for x in repo.get_dir_contents(""):
            # if(x.type == "submodule"):
                # print(x.url)

            #Checks if the instance is a submodule, then fetches it's details. 
            if(x.raw_data.get("type") == "submodule"):
                count += 1
                name = x.name
                print(name)
                url = x.raw_data.get("submodule_git_url")
                
                # ipdb.set_trace()

                instance = Plugin(name, url)
                instances.append(instance)
                # print(instances)

                # ipdb.set_trace()
        return instances

class FetchFromWiki():
    "fetching macros from wiki"

    def __init__(self):
        print("macros")

#obj = Fetch()
#obj.getInfo()

git = FetchFromGitHub()
plugins = git.getpluginsList()
# ipdb.set_trace()
