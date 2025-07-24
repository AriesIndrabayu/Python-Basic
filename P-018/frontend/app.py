from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_BASE = "http://127.0.0.1:8000/api/v1/notes"


@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 10, type=int)
    search = request.args.get("search", "", type=str)
    status = request.args.get("status", "Aktif")

    # params = {"page": page, "size": size, "search": search}
    params = {"search": search, "size": size, "page": page, "status": status}

    try:
        response = requests.get(f"{API_BASE}/paginated", params=params)
        data = response.json()
        notes = data.get("data", [])
        total_pages = data.get("total_pages", 1)
    except Exception:
        notes = []
        total_pages = 1

    return render_template(
        "index.html",
        notes=notes,
        page=page,
        total_pages=total_pages,
        search=search,
        size=size,
        status=status,
    )


if __name__ == "__main__":
    app.run(debug=True, port=8100)
