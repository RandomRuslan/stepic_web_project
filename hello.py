bind = "0.0.0.0:8080"
def application(env, resp):
	status = "200 OK"
	headers = [("Content-type","text/plain")]
	resp(status, headers)
	return env["QUERY_STRING"].replace("&", "\n")
	
	
#print(application({"QUERY_STRING":"a=1&b=2&b=3"}, 0))
