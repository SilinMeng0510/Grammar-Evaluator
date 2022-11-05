# Grammar-Evaluator

The project is demonstrating some form of parsing capabilities using antlr4, and evalute grammar of a specific language created by us. 
Details can be found in Expr.g4.

python 3 is used

virtualenv is used. Set it up through python3 -m pip install virtualenv -> python3 -m venv venv - > source venv/bin/activate

antlr4-tools
antlr4-parse
antlr4-python3-runtime are also needed.

call "antlr4 -Dlanguage=Python3 -visitor Expr.g4" to extract files (Note: Expr.g4 is the grammar file)
