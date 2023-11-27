# 1 - SELECT plaintext, occurences FROM wordform ORDER BY occurences DESC LIMIT 10

# 2 - SELECT plaintext FROM wordform WHERE plaintext ILIKE 'a%';

# 3 - SELECT title FROM work WHERE genretype = 'p';

# 4 - SELECT AVG(totalparagraphs) AS average_value FROM work WHERE genretype = 'p';

# 5 - SELECT title FROM work WHERE totalwords > (SELECT AVG(totalwords) FROM work);

# 6 - SELECT character.charname, character.speechcount, work.title FROM character
#     JOIN character_work ON character.charid = character_work.charid
#     JOIN work ON character_work.workid = work.workid;

# 7 - SELECT AVG(c.speechcount) FROM character c JOIN character_work k ON c.charid=k.charid JOIN work w ON w.title='Romeo and Juliet';

# 8 - SELECT SUM(wordcount) FROM paragraph;

# 9 - SELECT charname, speechcount FROM character WHERE 15 < speechcount AND speechcount < 30;

# 10 - SELECT title, year FROM work WHERE 1601 < year AND year < 1701; 

# 11 - SELECT longtitle FROM work WHERE longtitle ILIKE '%the%';

# 12 - SELECT DISTINCT section FROM paragraph;

# 13 - SELECT chapter.chapter, chapter.workid, chapter.description, work.title FROM chapter
#      JOIN work ON chapter.workid = work.workid;

# 14 - SELECT paragraph.paragraphnum, character.charname, character.speechcount FROM character
#      JOIN paragraph ON character.charid = paragraph.charid;

# 15 - SELECT paragraph.paragraphnum, work.title, work.year FROM work
#      JOIN paragraph ON work.workid = work.workid;