# image-grabber
Image grabber


## Usage

### Installation
```
$ git clone git@github.com:9oh9/image-grabber.git;

```

Install package with python3 / pip
```
$ pip install virtualenv;

```

create virtual env
```
$ virtualenv -p path/to/python3 venv;

```

Activate virtual env
```
$ source venv/bin/activate;

```

Install ImageGrabber package
```
$ pip install -e path/to/cloned/repo;

```

### Run

With activated virtual env, run:
```
$ cd path/to/cloned/repo;
$ python -m image_grabber;

```

### API

```

GET http:127.0.0.1:5000/deeplocal/home/images

```

#### Query Options

##### File Types

Grabs all png and jpg's in carousel.
```

	?ft=png:jpg

```

Grabs only png's in carousel.
```

	?ft=png

```

Grabs all png, jpg, and gif's in carousel.
```

	?ft=png:jpg:gif

```


##### Sort By

The addition of "sbf" query param will sort URI's by filename not entire URI.
```

	?ft=png:jpg&sbf=1

```
