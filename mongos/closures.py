def outer_fn(msg):
	def printer():
		print("Decorator begins")
		msg()
	return printer

@outer_fn
def second():
	print("This is second")


second()