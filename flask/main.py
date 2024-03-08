from flask import Flask
from concurrent.futures import ProcessPoolExecutor

app = Flask(__name__)
executor = ProcessPoolExecutor()


def cpu_bound_operation(BIGNUM):
    num = 0
    for i in range(BIGNUM):
        num += 1
    return num


@app.route("/flask/")
def root():
    return {"message": "Hello World"}


def sync_cpu_operation(BIGNUM):
    return cpu_bound_operation(BIGNUM)


@app.route("/flask/sync_cpu_bound/")
def sync_cpu_bound():
    BIGNUM = 5000000
    result = executor.submit(cpu_bound_operation, BIGNUM).result()
    return {"data": result, "message": "sync mode cpu operation"}


@app.route("/flask/sync_cpu_bound_slow/")
def sync_cpu_bound_slow():
    BIGNUM = 5000000
    cpu_bound_operation(BIGNUM)
    return {"message": "sync mode operation but pretend to run in async mode"}


if __name__ == "__main__":
    app.run(debug=True)
