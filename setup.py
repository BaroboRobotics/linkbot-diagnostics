#!/usr/bin/env python3

from setuptools import setup
import re

version = '0.0.6'

setup(
    name = "linkbot_diagnostics",
    packages = ["linkbot_diagnostics", 'linkbot_diagnostics.test_dialogs'],
    version = version,
    entry_points = {
        "console_scripts":
        [
         'linkbot-diagnostics=linkbot_diagnostics.LinkbotDiagnosticGui:main',
         'linkbot-diagnostics-summary=linkbot_diagnostics.MassageData:main',
         'linkbot-diagnostics-preassembly=linkbot_diagnostics.LinkbotPreAssemblyTest:main',
        ]
    },
    install_requires = ["PyLinkbot3 >= 3.0.0", "appdirs"],
    description = "Tool for testing Linkbots",
    zip_safe = False,
    include_package_data = True,
    author = "David Ko",
    author_email = "david@barobo.com",
    )

