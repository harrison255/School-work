CREATE TABLE quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    text TEXT NOT NULL,
    author TEXT
);

INSERT INTO quotes (text, author)
VALUES
("IM JEREMTY CLARKSON", "Jeremy Clarkson"),
("im jaMES MAY", "James May"),
("IM RIHCARD HAMPOND", "Richard Hammond");