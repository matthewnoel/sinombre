# Sinombre

_"They can make out more than a dozen other islands and black lava ruins that Darwin never had a chance to visit, including an islet known officially as Sin Nombre (that is, Nameless) and another black speck called Eden." - Jonathan Weiner. The Beak of the Finch_

## Demo

![Screen recording](example.gif)

## Dependencies

Install [Anaconda or Miniconda](https://docs.anaconda.com/anaconda/install/)

Create your environment

```
conda env create -f env.yml -n sinombre
```

Update your environment

```
conda env update –f env.yml –n sinombre
```

Activate your environment

```
conda activate sinombre
```

## Running The Simulator

```
python main.py
```

## Formatting

```
conda run black .
```

## Maintenance

Update environment file

```
conda env export > env.yml
```
