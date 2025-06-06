# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# look for source in the expected place
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
code_path = os.path.join(
    current_dir,
    '..',
    '..',
    'stubs'
)
sys.path.append(code_path)

project = 'LEGO Spike Prime Python API v3'
copyright = '2025, LEGO'
author = 'LEGO'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'nature'
html_static_path = ['_static']
autodoc_typehints = "description"

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "private-members": True,
}
