from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from services import note_service  # import service modular
import math

app = Flask(__name__)

API_BASE = "http://127.0.0.1:8000/api/v1/notes"
app.secret_key = "rahasia-123"  # ganti dengan kunci rahasia sesungguhnya


# Rote list data
@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 10, type=int)
    search = request.args.get("search", "", type=str)
    status = request.args.get("status", "Aktif")
    sort_by = request.args.get("sort_by", "updated_at__desc")

    try:
        # Ambil data dari API langsung
        params = {
            "search": search,
            "size": size,
            "page": page,
            "sort_by": sort_by,
            "status": status,
        }
        response = requests.get(f"{API_BASE}/paginated", params=params)
        data = response.json()

        notes = data.get("data", [])
        total_items = data.get("total", 0)
        print(f"Data: {data.get("total_page")}")

        # Pagination logic
        total_pages = data.get("total_page", 1)
        current_page = data.get("page", 1)
        has_next = data.get("has_next", False)
        has_prev = data.get("has_prev", False)

        # Hitung halaman tampil (misalnya current_page = 5 → [3, 4, 5, 6, 7])
        start_page = max(current_page - 2, 1)
        end_page = min(start_page + 4, total_pages)
        pages = list(range(start_page, end_page + 1))

        pagination = {
            "page": current_page,
            "total_pages": total_pages,
            "has_next": has_next,
            "has_prev": has_prev,
            "pages": pages,
        }

        return render_template(
            "index.html",
            notes=notes,
            pagination=pagination,
            search=search,
            status=status,
            sort_by=sort_by,
            size=size,
            page=page,
        )

    except requests.RequestException as e:
        return render_template(
            "index.html", notes=[], error=f"Gagal mengambil data: {e}"
        )


# route tambah data
@app.route("/tambah", methods=["GET", "POST"])
def tambah_catatan():
    if request.method == "POST":
        judul = request.form.get("judul", "").strip()
        isi = request.form.get("isi", "").strip()

        if not judul or not isi:
            flash("Judul dan isi tidak boleh kosong.", "danger")
            return render_template("tambah.html", judul=judul, isi=isi)

        try:
            payload = {"judul": judul, "isi": isi}
            response = requests.post(f"{API_BASE}", json=payload)
            result = response.json()

            if response.ok and result.get("success"):
                flash(result.get("message", "Catatan berhasil ditambahkan!"), "success")
                return redirect(url_for("index"))
            else:
                flash(result.get("message", "Gagal menambahkan catatan"), "danger")

        except Exception as e:
            flash(f"Terjadi kesalahan: {e}", "danger")

        return render_template("tambah.html", judul=judul, isi=isi)

    return render_template("tambah.html")


# Rute edit catatan
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_catatan(id):
    catatan = note_service.get_by_id(id)
    if not catatan:
        flash("Catatan tidak ditemukan", "danger")
        return redirect(url_for("index"))

    if request.method == "POST":
        judul = request.form.get("judul", "").strip()
        isi = request.form.get("isi", "").strip()

        if not judul or not isi:
            flash("Judul dan isi tidak boleh kosong.", "danger")
            return render_template("edit.html", catatan=catatan)

        success = note_service.update(id, judul, isi)
        print(f"[DEBUG] Update result: {success}")
        if success:

            flash("Catatan berhasil diperbarui", "success")
            return redirect(url_for("index"))
        else:
            flash("Gagal memperbarui catatan", "danger")

        return render_template(
            "edit.html", catatan={"id": id, "judul": judul, "isi": isi}
        )

    return render_template("edit.html", catatan=catatan)


# Rute hapus catatan
@app.route("/hapus/<int:id>", methods=["POST"])
def hapus_catatan(id):
    success = note_service.delete(id)
    if success:
        flash("Catatan berhasil dihapus", "success")
    else:
        flash("Gagal menghapus catatan", "danger")
    return redirect(url_for("index"))


@app.route("/restore/<int:note_id>", methods=["POST"])
def restore(note_id):
    success, message = note_service.restore_note(note_id)
    flash(message, "success" if success else "danger")
    return redirect(url_for("index"))


@app.route("/force-delete/<int:note_id>", methods=["POST"])
def force_delete(note_id):
    success, message = note_service.force_delete_note(note_id)
    flash(message, "success" if success else "danger")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=8100)
