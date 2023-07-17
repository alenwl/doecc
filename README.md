# Challenge description

A log file contains newline-terminated, space-separated text formatted like:

`<unix_timestamp> <hostname> <hostname>`

For example:
<br>
`1366815793 quark garak`
<br>
`366815795 brunt quark`
<br>
`1366815811 lilac garak`


Each line represents connection from a host (left) to another host (right) at a given time. The lines
are roughly sorted by timestamp. They might be out of order by maximum 5 minutes.
Implement a tool that parse log files like these, we provide you a input Data Example.

## Goals to Achieve

1. Parse the data with a time_init, time_end (Required ~3h)
Build a tool, that given the name of a file (with the format described above), an init_datetime , an
end_datetime, and a Hostname, returns:

   - A list of hostnames connected to the given host during the given period.

2. Unlimited Input Parser (Optional ~3h)
The tool should both parse previously written log files and terminate or collect input from a new log
file while it's being written and run indefinitely.
The script will output, once every hour:

   - A list of hostnames connected to a given (configurable) host during the last hour.
   - A list of hostnames received connections from a given (configurable) host during the last hour.
   - The hostname that generated most connections in the last hour.

Both the number of log lines and hostnames can be very high. Consider implementing a CPU and
memory-efficient solution. Please feel free to make assumptions as necessary with proper
documentation.

## Usage

```
usage: doecc [-h] --init_time INIT_TIME --end_time END_TIME --logfile LOGFILE [LOGFILE ...] --host HOST [HOST ...]

optional arguments:
  -h, --help            show this help message and exit
  --init_time INIT_TIME, -i INIT_TIME
                        Initial time
  --end_time END_TIME, -e END_TIME
                        End time
  --logfile LOGFILE [LOGFILE ...], -lf LOGFILE [LOGFILE ...]
                        Log file name
  --host HOST [HOST ...], -ho HOST [HOST ...]
                        End time
```

It is possible to provide multiple log files and hosts. Log files will be concatenated into a single data frame.
If more than one host name is provided, the tool will provide a separated analysis for each. For example:

`python __main__.py -i 1565647204351 -e 1565733598341 -ho Aaronjosh,Joyelle  -lf input-file-10000.txt,input-file-10001.txt`

The previous example will join both input files (`input-file-10000.txt` and `input-file-10001.txt`) and perform a search for 
connected hosts to `Aaronjosh` and `Joyelle` between `1565647204351` and `1565733598341`.

## Running example

1. Clone repo and cd to directory:
```
git clone <repo>
cd repo
```

2. Create a conda virtual environment with Python 3.9:

`conda create -n "temp" python=3.9`

3. Activate env:

`conda activate temp`

4. Install requirements via pip:

`pip install -r requirements.txt`

5. Run tests:

`pytest`

6. Run doecc:

```
python __main__.py -i 1565647204351 -e 1565733598341 -ho Aaronjosh -lf input-file-10000.txt

START TIME: 2019-08-12 23:00:04
END TIME: 2019-08-13 22:59:58

Hosts connected to `Aaronjosh` between given times:
        Makaiya, Ayania, Lizbett, Theresamarie, Taquana, Akos, Suhanee, Jacquis, Kayliyah, Genai, Maleya

```

## Installation

Alternatively, the module can be installed as follows:

1. Clone repo and cd to directory:
```
git clone <repo>
cd repo
```

2. Create a conda virtual environment with Python 3.9:

`conda create -n "temp" python=3.9`

3. Activate env:

`conda activate temp`

4. Install the `doecc` module:

`pip install .`

The previous command will run `setup.py` installing all the required dependencies and building `doecc`. Once the installation
is completed, the tool can be executed on the command line as follows:

`doecc -i 1565647204351 -e 1565733598341 -ho Aaronjosh -lf input-file-10000.txt`