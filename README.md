# ConAFL
AFL enhanced for concurrency bug and vulnerabilities
This repo mainly does two things:
- Evenly explore every forked threads
- If any pair(s) of sensitive concurrent operations are annotated, this fuzzer will enforce the execution order for those 2 operations. If no pair of sensitive operations are annotated, then this does nothing.

## How to run
1. First compile the AFL by just typing
```
make
``` 
2. Compile the target program with the generated *afl-gcc* ,also be sure to add `-g -pthread` flag when compiling the program
3. launch the fuzzer by `afl-fuzz -m 1GB -i <in dir> +  -o + <out dir> + -- <compiled executable> + @@`

`compile-run.py` is just an ad-hoc helper for step 2 and 3.