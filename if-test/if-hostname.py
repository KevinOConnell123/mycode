#!/usr/bin/env python3
prompt_hostname_msg = "What is the hostname?"
host_name = input(prompt_hostname_msg)
host_name = host_name.upper()
if host_name == 'MTG':
    print('The hostname was found to be mtg')
    print('The hostname matches expected config')
    print('Exiting the script.')
