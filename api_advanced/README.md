ALU Scripting API Advanced Project

This repository focuses on master level API utilization using the Reddit platform. The projects goals center around handling pagination, executing recursive tracking calls over standard endpoints, and handling dynamic filtering on nested object arrays.

Learning Goals
* Process documentation structures to map endpoints efficiently
* Manage tokenless API data retrieval safely under system rate limits
* Execute clean recursive data pipelines without standard loop fallbacks
* Sort structural dictionaries safely across complex multi criteria rules

Project Infrastructure and Directory Layout

alu scripting/
└── api_advanced/
    ├── 0 subs.py           
    ├── 1 top_ten.py        
    ├── 2 recurse.py        
    └── 3 count.py          

Environment Requirements

* Target Engine Linux Ubuntu 14.04 LTS
* Interpreter Version Python 3.4.3
* Quality Standards PEP 8 Style Rules

System Permission Preparation

Ensure execution boundaries are allowed across your target system files with

chmod +x api_advanced/*.py
