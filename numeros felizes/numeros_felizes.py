eh_feliz = lambda n, original = None, seq=[]: True if n == 1 else False if n in seq else eh_feliz(sum(map(lambda x: int(x)**2, str(n))),
	 original or n, seq + [n])
