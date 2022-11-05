from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class MyExprVisitor(ExprVisitor):
	def __init__(self):
		super(MyExprVisitor, self).__init__()
		self.stack = [] # Stack to evaluate the expression
		self.variables = {} # Dictionary to keep track of the variables

# Visit a parse tree produced by ExprParser#prog.
# def visitProg(self, ctx:ExprParser.ProgContext):
#    return self.visit(ctx.expr()) # Just visit the self expression
	def visitAssignStmt(self, ctx:ExprParser.AssignStmtContext):
		self.visit(ctx.exp)
		self.variables[str(ctx.var.text)] = self.stack.pop()

	def visitPrintStmt(self, ctx:ExprParser.PrintStmtContext):
		var = str(ctx.var.text)
		if var not in self.variables:
			print(f'{var} is undefined')
		else:
			print(f"{var} is {self.variables[var]}")
# Visit a parse tree produced by ExprParser#infixExpr.
	def visitInfixExpr(self, ctx:ExprParser.InfixExprContext):
		self.visit(ctx.left) # Evaluate the left expression and push to stack
		self.visit(ctx.right) # Evaluate the right expression and push to stack
		b = self.stack.pop() # Why is ‘b’ the first popped item?
		a = self.stack.pop()
		c = None

		if ctx.OP_ADD():
			c = a + b
		elif ctx.OP_SUB():
			c = a - b
		elif ctx.OP_MUL():
			c = a * b
		elif ctx.OP_DIV():
			c = a / b
		self.stack.append(c)
		return c
# Visit a parse tree produced by ExprParser#numberExpr.
	def visitNumberExpr(self, ctx:ExprParser.NumberExprContext):
		c = int(str(ctx.INT())) # Found a number, just insert to stack
		self.stack.append(c)
		return c
# Visit a parse tree produced by ExprParser#parensExpr.
	def visitParensExpr(self, ctx:ExprParser.ParensExprContext):
		return self.visit(ctx.expr()) # Since enclosed by parents, just visit expr
