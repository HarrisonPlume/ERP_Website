In order to run the server clone the repo.

Navigate to the second ERP website folder

run "docker-compose up --build"


In a seperate terminal navigate to where the ERP_Website repo was cloned.

run "docker-compose exec web python manage.py migrate"

After the ERP database is created, copy the current data into that with the following commands.

"docker cp data_only.sql erp_website-db-1:/data_only.sql"

"docker exec -it erp_website-db-1 bash"

"psql -U harrison -d connect_erp -f /data_only.sql"

"exit"

Now you can run the container and it should work beautifully.

Admin login: User: ERPAdmin Pass: Tq49XUQ7
