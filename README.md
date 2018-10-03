# OptimizeSort

Sort huge age data

## Create age data:
`python command.py create --output <specific output path> --amount <amount of age data>`

Example:
`python command.py create --output ./input/agetest.txt  --amount 1000000`

## Sort age data:
`python command.py sort --input-file <specific input path> --output-file <specific output path>`

Example:
`python command.py sort --input-file ./input/agetest.txt --output-file ./output/agetest.txt`

## Structure:
```
.
├── command.py
├── task2_compute.py
├── task2_create_file.py
├── input
│   └── agetest.txt
├── output
│   ├── agetest.txt
```

## Update:

##### Sort schema changed

* Mapping each number to temporary files (ex: 1 mapping to 01.txt, 10 mapping to 10.txt) 
* Sort temporary files
* Merge sorted temporary files