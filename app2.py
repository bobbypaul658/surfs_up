{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "054e0e51",
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
   "execution_count": 2,
   "id": "cd301f7b",
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
   "execution_count": 3,
   "id": "7fa448c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "37335553",
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "fac0afe5",
   "metadata": {},
   "outputs": [],
   "source": [
    "Base = automap_base()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0d931b87",
   "metadata": {},
   "outputs": [],
   "source": [
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "413db9e6",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "measurement",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/util/_collections.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m    185\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 186\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    187\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: 'measurement'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/7l/nztwq03j46x19j52xdfz9cth0000gn/T/ipykernel_1456/1266249183.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mMeasurement\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBase\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclasses\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmeasurement\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mStation\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBase\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclasses\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstation\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/util/_collections.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m    186\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    187\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 188\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    189\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    190\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__contains__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: measurement"
     ]
    }
   ],
   "source": [
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "00600952",
   "metadata": {},
   "outputs": [],
   "source": [
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a3c5effe",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (1616990076.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/7l/nztwq03j46x19j52xdfz9cth0000gn/T/ipykernel_1456/1616990076.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    @app.route(\"/\")\u001b[0m\n\u001b[0m                   ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "48a4d4ac",
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
   "execution_count": 11,
   "id": "87c56885",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (645207457.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/7l/nztwq03j46x19j52xdfz9cth0000gn/T/ipykernel_1456/645207457.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    flask run\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "flask run"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a1260013",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (262878934.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/7l/nztwq03j46x19j52xdfz9cth0000gn/T/ipykernel_1456/262878934.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    @app.route(\"/api/v1.0/precipitation\")\u001b[0m\n\u001b[0m                                         ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/api/v1.0/precipitation\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "1d2b93ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "def precipitation():\n",
    "    return"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "64867bb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def precipitation():\n",
    "   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "   precipitation = session.query(Measurement.date, Measurement.prcp).\\\n",
    "      filter(Measurement.date >= prev_year).all()\n",
    "   return"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8e83a888",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (1802364990.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/7l/nztwq03j46x19j52xdfz9cth0000gn/T/ipykernel_1456/1802364990.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    @app.route(\"/api/v1.0/stations\")\u001b[0m\n\u001b[0m                                    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/api/v1.0/stations\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "aad4b93e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def stations():\n",
    "    return"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "967edd27",
   "metadata": {},
   "outputs": [],
   "source": [
    "def stations():\n",
    "    results = session.query(Station.station).all()\n",
    "    stations = list(np.ravel(results))\n",
    "    return jsonify(stations=stations)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "06afbe78",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (3710546096.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/7l/nztwq03j46x19j52xdfz9cth0000gn/T/ipykernel_1456/3710546096.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    @app.route(\"/api/v1.0/tobs\")\u001b[0m\n\u001b[0m                                ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/api/v1.0/tobs\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "b222627a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def temp_monthly():\n",
    "    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "    results = session.query(Measurement.tobs).\\\n",
    "        filter(Measurement.station == 'USC00519281').\\\n",
    "        filter(Measurement.date >= prev_year).all()\n",
    "    return"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "86e6f557",
   "metadata": {},
   "outputs": [],
   "source": [
    "def temp_monthly():\n",
    "    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "    results = session.query(Measurement.tobs).\\\n",
    "      filter(Measurement.station == 'USC00519281').\\\n",
    "      filter(Measurement.date >= prev_year).all()\n",
    "    temps = list(np.ravel(results))\n",
    "    return jsonify(temps=temps)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4b0ad50e",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (645207457.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/7l/nztwq03j46x19j52xdfz9cth0000gn/T/ipykernel_1456/645207457.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    flask run\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "flask run"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "866130e4",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (2677888708.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/7l/nztwq03j46x19j52xdfz9cth0000gn/T/ipykernel_1456/2677888708.py\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    @app.route(\"/api/v1.0/temp/<start>/<end>\")\u001b[0m\n\u001b[0m                                              ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/api/v1.0/temp/<start>\")\n",
    "@app.route(\"/api/v1.0/temp/<start>/<end>\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "7b85da31",
   "metadata": {},
   "outputs": [],
   "source": [
    "def stats(start=None, end=None):\n",
    "    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "d9e87cae",
   "metadata": {},
   "outputs": [],
   "source": [
    "def stats(start=None, end=None):\n",
    "    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]\n",
    "\n",
    "    if not end:\n",
    "        results = session.query(*sel).\\\n",
    "            filter(Measurement.date >= start).all()\n",
    "        temps = list(np.ravel(results))\n",
    "        return jsonify(temps=temps)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "60c255aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "def stats(start=None, end=None):\n",
    "    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]\n",
    "\n",
    "    if not end:\n",
    "        results = session.query(*sel).\\\n",
    "            filter(Measurement.date >= start).all()\n",
    "        temps = list(np.ravel(results))\n",
    "        return jsonify(temps)\n",
    "\n",
    "    results = session.query(*sel).\\\n",
    "        filter(Measurement.date >= start).\\\n",
    "        filter(Measurement.date <= end).all()\n",
    "    temps = list(np.ravel(results))\n",
    "    return jsonify(temps)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "3946d2b5",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (645207457.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/7l/nztwq03j46x19j52xdfz9cth0000gn/T/ipykernel_1456/645207457.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    flask run\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
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
   "id": "fde099d1",
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
