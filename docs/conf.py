# Configuration file for the Sphinx documentation builder.

project = 'Bible of Babylon'
copyright = '2026, chatelao'
author = 'chatelao'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'xelatex'
html_static_path = ['_static']

html_context = {
    "display_github": True,
    "github_user": "chatelao",
    "github_repo": "bible-of-babylon",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
