# python-password

## An example project for securely hashing and storing passwords in Python

### Installation

1. Set up a virtual environment ([virtualenv docs](https://virtualenv.pypa.io/en/latest/userguide/#usage))
2. `pip install pip-tools`
3. `pip-sync`

### Examples

#### Get Help

```bash
python app.py --help
```

#### Create a new user

```bash
python app.py --user myuser --password coolpass --new
```

#### Create a new admin user

```bash
python app.py --user myadminguy --password securepass --new --admin
```

#### Test password

```bash
python app.py --user myuser --password coolpass

# Output:
# Login Successful!

```
