As an input from the user, the whole path to the file that has to be worked on has to be given as an Input.

There have been 3 cases mentioned in the problem statement, the output will be according to them. 

There are more cases that can be encountered.

If the files have the same names but the duplicate keys in them have values with different types(eg child has list and parent has an integer value for the same key), following assumptions are made:

For duplicate keys:

1. If the child’s key has an integer/string/float value and the parent’s key has int/float/str/list/dict then we will keep the value of key as the integer value of the child.

2. If the child’s key has a list value and the parent’s key has int/float/str/list/dict then we will append the values of the parent’s key to the child’s key.

3. If the child’s key has a dict value and the parent’s key has int/float/str/list then we will ignore the parent’s key.

The code ensures that all keys are maintained.
