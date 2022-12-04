db="tpch.sqlite"
rm -f ${db}
touch ${db}

python3 advertisements.py

sqlite3 ${db} < import.sql
sqlite3 ${db} < query.sql