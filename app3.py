{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e4bbed5b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4063d3de",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "705b50dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9ca35e3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "728e2e45",
   "metadata": {},
   "outputs": [],
   "source": [
    "Base = automap_base()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2ce49984",
   "metadata": {},
   "outputs": [],
   "source": [
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ea3c397b",
   "metadata": {},
   "outputs": [],
   "source": [
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b9f27ba3",
   "metadata": {},
   "outputs": [],
   "source": [
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6429dd15",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "08787dd5",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (1616990076.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/7l/nztwq03j46x19j52xdfz9cth0000gn/T/ipykernel_814/1616990076.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    @app.route(\"/\")\u001b[0m\n\u001b[0m                   ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "36754971",
   "metadata": {},
   "outputs": [],
   "source": [
    "def welcome():\n",
    "    return(\n",
    "    '''\n",
    "    Welcome to the Climate Analysis API!\n",
    "    Available Routes:\n",
    "    /api/v1.0/precipitation\n",
    "    /api/v1.0/stations\n",
    "    /api/v1.0/tobs\n",
    "    /api/v1.0/temp/start/end\n",
    "    ''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b1eba6c9",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (645207457.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/7l/nztwq03j46x19j52xdfz9cth0000gn/T/ipykernel_814/645207457.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    flask run\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "flask run"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbf98f7c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
