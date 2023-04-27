import sqlite3

conn = sqlite3.connect('test9.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_submission223 ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_png TEXT, \
        col_txt TEXT, \
        col_docx TEXT, \
        col_mpg TEXT, \
        col_jpg TEXT, \
        col_text1 TEXT \
        )")

    conn.commit()
conn.close()

conn = sqlite3.connect('test9.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_submission223 (col_png, col_txt, col_docx, col_jpg, col_mpg, col_text1) VALUES (?, ?, ?, ?, ?, ?)", \
        ('myImage.png', 'Hello.txt', 'information.docx', 'myPhoto.jpg', 'myMovie.mpg', 'World.text1'))

   
    conn.commit()
conn.close()

conn = sqlite3.connect('test9.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_txt FROM tbl_submission223 WHERE col_txt = 'Hello.txt'")
    varText = cur.fetchall()
    for item in varText:
        msg = "Text File: {}".format(item)
    print(msg)

conn = sqlite3.connect('test9.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_txt FROM tbl_submission223 WHERE col_text1 = 'World.text1'")
    varText = cur.fetchall()
    for item in varText:
        msg = "Text File: {}".format(item)
    print(msg)

