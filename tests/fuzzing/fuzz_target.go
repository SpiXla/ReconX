package main
import (
	"fmt"
	"net/http"
)

func main() {

	// 200 OK
	http.HandleFunc("/admin", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "Admin panel")
	})

	// 201 Created
	http.HandleFunc("/created", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusCreated)
		fmt.Fprintln(w, "Resource created")
	})

	// 301 Moved Permanently
	http.HandleFunc("/old-page", func(w http.ResponseWriter, r *http.Request) {
		http.Redirect(w, r, "/admin", http.StatusMovedPermanently)
	})

	// 302 Found
	http.HandleFunc("/temp-redirect", func(w http.ResponseWriter, r *http.Request) {
		http.Redirect(w, r, "/login", http.StatusFound)
	})

	// 400 Bad Request
	http.HandleFunc("/bad", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusBadRequest)
		fmt.Fprintln(w, "Bad request")
	})

	// 401 Unauthorized
	http.HandleFunc("/private", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusUnauthorized)
		fmt.Fprintln(w, "Unauthorized")
	})

	// 403 Forbidden
	http.HandleFunc("/uploads", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusForbidden)
		fmt.Fprintln(w, "Forbidden")
	})

	// 405 Method Not Allowed
	http.HandleFunc("/method", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			w.WriteHeader(http.StatusMethodNotAllowed)
			return
		}
		fmt.Fprintln(w, "POST accepted")
	})

	// 500 Internal Server Error
	http.HandleFunc("/crash", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusInternalServerError)
		fmt.Fprintln(w, "Internal server error")
	})

	// 503 Service Unavailable
	http.HandleFunc("/maintenance", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusServiceUnavailable)
		fmt.Fprintln(w, "Service unavailable")
	})

	// 404 for everything else
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusNotFound)
		fmt.Fprintln(w, "Custom 404 - Not Found")
	})

	fmt.Println("Server running on http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}
