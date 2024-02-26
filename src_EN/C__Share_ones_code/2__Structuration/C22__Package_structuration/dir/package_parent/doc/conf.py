# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from sys import path
path.insert(0,  r'/home/nerotb/Documents/5-Donnees_techniques/B. Developpement logiciel/Formations/Proposées/Cours SIE/C. Partager son code en Python/Structuration/C22_structurer_son_package/dir/package_parent')

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'my_package'
copyright = '2024, Nerot Boris'
author = 'Nerot Boris'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
                # 'sphinx.ext.autodoc',
              'sphinx.ext.napoleon'
]

add_module_names = False
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'nature'
html_static_path = ['_static']


