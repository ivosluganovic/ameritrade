"""Bindings for the Ameritrade REST API.

Homepage: https://developer.tdameritrade.com

Usage:

    api = ameritrade.open_with_dir(config_dir=config_dir,
                                   redirect_uri='https://localhost:8444')
    instruments = api.SearchInstruments(symbol='Vanguard', projection='desc-search')

See schema.py for a description of all available methods.
"""
__author__ = 'Martin Blais <blais@furius.ca>'
__license__ = "GNU GPLv2"

from ameritrade import api
open = api.open
open_with_dir = api.open_with_dir

from ameritrade import scripts
add_script_args = scripts.add_args
open_with_args = scripts.open_with_args
