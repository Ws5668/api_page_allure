import pytest
import allure
import yaml
import logging

def pytest_collection_modifyitems(session, config, items:list):
  for item in items:
      item.name = item.name.encode("utf-8").decode("unicode-escape")
      item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")


