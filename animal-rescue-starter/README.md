# Second Chance Animal Rescue 🐶🐱

This is a Flask site for a made-up animal rescue. It pulls the dogs and cats
up for adoption out of a SQLite database and shows them on their own pages.

| Page | URL |
| --- | --- |
| Home | `/` |
| Dogs | `/dogs` |
| Cats | `/cats` |

## Getting it running

Open a terminal in the `animal-rescue-starter` folder and run:

```bash
python -m pip install -r requirements.txt
python init_db.py                      # sets up rescue.db with the animals
python -m flask --app app run --debug
```

Then go to http://127.0.0.1:5000. Hit Ctrl+C when you're done.
(If `python` doesn't work, try `python3`.)

A few heads-ups:
- Only run `init_db.py` once. Run it again and you'll get every animal twice.
  If that happens, stop Flask, delete `rescue.db`, and run `python init_db.py` again.
- If port 5000 is taken, tack `--port 5055` (or any free number) onto the end of the run command.

## How a dog gets from the database onto the page

Here's what happens when you open `/dogs`:

1. The dogs live as rows in the `dogs` table. `schema.sql` makes the table,
   `seed.sql` adds the dogs, and `init_db.py` runs both and saves them into `rescue.db`.
2. Flask sees `/dogs` and runs the `dogs()` function in `app.py`.
3. That calls `get_dogs()` in `models.py`, which runs
   `SELECT * FROM dogs ORDER BY name` and hands back the rows.
   Each row works kind of like a dictionary, so you can grab `dog['name']` and so on.
4. `app.py` passes those rows to `templates/dogs.html`.
5. In the template, `{% for dog in dogs %}` makes one card per dog with the name,
   breed and age tags, and the description. If there aren't any dogs, you get the
   "listings are being updated" message instead.

Cats work exactly the same way, just with the `cats` table, `get_cats()`, and `cats.html`.

## What's in here

| File | What it does |
| --- | --- |
| `app.py` | The routes for the three pages |
| `models.py` | Talks to the database (`get_dogs()` and `get_cats()`) |
| `schema.sql` | Makes the `dogs` and `cats` tables |
| `seed.sql` | Adds the animals |
| `init_db.py` | Runs the SQL files to build `rescue.db` |
| `templates/` | The HTML pages (`base.html` is the shared layout) |
| `static/style.css` | All the styling, including the cards |
