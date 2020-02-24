from project import app

print("---in main---")

app.run(debug=True, port=5030, threaded=True)
