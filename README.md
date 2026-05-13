# Stream Fetcher

A Simple Flask application using a TMDB API

---

## Getting Started

To run the application locally, use:

```bash
flask --app app run
```
The server will start at:
`http://127.0.0.1:5000`

---

## Routes

### GET `/`
Health check route.

### GET `/movie`
Returns a list of movies based on a mood.

Example:

```http
GET /movie?mood=curiosity
```

### GET `/genres`
Returns the json list of movie genres from TMDB.

---

## Available Moods

The following moods are supported and mapped to TMDB genres:

- `curiosity`
- `joy`
- `tension`
- `reflection`
- `sadness`
- `comfort`
- `fascination`

> Note: Each mood maps to one or more genre IDs defined in `Config.MOVIE_MOODS` in `app/config.py`.

---

## Authors
| Micca | [GitHub](https://github.com/1micca)
