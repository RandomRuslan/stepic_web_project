def app(env, resp):
	status = "200 OK"
	headers = [("Content-type","text/plain")]
	#resp(status, headers)
	return env["QUERY_STRING"].replace("&", "\n")
	
	
print(app({"QUERY_STRING":"a=1&b=2&b=3"}, 0))